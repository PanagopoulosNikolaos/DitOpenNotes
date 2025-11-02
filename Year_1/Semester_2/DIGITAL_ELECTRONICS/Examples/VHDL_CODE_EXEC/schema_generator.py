import plotly.graph_objects as go
import networkx as nx
import re

def generate_schema(vhdl_code):
    """
    Generate a schematic diagram of the circuit based on VHDL code.
    
    Args:
        vhdl_code (str): VHDL code for the circuit
        
    Returns:
        Plotly Figure object: Schematic diagram
    """
    # Determine circuit type
    circuit_type = detect_circuit_type(vhdl_code)
    
    # Create a graph for the circuit
    G = nx.DiGraph()
    
    # Based on circuit type, create appropriate schematic
    if circuit_type == "JK_FF":
        create_jk_flipflop_schema(G)
    elif circuit_type == "D_FF":
        create_d_flipflop_schema(G)
    elif circuit_type == "SR_Latch":
        create_sr_latch_schema(G)
    else:
        # Generic circuit
        create_generic_schema(G, vhdl_code)
    
    return create_plot_from_graph(G, circuit_type)

def detect_circuit_type(vhdl_code):
    """Detect the type of circuit from the VHDL code."""
    vhdl_code = vhdl_code.lower()
    
    if "entity jk_ff" in vhdl_code or "jk flip" in vhdl_code:
        return "JK_FF"
    elif "entity d_ff" in vhdl_code or "d flip" in vhdl_code:
        return "D_FF"
    elif "entity sr_latch" in vhdl_code or "sr latch" in vhdl_code:
        return "SR_Latch"
    else:
        return "Unknown"

def create_jk_flipflop_schema(G):
    """Create JK flip-flop schema with appropriate gates and connections."""
    # Add nodes
    G.add_node("J", pos=(0, 2), node_type="input")
    G.add_node("K", pos=(0, 0), node_type="input")
    G.add_node("Clk", pos=(0, 1), node_type="input")
    
    G.add_node("AND1", pos=(1, 2), node_type="gate")
    G.add_node("AND2", pos=(1, 0), node_type="gate")
    G.add_node("AND3", pos=(3, 2.5), node_type="gate")
    G.add_node("AND4", pos=(3, -0.5), node_type="gate")
    
    G.add_node("NOR1", pos=(4, 2), node_type="gate")
    G.add_node("NOR2", pos=(4, 0), node_type="gate")
    
    G.add_node("Q", pos=(5, 2), node_type="output")
    G.add_node("Qbar", pos=(5, 0), node_type="output")
    
    # Add edges
    G.add_edge("J", "AND1")
    G.add_edge("K", "AND2")
    G.add_edge("Clk", "AND1")
    G.add_edge("Clk", "AND2")
    
    G.add_edge("AND1", "AND3")
    G.add_edge("AND2", "AND4")
    
    G.add_edge("AND3", "NOR1")
    G.add_edge("AND4", "NOR2")
    
    G.add_edge("NOR1", "Q")
    G.add_edge("NOR2", "Qbar")
    
    G.add_edge("NOR1", "AND4")
    G.add_edge("NOR2", "AND3")
    
    return G

def create_d_flipflop_schema(G):
    """Create D flip-flop schema with appropriate gates and connections."""
    # Add nodes
    G.add_node("D", pos=(0, 1.5), node_type="input")
    G.add_node("Clk", pos=(0, 0.5), node_type="input")
    
    G.add_node("NOT", pos=(1, 1.5), node_type="gate")
    
    G.add_node("AND1", pos=(2, 1.5), node_type="gate")
    G.add_node("AND2", pos=(2, 0.5), node_type="gate")
    
    G.add_node("NOR1", pos=(3, 1.5), node_type="gate")
    G.add_node("NOR2", pos=(3, 0.5), node_type="gate")
    
    G.add_node("Q", pos=(4, 1.5), node_type="output")
    G.add_node("Qbar", pos=(4, 0.5), node_type="output")
    
    # Add edges
    G.add_edge("D", "AND1")
    G.add_edge("D", "NOT")
    G.add_edge("NOT", "AND2")
    G.add_edge("Clk", "AND1")
    G.add_edge("Clk", "AND2")
    
    G.add_edge("AND1", "NOR1")
    G.add_edge("AND2", "NOR2")
    
    G.add_edge("NOR1", "Q")
    G.add_edge("NOR2", "Qbar")
    
    G.add_edge("NOR1", "NOR2")
    G.add_edge("NOR2", "NOR1")
    
    return G

