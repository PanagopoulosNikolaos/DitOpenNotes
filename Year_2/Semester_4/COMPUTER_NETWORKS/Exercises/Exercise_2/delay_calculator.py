def calculateDelay(packet_size_bytes, rate_kbps, distance_km, prop_speed):
    """
    Calculates the total network delay including transmission and propagation.

    Args:
        packet_size_bytes (int): The length of the packet in bytes.
        rate_kbps (float): The transmission rate in kilobits per second.
        distance_km (float): The distance between nodes in kilometers.
        prop_speed (float): The propagation speed in meters per second.

    Returns:
        float: The total calculated delay in milliseconds.
    """
    transmission_delay = (packet_size_bytes * 8) / (rate_kbps * 1000) # Converts bytes to bits and kbps to bps.
    propagation_delay = (distance_km * 1000) / prop_speed # Converts km to meters.
    return (transmission_delay + propagation_delay) * 1000 # Returns total delay in ms.

# Constants and parameters
propagation_speed = 2.8e8 # Speed used in the provided formulas.

# Table 1-1: Delay vs. Distance (R = 512 Kbps, L = 100 Bytes)
print("#### Table 1-1: Delay vs. Distance (Parameters: R = 512 Kbps, L = 100 Bytes)")
print(f"{'Distance (d)':<15} | {'Measured Delay (A1)':<20} | {'Calculated Delay (A2)':<20}")
print("-" * 60)
distances = [10, 100, 500, 1000]
measured_1_1 = ["1.6 ms", "1.090 ms", "4.06 ms", "6.56 ms"]
for d, m in zip(distances, measured_1_1):
    calc = calculateDelay(100, 512, d, propagation_speed)
    print(f"{d:<3} Km{'':<10} | {m:<20} | {calc:.4f} ms")

# Table 1-2: Delay vs. Packet Size (d = 10 Km, R = 512 Kbps)
print("\n#### Table 1-2: Delay vs. Packet Size (Parameters: d = 10 Km, R = 512 Kbps)")
print(f"{'Packet Size (L)':<15} | {'Measured Delay (A1)':<20} | {'Calculated Delay (A2)':<20}")
print("-" * 60)
packet_sizes = [100, 500, 1000, 2000] # 1 KB and 2 KB treated as 1000 and 2000 bytes per prompt formulas.
labels_1_2 = ["100 Bytes", "500 Bytes", "1 KB", "2 KB"]
measured_1_2 = ["1.612 ms", "7.86 ms", "16.05 ms", "32.05 ms"]
for size, label, m in zip(packet_sizes, labels_1_2, measured_1_2):
    calc = calculateDelay(size, 512, 10, propagation_speed)
    print(f"{label:<15} | {m:<20} | {calc:.4f} ms")

# Table 1-3: Delay vs. Transmission Rate (d = 10 Km, L = 500 Bytes)
print("\n#### Table 1-3: Delay vs. Transmission Rate (Parameters: d = 10 Km, L = 500 Bytes)")
print(f"{'Rate (R)':<15} | {'Measured Delay (A1)':<20} | {'Calculated Delay (A2)':<20}")
print("-" * 60)
rates = [512, 1000, 10000, 100000]
labels_1_3 = ["512 Kbps", "1 Mbps", "10 Mbps", "100 Mbps"]
for r, label in zip(rates, labels_1_3):
    calc = calculateDelay(500, r, 10, propagation_speed)
    print(f"{label:<15} | {'N/A':<20} | {calc:.4f} ms")
