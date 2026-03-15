import os
import subprocess
import re
import numpy as np
import matplotlib
try:
    matplotlib.use('TkAgg')
except ImportError:
    matplotlib.use('Agg')

import matplotlib.pyplot as plt

def pingTargets(targets: list, sizes: list, count: int = 30) -> dict:
    """
    Executes iterative ping searches to collect latency metrics across hosts.

    Args:
        targets (list): Hostnames or IP addresses to probe via ICMP.
        sizes (list): Integer list of payload sizes (bytes) to test.
        count (int): Number of echo requests to transmit per configuration.

    Returns:
        dict: A structured mapping of targets and sizes to RTT statistics.
    """
    results = {}
    for target in targets:
        results[target] = {}
        for size in sizes:
            # Executes the system ping command with specified data size and count.
            cmd = ["ping", "-s", str(size), "-c", str(count), target]
            try:
                process_result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
                
                # Parses the min/avg/max/mdev string from the ping summary output.
                match = re.search(r"(\d+\.?\d*)/(\d+\.?\d*)/(\d+\.?\d*)", process_result.stdout)
                if match:
                    results[target][size] = {
                        "min": float(match.group(1)),
                        "avg": float(match.group(2)),
                        "max": float(match.group(3))
                    }
                else:
                    results[target][size] = None  # Indicates failure to parse or reach host.
            except (subprocess.TimeoutExpired, Exception):
                results[target][size] = None  # Handles network timeouts or process errors.
                
    return results

def displayResults(results: dict, targets: list, sizes: list):
    """
    Outputs a human-readable table containing the summarized network metrics.

    Args:
        results (dict): The data structure containing collected RTT values.
        targets (list): The specific hosts to include in the display output.
        sizes (list): The specific packet sizes to include in the display output.
    """
    print(f"{'Target':<20} {'Size':>6} {'Min':>8} {'Avg':>8} {'Max':>8}")
    print("-" * 55)
    for target in targets:
        for size in sizes:
            data_point = results.get(target, {}).get(size)
            if data_point:
                print(f"{target:<20} {size:>6} {data_point['min']:>8.2f} {data_point['avg']:>8.2f} {data_point['max']:>8.2f}")

def visualizeResults(results: dict, targets: list, sizes: list):
    """
    Constructs a 3D visualization of average latency relative to host and size.

    Args:
        results (dict): The data structure containing collected RTT values.
        targets (list): The hostnames serving as the X-axis categories.
        sizes (list): The packet sizes (bytes) serving as the Y-axis categories.
    """
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')

    x_indices = np.arange(len(targets))
    y_indices = np.arange(len(sizes))
    x_grid, y_grid = np.meshgrid(x_indices, y_indices)
    
    # Flattens grids to prepare for 3D bar representation.
    x_flat = x_grid.flatten()
    y_flat = y_grid.flatten()
    z_baseline = np.zeros_like(x_flat)
    
    latency_values = []
    for s_idx, size in enumerate(sizes):
        for t_idx, target in enumerate(targets):
            # Fallback to 0 if data is missing for a specific probe point.
            val = results[target][size]["avg"] if results.get(target) and results[target].get(size) else 0
            latency_values.append(val)
    
    # Renders the 3D bars with custom styling for clarity.
    ax.bar3d(x_flat, y_flat, z_baseline, 0.5, 0.5, latency_values, shade=True, color='#4A90E2')

    ax.set_xticks(x_indices)
    ax.set_xticklabels(targets)
    ax.set_yticks(y_indices)
    ax.set_yticklabels([f"{s} B" for s in sizes])
    ax.set_zlabel('Avg RTT (ms)')
    ax.set_title('3D Average Latency Analysis by Target and Payload Size')

    # Ensures the output directory exists before attempting to save graphics.
    output_dir = "images"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    save_path = os.path.join(output_dir, 'rtt_3d_analysis.png')
    plt.savefig(save_path)
    print(f"\nStatistical visualization preserved at: {save_path}")
    plt.show()

if __name__ == "__main__":
    test_hosts = ["google.com", "youtube.com", "wikipedia.org", "uoi.gr"]
    test_sizes = [56, 512, 1024]
    probes_per_config = 5  # Reduced count for faster validation in demonstration.

    ping_stats = pingTargets(test_hosts, test_sizes, probes_per_config)
    displayResults(ping_stats, test_hosts, test_sizes)
    visualizeResults(ping_stats, test_hosts, test_sizes)
