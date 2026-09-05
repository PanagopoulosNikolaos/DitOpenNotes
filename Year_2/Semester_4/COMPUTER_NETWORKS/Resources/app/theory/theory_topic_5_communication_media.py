"""Topic 5: Communication Media theory renderer.

Covers Guided vs Unguided Media, Twisted Pair (UTP/STP Cat5e-Cat8, Crosstalk),
Coaxial Cable (Baseband vs Broadband), Optical Fiber (Total Internal Reflection, SMF Laser vs MMF LED),
Wireless/Radio, Satellite orbits (GEO vs LEO), and Shannon-Hartley Channel Capacity.
"""

from nicegui import ui


def renderTopic5CommunicationMedia() -> None:
    """Renders the comprehensive theory module for Topic 5: Communication Media."""
    with ui.column().classes("w-full gap-6 text-[#f4f1ea] latex-target"):
        # Header Banner
        with ui.column().classes(
            "w-full glass-panel p-6 md:p-8 rounded-2xl border border-[rgba(224,107,58,0.35)] gap-3"
        ):
            with ui.row().classes("items-center gap-3"):
                ui.html('<i class="fa-solid fa-network-wired text-[#e06b3a] text-3xl"></i>')
                with ui.column().classes("gap-0"):
                    ui.html('<h2 class="text-xl md:text-2xl font-bold gradient-title m-0">Topic 5: Communication Media</h2>')
                    ui.label(
                        "Guided & Unguided Media, Twisted Pair (UTP/STP), Coaxial Cable, "
                        "Optical Fiber (SMF/MMF), Satellites, and Shannon Channel Capacity."
                    ).classes("text-xs md:text-sm text-[#b5b0a4]")

        # =========================================================================
        # SECTION 1: Guided Media (Twisted Pair & Coaxial)
        # =========================================================================
        with ui.column().classes("w-full glass-panel p-6 rounded-2xl gap-4"):
            with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3"):
                ui.html('<i class="fa-solid fa-lines-leaning text-amber-400 text-lg"></i>')
                ui.html('<h3 class="text-lg font-bold m-0 text-[#f4f1ea]">1. Guided Copper Media: Twisted Pair & Coaxial Cable</h3>')

            with ui.grid().classes("grid-cols-1 md:grid-cols-2 gap-4 w-full text-xs"):
                # Twisted Pair Card
                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(224,107,58,0.3)] gap-2"):
                    ui.label("Twisted Pair (UTP / STP)").classes("font-bold text-[#e06b3a] text-sm")
                    ui.html("""
                    <ul class="m-0 pl-4 space-y-1.5 text-[#b5b0a4]">
                        <li><strong class="text-stone-200">Twisting Principle:</strong> Two insulated copper conductors are twisted into a helical geometry. The twists cancel electromagnetic interference (EMI) and crosstalk from adjacent pairs via differential signaling.</li>
                        <li><strong class="text-stone-200">UTP vs STP:</strong> UTP (Unshielded) is cost-effective and flexible. STP (Shielded) incorporates metallic foil/braid shielding for noisy industrial environments.</li>
                        <li><strong class="text-stone-200">Categories:</strong>
                            <br>&bull; <span class="text-stone-200">Cat5e:</span> 100 MHz &rarr; 1 Gbps (1000BASE-T up to 100m).
                            <br>&bull; <span class="text-stone-200">Cat6 / 6a:</span> 250/500 MHz &rarr; 10 Gbps (10GBASE-T).
                            <br>&bull; <span class="text-stone-200">Cat7 / 8:</span> 600/2000 MHz &rarr; 25/40 Gbps in high-density data centers.
                        </li>
                    </ul>
                    """)

                # Coaxial Cable Card
                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(245,158,11,0.3)] gap-2"):
                    ui.label("Coaxial Cable").classes("font-bold text-amber-300 text-sm")
                    ui.html("""
                    <ul class="m-0 pl-4 space-y-1.5 text-[#b5b0a4]">
                        <li><strong class="text-stone-200">Construction:</strong> Center copper core conductor, dielectric insulator, outer braided metal shield, and outer protective jacket.</li>
                        <li><strong class="text-stone-200">Baseband (50 $\\Omega$):</strong> Single digital transmission channel across the entire medium (legacy Ethernet 10BASE2/10BASE5).</li>
                        <li><strong class="text-stone-200">Broadband (75 $\\Omega$):</strong> Analog Frequency-Division Multiplexing (FDM) carrying multiple concurrent channels (Cable TV, HFC Cable DOCSIS).</li>
                        <li><strong class="text-stone-200">Characteristics:</strong> Substantially higher noise immunity than UTP, but heavier, stiffer, and more expensive to deploy.</li>
                    </ul>
                    """)

        # =========================================================================
        # SECTION 2: Optical Fiber (SMF vs MMF)
        # =========================================================================
        with ui.column().classes("w-full glass-panel p-6 rounded-2xl gap-4"):
            with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3"):
                ui.html('<i class="fa-solid fa-bolt text-cyan-400 text-lg"></i>')
                ui.html('<h3 class="text-lg font-bold m-0 text-[#f4f1ea]">2. Optical Fiber: Total Internal Reflection & Single-Mode vs Multi-Mode</h3>')

            ui.label(
                "Optical fiber conveys digital data as light pulses through a thin glass or silica core. "
                "Light propagation relies on Total Internal Reflection (TIR), which occurs when the refractive index "
                "of the core exceeds that of the cladding (n_core > n_cladding) and the angle of incidence "
                "exceeds the critical angle theta_c."
            ).classes("text-xs md:text-sm text-[#b5b0a4]")

            with ui.grid().classes("grid-cols-1 md:grid-cols-2 gap-4 w-full text-xs"):
                # Single-Mode Fiber Card
                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(6,182,212,0.3)] gap-2"):
                    ui.label("Single-Mode Fiber (SMF)").classes("font-bold text-cyan-300 text-sm")
                    ui.html("""
                    <ul class="m-0 pl-4 space-y-1.5 text-[#b5b0a4]">
                        <li><strong class="text-stone-200">Core Diameter:</strong> Extremely narrow ($8 - 10\\ \\mu\\text{m}$).</li>
                        <li><strong class="text-stone-200">Light Source:</strong> Semiconductor laser ($1310\\text{ nm}, 1550\\text{ nm}$).</li>
                        <li><strong class="text-stone-200">Dispersion:</strong> <em>Zero modal dispersion</em> (only 1 propagation optical mode).</li>
                        <li><strong class="text-emerald-400">Reach:</strong> Tens to hundreds of kilometers (Core backbones, MAN, WAN, submarine transoceanic cables).</li>
                    </ul>
                    """)

                # Multi-Mode Fiber Card
                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(245,158,11,0.3)] gap-2"):
                    ui.label("Multi-Mode Fiber (MMF)").classes("font-bold text-amber-300 text-sm")
                    ui.html("""
                    <ul class="m-0 pl-4 space-y-1.5 text-[#b5b0a4]">
                        <li><strong class="text-stone-200">Core Diameter:</strong> Wider core ($50 - 62.5\\ \\mu\\text{m}$).</li>
                        <li><strong class="text-stone-200">Light Source:</strong> LED / VCSEL ($850\\text{ nm}$).</li>
                        <li><strong class="text-amber-300">Modal Dispersion:</strong> Multiple light rays bounce at differing reflection angles and arrive at slightly different intervals (Pulse Spreading).</li>
                        <li><strong class="text-red-400">Reach:</strong> Constrained to short distances (up to 300 - 550m in data centers and enterprise LANs).</li>
                    </ul>
                    """)

        # =========================================================================
        # SECTION 3: Shannon Capacity & Radio Propagation
        # =========================================================================
        with ui.column().classes("w-full glass-panel p-6 rounded-2xl gap-4"):
            with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3"):
                ui.html('<i class="fa-solid fa-square-root-variable text-emerald-400 text-lg"></i>')
                ui.html('<h3 class="text-lg font-bold m-0 text-[#f4f1ea]">3. Shannon Channel Capacity & Wireless Signal Propagation</h3>')

            with ui.grid().classes("grid-cols-1 md:grid-cols-2 gap-4 w-full text-xs"):
                with ui.column().classes("p-4 rounded-xl bg-[#141413] border border-[rgba(16,185,129,0.3)] gap-2"):
                    ui.label("Shannon-Hartley Channel Capacity Theorem").classes("font-bold text-emerald-400 text-sm")
                    ui.html("""
                    <div class="formula-box text-xs mb-2">
                        $$C = B \\cdot \\log_2\\left(1 + \\text{SNR}\\right) = B \\cdot \\log_2\\left(1 + \\frac{S}{N}\\right)$$
                    </div>
                    <ul class="m-0 pl-4 space-y-1 text-[#b5b0a4]">
                        <li><strong class="text-stone-200">C:</strong> Theoretical maximum channel capacity (bps).</li>
                        <li><strong class="text-stone-200">B:</strong> Channel frequency bandwidth in Hertz (Hz).</li>
                        <li><strong class="text-stone-200">SNR:</strong> Signal-to-noise power ratio ($S/N$ linear ratio, $\\text{SNR}_{\\text{dB}} = 10 \\log_{10}(S/N)$).</li>
                        <li><strong class="text-stone-200">Nyquist Theorem (Noiseless Channel):</strong> $$C_{\\text{max}} = 2B \\cdot \\log_2(M)$$</li>
                    </ul>
                    """)

                with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(79,142,201,0.3)] gap-2"):
                    ui.label("Wireless Signal Propagation Mechanisms").classes("font-bold text-blue-300 text-sm")
                    ui.html("""
                    <ul class="m-0 pl-4 space-y-1.5 text-[#b5b0a4]">
                        <li><strong class="text-stone-200">Reflection:</strong> Wave impinges on surfaces with dimensions significantly larger than the wavelength (e.g., walls, terrain).</li>
                        <li><strong class="text-stone-200">Diffraction:</strong> Bending of radio waves around sharp obstacle edges into shadowed non-line-of-sight zones.</li>
                        <li><strong class="text-stone-200">Scattering:</strong> Energy dispersed in all directions by objects comparable in size to the wavelength (foliage, rain droplets).</li>
                        <li><strong class="text-stone-200">Path Loss (Free-Space Loss):</strong> Signal power drops inversely with the square of the propagation distance ($1/d^2$).</li>
                    </ul>
                    """)