def create_sr_latch_schema(G):
    """Create SR latch schema with appropriate gates and connections."""
    # Add nodes
    G.add_node("S", pos=(0, 1.5), node_type="input")
    G.add_node("R", pos=(0, 0.5), node_type="input")
    
    G.add_node("NOR1", pos=(1.5, 1.5), node_type="gate")
    G.add_node("NOR2", pos=(1.5, 0.5), node_type="gate")
    
    G.add_node("Q", pos=(3, 1.5), node_type="output")
    G.add_node("Qbar", pos=(3, 0.5), node_type="output")
    
    # Add edges
    G.add_edge("S", "NOR1")
    G.add_edge("R", "NOR2")
    
    G.add_edge("NOR1", "Q")
    G.add_edge("NOR2", "Qbar")
    
    G.add_edge("NOR1", "NOR2")
    G.add_edge("NOR2", "NOR1")
    
    return G

def create_generic_schema(G, vhdl_code):
    """Create a generic schema based on extracted ports and signals from VHDL code."""
    # Extract port declarations from VHDL code
    port_pattern = r'port\s*\((.*?)\);'
    port_match = re.search(port_pattern, vhdl_code, re.DOTALL | re.IGNORECASE)
    
    if not port_match:
        # Default fallback if no ports are found
        G.add_node("Input", pos=(0, 1), node_type="input")
        G.add_node("Process", pos=(1, 1), node_type="gate")
        G.add_node("Output", pos=(2, 1), node_type="output")
        G.add_edge("Input", "Process")
        G.add_edge("Process", "Output")
        return G
    
    # Parse the port declaration
    port_text = port_match.group(1)
    port_lines = port_text.split(';')
    
    inputs = []
    outputs = []
    
    for line in port_lines:
        if ':' not in line:
            continue
            
        signal_names, direction = line.split(':', 1)
        signal_names = [s.strip() for s in signal_names.split(',')]
        
        if 'in' in direction.lower():
            inputs.extend(signal_names)
        elif 'out' in direction.lower():
            outputs.extend(signal_names)
    
    # Create a basic layout with inputs on the left, processing in the middle, outputs on the right
    for i, input_name in enumerate(inputs):
        G.add_node(input_name, pos=(0, i+1), node_type="input")
    
    # Add a "process" node in the middle
    G.add_node("Process", pos=(1, len(inputs)/2), node_type="gate")
    
    for i, output_name in enumerate(outputs):
        G.add_node(output_name, pos=(2, i+1), node_type="output")
    
    # Connect inputs to process, and process to outputs
    for input_name in inputs:
        G.add_edge(input_name, "Process")
    
    for output_name in outputs:
        G.add_edge("Process", output_name)
    
    return G

def create_plot_from_graph(G, circuit_type):
    """Create a Plotly figure from a NetworkX graph."""
    pos = nx.get_node_attributes(G, 'pos')
    
    # Create edge trace
    edge_x = []
    edge_y = []
    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x.extend([x0, x1, None])
        edge_y.extend([y0, y1, None])
    
    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(width=2, color='#888'),
        hoverinfo='none',
        mode='lines')
    
    # Create node traces for different types of nodes
    input_trace = go.Scatter(
        x=[], y=[],
        mode='markers+text',
        name='Inputs',
        marker=dict(
            color='blue',
            size=15,
            line=dict(width=2, color='DarkSlateGrey')
        ),
        text=[],
        textposition="bottom center",
        hoverinfo='text'
    )
    
    gate_trace = go.Scatter(
        x=[], y=[],
        mode='markers+text',
        name='Gates',
        marker=dict(
            color='green',
            size=20,
            symbol='square',
            line=dict(width=2, color='DarkSlateGrey')
        ),
        text=[],
        textposition="bottom center",
        hoverinfo='text'
    )
    
    output_trace = go.Scatter(
        x=[], y=[],
        mode='markers+text',
        name='Outputs',
        marker=dict(
            color='red',
            size=15,
            line=dict(width=2, color='DarkSlateGrey')
        ),
        text=[],
        textposition="bottom center",
        hoverinfo='text'
    )
    
    # Populate node traces
    for node in G.nodes():
        x, y = pos[node]
        node_type = G.nodes[node].get('node_type', 'unknown')
        
        if node_type == 'input':
            input_trace['x'] = input_trace['x'] + (x,)
            input_trace['y'] = input_trace['y'] + (y,)
            input_trace['text'] = input_trace['text'] + (node,)
        elif node_type == 'gate':
            gate_trace['x'] = gate_trace['x'] + (x,)
            gate_trace['y'] = gate_trace['y'] + (y,)
            gate_trace['text'] = gate_trace['text'] + (node,)
        elif node_type == 'output':
            output_trace['x'] = output_trace['x'] + (x,)
            output_trace['y'] = output_trace['y'] + (y,)
            output_trace['text'] = output_trace['text'] + (node,)
    
    # Create figure
    fig = go.Figure(data=[edge_trace, input_trace, gate_trace, output_trace],
                   layout=go.Layout(
                       title=f"{circuit_type} Circuit Diagram",
                       showlegend=True,
                       hovermode='closest',
                       margin=dict(b=20, l=5, r=5, t=40),
                       xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                       yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)
                   ))
    
    return fig