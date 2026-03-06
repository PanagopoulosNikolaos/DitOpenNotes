
import tkinter as tk
from tkinter import ttk
import time

# ── palette ────────────────────────────────────────────────────────────────
BG        = "#12111a"
SURFACE   = "#1e1c2e"
SURFACE2  = "#252338"
ACCENT    = "#7c6af7"
ACCENT_LT = "#9d8fff"
ACCENT2   = "#e06c75"
ACCENT2_LT= "#f08090"
TEXT      = "#e2e0f5"
SUBTEXT   = "#7b7a99"
GREEN     = "#6ee7b7"
GREEN_DK  = "#34c98a"
YELLOW    = "#fde68a"
BORDER    = "#312f50"
CARD_BG   = "#1a1828"

# ── geometry ───────────────────────────────────────────────────────────────
WIN_W        = 920
CANVAS_W     = 980
CANVAS_H     = 200
LINK_Y       = 100
LINK_X0      = 70
LINK_X1      = 810
LINK_LEN_PX  = LINK_X1 - LINK_X0
PACKET_H     = 30
FPS          = 60
LIGHT_SPEED  = 2e8   # m/s in copper/fibre (approx)


def ms(s):
    """Converts a duration in seconds to a formatted millisecond string.

    Args:
        s (float): Duration in seconds.

    Returns:
        str: Duration in milliseconds, formatted to 3 decimal places.
    """
    return f"{s * 1000:.3f} ms"


