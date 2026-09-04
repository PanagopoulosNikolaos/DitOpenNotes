import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio
from pathlib import Path
import re
import os
import sys

SCRIPT_DIR = Path(__file__).parent.absolute() # Get the absolute path of the script directory.
IMG_DIR = SCRIPT_DIR / "images" # Get the absolute path of the images directory.

#=================================================
# Constants and Configuration
# IMG_DIR = "./images" # improved version on line 10
PING_FILE = "./ping_output.txt"
SHOW_PLOTS = "--show" in sys.argv
PLOT_WIDTH = 1400  #

pio.templates.default = "plotly_dark"
COLOR_MEASURED = "#00D1FF"  # Electric Blue
COLOR_THEORY = "#FF007A"    # Pink
COLOR_JITTER = "#BFFF00"    # Lime Green
BG_COLOR = "#0E1117" 
GRID_COLOR = "rgba(255,255,255,0.08)"
#=================================================



def extractPingData(file_path):
    """
    Parses ping output to extract RTT values.

    Args:
        file_path (str): Path to the txt file.

    Returns:
        list(float): Individual delay measurements in milliseconds.
    """
    delays = []
    if not os.path.exists(file_path):
        return []
    with open(file_path, 'r') as f:
        for line in f:
            match = re.search(r"time=([\d.]+) ms", line)
            if match:
                delays.append(float(match.group(1)))
    return delays

def saveFig(fig, name):
    """
    Saves figure as PNG and optionally shows it.

    Args:
        fig (plotly.graph_objects.Figure): The figure object to save.
        name (str): Filename for the exported image.

    Returns:
        None: Does not return any value.
    """
    path = os.path.join(IMG_DIR, f"{name}.png")
    fig.write_image(path, scale=4)
    print(f"Exported: {path}")
    if SHOW_PLOTS:
        fig.show()

def getBaseLayout(title):
    """
    Returns a consistent styling for all plots.

    Args:
        title (str): Title text for the plot.

    Returns:
        dict: Layout configuration for Plotly figures.
    """
    return dict(
        title=dict(text=title, font=dict(size=22, color='white', family="Outfit, Sans-serif")),
        paper_bgcolor=BG_COLOR,
        plot_bgcolor=BG_COLOR,
        xaxis=dict(gridcolor=GRID_COLOR, zeroline=False),
        yaxis=dict(gridcolor=GRID_COLOR, zeroline=False),
        font=dict(color="white"),
        margin=dict(l=60, r=40, t=100, b=60),
        width=PLOT_WIDTH
    )

