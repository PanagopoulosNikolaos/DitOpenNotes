"""Topic 5: Communication Media (Μέσα Επικοινωνίας) theory renderer.

Covers Guided Media (Twisted Pair UTP/STP, Coaxial, Optical Fiber Single/Multi-mode)
and Unguided Wireless Media (Microwave, GEO/LEO Satellites).
"""

from nicegui import ui


def renderTopic5CommunicationMedia() -> None:
    """Renders the comprehensive theory module for Topic 5: Communication Media."""
    with ui.column().classes("w-full gap-6 text-[#f4f1ea]"):
        # Header Banner
        with ui.column().classes(
            "w-full glass-panel p-6 rounded-2xl border border-[rgba(224,107,58,0.35)] gap-3"
        ):
            with ui.row().classes("items-center gap-3"):
                ui.html('<i class="fa-solid fa-cable-car text-[#e06b3a] text-2xl"></i>')
                with ui.column().classes("gap-0"):
                    ui.html('<h2 class="text-xl font-bold gradient-title m-0">Θέμα 5: Μέσα Επικοινωνίας (Communication Media)</h2>')
                    ui.label("Καθοδηγούμενα Μέσα (UTP, STP, Coax, SMF/MMF Οπτικές Ίνες) & Μη Καθοδηγούμενα (Μικροκύματα, Δορυφόροι GEO/LEO)").classes("text-sm text-[#b5b0a4]")

        # Section 1: Guided Media
        with ui.column().classes("w-full glass-panel p-6 rounded-2xl gap-4"):
            with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3"):
                ui.html('<i class="fa-solid fa-lines-leaning text-amber-400 text-lg"></i>')
                ui.html('<h3 class="text-lg font-bold m-0 text-[#f4f1ea]">1. Καθοδηγούμενα Μέσα (Guided Media)</h3>')

            with ui.grid().classes("grid-cols-1 md:grid-cols-3 gap-3 w-full text-xs"):
                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(255,255,255,0.06)] gap-2"):
                    ui.label("Συνεστραμμένο Ζεύγος (UTP/STP)").classes("font-bold text-amber-400 text-sm")
                    ui.label(
                        "• Η συστροφή των αγωγών μειώνει τις ηλεκτρομαγνητικές παρεμβολές (Crosstalk).\n"
                        "• Cat5e (1 Gbps / 100m), Cat6/6a (10 Gbps / 55-100m).\n"
                        "• Ευρέως διαδεδομένο, χαμηλού κόστους, ευέλικτο."
                    ).classes("text-[#b5b0a4] whitespace-pre-line")

                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(255,255,255,0.06)] gap-2"):
                    ui.label("Ομοαξονικό Καλώδιο (Coaxial)").classes("font-bold text-blue-400 text-sm")
                    ui.label(
                        "• Κεντρικός χάλκινος αγωγός με διηλεκτρική μόνωση και μεταλλικό πλέγμα θωράκισης.\n"
                        "• Υψηλότερη ανοσία σε θόρυβο από το UTP.\n"
                        "• Χρήση σε καλωδιακή τηλεόραση και δίκτυα HFC (DOCSIS)."
                    ).classes("text-[#b5b0a4] whitespace-pre-line")

                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(224,107,58,0.3)] gap-2"):
                    ui.label("Οπτική Ίνα (Optical Fiber)").classes("font-bold text-[#e06b3a] text-sm")
                    ui.label(
                        "• Μεταφέρει φωτεινούς παλμούς μέσω ολικής εσωτερικής ανάκλασης (υψηλός δείκτης πυρήνα, χαμηλός περιβλήματος).\n"
                        "• Πλήρης ανοσία σε ηλεκτρομαγνητικές παρεμβολές (EMI).\n"
                        "• Πολύ χαμηλή εξασθένηση σε τεράστιες αποστάσεις (δεκάδες km)."
                    ).classes("text-[#b5b0a4] whitespace-pre-line")

        # Section 2: Single-Mode vs Multi-Mode Fiber
        with ui.column().classes("w-full glass-panel p-6 rounded-2xl gap-4"):
            with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3"):
                ui.html('<i class="fa-solid fa-lightbulb text-emerald-400 text-lg"></i>')
                ui.html('<h3 class="text-lg font-bold m-0 text-[#f4f1ea]">2. Οπτικές Ίνες: Single-Mode (SMF) vs Multi-Mode (MMF)</h3>')

            with ui.grid().classes("grid-cols-1 md:grid-cols-2 gap-4 w-full text-xs leading-relaxed"):
                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(224,107,58,0.2)] gap-2"):
                    ui.label("Single-Mode Fiber (SMF) - Μονότροπες").classes("font-bold text-[#e06b3a] text-sm")
                    ui.label(
                        "• Διάμετρος πυρήνα: Πολύ λεπτός (~8-10 μm).\n"
                        "• Πηγή φωτός: Laser.\n"
                        "• Διαδρομές φωτός: Μία μόνο φωτεινή διαδρομή (μηδενική τροπική διασπορά - modal dispersion).\n"
                        "• Εφαρμογή: Υπεραστικά δίκτυα κορμού (Backbone), υπερωκεάνια καλώδια (>10-80 km)."
                    ).classes("text-[#b5b0a4] whitespace-pre-line")

                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(79,142,201,0.2)] gap-2"):
                    ui.label("Multi-Mode Fiber (MMF) - Πολύτροπες").classes("font-bold text-blue-400 text-sm")
                    ui.label(
                        "• Διάμετρος πυρήνα: Παχύτερος (~50-62.5 μm).\n"
                        "• Πηγή φωτός: LEDs ή φθηνά VCSEL lasers.\n"
                        "• Διαδρομές φωτός: Πολλαπλές φωτεινές διαδρομές (εμφανίζεται τροπική διασπορά που περιορίζει την απόσταση).\n"
                        "• Εφαρμογή: Ενδοεταιρικά LANs, Data Centers, μικρές αποστάσεις (<500m)."
                    ).classes("text-[#b5b0a4] whitespace-pre-line")

        # Section 3: Satellites: GEO vs LEO
        with ui.column().classes("w-full glass-panel p-6 rounded-2xl gap-4"):
            with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3"):
                ui.html('<i class="fa-solid fa-satellite text-blue-400 text-lg"></i>')
                ui.html('<h3 class="text-lg font-bold m-0 text-[#f4f1ea]">3. Δορυφορικές Επικοινωνίες: GEO vs LEO</h3>')

            with ui.grid().classes("grid-cols-1 md:grid-cols-2 gap-4 w-full text-xs"):
                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(255,255,255,0.06)] gap-2"):
                    ui.label("Γεωστατικοί Δορυφόροι (GEO - Geostationary)").classes("font-bold text-[#f4f1ea]")
                    ui.label(
                        "• Ύψος τροχιάς: ~35.786 km πάνω από τον ισημερινό.\n"
                        "• Καθυστέρηση διάδοσης (Propagation Delay): ~250-280 ms (RTT ~500-600 ms).\n"
                        "• Κάλυψη: 3 δορυφόροι αρκούν για παγκόσμια κάλυψη."
                    ).classes("text-[#b5b0a4] whitespace-pre-line")

                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(255,255,255,0.06)] gap-2"):
                    ui.label("Δορυφόροι Χαμηλής Τροχιάς (LEO - Low Earth Orbit)").classes("font-bold text-[#f4f1ea]")
                    ui.label(
                        "• Ύψος τροχιάς: ~500-1.200 km (π.χ. Starlink, OneWeb).\n"
                        "• Καθυστέρηση διάδοσης: ~20-40 ms (ανταγωνιστική των επίγειων ινών).\n"
                        "• Κάλυψη: Απαιτούνται αστερισμοί χιλιάδων δορυφόρων με συνεχές handoff."
                    ).classes("text-[#b5b0a4] whitespace-pre-line")
