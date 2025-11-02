import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from vhdl_simulator import VHDLSimulator
from waveform_generator import generate_waveform
from schema_generator import generate_schema
from database_manager import DatabaseManager
import tempfile
import os
import json
import time
from datetime import datetime

# Initialize session state
# Ensure db_manager is initialized first as other initializations might depend on it
if 'db_manager' not in st.session_state:
    try:
        st.session_state.db_manager = DatabaseManager()
    except Exception as e:
        st.error(f"Failed to initialize Database Manager: {e}")
        # Handle error appropriately, maybe stop the app or use default values
        st.stop()

# Initialize other state variables, ensuring dependencies like db_manager exist
if 'current_code_id' not in st.session_state:
    st.session_state.current_code_id = None

# Initialize circuit_type early, as it's used for dropdowns and logic
if 'circuit_type' not in st.session_state:
    st.session_state.circuit_type = "JK Flip-Flop" # Default value

if 'last_simulation_result' not in st.session_state:
    st.session_state.last_simulation_result = None

if 'simulation_history' not in st.session_state:
    st.session_state.simulation_history = []

# Load code history using the initialized db_manager
if 'code_history' not in st.session_state:
    try:
        st.session_state.code_history = st.session_state.db_manager.get_code_history()
    except Exception as e:
        st.warning(f"Failed to load code history: {e}")
        st.session_state.code_history = [] # Initialize empty on failure

if 'show_history_panel' not in st.session_state:
    st.session_state.show_history_panel = False

# Get user preferences using the initialized db_manager
# Initialize with default empty dict
user_prefs = {}
try:
    user_prefs = st.session_state.db_manager.get_preferences()
except Exception as e:
    st.warning(f"Failed to load user preferences: {e}")
    # Keep user_prefs as empty dict or load defaults if needed

st.set_page_config(
    page_title="VHDL Simulation Platform",
    page_icon="🔌",
    layout="wide"
)

# Top navigation bar
st.title("VHDL Simulation Platform")
st.write("Test and visualize digital circuits like the JK flip-flop")

# Top menu with three dots and options
col1, col2, col3 = st.columns([3, 1, 1])
with col3:
    menu_options = st.selectbox(
        "⋮",
        ["Menu", "History", "Examples", "Preferences", "Clear Data"],
        label_visibility="collapsed",
        key="menu_options"
    )
    
    if menu_options == "History":
        st.session_state.show_history_panel = True
    elif menu_options == "Examples":
        example_codes = st.session_state.db_manager.get_code_history(code_type="Example")
        if example_codes:
            example_selection = st.selectbox(
                "Select Example",
                [f"{code['name']}" for code in example_codes],
                key="example_selector"
            )
            
            selected_example = next((code for code in example_codes if code['name'] == example_selection), None)
            if selected_example and st.button("Load Example"):
                st.session_state.current_code_id = selected_example.doc_id
                st.rerun()
    elif menu_options == "Preferences":
        dark_mode = st.checkbox("Dark Mode", value=user_prefs.get('dark_mode', False))
        auto_save = st.checkbox("Auto Save Code", value=user_prefs.get('auto_save', True))
        
        if st.button("Save Preferences"):
            st.session_state.db_manager.save_preferences({
                'dark_mode': dark_mode,
                'auto_save': auto_save,
                'clock_frequency': user_prefs.get('clock_frequency', 100),
                'simulation_time': user_prefs.get('simulation_time', 100),
            })
            st.success("Preferences saved!")
    elif menu_options == "Clear Data":
        clear_option = st.selectbox(
            "Select what to clear",
            ["All History", "Code History", "Simulation Results", "Error Logs"],
            key="clear_option"
        )
        
        if st.button("Clear Data"):
            if clear_option == "All History":
                st.session_state.db_manager.clear_history()
            elif clear_option == "Code History":
                st.session_state.db_manager.clear_history(table_name='code_history')
            elif clear_option == "Simulation Results":
                st.session_state.db_manager.clear_history(table_name='simulation_results')
            elif clear_option == "Error Logs":
                st.session_state.db_manager.clear_history(table_name='error_logs')
                
            st.success(f"{clear_option} cleared!")
            st.session_state.code_history = st.session_state.db_manager.get_code_history()

