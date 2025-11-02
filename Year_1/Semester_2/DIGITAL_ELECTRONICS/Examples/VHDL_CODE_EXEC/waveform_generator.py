import plotly.graph_objects as go
import pandas as pd
import numpy as np

def generate_waveform(data, input_signals, output_signals):
    """
    Generate a waveform display using Plotly.
    
    Args:
        data: DataFrame containing signal values
        input_signals: List of input signal names
        output_signals: List of output signal names
        
    Returns:
        Plotly Figure object
    """
    # Convert data to DataFrame if it's a dictionary
    if isinstance(data, dict):
        df = pd.DataFrame(data)
    else:
        df = data
    
    # Create figure with bigger size
    fig = go.Figure()
    
    # Signal height settings
    signal_height = 1.0
    spacing = 1.5
    
    # Set color scheme
    input_color = "blue"
    output_color = "red"
    
    # Add time axis in nanoseconds (assuming 10ns per cycle)
    time_ns = df['Time'] * 10
    
    # Plot signals
    y_pos = 0
    all_signals = []
    
    # Add input signals
    for signal in input_signals:
        if signal in df.columns:
            y_pos -= spacing
            all_signals.append((signal, y_pos, input_color))
    
    # Add output signals
    for signal in output_signals:
        if signal in df.columns:
            y_pos -= spacing
            all_signals.append((signal, y_pos, output_color))
    
    # Draw signal plots
    for signal_name, signal_y, signal_color in all_signals:
        # Create a step plot for each signal
        y_values = []
        x_values = []
        
        for i, value in enumerate(df[signal_name]):
            if i > 0:
                # Add a vertical line at the transition point
                x_values.append(time_ns[i])
                y_values.append(get_digital_value(df[signal_name][i-1], signal_y, signal_height))
            
            x_values.append(time_ns[i])
            y_values.append(get_digital_value(value, signal_y, signal_height))
            
            # Add point for the end of the plot
            if i == len(df[signal_name]) - 1:
                x_values.append(time_ns[i] + 10)  # Extend 10ns past the last point
                y_values.append(get_digital_value(value, signal_y, signal_height))
        
        # Add the signal trace
        fig.add_trace(go.Scatter(
            x=x_values, 
            y=y_values,
            mode='lines',
            line=dict(color=signal_color, width=2),
            name=signal_name,
            hoverinfo='name+text',
            text=[f"{signal_name}={v}" for v in df[signal_name]]
        ))
        
        # Add signal label
        fig.add_annotation(
            x=-5,  # Slightly to the left of the y-axis
            y=signal_y,
            text=signal_name,
            showarrow=False,
            font=dict(color=signal_color, size=14),
            xanchor="right"
        )
    
    # Set layout
    fig.update_layout(
        title="Waveform Display (10ns resolution)",
        xaxis_title="Time (ns)",
        height=100 + (len(all_signals) * 100),  # Dynamic height based on number of signals
        width=900,
        showlegend=False,
        plot_bgcolor='white',
        xaxis=dict(
            zeroline=False,
            showgrid=True,
            gridcolor='lightgray',
            tickmode='linear',
            dtick=100,  # Tick every 100ns
            range=[0, max(time_ns) + 10]  # Add some padding
        ),
        yaxis=dict(
            zeroline=False,
            showticklabels=False,
            showgrid=False,
            range=[y_pos - spacing, spacing]
        ),
        margin=dict(l=50, r=20, t=50, b=50)
    )
    
    # Add grid lines for better readability
    for i in range(0, int(max(time_ns) + 100), 100):
        fig.add_shape(
            type="line",
            x0=i, y0=y_pos - spacing,
            x1=i, y1=spacing,
            line=dict(color="lightgray", width=1, dash="dash")
        )
    
    return fig
    
def get_digital_value(signal_value, y_offset, height):
    """Convert digital signal values to y-coordinates for plotting."""
    if signal_value == '1':
        return y_offset + height/2
    elif signal_value == '0':
        return y_offset - height/2
    else:
        # For undefined values like 'X'
        return y_offset