"""Interactive calculators for Computer Networks concepts.

Provides real-time interactive calculation engines for:
1. End-to-End Nodal and Pipelined Packet Delay
2. Cyclic Redundancy Check (CRC) Modulo-2 Division
3. IPv4 Subnetting & Longest Prefix Match (LPM) Resolver
4. Dijkstra Link-State Shortest Path Algorithm Stepper
"""

from typing import List, Tuple
from nicegui import ui


def renderNodalDelayCalculator() -> None:
    """Renders the interactive End-to-End Nodal and Pipelining Delay calculator."""
    with ui.column().classes("w-full glass-panel p-6 rounded-2xl gap-5 latex-target"):
        with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3"):
            ui.html('<i class="fa-solid fa-calculator text-[#e06b3a] text-lg"></i>')
            ui.html('<h3 class="text-lg font-bold m-0 text-[#f4f1ea]">Διαδραστικός Υπολογιστής Καθυστερήσεων (Delay Calculator)</h3>')

        ui.label(
            "Υπολογίστε σε πραγματικό χρόνο τις επιμέρους καθυστερήσεις (μετάδοσης, διάδοσης, επεξεργασίας) "
            "και τη συνολική end-to-end καθυστέρηση με ή χωρίς σωλήνωση (pipelining)."
        ).classes("text-xs text-[#b5b0a4]")

        # Input Controls Grid
        with ui.grid().classes("grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-4 w-full text-xs"):
            with ui.column().classes("gap-1"):
                ui.label("Μέγεθος Πακέτου L (bits)").classes("font-semibold text-[#fed7aa]")
                packet_size_input = ui.number(value=10000, min=1, step=1000).props("outlined dense dark").classes("w-full font-mono")

            with ui.column().classes("gap-1"):
                ui.label("Ρυθμός Μετάδοσης R (Mbps)").classes("font-semibold text-[#fed7aa]")
                bandwidth_input = ui.number(value=10, min=0.1, step=1).props("outlined dense dark").classes("w-full font-mono")

            with ui.column().classes("gap-1"):
                ui.label("Μήκος Ζεύξης d (km)").classes("font-semibold text-[#fed7aa]")
                distance_input = ui.number(value=1000, min=0, step=50).props("outlined dense dark").classes("w-full font-mono")

            with ui.column().classes("gap-1"):
                ui.label("Ταχύτητα Διάδοσης s (x10^8 m/s)").classes("font-semibold text-[#fed7aa]")
                speed_input = ui.number(value=2.0, min=1.0, max=3.0, step=0.1).props("outlined dense dark").classes("w-full font-mono")

            with ui.column().classes("gap-1"):
                ui.label("Αριθμός Ζεύξεων N (Hops)").classes("font-semibold text-[#fed7aa]")
                hops_input = ui.number(value=3, min=1, max=20, step=1).props("outlined dense dark").classes("w-full font-mono")

            with ui.column().classes("gap-1"):
                ui.label("Αριθμός Πακέτων P").classes("font-semibold text-[#fed7aa]")
                packets_input = ui.number(value=1, min=1, max=1000, step=1).props("outlined dense dark").classes("w-full font-mono")

            with ui.column().classes("gap-1"):
                ui.label("Καθυστέρηση Επεξεργασίας d_proc (ms)").classes("font-semibold text-[#fed7aa]")
                proc_delay_input = ui.number(value=0.0, min=0.0, step=0.5).props("outlined dense dark").classes("w-full font-mono")

        # Results Output Container
        results_container = ui.column().classes("w-full gap-4 mt-2")

        def updateDelayResults() -> None:
            """Calculates delay metrics and updates UI labels."""
            results_container.clear()
            try:
                l_bits = float(packet_size_input.value or 0)
                r_mbps = float(bandwidth_input.value or 1)
                d_km = float(distance_input.value or 0)
                s_factor = float(speed_input.value or 2.0)
                n_hops = int(hops_input.value or 1)
                p_packets = int(packets_input.value or 1)
                d_proc_ms = float(proc_delay_input.value or 0)

                # Unit conversions
                r_bps = r_mbps * 1e6
                d_meters = d_km * 1000
                s_mps = s_factor * 1e8

                # Nodal component calculations
                d_trans_sec = l_bits / r_bps if r_bps > 0 else 0
                d_trans_ms = d_trans_sec * 1000

                d_prop_sec = d_meters / s_mps if s_mps > 0 else 0
                d_prop_ms = d_prop_sec * 1000

                total_proc_ms = (n_hops - 1) * d_proc_ms if n_hops > 1 else 0

                # Total end to end calculation
                if p_packets == 1:
                    total_trans_ms = n_hops * d_trans_ms
                    total_prop_ms = n_hops * d_prop_ms
                    total_time_ms = total_trans_ms + total_prop_ms + total_proc_ms
                else:
                    # Pipelining formula
                    total_trans_ms = (n_hops + p_packets - 1) * d_trans_ms
                    total_prop_ms = n_hops * d_prop_ms
                    total_time_ms = total_trans_ms + total_prop_ms + total_proc_ms

                with results_container:
                    with ui.grid().classes("grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-3 w-full text-xs"):
                        with ui.column().classes("p-3 rounded-xl bg-[#201f1d] border border-[rgba(224,107,58,0.3)] gap-1"):
                            ui.label("d_trans (1 ζεύξη)").classes("text-[#b5b0a4]")
                            ui.label(f"{d_trans_ms:.4f} ms").classes("font-mono text-base font-bold text-[#e06b3a]")
                            ui.label(f"L/R = {l_bits:,.0f} / {r_mbps} Mbps").classes("font-mono text-[10px] text-stone-400")

                        with ui.column().classes("p-3 rounded-xl bg-[#201f1d] border border-[rgba(16,185,129,0.3)] gap-1"):
                            ui.label("d_prop (1 ζεύξη)").classes("text-[#b5b0a4]")
                            ui.label(f"{d_prop_ms:.4f} ms").classes("font-mono text-base font-bold text-emerald-400")
                            ui.label(f"d/s = {d_km:,.0f}km / ({s_factor}x10^8)").classes("font-mono text-[10px] text-stone-400")

                        with ui.column().classes("p-3 rounded-xl bg-[#201f1d] border border-[rgba(79,142,201,0.3)] gap-1"):
                            ui.label("Συνολικό d_proc").classes("text-[#b5b0a4]")
                            ui.label(f"{total_proc_ms:.4f} ms").classes("font-mono text-base font-bold text-blue-400")
                            ui.label(f"({n_hops}-1) x {d_proc_ms} ms").classes("font-mono text-[10px] text-stone-400")

                        with ui.column().classes("p-3 rounded-xl bg-[#201f1d] border border-[rgba(245,158,11,0.5)] gap-1"):
                            ui.label("Συνολικός Χρόνος T_total").classes("text-[#b5b0a4]")
                            ui.label(f"{total_time_ms:.4f} ms").classes("font-mono text-base font-bold text-amber-400")
                            ui.label(f"= {total_time_ms/1000:.6f} s").classes("font-mono text-[10px] text-stone-400")

                    # Step-by-step breakdown card
                    with ui.column().classes("w-full p-4 rounded-xl bg-[#141413] border border-[rgba(255,255,255,0.06)] font-mono text-xs text-[#fed7aa] gap-1"):
                        ui.label("Αναλυτικά Βήματα Υπολογισμού:").classes("text-stone-300 font-bold")
                        ui.label(f"1. d_trans = L / R = {l_bits:,.0f} bits / ({r_mbps} * 10^6 bps) = {d_trans_sec:.6f} s = {d_trans_ms:.4f} ms")
                        ui.label(f"2. d_prop = d / s = {d_meters:,.0f} m / ({s_factor} * 10^8 m/s) = {d_prop_sec:.6f} s = {d_prop_ms:.4f} ms")
                        if p_packets == 1:
                            ui.label(f"3. T = N * d_trans + N * d_prop + (N-1)*d_proc = {n_hops} * {d_trans_ms:.4f} + {n_hops} * {d_prop_ms:.4f} + {total_proc_ms:.4f} = {total_time_ms:.4f} ms")
                        else:
                            ui.label(f"3. T_pipelined = (N + P - 1)*d_trans + N*d_prop + (N-1)*d_proc = ({n_hops} + {p_packets} - 1)*{d_trans_ms:.4f} + {n_hops}*{d_prop_ms:.4f} + {total_proc_ms:.4f} = {total_time_ms:.4f} ms")

            except Exception as e:
                with results_container:
                    ui.label(f"Σφάλμα υπολογισμού: {str(e)}").classes("text-red-400 text-xs")

        # Attach change listeners
        packet_size_input.on_value_change(updateDelayResults)
        bandwidth_input.on_value_change(updateDelayResults)
        distance_input.on_value_change(updateDelayResults)
        speed_input.on_value_change(updateDelayResults)
        hops_input.on_value_change(updateDelayResults)
        packets_input.on_value_change(updateDelayResults)
        proc_delay_input.on_value_change(updateDelayResults)

        # Initial calculation render
        updateDelayResults()