class NetworkSim:
    """Interactive GUI simulator for transmission vs propagation delay.

    Renders a Tkinter window with configurable parameters (link distance,
    transmission rate, packet size), animates a packet traversing the link,
    and displays computed delay metrics alongside a comparison table.

    Functions:
        _build_ui: Constructs all top-level Tkinter widgets and frames.
        _build_param_row: Creates the parameter input row with labels and entries.
        _build_canvas_frame: Wraps the animation canvas in a styled frame.
        _build_status_cards: Creates the three metric cards below the canvas.
        _build_table_frame: Builds the delay comparison table and formula area.
        _mk_btn: Factory for styled flat command buttons.
        _draw_static: Draws permanent canvas elements.
        _clear_dynamic: Removes all animation-tagged canvas items.
        _pkt_bits_value: Reads packet size and converts to bits.
        _update_pkt_label: Refreshes the packet size field label after a unit switch.
        _parse_inputs: Reads and validates the three simulation parameters.
        _start: Computes delays and launches the animation loop.
        _animate: Per-frame animation callback.
        _reset: Cancels animation and restores UI to its initial state.
        _populate_table: Fills the delay table for distances relative to the input.
    """

    def __init__(self, root):
        self.root = root
        root.title("Transmission vs Propagation Delay")
        root.configure(bg=BG)
        root.resizable(False, False)

        # Tracks whether packet size is entered in bytes (True) or bits (False).
        self._use_bytes = tk.BooleanVar(value=True)

        self._anim_id  = None
        self._running  = False
        self._t0       = 0.0
        self._t_tx_end = 0.0
        self._t_prop   = 0.0
        self._t_total  = 0.0
        self._sim_scale= 1.0
        self._pkt_bits = 0.0
        self._rate_bps = 0.0
        self._d_km     = 0.0

        self._build_ui()

    # ── UI construction ────────────────────────────────────────────────────
    def _build_ui(self):
        """Constructs and arranges all Tkinter widgets for the simulator window."""
        root = self.root

        # ── header
        hdr = tk.Frame(root, bg=BG)
        hdr.pack(fill="x", pady=(18, 4))
        tk.Label(hdr, text="Transmission  vs  Propagation  Delay",
                 bg=BG, fg=ACCENT_LT,
                 font=("Segoe UI", 16, "bold")).pack()
        tk.Label(hdr, text="Interactive Network Delay Simulator",
                 bg=BG, fg=SUBTEXT,
                 font=("Segoe UI", 9)).pack(pady=(2, 0))

        # ── separator
        tk.Frame(root, bg=BORDER, height=1).pack(fill="x", padx=20, pady=(8, 0))

        self._build_param_row(root)
        self._build_canvas_frame(root)
        self._build_status_cards(root)
        self._build_table_frame(root)

    def _build_param_row(self, root):
        """Creates the parameter input row: Link Length, Rate, Packet Size, and unit toggle.

        Args:
            root (tk.Tk): The root window to attach the frame to.
        """
        pf = tk.Frame(root, bg=SURFACE2,
                      highlightbackground=BORDER, highlightthickness=1)
        pf.pack(padx=20, pady=10, fill="x")

        # Configures the three columns to space evenly.
        for c in range(6):
            pf.columnconfigure(c, weight=1)

        self._vars = {}

        # Static parameters: distance and rate.
        static_params = [
            ("Link Length", "km",   "length_km",  "10",  0),
            ("Trans. Rate", "kbps", "rate_kbps",  "512", 2),
        ]
        for label, unit, key, default, start_col in static_params:
            self._add_param_cell(pf, label, unit, key, default, start_col)

        # Packet size cell with dynamic unit label.
        self._pkt_label_var = tk.StringVar(value="Packet Size")
        self._pkt_unit_var  = tk.StringVar(value="Bytes")
        self._add_param_cell(pf, None, None, "pkt_size", "100", 4,
                             label_var=self._pkt_label_var,
                             unit_var=self._pkt_unit_var)

        # Bytes / Bits radio toggle.
        toggle_outer = tk.Frame(pf, bg=SURFACE2)
        toggle_outer.grid(row=0, column=6, padx=(8, 20), pady=14, sticky="e")

        tk.Label(toggle_outer, text="Unit", bg=SURFACE2, fg=SUBTEXT,
                 font=("Segoe UI", 8, "bold")).pack(anchor="w")

        rb_frame = tk.Frame(toggle_outer, bg=SURFACE, bd=0,
                            highlightbackground=BORDER, highlightthickness=1)
        rb_frame.pack(pady=(3, 0))

        for text, val in [("Bytes", True), ("Bits", False)]:
            rb = tk.Radiobutton(
                rb_frame, text=text, variable=self._use_bytes, value=val,
                bg=SURFACE, fg=TEXT, selectcolor=ACCENT,
                activebackground=SURFACE, activeforeground=ACCENT_LT,
                font=("Segoe UI", 9), indicatoron=True,
                command=self._update_pkt_label, cursor="hand2",
                relief="flat", bd=0
            )
            rb.pack(side="left", padx=8, pady=4)

    def _add_param_cell(self, parent, label, unit, key, default, col,
                        label_var=None, unit_var=None):
        """Adds a labelled entry cell at the given column in the parameter row.

        Args:
            parent (tk.Frame): The grid container.
            label (str or None): Static label text; ignored if label_var is given.
            unit (str or None): Static unit string; ignored if unit_var is given.
            key (str): Dictionary key for self._vars.
            default (str): Initial value for the entry field.
            col (int): Grid column index.
            label_var (tk.StringVar or None): Dynamic variable for the label text.
            unit_var (tk.StringVar or None): Dynamic variable for the unit text.
        """
        cell = tk.Frame(parent, bg=SURFACE2)
        cell.grid(row=0, column=col, columnspan=2, padx=(16, 8), pady=10, sticky="w")

        # Label row: name + unit.
        lbl_frame = tk.Frame(cell, bg=SURFACE2)
        lbl_frame.pack(anchor="w")

        if label_var is not None:
            tk.Label(lbl_frame, textvariable=label_var, bg=SURFACE2, fg=SUBTEXT,
                     font=("Segoe UI", 8, "bold")).pack(side="left")
        else:
            tk.Label(lbl_frame, text=label, bg=SURFACE2, fg=SUBTEXT,
                     font=("Segoe UI", 8, "bold")).pack(side="left")

        if unit_var is not None:
            tk.Label(lbl_frame, textvariable=unit_var, bg=SURFACE2, fg=ACCENT_LT,
                     font=("Segoe UI", 8)).pack(side="left", padx=(4, 0))
        elif unit:
            tk.Label(lbl_frame, text=f" ({unit})", bg=SURFACE2, fg=ACCENT_LT,
                     font=("Segoe UI", 8)).pack(side="left")

        # Entry field.
        var = tk.StringVar(value=default)
        self._vars[key] = var

        entry_frame = tk.Frame(cell, bg=ACCENT, bd=0)
        entry_frame.pack(fill="x", pady=(4, 0))

        tk.Entry(entry_frame, textvariable=var, width=14,
                 bg=CARD_BG, fg=TEXT, insertbackground=ACCENT_LT,
                 relief="flat", font=("Consolas", 12),
                 bd=6).pack(fill="x")

    def _build_canvas_frame(self, root):
        """Creates the styled frame containing the animation canvas.

        Args:
            root (tk.Tk): The root window.
        """
        cf = tk.Frame(root, bg=SURFACE,
                      highlightbackground=BORDER, highlightthickness=1)
        cf.pack(padx=20, pady=(0, 8), fill="x")

        self._canvas = tk.Canvas(cf, width=CANVAS_W, height=CANVAS_H,
                                  bg=BG, highlightthickness=0)
        self._canvas.pack(padx=0, pady=0)
        self._draw_static()

        # ── button bar inside canvas frame
        bf = tk.Frame(cf, bg=SURFACE)
        bf.pack(pady=(4, 10))
        self._btn_start = self._mk_btn(bf, "  Start", self._start, ACCENT)
        self._btn_start.pack(side="left", padx=8)
        self._mk_btn(bf, "  Reset", self._reset, ACCENT2).pack(side="left", padx=8)

        self._lbl_msg = tk.Label(cf, text="", bg=SURFACE, fg=YELLOW,
                                  font=("Segoe UI", 9, "italic"))
        self._lbl_msg.pack(pady=(0, 8))

    def _mk_btn(self, parent, text, cmd, color):
        """Creates and returns a styled flat Tkinter Button.

        Args:
            parent (tk.Widget): The parent widget.
            text (str): Button label text.
            cmd (callable): Callback invoked on click.
            color (str): Hex background colour.

        Returns:
            tk.Button: The configured button widget (not yet packed).
        """
        btn = tk.Button(parent, text=text, command=cmd,
                        bg=color, fg="white", activebackground=color,
                        activeforeground="white", relief="flat",
                        font=("Segoe UI", 10, "bold"),
                        padx=22, pady=7, cursor="hand2", bd=0)
        btn.bind("<Enter>", lambda e: btn.config(bg=self._lighten(color)))
        btn.bind("<Leave>", lambda e: btn.config(bg=color))
        return btn

    @staticmethod
    def _lighten(hex_color):
        """Returns a slightly lighter hex colour for hover effects.

        Args:
            hex_color (str): Source colour in '#rrggbb' format.

        Returns:
            str: Lightened colour in '#rrggbb' format.
        """
        r = min(255, int(hex_color[1:3], 16) + 28)
        g = min(255, int(hex_color[3:5], 16) + 28)
        b = min(255, int(hex_color[5:7], 16) + 28)
        return f"#{r:02x}{g:02x}{b:02x}"

    def _build_status_cards(self, root):
        """Creates the three metric cards (TX delay, Prop delay, Total delay).

        Args:
            root (tk.Tk): The root window.
        """
        sf = tk.Frame(root, bg=BG)
        sf.pack(padx=20, pady=(0, 10), fill="x")

        cards = [
            ("Transmission Delay", "lbl_tx",   ACCENT),
            ("Propagation Delay",  "lbl_prop",  GREEN_DK),
            ("End-to-End Delay",   "lbl_tot",   ACCENT2),
        ]

        for i, (title, attr, color) in enumerate(cards):
            card = tk.Frame(sf, bg=CARD_BG,
                            highlightbackground=color, highlightthickness=1)
            card.grid(row=0, column=i, sticky="nsew", padx=(0 if i == 0 else 8, 0))
            sf.columnconfigure(i, weight=1)

            tk.Label(card, text=title, bg=CARD_BG, fg=SUBTEXT,
                     font=("Segoe UI", 8, "bold")).pack(pady=(10, 2))

            var = tk.StringVar(value="—")
            tk.Label(card, textvariable=var, bg=CARD_BG, fg=color,
                     font=("Consolas", 15, "bold")).pack(pady=(0, 10))

            setattr(self, f"_{attr}", var)

    def _build_table_frame(self, root):
        """Builds the delay comparison table and the formula display area.

        Args:
            root (tk.Tk): The root window.
        """
        tf = tk.Frame(root, bg=SURFACE,
                      highlightbackground=BORDER, highlightthickness=1)
        tf.pack(padx=20, pady=(0, 18), fill="x")

        tk.Label(tf, text="Delay Table  —  varying distance",
                 bg=SURFACE, fg=ACCENT_LT,
                 font=("Segoe UI", 10, "bold")).pack(pady=(12, 6))

        # ── treeview
        cols = ("Distance (km)", "Measured Delay (A1)", "Calculated Delay (A2)")
        self._tree = ttk.Treeview(tf, columns=cols, show="headings",
                                   height=5, style="Custom.Treeview")
        for c in cols:
            self._tree.heading(c, text=c)
            self._tree.column(c, anchor="center", width=265)
        self._tree.pack(padx=16, pady=4, fill="x")

        # ── formula area (Text widget for proper multiline rendering)
        formula_frame = tk.Frame(tf, bg=BG,
                                  highlightbackground=BORDER, highlightthickness=1)
        formula_frame.pack(padx=16, pady=(6, 14), fill="x")

        self._formula_text = tk.Text(
            formula_frame, bg=BG, fg=YELLOW,
            font=("Consolas", 9), relief="flat",
            height=5, bd=8, state="disabled",
            wrap="none", cursor="arrow",
            selectbackground=BG, selectforeground=YELLOW,
        )
        self._formula_text.pack(fill="x")

        # ── apply dark treeview style
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Custom.Treeview",
                         background=CARD_BG, foreground=TEXT,
                         fieldbackground=CARD_BG, rowheight=28,
                         font=("Consolas", 10))
        style.configure("Custom.Treeview.Heading",
                         background=SURFACE2, foreground=ACCENT_LT,
                         font=("Segoe UI", 9, "bold"), relief="flat")
        style.map("Custom.Treeview",
                  background=[("selected", ACCENT)],
                  foreground=[("selected", "white")])

    # ── canvas helpers ─────────────────────────────────────────────────────
    def _draw_static(self):
        """Draws permanent canvas elements: the link line, sender, and receiver nodes."""
        c = self._canvas
        NODE_R = 22

        # Link line.
        c.create_line(LINK_X0, LINK_Y, LINK_X1, LINK_Y, fill=BORDER, width=4)

        # Sender circle with gradient illusion (two overlapping ovals).
        c.create_oval(LINK_X0 - NODE_R, LINK_Y - NODE_R,
                      LINK_X0 + NODE_R, LINK_Y + NODE_R,
                      fill=ACCENT, outline=ACCENT_LT, width=2)
        c.create_text(LINK_X0, LINK_Y, text="S", fill="white",
                      font=("Segoe UI", 13, "bold"))
        c.create_text(LINK_X0, LINK_Y + NODE_R + 14, text="Sender",
                      fill=SUBTEXT, font=("Segoe UI", 8))

        # Receiver circle.
        c.create_oval(LINK_X1 - NODE_R, LINK_Y - NODE_R,
                      LINK_X1 + NODE_R, LINK_Y + NODE_R,
                      fill=ACCENT2, outline=ACCENT2_LT, width=2)
        c.create_text(LINK_X1, LINK_Y, text="R", fill="white",
                      font=("Segoe UI", 13, "bold"))
        c.create_text(LINK_X1, LINK_Y + NODE_R + 14, text="Receiver",
                      fill=SUBTEXT, font=("Segoe UI", 8))

    def _clear_dynamic(self):
        """Removes all canvas items tagged as 'dynamic'."""
        self._canvas.delete("dynamic")

    # ── unit helpers ───────────────────────────────────────────────────────
    def _pkt_bits_value(self):
        """Reads the packet size entry and converts it to bits using the active unit.

        Returns:
            float: Packet size in bits.
        """
        raw = float(self._vars["pkt_size"].get())
        return raw * 8 if self._use_bytes.get() else raw

    def _update_pkt_label(self):
        """Updates the packet size label and unit suffix to reflect the selected unit."""
        if self._use_bytes.get():
            self._pkt_label_var.set("Packet Size")
            self._pkt_unit_var.set(" (Bytes)")
        else:
            self._pkt_label_var.set("Packet Size")
            self._pkt_unit_var.set(" (Bits)")

    # ── simulation logic ───────────────────────────────────────────────────
    def _parse_inputs(self):
        """Reads and returns the three simulation parameters from the entry fields.

        Returns:
            tuple[float, float, float]: Distance in km, rate in kbps, packet
                size in bits.

        Raises:
            ValueError: If any field contains a non-numeric value.
        """
        d_km      = float(self._vars["length_km"].get())
        rate_kbps = float(self._vars["rate_kbps"].get())
        pkt_bits  = self._pkt_bits_value()
        return d_km, rate_kbps, pkt_bits

    def _start(self):
        """Validates inputs, computes delay metrics, and starts the animation loop."""
        if self._running:
            return
        try:
            d_km, rate_kbps, pkt_bits = self._parse_inputs()
        except ValueError:
            self._lbl_msg.config(text="  Invalid input — please enter numeric values.")
            return

        rate_bps = rate_kbps * 1000
        d_m      = d_km * 1000
        t_tx     = pkt_bits / rate_bps    # transmission delay (s)
        t_prop   = d_m / LIGHT_SPEED       # propagation delay (s)
        t_total  = t_tx + t_prop

        self._t_tx_end  = t_tx
        self._t_prop    = t_prop
        self._t_total   = t_total
        self._d_km      = d_km
        self._pkt_bits  = pkt_bits
        self._rate_bps  = rate_bps
        # Maps the full simulation time onto a comfortable 4-second animation.
        self._sim_scale = 4.0 / t_total

        self._lbl_tx.set(ms(t_tx))
        self._lbl_prop.set(ms(t_prop))
        self._lbl_tot.set(ms(t_total))

        if t_prop < t_tx:
            self._lbl_msg.config(
                fg=YELLOW,
                text="  Head-of-packet reaches receiver BEFORE transmission finishes at sender!")
        else:
            self._lbl_msg.config(text="")

        self._populate_table(rate_kbps, pkt_bits, d_km, t_tx, t_prop, t_total)

        self._running = True
        self._t0      = time.time()
        self._btn_start.config(state="disabled")
        self._animate()

    def _animate(self):
        """Per-frame animation callback that moves the packet and updates overlay text."""
        now     = time.time()
        elapsed = (now - self._t0) / self._sim_scale   # simulated seconds
        t_tx    = self._t_tx_end
        t_total = self._t_total

        self._clear_dynamic()
        c = self._canvas

        # Head bit: enters link at t=0, travels continuously to the right.
        head_sim = min(elapsed / t_total, 1.0)
        # Tail bit: not yet on the wire until the last bit is transmitted.
        tail_sim = (
            max(0.0, min((elapsed - t_tx) / t_total, 1.0))
            if elapsed >= t_tx else 0.0
        )

        head_x = LINK_X0 + head_sim * LINK_LEN_PX
        tail_x = LINK_X0 + tail_sim * LINK_LEN_PX

        pkt_x0 = min(tail_x, head_x)
        pkt_x1 = max(tail_x, head_x)

        # Renders the packet body only when it has a visible width.
        if pkt_x1 - pkt_x0 > 2:
            c.create_rectangle(
                pkt_x0, LINK_Y - PACKET_H // 2,
                pkt_x1, LINK_Y + PACKET_H // 2,
                fill=ACCENT, outline=ACCENT_LT, width=1,
                tags="dynamic"
            )
            c.create_text(
                (pkt_x0 + pkt_x1) / 2, LINK_Y,
                text="PKT", fill="white",
                font=("Segoe UI", 8, "bold"), tags="dynamic"
            )

        # Overlay: simulated time and percentage indicators.
        tx_pct   = min(elapsed / t_tx,    1.0) * 100 if t_tx > 0 else 100.0
        prop_pct = min(elapsed / t_total, 1.0) * 100
        c.create_text(
            CANVAS_W // 2, 18,
            text=(f"Sim time: {elapsed * 1000:.2f} ms"
                  f"  |  TX: {tx_pct:.0f}%"
                  f"  |  Prop: {prop_pct:.0f}%"),
            fill=SUBTEXT, font=("Consolas", 9), tags="dynamic"
        )

        # Propagation front arrow above the link.
        if elapsed > 0:
            arrow_x1 = LINK_X0 + head_sim * LINK_LEN_PX
            c.create_line(LINK_X0, LINK_Y - 48,
                           arrow_x1, LINK_Y - 48,
                           fill=GREEN, width=1, dash=(5, 3),
                           arrow="last", tags="dynamic")
            c.create_text(
                LINK_X0 + head_sim * LINK_LEN_PX / 2, LINK_Y - 60,
                text="Propagation \u2192", fill=GREEN,
                font=("Segoe UI", 8), tags="dynamic"
            )

        # Completion state.
        if elapsed >= t_total:
            self._running = False
            self._btn_start.config(state="normal")
            c.create_text(
                CANVAS_W // 2, CANVAS_H - 16,
                text="  Packet fully received!",
                fill=GREEN, font=("Segoe UI", 11, "bold"), tags="dynamic"
            )
            return

        self._anim_id = self.root.after(1000 // FPS, self._animate)

    def _reset(self):
        """Cancels any running animation and restores the UI to its initial state."""
        if self._anim_id:
            self.root.after_cancel(self._anim_id)
        self._running = False
        self._clear_dynamic()
        self._btn_start.config(state="normal")
        self._lbl_tx.set("—")
        self._lbl_prop.set("—")
        self._lbl_tot.set("—")
        self._lbl_msg.config(text="")
        for row in self._tree.get_children():
            self._tree.delete(row)
        self._formula_text.config(state="normal")
        self._formula_text.delete("1.0", "end")
        self._formula_text.config(state="disabled")

    def _populate_table(self, rate_kbps, pkt_bits, cur_d, t_tx, t_prop, t_total):
        """Fills the delay table with five distances centred on the user's input.

        Uses multipliers [0.5, 0.75, 1.0, 1.5, 2.0] so the table spans
        from half to double the configured distance without going far beyond it.

        Args:
            rate_kbps (float): Transmission rate in kilobits per second.
            pkt_bits (float): Packet size in bits.
            cur_d (float): Link distance in kilometres entered by the user.
            t_tx (float): Transmission delay in seconds.
            t_prop (float): Propagation delay in seconds for cur_d.
            t_total (float): End-to-end delay in seconds for cur_d.
        """
        for row in self._tree.get_children():
            self._tree.delete(row)

        # Multipliers are centred on 1.0 (the entered distance) and reach 2× at most.
        multipliers = [0.5, 0.75, 1.0, 1.5, 2.0]
        rate_bps    = rate_kbps * 1000

        for m in multipliers:
            d   = cur_d * m
            d_m = d * 1000
            prop_d   = d_m / LIGHT_SPEED
            total_d  = t_tx + prop_d
            delay_ms = f"{total_d * 1000:.4f} ms"
            # Highlight the row that matches the user-entered distance.
            tag = "current" if m == 1.0 else ""
            self._tree.insert("", "end",
                               values=(f"{d:.2f} km", delay_ms, delay_ms),
                               tags=(tag,))

        # Highlight the current distance row.
        self._tree.tag_configure("current", background=SURFACE2, foreground=ACCENT_LT)

        # Build the formula string.
        using_bytes  = self._use_bytes.get()
        pkt_display  = pkt_bits / 8 if using_bytes else pkt_bits
        unit_label   = "B" if using_bytes else "bits"
        conv_note    = (f"  ({pkt_display:.0f} {unit_label} × 8 = {pkt_bits:.0f} bits)"
                        if using_bytes else "")

        formula = (
            f"  Formula:\n"
            f"  d_trans  = L / R"
            f"  =  {pkt_bits:.0f} bits / {rate_bps:.0f} bps"
            f"  =  {t_tx * 1000:.4f} ms{conv_note}\n"
            f"  d_prop   = d / s"
            f"  =  {cur_d * 1000:.0f} m / {LIGHT_SPEED:.2e} m/s"
            f"  =  {t_prop * 1000:.4f} ms\n"
            f"  d_total  = d_trans + d_prop"
            f"  =  {t_tx * 1000:.4f} + {t_prop * 1000:.4f}"
            f"  =  {t_total * 1000:.4f} ms\n"
            f"  (s = speed of light in medium \u2248 2\u00d710\u2078 m/s)"
        )

        self._formula_text.config(state="normal")
        self._formula_text.delete("1.0", "end")
        self._formula_text.insert("1.0", formula)
        self._formula_text.config(state="disabled")


def main():
    """Entry point — creates the Tk root window and starts the event loop."""
    root = tk.Tk()
    root.geometry(f"{WIN_W}x760")
    NetworkSim(root)
    root.mainloop()


if __name__ == "__main__":
    main()