def generateDelaySubplots():
    """
    Creates a combined 3-panel plot for Distance, Size, and Rate.

    Returns:
        None: Does not return any value.
    """
    fig = make_subplots(
        rows=1, cols=3, 
        subplot_titles=("Delay vs. Distance", "Delay vs. Packet Size", "Delay vs. Rate"),
        horizontal_spacing=0.1
    )

    # Data 1: Distance 
    d_x = [10, 100, 500, 1000] # Distance (d) in km
    d_m = [1.6, 2.09, None, 7.03] # Measured Delay (A1) in ms
    d_c = [1.5982, 1.9196, 3.3482, 5.1339] # Calculated Delay (A2) in ms
    
    fig.add_trace(go.Scatter(x=d_x, y=d_m, mode='lines+markers', name='Measured', line=dict(color=COLOR_MEASURED), marker=dict(size=8)), row=1, col=1)
    fig.add_trace(go.Scatter(x=d_x, y=d_c, mode='lines+markers', name='Theoretical', line=dict(color=COLOR_THEORY, dash='dash')), row=1, col=1)

    # Data 2: Size (100, 500, 1000, 2000)
    s_x = [100, 500, 1000, 2000] # Packet Size (L) in Bytes
    s_m = [1.6, 7.74, 15.43, None] # Measured Delay (A1) in ms
    s_c = [1.5982, 7.8482, 15.6607, 31.2857] # Calculated Delay (A2) in ms
    
    fig.add_trace(go.Scatter(x=s_x, y=s_m, mode='lines+markers', line=dict(color=COLOR_MEASURED), showlegend=False), row=1, col=2)
    fig.add_trace(go.Scatter(x=s_x, y=s_c, mode='lines+markers', line=dict(color=COLOR_THEORY, dash='dash'), showlegend=False), row=1, col=2)

    # Data 3: Rate (Log scale visualization)
    r_labels = ["512K", "1M", "10M", "100M"] # Rate (R) in Kbps
    r_m = [1.6, 0.85, 0.14, 0.07] # Measured Delay (A1) in ms
    r_c = [7.8482, 4.0357, 0.4357, 0.0757] # Calculated Delay (A2) in ms
    
    fig.add_trace(go.Scatter(x=r_labels, y=r_m, mode='lines+markers', line=dict(color=COLOR_MEASURED), showlegend=False), row=1, col=3)
    fig.add_trace(go.Scatter(x=r_labels, y=r_c, mode='lines+markers', line=dict(color=COLOR_THEORY, dash='dash'), showlegend=False), row=1, col=3)

    fig.update_layout(getBaseLayout("Network Performance Comparison: Measured vs. Theoretical"))
    fig.update_xaxes(title_text="Distance (km)", row=1, col=1)
    fig.update_xaxes(title_text="Packet Size (Bytes)", row=1, col=2)
    fig.update_xaxes(title_text="Transmission Rate", row=1, col=3)
    fig.update_yaxes(title_text="Delay (ms)", row=1, col=1)
    
    saveFig(fig, "combined_delay_analysis")

def generateJitterSubplots(delays):
    """
    Creates a 4-panel Jitter investigation board.

    Args:
        delays (list(float)): Sequence of RTT measurements.

    Returns:
        None: Does not return any value.
    """
    if not delays:
        print("No ping data found.")
        return

    # Calculate Jitter sequence
    jitter_seq = [abs(delays[i] - delays[i-1]) for i in range(1, len(delays))]
    avg_jitter = sum(jitter_seq) / len(jitter_seq)

    fig = make_subplots(
        rows=2, cols=2,
        subplot_titles=("Packet Delay (RTT)", "Inter-Packet Jitter", "RTT Distribution", "Jitter Deviation"),
        vertical_spacing=0.15,
        horizontal_spacing=0.1
    )

    # 1. RTT Line Plot
    fig.add_trace(go.Scatter(y=delays, mode='lines', name='RTT', line=dict(color=COLOR_MEASURED, width=2)), row=1, col=1)
    
    # 2. Jitter Bar Plot
    fig.add_trace(go.Bar(y=jitter_seq, name='Jitter', marker_color=COLOR_JITTER, opacity=0.7), row=1, col=2)
    
    # 3. RTT Histogram
    fig.add_trace(go.Histogram(x=delays, name='RTT Dist', marker_color=COLOR_MEASURED, nbinsx=20), row=2, col=1)
    
    # 4. Box/Violin plot for jitter
    fig.add_trace(go.Box(y=jitter_seq, name='Jitter Spread', marker_color=COLOR_JITTER, boxmean='sd'), row=2, col=2)

    full_title = f"Network Jitter Analysis (Mean Jitter: {avg_jitter:.4f} ms)"
    fig.update_layout(getBaseLayout(full_title))
    fig.update_layout(showlegend=False, height=900)
    
    saveFig(fig, "combined_jitter_analysis")

if __name__ == "__main__":
    
    # Part 1: Delay Analysis
    generateDelaySubplots()
    
    # Part 2: Jitter Analysis
    delays = extractPingData(PING_FILE)
    generateJitterSubplots(delays)
    
    print("\nAll plots have been generated and saved to the 'images' folder.")
    if not SHOW_PLOTS:
        print("NOTE: Run with '--show' argument to open pop-up windows.")