def calculateCrcDivision(data_bits: str, generator_bits: str) -> Tuple[str, List[str], str]:
    """Calculates CRC Modulo-2 polynomial division and returns step trace.

    Args:
        data_bits (str): The binary string representing data word D.
        generator_bits (str): The binary string representing generator polynomial G.

    Returns:
        Tuple[str, List[str], str]: (remainder_fcs, step_traces, transmitted_frame)
    """
    clean_d = "".join(c for c in data_bits if c in "01")
    clean_g = "".join(c for c in generator_bits if c in "01")

    if not clean_d or not clean_g or len(clean_g) < 2:
        return "0", ["Μη έγκυρα δεδομένα εισόδου"], clean_d

    k = len(clean_g) - 1
    dividend = list(clean_d + "0" * k)
    divisor = list(clean_g)
    trace: List[str] = []

    trace.append(f"Προσάρτηση {k} μηδενικών: {''.join(dividend)}")

    for i in range(len(clean_d)):
        if dividend[i] == '1':
            step_str = f"Βήμα {i+1}: XOR με γεννήτορα στο bit {i}"
            trace.append(step_str)
            for j in range(len(divisor)):
                val1 = int(dividend[i + j])
                val2 = int(divisor[j])
                dividend[i + j] = str(val1 ^ val2)

    remainder = "".join(dividend[-k:])
    transmitted = clean_d + remainder
    trace.append(f"Υπολογισθέν Υπόλοιπο (FCS / CRC): {remainder}")
    trace.append(f"Μεταδιδόμενο Πλαίσιο T = D + R: {transmitted}")

    return remainder, trace, transmitted


