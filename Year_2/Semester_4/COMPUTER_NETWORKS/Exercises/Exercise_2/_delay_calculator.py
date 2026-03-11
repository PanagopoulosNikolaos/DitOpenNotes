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
propagation_speed = 2.8e8 # Speed 

def printTables():
    #========================================================================================================
    # Table 1-1: Delay vs. Distance (R = 512 Kbps, L = 100 Bytes)


    print("#### Table 1-1: Delay vs. Distance (Parameters: R = 512 Kbps, L = 100 Bytes)")
    print(f"{'Distance (d)':<15} | {'Measured Delay (A1)':<20} | {'Calculated Delay (A2)':<20}")
    print("-" * 60)
    distances = [10, 100, 500, 1000]
    measured_1_1 = ["1.6 ms", "2.090 ms", " null(`website does not support it`) ", "7.030 ms"]
    for d, m in zip(distances, measured_1_1):
        calc = calculateDelay(100, 512, d, propagation_speed)
        print(f"{d:<3} Km{'':<10} | {m:<20} | {calc:.4f} ms")


    #========================================================================================================
    # Table 1-2: Delay vs. Packet Size (d = 10 Km, R = 512 Kbps)


    print("\n#### Table 1-2: Delay vs. Packet Size (Parameters: d = 10 Km, R = 512 Kbps)")
    print(f"{'Packet Size (L)':<15} | {'Measured Delay (A1)':<20} | {'Calculated Delay (A2)':<20}")
    print("-" * 60)
    packet_sizes = [100, 500, 1000, 2000] # 1 KB and 2 KB treated as 1000 and 2000 bytes per prompt formulas.
    labels_1_2 = ["100 Bytes", "500 Bytes", "1 KB", "2 KB"]
    measured_1_2 = ["1.600 ms", "7.74 ms", "15.430 ms", " null(`website does not support it`)"]
    for size, label, m in zip(packet_sizes, labels_1_2, measured_1_2):
        calc = calculateDelay(size, 512, 10, propagation_speed)
        print(f"{label:<15} | {m:<20} | {calc:.4f} ms")

    #========================================================================================================
    # Table 1-3: Delay vs. Transmission Rate (d = 10 Km, L = 500 Bytes)


    print("\n#### Table 1-3: Delay vs. Transmission Rate (Parameters: d = 10 Km, L = 500 Bytes)")
    print(f"{'Rate (R)':<15} | {'Measured Delay (A1)':<20} | {'Calculated Delay (A2)':<20}")
    print("-" * 60)
    rates = [512, 1000, 10000, 100000]
    labels_1_3 = ["512 Kbps", "1 Mbps", "10 Mbps", "100 Mbps"]
    measured_1_3 = ["1.600 ms", "0.850 ms", "0.140 ms", "0.070 ms"]
    for r, label, m in zip(rates, labels_1_3, measured_1_3):
        calc = calculateDelay(500, r, 10, propagation_speed)
        print(f"{label:<15} | {m:<20} | {calc:.4f} ms")
    #========================================================================================================