# Show history panel if requested
if st.session_state.show_history_panel:
    with st.expander("Code History", expanded=True):
        history = st.session_state.db_manager.get_code_history(limit=20)
        
        if not history:
            st.write("No code history found.")
        else:
            # Create a table for history
            history_data = []
            for code in history:
                # Convert timestamp to readable format
                timestamp = datetime.fromisoformat(code.get('timestamp', ''))
                formatted_time = timestamp.strftime("%Y-%m-%d %H:%M:%S")
                
                history_data.append({
                    "ID": code.doc_id,
                    "Name": code.get('name', 'Unnamed'),
                    "Type": code.get('type', 'User'),
                    "Last Modified": formatted_time,
                    "Times Used": code.get('times_used', 0)
                })
            
            history_df = pd.DataFrame(history_data)
            st.dataframe(history_df)
            
            col1, col2 = st.columns(2)
            with col1:
                selected_id = st.number_input("Enter ID to load", min_value=1, step=1)
            with col2:
                if st.button("Load Selected Code"):
                    code = st.session_state.db_manager.get_code_by_id(selected_id)
                    if code:
                        st.session_state.current_code_id = selected_id
                        st.session_state.db_manager.increment_code_usage(selected_id)
                        st.session_state.show_history_panel = False
                        st.rerun()
                    else:
                        st.error(f"No code found with ID {selected_id}")
        
        if st.button("Close History"):
            st.session_state.show_history_panel = False
            st.session_state.current_code_id = None
            st.session_state.circuit_type = "JK Flip-Flop"
            st.rerun()

# Sidebar for configuration
with st.sidebar:
    st.header("Configuration")
    
    # Simulation settings
    st.subheader("Simulation Settings")
    clock_frequency = st.number_input("Clock Frequency (Hz)", min_value=1, max_value=1000, value=user_prefs.get('clock_frequency', 100))
    simulation_time = st.number_input("Simulation Time (ms)", min_value=1, max_value=1000, value=user_prefs.get('simulation_time', 100))
    
    # Calculate number of clock cycles
    num_cycles = int((simulation_time / 1000) * clock_frequency)
    
    # Ensure we have at least 96 clock cycles (for 0-960ns display at 10ns per cycle)
    num_cycles = max(num_cycles, 96)
    st.write(f"Number of clock cycles: {num_cycles}")
    st.write(f"Time range: 0-{num_cycles*10}ns (10ns per cycle)")
    
    # Save preferences
    if st.button("Save as Default"):
        st.session_state.db_manager.save_preferences({
            'clock_frequency': clock_frequency,
            'simulation_time': simulation_time,
            'dark_mode': user_prefs.get('dark_mode', False),
            'auto_save': user_prefs.get('auto_save', True),
        })
        st.success("Settings saved as default!")
    
    # Test pattern selection
    st.subheader("Test Pattern")
    test_pattern = st.selectbox(
        "Select a test pattern",
        ["All modes (hold, set, reset, toggle)", "Custom"],
        key="test_pattern"
    )

# Choose circuit type and load code
circuit_types = {
    "JK Flip-Flop": "default_codes/jk_flipflop.vhd",
    "D Flip-Flop": "default_codes/d_flipflop.vhd",
    "SR Latch": "default_codes/sr_latch.vhd",
    "Custom Circuit": None
}

# Initialize circuit type in session state
keys = list(circuit_types.keys())
# Validate or initialize circuit_type
if 'circuit_type' not in st.session_state or st.session_state.circuit_type not in keys:
    st.session_state.circuit_type = keys[0] # Default to first type if invalid or not set

# Determine the initial index for the selectbox based on the current session state
try:
    # Use the circuit_type from session state to determine the index
    selected_index = keys.index(st.session_state.circuit_type)
except ValueError:
    selected_index = 0 # Default to the first item if the current type isn't in the list

# Circuit type selector - always enabled
new_circuit_type = st.selectbox(
    "Circuit Type",
    keys, # Use the keys directly
    index=selected_index,
    key="circuit_type_selector" # Use a distinct key to track changes
)

# Handle change in selection
if new_circuit_type != st.session_state.circuit_type:
    st.session_state.circuit_type = new_circuit_type
    # If the user selects a different type, clear the loaded code ID and variable
    st.session_state.current_code_id = None
    st.rerun() # Rerun to load the default code for the new type

# Initialize current_code to None before potentially using it
current_code = None

# Load code based on state if an ID exists
if st.session_state.current_code_id is not None:
    current_code = st.session_state.db_manager.get_code_by_id(st.session_state.current_code_id)
    if not current_code:
        # If code ID is invalid or code not found, reset the ID and log a warning
        st.warning(f"Code with ID {st.session_state.current_code_id} not found. Resetting.")
        st.session_state.current_code_id = None