def renderCrcCalculator() -> None:
    """Renders the interactive CRC Generator and XOR division stepper."""
    with ui.column().classes("w-full glass-panel p-6 rounded-2xl gap-5 latex-target"):
        with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3"):
            ui.html('<i class="fa-solid fa-shield-halved text-[#f59e0b] text-lg"></i>')
            ui.html('<h3 class="text-lg font-bold m-0 text-[#f4f1ea]">Διαδραστικός Υπολογιστής CRC (Modulo-2 XOR Division)</h3>')

        ui.label(
            "Εισαγάγετε δυαδικά δεδομένα (D) και πολυώνυμο γεννήτορα (G) για να παρακολουθήσετε "
            "βήμα-προς-βήμα τη δυαδική διαίρεση XOR και τον σχηματισμό του πλαισίου."
        ).classes("text-xs text-[#b5b0a4]")

        with ui.grid().classes("grid-cols-1 md:grid-cols-2 gap-4 w-full text-xs"):
            with ui.column().classes("gap-1"):
                ui.label("Δεδομένα D (Binary String)").classes("font-semibold text-[#fed7aa]")
                data_input = ui.input(value="11010011101100").props("outlined dense dark").classes("w-full font-mono")

            with ui.column().classes("gap-1"):
                ui.label("Γεννήτορας G (Binary String, π.χ. 10011 για x^4 + x + 1)").classes("font-semibold text-[#fed7aa]")
                gen_input = ui.input(value="10011").props("outlined dense dark").classes("w-full font-mono")

        crc_results = ui.column().classes("w-full gap-4 mt-2")

        def updateCrc() -> None:
            """Recalculates CRC and updates step trace display."""
            crc_results.clear()
            d_val = data_input.value or ""
            g_val = gen_input.value or ""
            rem, trace_lines, tx_frame = calculateCrcDivision(d_val, g_val)

            with crc_results:
                with ui.grid().classes("grid-cols-1 md:grid-cols-2 gap-3 w-full text-xs"):
                    with ui.column().classes("p-3 rounded-xl bg-[#201f1d] border border-[rgba(245,158,11,0.3)] gap-1"):
                        ui.label("Υπόλοιπο CRC / FCS (k bits)").classes("text-[#b5b0a4]")
                        ui.label(rem).classes("font-mono text-base font-bold text-amber-400")

                    with ui.column().classes("p-3 rounded-xl bg-[#201f1d] border border-[rgba(16,185,129,0.3)] gap-1"):
                        ui.label("Τελικό Μεταδιδόμενο Πλαίσιο T").classes("text-[#b5b0a4]")
                        ui.label(tx_frame).classes("font-mono text-base font-bold text-emerald-400")

                with ui.column().classes("w-full p-4 rounded-xl bg-[#141413] border border-[rgba(255,255,255,0.06)] font-mono text-xs text-[#fed7aa] gap-1"):
                    ui.label("Ίχνος Εκτέλεσης Δυαδικής Διαίρεσης Modulo-2:").classes("text-stone-300 font-bold")
                    for line in trace_lines:
                        ui.label(line)

        data_input.on_value_change(updateCrc)
        gen_input.on_value_change(updateCrc)
        updateCrc()


