import subprocess
import tempfile
import os
import shutil
import pandas as pd
import time
from collections import defaultdict

class VHDLSimulator:
    """
    A class that handles VHDL simulation using MyHDL principles without direct dependency.
    This is a simplified simulator that emulates the behavior of VHDL components.
    """
    
    def __init__(self, vhdl_file):
        """
        Initialize the simulator with the VHDL file path.
        
        Args:
            vhdl_file (str): Path to the VHDL file to simulate
        """
        self.vhdl_file = vhdl_file
        self.entity_name = self._extract_entity_name()
        
    def _extract_entity_name(self):
        """Extract the entity name from the VHDL file."""
        with open(self.vhdl_file, 'r') as f:
            content = f.read().lower()
            
        # Simple parsing to extract entity name
        if 'entity ' in content and ' is' in content:
            start_idx = content.find('entity ') + 7
            end_idx = content.find(' is', start_idx)
            return content[start_idx:end_idx].strip()
        
        # Default to JK_FF if not found
        return "JK_FF"
        
    def detect_circuit_type(self):
        """
        Detect the type of circuit from the VHDL file.
        
        Returns:
            str: The detected circuit type ('JK_FF', 'D_FF', 'SR_Latch', or 'Unknown')
        """
        entity_name = self._extract_entity_name().upper()
        
        if entity_name == "JK_FF":
            return "JK_FF"
        elif entity_name == "D_FF":
            return "D_FF"
        elif entity_name == "SR_LATCH":
            return "SR_Latch"
        else:
            return "Unknown"
            
    def detect_signals(self):
        """
        Detect input and output signals from the VHDL file.
        
        Returns:
            tuple: (input_signals, output_signals)
        """
        circuit_type = self.detect_circuit_type()
        
        if circuit_type == "JK_FF":
            return ["J", "K", "Clk"], ["Q", "Qbar"]
        elif circuit_type == "D_FF":
            return ["D", "Clk"], ["Q", "Qbar"]
        elif circuit_type == "SR_Latch":
            return ["S", "R"], ["Q", "Qbar"]
        else:
            # For unknown circuits, try to parse the port declarations
            # This is a simplified implementation
            input_signals = []
            output_signals = []
            
            with open(self.vhdl_file, 'r') as f:
                content = f.read().lower()
                
            # Try to find the port declarations
            if 'port (' in content and ');' in content:
                port_start = content.find('port (') + 6
                port_end = content.find(');', port_start)
                port_section = content[port_start:port_end].strip()
                
                # Extract signal names and directions
                for line in port_section.split(';'):
                    if ':' not in line:
                        continue
                        
                    signal_names, signal_info = line.split(':', 1)
                    signal_names = [name.strip() for name in signal_names.split(',')]
                    
                    if 'in' in signal_info:
                        input_signals.extend(signal_names)
                    elif 'out' in signal_info:
                        output_signals.extend(signal_names)
            
            # If parsing failed, return default signals
            if not input_signals and not output_signals:
                return ["Clock", "Input"], ["Output"]
                
            return input_signals, output_signals
    
    def run_jk_test(self, num_cycles, clock_frequency):
        """
        Run a JK flip-flop test covering all modes: hold, set, reset, toggle.
        
        Args:
            num_cycles (int): Number of clock cycles to simulate
            clock_frequency (int): Clock frequency in Hz
            
        Returns:
            dict: Simulation results
        """
        # Create signals dictionary to store all values over time
        signals = defaultdict(list)
        
        # Generate clock signal
        clk = ['0', '1'] * (num_cycles // 2 + 1)
        clk = clk[:num_cycles]
        
        # Generate J and K signals to test all modes
        j = []
        k = []
        
        # Ensure we test each mode for a longer period to be clearly visible in the 0-960ns display
        # Test sequence: hold (00), set (10), reset (01), toggle (11), repeat
        # Each mode should last at least 10 clock cycles (100ns) for better visibility
        cycles_per_mode = max(10, num_cycles // 8)  # At least 10 cycles per mode, or we divide the total into 8 parts (4 modes x 2)
        
        # Calculate how many complete mode sets we can fit
        num_complete_sets = num_cycles // (cycles_per_mode * 4)
        remaining_cycles = num_cycles % (cycles_per_mode * 4)
        
        # Generate the pattern for complete sets
        for _ in range(num_complete_sets):
            # Hold mode (J=0, K=0)
            j.extend(['0'] * cycles_per_mode)
            k.extend(['0'] * cycles_per_mode)
            
            # Set mode (J=1, K=0)
            j.extend(['1'] * cycles_per_mode)
            k.extend(['0'] * cycles_per_mode)
            
            # Reset mode (J=0, K=1)
            j.extend(['0'] * cycles_per_mode)
            k.extend(['1'] * cycles_per_mode)
            
            # Toggle mode (J=1, K=1)
            j.extend(['1'] * cycles_per_mode)
            k.extend(['1'] * cycles_per_mode)
        
        # Handle remaining cycles
        remaining_cycles = num_cycles - len(j)
        if remaining_cycles > 0:
            # Add hold mode for any remaining cycles
            j.extend(['0'] * remaining_cycles)
            k.extend(['0'] * remaining_cycles)
        
        # Trim to the requested number of cycles
        j = j[:num_cycles]
        k = k[:num_cycles]
        
        # Save input signals
        signals['Clk'] = clk
        signals['J'] = j
        signals['K'] = k
        
        # Simulate JK flip-flop behavior
        q = ['0']  # Initial state
        qbar = ['1']  # Initial state
        
        for i in range(1, num_cycles):
            # Check for rising edge of clock
            if clk[i-1] == '0' and clk[i] == '1':
                j_val = j[i]
                k_val = k[i]
                prev_q = q[i-1]
                
                # JK flip-flop logic
                if j_val == '0' and k_val == '0':
                    # Hold mode - maintain current state
                    new_q = prev_q
                elif j_val == '0' and k_val == '1':
                    # Reset mode - Q = 0
                    new_q = '0'
                elif j_val == '1' and k_val == '0':
                    # Set mode - Q = 1
                    new_q = '1'
                else:  # j_val == '1' and k_val == '1'
                    # Toggle mode - Q = not Q
                    new_q = '1' if prev_q == '0' else '0'
            else:
                # No clock edge, maintain state
                new_q = q[i-1]
            
            q.append(new_q)
            qbar.append('1' if new_q == '0' else '0')
        
        # Save output signals
        signals['Q'] = q
        signals['Qbar'] = qbar
        
        # Add time column
        signals['Time'] = list(range(num_cycles))
        
        return signals
    
    def run_with_custom_patterns(self, custom_patterns, num_cycles, clock_frequency):
        """
        Run simulation with custom input patterns.
        
        Args:
            custom_patterns (dict): Dictionary of signal name to list of values
            num_cycles (int): Number of clock cycles to simulate
            clock_frequency (int): Clock frequency in Hz
            
        Returns:
            dict: Simulation results
        """
        # Create signals dictionary to store all values over time
        signals = defaultdict(list)
        
        # Generate clock signal if not provided
        if 'Clk' not in custom_patterns:
            custom_patterns['Clk'] = ['0', '1'] * (num_cycles // 2 + 1)
            custom_patterns['Clk'] = custom_patterns['Clk'][:num_cycles]
        
        # Copy input signals to the signals dictionary
        for signal_name, pattern in custom_patterns.items():
            signals[signal_name] = pattern[:num_cycles]
        
        # For JK flip-flop, simulate behavior and generate output signals
        if self.entity_name.lower() == "jk_ff":
            # Initialize output signals
            signals['Q'] = ['0']  # Initial state
            signals['Qbar'] = ['1']  # Initial state
            
            clk = signals['Clk']
            j = signals['J']
            k = signals['K']
            
            # Simulate for each cycle
            for i in range(1, num_cycles):
                # Check for rising edge of clock
                if i > 0 and clk[i-1] == '0' and clk[i] == '1':
                    j_val = j[i]
                    k_val = k[i]
                    prev_q = signals['Q'][i-1]
                    
                    # JK flip-flop logic
                    if j_val == '0' and k_val == '0':
                        # Hold mode - maintain current state
                        new_q = prev_q
                    elif j_val == '0' and k_val == '1':
                        # Reset mode - Q = 0
                        new_q = '0'
                    elif j_val == '1' and k_val == '0':
                        # Set mode - Q = 1
                        new_q = '1'
                    else:  # j_val == '1' and k_val == '1'
                        # Toggle mode - Q = not Q
                        new_q = '1' if prev_q == '0' else '0'
                else:
                    # No clock edge, maintain state
                    new_q = signals['Q'][i-1]
                
                signals['Q'].append(new_q)
                signals['Qbar'].append('1' if new_q == '0' else '0')
        
        # Add time column
        signals['Time'] = list(range(num_cycles))
        
        return signals
