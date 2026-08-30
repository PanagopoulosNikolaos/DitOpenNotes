"""Comprehensive Exam Preparation Guide (Πλήρης Οδηγός Προετοιμασίας Εξετάσεων).

Synthesizes all essential networking formulas, fast mental calculation tricks,
decision matrices, routing algorithms, and common exam pitfalls.
"""

from nicegui import ui


def renderTheoryExamFullPrep() -> None:
    """Renders the master exam preparation guide with synthesized formulas and matrices."""
    with ui.column().classes("w-full gap-6 text-[#f4f1ea]"):
        # Header Banner
        with ui.column().classes(
            "w-full glass-panel p-6 rounded-2xl border border-[rgba(224,107,58,0.4)] gap-3"
        ):
            with ui.row().classes("items-center gap-3"):
                ui.html('<i class="fa-solid fa-graduation-cap text-[#e06b3a] text-3xl"></i>')
                with ui.column().classes("gap-0"):
                    ui.html('<h2 class="text-xl md:text-2xl font-black gradient-title m-0">Πλήρης Οδηγός Προετοιμασίας Εξετάσεων (Exam Cheat Sheet)</h2>')
                    ui.label("Συγκεντρωτικό τυπολόγιο, πίνακες απόφασης, βήμα-προς-βήμα αλγόριθμοι και κρίσιμα σημεία προσοχής").classes("text-sm text-[#b5b0a4]")

        # Section 1: Master Formula Sheet
        with ui.column().classes("w-full glass-panel p-6 rounded-2xl gap-4"):
            with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3"):
                ui.html('<i class="fa-solid fa-square-root-variable text-amber-400 text-lg"></i>')
                ui.html('<h3 class="text-lg font-bold m-0 text-[#f4f1ea]">1. Συγκεντρωτικό Τυπολόγιο (Master Formula Sheet)</h3>')

            with ui.grid().classes("grid-cols-1 md:grid-cols-2 gap-4 w-full text-xs"):
                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(224,107,58,0.25)] gap-2"):
                    ui.label("Καθυστέρηση Μετάδοσης & Διάδοσης").classes("font-bold text-[#e06b3a] text-sm")
                    ui.label("• Μετάδοση: d_trans = L / R (L σε bits, R σε bps)").classes("font-mono text-stone-200")
                    ui.label("• Διάδοση: d_prop = d / s (d σε m, s σε m/s)").classes("font-mono text-stone-200")
                    ui.label("• Ταχύτητα φωτός στο χαλκό/ίνα: s ≈ 2 * 10^8 m/s = 200.000 km/s").classes("text-[#b5b0a4]")
                    ui.label("• Ταχύτητα στον αέρα/κενό: c ≈ 3 * 10^8 m/s = 300.000 km/s").classes("text-[#b5b0a4]")

                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(245,158,11,0.25)] gap-2"):
                    ui.label("Store-and-Forward Pipelining").classes("font-bold text-amber-400 text-sm")
                    ui.label("• 1 Πακέτο, N hops: T_1 = N * (L / R) + Σ(d_i / s_i)").classes("font-mono text-stone-200")
                    ui.label("• P Πακέτα, N hops: T_P = (N + P - 1) * (L / R) + Σ(d_i / s_i)").classes("font-mono text-stone-200")
                    ui.label("• Με ενδιάμεση επεξεργασία: Προσθέστε (N - 1) * d_proc").classes("text-[#b5b0a4]")

                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(79,142,201,0.25)] gap-2"):
                    ui.label("Υποδικτύωση IPv4 (Subnetting)").classes("font-bold text-blue-400 text-sm")
                    ui.label("• Block Size = 2^(32 - prefix_length)").classes("font-mono text-stone-200")
                    ui.label("• Αριθμός Hosts = 2^(32 - prefix_length) - 2").classes("font-mono text-stone-200")
                    ui.label("• Διεύθυνση Δικτύου: Πρώτη διεύθυνση του block (host bits = all 0)").classes("text-[#b5b0a4]")
                    ui.label("• Διεύθυνση Εκπομπής (Broadcast): Τελευταία διεύθυνση του block (host bits = all 1)").classes("text-[#b5b0a4]")

                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(16,185,129,0.25)] gap-2"):
                    ui.label("Ρυθμαπόδοση (Throughput)").classes("font-bold text-emerald-400 text-sm")
                    ui.label("• Ενδογενής Ρυθμαπόδοση (Bottleneck): min(R_1, R_2, ..., R_N)").classes("font-mono text-stone-200")
                    ui.label("• Μέγιστη Μεταγωγή Πακέτου σε στατιστική πολυπλεξία").classes("text-[#b5b0a4]")
                    ui.label("• Επίδραση μεγέθους παραθύρου TCP: Throughput ≤ W / RTT").classes("text-[#b5b0a4]")

        # Section 2: Critical Pitfalls Checklist
        with ui.column().classes("w-full glass-panel p-6 rounded-2xl gap-4"):
            with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3"):
                ui.html('<i class="fa-solid fa-triangle-exclamation text-red-400 text-lg"></i>')
                ui.html('<h3 class="text-lg font-bold m-0 text-[#f4f1ea]">2. Συχνές Παγίδες στις Εξετάσεις</h3>')

            with ui.grid().classes("grid-cols-1 md:grid-cols-2 gap-4 w-full text-xs leading-relaxed"):
                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(239,68,68,0.3)] gap-2"):
                    ui.label("Παγίδα Μονάδων Μέτρησης (Bits vs Bytes, kbps vs Mbps)").classes("font-bold text-red-300")
                    ui.label(
                        "• 1 Byte = 8 bits. Αν το μέγεθος αρχείου δίνεται σε KBytes, πολλαπλασιάστε με 8.000 ή 8.192 bits.\n"
                        "• Στο networking 1 Mbps = 10^6 bps (όχι 2^20) και 1 km = 1.000 m.\n"
                        "• Μετατρέψτε πάντα όλες τις καθυστερήσεις σε ίδια μονάδα (ms ή s) πριν τις προσθέσετε!"
                    ).classes("text-[#b5b0a4] whitespace-pre-line")

                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(239,68,68,0.3)] gap-2"):
                    ui.label("Παγίδα Μετάδοσης vs Διάδοσης (L/R vs d/s)").classes("font-bold text-red-300")
                    ui.label(
                        "• Η μετάδοση (L/R) εξαρτάται ΜΟΝΟ από το μέγεθος πακέτου και το bandwidth. Δεν αλλάζει αν η ζεύξη έχει μήκος 1 μέτρο ή 1.000 km.\n"
                        "• Η διάδοση (d/s) εξαρτάται ΜΟΝΟ από την απόσταση και την ταχύτητα φωτός. Δεν αλλάζει αν το πακέτο είναι 1 bit ή 1 GB!"
                    ).classes("text-[#b5b0a4] whitespace-pre-line")