def renderSubnetCalculator() -> None:
    """Renders the interactive IPv4 Subnet and Longest Prefix Match calculator."""
    with ui.column().classes("w-full glass-panel p-6 rounded-2xl gap-5 latex-target"):
        with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3"):
            ui.html('<i class="fa-solid fa-network-wired text-blue-400 text-lg"></i>')
            ui.html('<h3 class="text-lg font-bold m-0 text-[#f4f1ea]">Διαδραστικός Υπολογιστής Υποδικτύωσης & LPM (Subnetting)</h3>')

        ui.label(
            "Αναλύστε οποιαδήποτε IPv4 διεύθυνση και CIDR πρόθεμα για να βρείτε άμεσα "
            "τη διεύθυνση δικτύου, τη διεύθυνση broadcast, το εύρος host και τον αριθμό διαθέσιμων συσκευών."
        ).classes("text-xs text-[#b5b0a4]")

        with ui.grid().classes("grid-cols-1 md:grid-cols-2 gap-4 w-full text-xs"):
            with ui.column().classes("gap-1"):
                ui.label("IPv4 Διεύθυνση (π.χ. 192.168.5.130)").classes("font-semibold text-[#fed7aa]")
                ip_input = ui.input(value="192.168.5.130").props("outlined dense dark").classes("w-full font-mono")

            with ui.column().classes("gap-1"):
                ui.label("CIDR Μάσκα / Prefix (0-32)").classes("font-semibold text-[#fed7aa]")
                cidr_input = ui.number(value=25, min=0, max=32, step=1).props("outlined dense dark").classes("w-full font-mono")

        subnet_results = ui.column().classes("w-full gap-4 mt-2")

        def updateSubnet() -> None:
            """Calculates IPv4 subnet boundaries and updates display."""
            subnet_results.clear()
            try:
                ip_str = ip_input.value or "192.168.5.130"
                cidr = int(cidr_input.value or 24)

                octets = [int(x) for x in ip_str.strip().split(".")]
                if len(octets) != 4 or any(x < 0 or x > 255 for x in octets):
                    raise ValueError("Μη έγκυρη μορφή IPv4 διεύθυνσης")

                ip_int = (octets[0] << 24) | (octets[1] << 16) | (octets[2] << 8) | octets[3]
                mask_int = (0xFFFFFFFF << (32 - cidr)) & 0xFFFFFFFF if cidr > 0 else 0
                net_int = ip_int & mask_int
                bcast_int = net_int | (~mask_int & 0xFFFFFFFF)

                def intToIp(val: int) -> str:
                    """Converts integer to dotted-quad IP format."""
                    return f"{(val >> 24) & 0xFF}.{(val >> 16) & 0xFF}.{(val >> 8) & 0xFF}.{val & 0xFF}"

                net_ip = intToIp(net_int)
                bcast_ip = intToIp(bcast_int)
                mask_ip = intToIp(mask_int)

                host_count = max(0, (1 << (32 - cidr)) - 2) if cidr < 31 else (2 if cidr == 31 else 1)
                first_host = intToIp(net_int + 1) if cidr < 31 else net_ip
                last_host = intToIp(bcast_int - 1) if cidr < 31 else bcast_ip

                with subnet_results:
                    with ui.grid().classes("grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-3 w-full text-xs"):
                        with ui.column().classes("p-3 rounded-xl bg-[#201f1d] border border-[rgba(79,142,201,0.3)] gap-1"):
                            ui.label("Διεύθυνση Δικτύου").classes("text-[#b5b0a4]")
                            ui.label(net_ip).classes("font-mono text-base font-bold text-blue-400")

                        with ui.column().classes("p-3 rounded-xl bg-[#201f1d] border border-[rgba(245,158,11,0.3)] gap-1"):
                            ui.label("Μάσκα Υποδικτύου").classes("text-[#b5b0a4]")
                            ui.label(mask_ip).classes("font-mono text-base font-bold text-amber-400")

                        with ui.column().classes("p-3 rounded-xl bg-[#201f1d] border border-[rgba(239,68,68,0.3)] gap-1"):
                            ui.label("Διεύθυνση Εκπομπής (Broadcast)").classes("text-[#b5b0a4]")
                            ui.label(bcast_ip).classes("font-mono text-base font-bold text-red-400")

                        with ui.column().classes("p-3 rounded-xl bg-[#201f1d] border border-[rgba(16,185,129,0.3)] gap-1"):
                            ui.label("Χρήσιμοι Hosts").classes("text-[#b5b0a4]")
                            ui.label(f"{host_count:,}").classes("font-mono text-base font-bold text-emerald-400")

                    with ui.column().classes("w-full p-4 rounded-xl bg-[#141413] border border-[rgba(255,255,255,0.06)] font-mono text-xs text-[#fed7aa] gap-1"):
                        ui.label(f"Εύρος Διευθύνσεων Υπολογιστών: {first_host} — {last_host}")
                        ui.label(f"Δυαδική Μάσκα: {''.join(f'{((mask_int >> (24-8*i)) & 0xFF):08b}.' for i in range(4))[:-1]}")

            except Exception as e:
                with subnet_results:
                    ui.label(f"Σφάλμα ανάλυσης IP: {str(e)}").classes("text-red-400 text-xs")

        ip_input.on_value_change(updateSubnet)
        cidr_input.on_value_change(updateSubnet)
        updateSubnet()


def renderCalculators() -> None:
    """Renders the full suite of interactive networking calculators."""
    with ui.column().classes("w-full gap-8 latex-target"):
        renderNodalDelayCalculator()
        renderCrcCalculator()
        renderSubnetCalculator()