# Display the code editor
# Use unique keys for the text_area to ensure it updates correctly
editor_key = "vhdl_editor" # Base key
if current_code and st.session_state.current_code_id is not None:
    # If a code is loaded from history (and type wasn't just changed), use its content
    editor_key = f"vhdl_editor_hist_{st.session_state.current_code_id}"
    code_to_display = current_code.get('code', '')
elif st.session_state.circuit_type != "Custom Circuit":
    # Load default code for the selected type (if not custom and no history loaded)
    editor_key = f"vhdl_editor_default_{st.session_state.circuit_type}"
    default_file_path = circuit_types.get(st.session_state.circuit_type)
    if default_file_path:
        try:
            with open(default_file_path, "r") as f:
                code_to_display = f.read()
        except FileNotFoundError:
            st.error(f"Default code file not found: {default_file_path}")
            code_to_display = ""
            editor_key = "vhdl_editor_error"
        except Exception as e:
            st.error(f"Error loading default code: {e}")
            code_to_display = ""
            editor_key = "vhdl_editor_exception"
    else:
        st.error(f"No default code path defined for {st.session_state.circuit_type}")
        code_to_display = ""
        editor_key = "vhdl_editor_no_path"
else:
    # Custom circuit selected, and no history loaded
    editor_key = "vhdl_editor_custom"
    st.subheader("Custom VHDL Code")
    code_to_display = "" # Start with empty for custom

vhdl_code = st.text_area("VHDL Code", code_to_display, height=400, key=editor_key)

# Add option to save code
col1, col2 = st.columns(2)
with col1:
    save_name = st.text_input("Circuit Name (for saving)", value="My Circuit" if not current_code else current_code.get('name', 'My Circuit'))
with col2:
    if st.button("Save Circuit"):
        if current_code:
            # Update existing code
            st.session_state.db_manager.update_code(
                st.session_state.current_code_id,
                name=save_name,
                code_content=vhdl_code,
                description=f"Updated {st.session_state.circuit_type} circuit"
            )
            st.success(f"Updated circuit: {save_name}")
        else:
            # Add new code
            code_id = st.session_state.db_manager.add_code(
                save_name,
                vhdl_code,
                "User",
                f"User created {st.session_state.circuit_type} circuit"
            )
            st.session_state.current_code_id = code_id
            st.success(f"Saved new circuit: {save_name}")
        
        # Refresh code history
        st.session_state.code_history = st.session_state.db_manager.get_code_history()

# Create a temporary file with the VHDL code
temp_dir = tempfile.mkdtemp()
vhdl_file_path = os.path.join(temp_dir, "circuit.vhd")
with open(vhdl_file_path, "w") as f:
    f.write(vhdl_code)

# Create tabs for code editing, preview, and schema
code_tab, preview_tab, schema_tab = st.tabs(["Code Editor", "Code Preview", "Circuit Schema"])

with code_tab:
    # If we're already in code editing mode, this content has been shown above
    st.write("Edit the VHDL code in the text area above")
    
    # Add a syntax highlighting helper
    if st.checkbox("Show VHDL Syntax Guide"):
        st.info("""
        **VHDL Syntax Guide**
        
        **Entity Declaration**:
        ```vhdl
        entity ENTITY_NAME is
          port (
            SIGNAL_NAME : in std_logic;  -- Input signal
            SIGNAL_NAME : out std_logic  -- Output signal
          );
        end entity ENTITY_NAME;
        ```
        
        **Architecture Body**:
        ```vhdl
        architecture ARCH_NAME of ENTITY_NAME is
          -- Signal declarations
          signal INTERNAL_SIGNAL : std_logic := '0';
        begin
          -- Concurrent statements or processes
          
          -- Process example
          process (SENSITIVITY_LIST)
          begin
            if CONDITION then
              SIGNAL <= VALUE;
            end if;
          end process;
        end architecture ARCH_NAME;
        ```
        """)

with preview_tab:
    st.subheader("VHDL Code Preview")
    st.code(vhdl_code, language="vhdl")
    
    # Initialize simulator to detect circuit type and signals
    simulator = VHDLSimulator(vhdl_file_path)
    circuit_type = simulator.detect_circuit_type()
    
    # Determine input signals using the detector
    input_signals, output_signals = simulator.detect_signals()
    
    # Display circuit info
    if circuit_type != "Unknown":
        st.info(f"Detected circuit type: {circuit_type}")
    else:
        st.warning("Unknown circuit type. Signal detection may be limited.")
        
    st.write(f"Input signals: {', '.join(input_signals)}")
    st.write(f"Output signals: {', '.join(output_signals)}")