def calculateFileTransfer(file_size_kb, rate_mbps=1.0, packet_size_kb=1, header_bytes=40,
                          one_way_delay_ms=40.0):
    """
    Calculates total file transfer time under three transmission strategies.

    Covers Case A (continuous transmission), Case B (stop-and-wait), and
    Case C (TCP slow-start style exponential window growth with infinite bandwidth).

    Args:
        file_size_kb (float): Total file size in kilobytes (using 1 KB = 1024 bytes).
        rate_mbps (float): Link rate in megabits per second (1 Mbps = 10^6 bps).
        packet_size_kb (float): Payload size per packet in kilobytes.
        header_bytes (int): Per-packet header overhead in bytes.
        one_way_delay_ms (float): One-way propagation delay in milliseconds.

    Returns:
        dict: A dictionary with keys 'case_a', 'case_b', 'case_c', each holding
              the total transfer time in milliseconds for the respective case.
    """
    rtt_ms = 2 * one_way_delay_ms                          # Round-trip time in ms.
    rate_bps = rate_mbps * 1e6                              # Converts Mbps to bps.

    file_bytes = file_size_kb * 1024                        # Converts KB to bytes (1 KB = 1024 bytes).
    payload_bytes = packet_size_kb * 1024                   # Payload bytes per packet.
    packet_bytes = payload_bytes + header_bytes             # Total bytes on wire per packet.
    packet_bits = packet_bytes * 8                          # Bits per packet.

    # Transmission time for a single packet at the given rate.
    t_packet_ms = (packet_bits / rate_bps) * 1000

    # Total number of packets required to transmit the file.
    num_packets = file_bytes / payload_bytes

    # Handshake cost is one full RTT before any data is sent.
    handshake_ms = rtt_ms

    sep = "=" * 70

    print(sep)
    print("Part 3: File Transfer Performance")
    print(sep)
    print(f"  File size            : {file_size_kb} KB  ({file_bytes:,.0f} bytes)")
    print(f"  Link rate            : {rate_mbps} Mbps  ({rate_bps:,.0f} bps)")
    print(f"  Packet payload       : {packet_size_kb} KB  ({payload_bytes} bytes)")
    print(f"  Header overhead      : {header_bytes} bytes")
    print(f"  Packet total on wire : {packet_bytes} bytes  ({packet_bits} bits)")
    print(f"  One-way delay        : {one_way_delay_ms} ms  |  RTT = {rtt_ms} ms")
    print(f"  Handshake cost       : 1 RTT = {handshake_ms} ms")
    print(f"  Number of packets    : {num_packets:,.0f}")
    print(f"  Tx time / packet     : {t_packet_ms:.6f} ms")

    #========================================================================================================
    #  Case A
    print(f"\n{'-' * 70}")
    print("Case A: Continuous Transmission")
    print(f"{'-' * 70}")
    print("  Formula: T = Handshake + (TotalBits / Rate) + PropDelay")
    total_bits = file_bytes * 8
    tx_time_ms = (total_bits / rate_bps) * 1000             # Time to clock all bits onto the wire.
    case_a_ms = handshake_ms + tx_time_ms + one_way_delay_ms
    print(f"  Total file bits      : {total_bits:,.0f} bits")
    print(f"  Tx time (all bits)   : {total_bits:,.0f} / {rate_bps:,.0f} = {tx_time_ms:.4f} ms")
    print(f"  Propagation delay    : {one_way_delay_ms} ms  (last bit reaching receiver)")
    print(f"  T = {handshake_ms} + {tx_time_ms:.4f} + {one_way_delay_ms}")
    print(f"  T = {case_a_ms:.4f} ms  ({case_a_ms / 1000:.4f} s)")

    #========================================================================================================
    #  Case B
    print(f"\n{'-' * 70}")
    print("Case B: Stop-and-Wait")
    print(f"{'-' * 70}")
    print("  Methodology: after each packet the sender waits one full RTT.")
    print("  Formula: T = Handshake + N * (TxPacket + RTT)")
    # Each cycle: transmit one packet, then wait for ACK (RTT includes prop there + back).
    # The last packet only needs prop delay to reach receiver, but we count RTT for ACK.
    cycle_ms = t_packet_ms + rtt_ms                         # Time per packet cycle.
    case_b_ms = handshake_ms + num_packets * cycle_ms
    print(f"  Cycle per packet     : {t_packet_ms:.6f} + {rtt_ms} = {cycle_ms:.6f} ms")
    print(f"  T = {handshake_ms} + {num_packets:,.0f} × {cycle_ms:.6f}")
    print(f"  T = {handshake_ms} + {num_packets * cycle_ms:.4f}")
    print(f"  T = {case_b_ms:.4f} ms  ({case_b_ms / 1000:.4f} s)")

    #========================================================================================================
    #  Case C
    print(f"\n{'-' * 70}")
    print("Case C: Exponential Window Growth (TCP Slow-Start style)")
    print(f"{'-' * 70}")
    print("  Methodology: window = 1, 2, 4, 8 ... packets per RTT (infinite bandwidth).")
    print("  Formula: advance window each RTT; count RTTs until all packets are sent.")
    print("  Note: 'Infinite bandwidth' means Tx time per packet is negligible (0 ms).")

    # With infinite bandwidth, transmission delay per packet = 0.
    # Each RTT, the window doubles; packets are counted until file exhausted.
    packets_remaining = num_packets
    window = 1          # Packets sendable in the first RTT.
    rtts_used = 0       # Number of data-phase RTTs consumed.
    rtt_log = []        # Stores (rtt_index, window, sent_this_rtt) for display.

    while packets_remaining > 0:
        sent_this_rtt = min(window, packets_remaining)      # Cannot send more than remaining.
        rtt_log.append((rtts_used + 1, window, sent_this_rtt))
        packets_remaining -= sent_this_rtt
        rtts_used += 1
        window *= 2     # Doubles window capacity each RTT (slow-start doubling rule).

    case_c_ms = handshake_ms + rtts_used * rtt_ms          # No propagation term; RTT subsumes it.

    print(f"  {'RTT':<6} {'Window (pkts)':<16} {'Sent this RTT':<18} {'Remaining after'}")
    print(f"  {'-'*6} {'-'*16} {'-'*18} {'-'*15}")
    pkts_sent_so_far = 0
    for rtt_idx, win, sent in rtt_log:
        pkts_sent_so_far += sent
        print(f"  {rtt_idx:<6} {win:<16} {sent:<18.0f} {num_packets - pkts_sent_so_far:.0f}")

    print(f"\n  RTTs required (data) : {rtts_used}")
    print(f"  T = Handshake + DataRTTs × RTT")
    print(f"  T = {handshake_ms} + {rtts_used} × {rtt_ms}")
    print(f"  T = {case_c_ms:.4f} ms  ({case_c_ms / 1000:.4f} s)")

    print(f"\n{sep}")
    print("Summary")
    print(sep)
    print(f"  Case A (Continuous)     : {case_a_ms:.4f} ms  ({case_a_ms / 1000:.4f} s)")
    print(f"  Case B (Stop-and-Wait)  : {case_b_ms:.4f} ms  ({case_b_ms / 1000:.4f} s)")
    print(f"  Case C (Exp. Growth)    : {case_c_ms:.4f} ms  ({case_c_ms / 1000:.4f} s)")
    print(sep)

    return {
        "case_a": case_a_ms,
        "case_b": case_b_ms,
        "case_c": case_c_ms,
    }


if __name__ == "__main__":
    # printTables()
    print("\n\n")
    # AM file size: 3323 KB
    calculateFileTransfer(
        file_size_kb=3323,
        rate_mbps=1.0,
        packet_size_kb=1,
        header_bytes=40,
        one_way_delay_ms=40.0,
    )