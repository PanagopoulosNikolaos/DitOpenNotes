
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
    Executes ping searches for multiple hosts with varying payload sizes.

    Args:
        targets (list): Hostnames or IP addresses to reach.
        sizes (list): Integer list of payload sizes in bytes.
        count (int): Number of ICMP echoes to transmit per target/size.

    Returns:
        dict: Hierarchical dictionary containing min, avg, max RTT statistics.
    """
    results = {}
    for target in targets:
        results[target] = {}
        for size in sizes:
            cmd = ["ping", "-s", str(size), "-c", str(count), target]
            process_result = subprocess.run(cmd, capture_output=True, text=True)
            
            match = re.search(r"(\d+\.?\d*)/(\d+\.?\d*)/(\d+\.?\d*)", process_result.stdout)
            if match:
                results[target][size] = {
                    "min": float(match.group(1)),
                    "avg": float(match.group(2)),
                    "max": float(match.group(3))
                }
            else:
                results[target][size] = None
    return results

def displayResults(results: dict, targets: list, sizes: list):
    """
    Prints a formatted table of the collected RTT metrics.

    Args:
        results (dict): Population data containing the ping statistics.
        targets (list): The list of targets to include in the table.
        sizes (list): The list of packet sizes to include in the table.
    """
    print(f"{'Target':<20} {'Size':>6} {'Min':>8} {'Avg':>8} {'Max':>8}")
    print("-" * 55)
    for target in targets:
        for size in sizes:
            if results.get(target) and results[target].get(size):
                r = results[target][size]
                print(f"{target:<20} {size:>6} {r['min']:>8.2f} {r['avg']:>8.2f} {r['max']:>8.2f}")

def visualizeResults(results: dict, targets: list, sizes: list):
    """
    Generates a 3D bar chart representing the Average RTT across targets and sizes.

    Args:
        results (dict): Population data containing the ping statistics.
        targets (list): Valid hostnames used as one axis.
        sizes (list): Integer sizes used as the second axis.
    """
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')

    x_positions = np.arange(len(targets))
    y_positions = np.arange(len(sizes))
    x_positions, y_positions = np.meshgrid(x_positions, y_positions)
    
    x_flattened = x_positions.flatten()
    y_flattened = y_positions.flatten()
    z_bottom = np.zeros_like(x_flattened)
    
    rtt_values = []
    for s_idx, size in enumerate(sizes):
        for t_idx, target in enumerate(targets):
            val = results[target][size]["avg"] if results[target][size] else 0
            rtt_values.append(val)
    
    ax.bar3d(x_flattened, y_flattened, z_bottom, 0.5, 0.5, rtt_values, shade=True, color='skyblue')

    ax.set_xticks(np.arange(len(targets)))
    ax.set_xticklabels(targets)
    ax.set_yticks(np.arange(len(sizes)))
    ax.set_yticklabels([f"{s} B" for s in sizes])
    ax.set_zlabel('Avg RTT (ms)')
    ax.set_title('3D Average RTT Analysis per Target and Packet Size')

    plt.savefig('images/rtt_3d_analysis.png')
    print("\nVisualization saved to images/rtt_3d_analysis.png")
    plt.show()

if __name__ == "__main__":
    target_list = ["google.com", "youtube.com", "wikipedia.org", "uoi.gr"]
    size_list = [56, 512, 1024]
    packet_count = 30 

    ping_data = pingTargets(target_list, size_list, packet_count)
    displayResults(ping_data, target_list, size_list)
    visualizeResults(ping_data, target_list, size_list)