with schema_tab:
    st.subheader("Circuit Schematic")
    
    try:
        # Generate schema figure
        schema_fig = generate_schema(vhdl_code)
        st.plotly_chart(schema_fig, use_container_width=True)
        
        st.info("The schematic shows the connections between gates in the circuit. Blue dots represent inputs, green squares represent logic gates, and red dots represent outputs.")
    except Exception as e:
        st.error(f"Could not generate circuit schema: {str(e)}")
        st.info("Schema generation works best with standard circuit types (JK flip-flop, D flip-flop, SR latch).")

# Custom input pattern section (only shown when "Custom" test pattern is selected)
custom_patterns = {}
if test_pattern == "Custom":
    st.subheader("Custom Input Patterns")
    
    for signal in input_signals:
        if signal == "Clk":
            st.write("Clock signal is automatically generated")
            continue
            
        st.write(f"Signal: {signal}")
        pattern_type = st.selectbox(
            f"Pattern type for {signal}",
            ["Constant", "Alternating", "Custom"],
            key=f"pattern_type_{signal}"
        )
        
        if pattern_type == "Constant":
            value = st.selectbox(f"Value for {signal}", ["0", "1"], key=f"constant_value_{signal}")
            custom_patterns[signal] = [value] * num_cycles
        
        elif pattern_type == "Alternating":
            frequency = st.slider(
                f"Change frequency for {signal} (cycles)",
                min_value=1,
                max_value=num_cycles // 2,
                value=5,
                key=f"alt_freq_{signal}"
            )
            
            pattern = []
            for i in range(num_cycles):
                if (i // frequency) % 2 == 0:
                    pattern.append("0")
                else:
                    pattern.append("1")
            custom_patterns[signal] = pattern
            
        elif pattern_type == "Custom":
            pattern_str = st.text_input(
                f"Enter pattern for {signal} (0s and 1s, e.g., '00110101')",
                "01010101",
                key=f"custom_pattern_{signal}"
            )
            # Validate pattern
            if not all(c in "01" for c in pattern_str):
                st.error(f"Invalid pattern for {signal}. Use only 0s and 1s.")
            else:
                # Extend or truncate pattern to match num_cycles
                pattern = list((pattern_str * (num_cycles // len(pattern_str) + 1))[:num_cycles])
                custom_patterns[signal] = pattern

# Run simulation button
if st.button("Run Simulation"):
    with st.spinner("Running simulation..."):
        try:
            # Initialize simulator
            simulator = VHDLSimulator(vhdl_file_path)
            
            # Run simulation with appropriate test pattern
            if test_pattern == "All modes (hold, set, reset, toggle)":
                # Predefined test for JK flip-flop covering all modes
                simulation_data = simulator.run_jk_test(num_cycles, clock_frequency)
            else:
                # Run with custom patterns
                simulation_data = simulator.run_with_custom_patterns(
                    custom_patterns,
                    num_cycles,
                    clock_frequency
                )
                
            # Save simulation result to database
            simulation_params = {
                'clock_frequency': clock_frequency,
                'simulation_time': simulation_time,
                'num_cycles': num_cycles,
                'test_pattern': test_pattern
            }
            
            # If we have a current code ID, link the simulation to it
            if st.session_state.current_code_id:
                st.session_state.db_manager.save_simulation_result(
                    st.session_state.current_code_id,
                    vhdl_code,
                    simulation_data,
                    simulation_params
                )
            else:
                # Save as a new code entry if not already in database
                code_id = st.session_state.db_manager.add_code(
                    f"Simulation {datetime.now().strftime('%Y-%m-%d %H:%M')}",
                    vhdl_code,
                    "Simulation",
                    f"Circuit simulated with {test_pattern} pattern"
                )
                st.session_state.current_code_id = code_id
                
                # Link the simulation to the new code
                st.session_state.db_manager.save_simulation_result(
                    code_id,
                    vhdl_code,
                    simulation_data,
                    simulation_params
                )
            
            # Display results
            st.subheader("Simulation Results")
            
            # Convert simulation data to DataFrame for display
            df = pd.DataFrame(simulation_data)
            
            # Display data table
            st.write("Signal Values:")
            st.dataframe(df)
            
            # Generate and display waveform with time in nanoseconds
            st.subheader("Waveform Display (10ns resolution)")
            
            # Add time in nanoseconds column for display
            df_display = df.copy()
            df_display['Time (ns)'] = df_display['Time'] * 10
            
            fig = generate_waveform(df, input_signals, output_signals)
            st.plotly_chart(fig, use_container_width=True)
            
            # State transitions table (for JK flip-flop)
            if "JK_FF" in vhdl_code:
                st.subheader("State Transitions")
                transitions = []
                
                for i in range(1, len(df)):
                    if df["Clk"][i-1] == "0" and df["Clk"][i] == "1":  # Rising edge
                        # Determine JK mode
                        j_val = df["J"][i]
                        k_val = df["K"][i]
                        mode = "Hold"
                        if j_val == "0" and k_val == "0":
                            mode = "Hold"
                        elif j_val == "0" and k_val == "1":
                            mode = "Reset"
                        elif j_val == "1" and k_val == "0":
                            mode = "Set"
                        else:  # j_val == "1" and k_val == "1"
                            mode = "Toggle"
                            
                        transitions.append({
                            "Time": i,
                            "Time (ns)": i * 10,  # Convert to nanoseconds
                            "J": j_val,
                            "K": k_val,
                            "Previous Q": df["Q"][i-1],
                            "New Q": df["Q"][i],
                            "Mode": mode,
                        })
                
                transitions_df = pd.DataFrame(transitions)
                if not transitions_df.empty:
                    st.dataframe(transitions_df)
                else:
                    st.write("No state transitions detected in the simulation.")
            
        except Exception as e:
            error_msg = str(e)
            st.error(f"Simulation error: {error_msg}")
            
            # Log the error to the database
            if st.session_state.current_code_id:
                st.session_state.db_manager.log_error(
                    error_msg,
                    "Simulation Error",
                    vhdl_code,
                    {
                        'clock_frequency': clock_frequency,
                        'simulation_time': simulation_time,
                        'num_cycles': num_cycles,
                        'test_pattern': test_pattern
                    }
                )

# Function removed as it's no longer needed

# Add explanatory information
st.markdown("""
---
---
### About JK Flip-Flop

The JK flip-flop is a bistable multivibrator with two inputs, J and K, and two outputs, Q and Q̅.  
It operates according to the following truth table:

| J | K | Operation           |
|---|---|---------------------|
| 0 | 0 | Hold (no change)    |
| 0 | 1 | Reset (Q = 0)       |
| 1 | 0 | Set (Q = 1)         |
| 1 | 1 | Toggle (Q = not Q)  |

The flip-flop changes state only on the rising edge of the clock signal.

---

### About D Flip-Flop

The D (Data or Delay) flip-flop has a single data input (D) and one output (Q).  
It stores the value of D at the moment of the clock edge and holds it until the next clock event:

| D | Q(n+1) | Operation      |
|---|--------|---------------|
| 0 |   0    | Reset         |
| 1 |   1    | Set           |

- Q(n+1) = D (the next state equals the input at the clock edge).

---

### About SR Latch

The SR (Set-Reset) latch is a basic memory element with two inputs, S (Set) and R (Reset), and two outputs, Q and Q̅.  
It is asynchronous and maintains its state until inputs change:

| S | R | Q (Next State) | Operation      |
|---|---|----------------|---------------|
| 0 | 0 | Previous Q     | Hold          |
| 0 | 1 | 0              | Reset         |
| 1 | 0 | 1              | Set           |
| 1 | 1 | Invalid        | Forbidden     |

- The "forbidden" state (S=1, R=1) should be avoided as it leads to an invalid output.

---

**Summary Table**

| Device      | Inputs      | Outputs | Key Operation                        |
|-------------|-------------|---------|--------------------------------------|
| JK Flip-Flop| J, K        | Q, Q̅   | Set, Reset, Toggle, Hold             |
| D Flip-Flop | D           | Q, Q̅   | Q follows D on clock edge            |
| SR Latch    | S, R        | Q, Q̅   | Set, Reset, Hold, (Forbidden state)  |
""")

st.markdown("""
---
### How to Use This Platform

1. Review or modify the VHDL code
2. Configure simulation parameters in the sidebar
3. Choose a test pattern or create custom input patterns
4. Click "Run Simulation" to see the results
5. Analyze the waveform and state transitions
""")
