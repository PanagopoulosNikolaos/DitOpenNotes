"""Theme configuration and styling rules for the ER Analysis application.

This module provides design tokens, color constants, and custom CSS
adhering to the Orange and Dark Soft design specification.
"""

# Color tokens from the Orange and Dark Soft design specification
BG_DEEP = "#141413"
BG_BASE = "#1c1b1a"
BG_MID = "#242321"
BG_CARD = "#201f1d"

SURFACE = "rgba(255, 255, 255, 0.045)"
SURFACE_2 = "rgba(255, 255, 255, 0.075)"
SURFACE_HOVER = "rgba(255, 255, 255, 0.09)"

BORDER = "rgba(255, 255, 255, 0.08)"
BORDER_ACCENT = "rgba(224, 107, 58, 0.35)"
BORDER_FOCUS = "rgba(234, 88, 12, 0.65)"

ACCENT = "#e06b3a"
ACCENT_LIGHT = "#f59e0b"
ACCENT_DARK = "#c2410c"
AMBER = "#d97706"
ORANGE = "#ea580c"

TEXT_1 = "#f4f1ea"
TEXT_2 = "#b5b0a4"
TEXT_3 = "#78756d"

GREEN_OK = "#10b981"
GREEN_LIGHT = "#34d399"
RED_ERR = "#ef4444"
RED_LIGHT = "#f87171"
BLUE_ACTION = "#4f8ec9"
BLUE_HOVER = "#62a1dc"

CUSTOM_CSS = """
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600;700&display=swap');
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css');

:root {
    --bg-deep: #141413;
    --bg-base: #1c1b1a;
    --bg-mid: #242321;
    --bg-card: #201f1d;
    --surface: rgba(255, 255, 255, 0.045);
    --surface-2: rgba(255, 255, 255, 0.075);
    --surface-hover: rgba(255, 255, 255, 0.09);
    --border: rgba(255, 255, 255, 0.08);
    --border-accent: rgba(224, 107, 58, 0.35);
    --border-focus: rgba(234, 88, 12, 0.65);
    --accent: #e06b3a;
    --accent-light: #f59e0b;
    --accent-dark: #c2410c;
    --amber: #d97706;
    --orange: #ea580c;
    --text-1: #f4f1ea;
    --text-2: #b5b0a4;
    --text-3: #78756d;
    --green-ok: #10b981;
    --green-light: #34d399;
    --red-err: #ef4444;
    --red-light: #f87171;
    --blue-action: #4f8ec9;
    --blue-hover: #62a1dc;
    --shadow-sm: 0 4px 16px rgba(0, 0, 0, 0.40);
    --shadow-md: 0 6px 28px rgba(0, 0, 0, 0.50);
    --shadow-lg: 0 10px 48px rgba(0, 0, 0, 0.60);
    --r-xs: 6px;
    --r-sm: 10px;
    --r-md: 16px;
    --r-lg: 22px;
    --r-xl: 28px;
    --r-pill: 9999px;
}

*, *::before, *::after {
    box-sizing: border-box;
}

body {
    margin: 0;
    padding: 0;
    font-family: 'Outfit', system-ui, -apple-system, sans-serif !important;
    background: var(--bg-base) !important;
    color: var(--text-1) !important;
    min-height: 100vh;
    overflow-x: hidden;
}

body::before {
    content: '';
    position: fixed;
    inset: 0;
    background:
        radial-gradient(ellipse 75% 55% at 15% 5%, rgba(224, 107, 58, 0.09) 0%, transparent 65%),
        radial-gradient(ellipse 55% 45% at 85% 95%, rgba(217, 119, 6, 0.07) 0%, transparent 60%),
        linear-gradient(160deg, var(--bg-deep) 0%, var(--bg-base) 45%, var(--bg-mid) 100%);
    pointer-events: none;
    z-index: -1;
}

/* Glassmorphism Card Container */
.glass-panel {
    background: var(--surface);
    backdrop-filter: blur(16px) saturate(1.4);
    -webkit-backdrop-filter: blur(16px) saturate(1.4);
    border: 1px solid var(--border);
    border-radius: var(--r-xl);
    padding: 1.75rem;
    box-shadow: var(--shadow-md);
    transition: all 0.28s ease;
}

.glass-panel:hover {
    border-color: var(--border-accent);
    box-shadow: var(--shadow-lg), 0 0 32px rgba(224, 107, 58, 0.12);
}

.glass-panel-accent {
    background: var(--surface);
    backdrop-filter: blur(16px) saturate(1.4);
    -webkit-backdrop-filter: blur(16px) saturate(1.4);
    border: 1px solid var(--border-accent);
    border-radius: var(--r-xl);
    padding: 1.75rem;
    box-shadow: var(--shadow-md);
    transition: all 0.28s ease;
}

.glass-panel-accent:hover {
    border-color: rgba(224, 107, 58, 0.75);
    box-shadow: var(--shadow-lg), 0 0 36px rgba(224, 107, 58, 0.18);
    transform: translateY(-2px);
}

/* Typography Gradient Headers */
.gradient-title {
    font-size: clamp(1.8rem, 3.5vw, 2.5rem);
    font-weight: 900;
    letter-spacing: -0.03em;
    background: linear-gradient(135deg, #f4f1ea 30%, var(--accent) 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin: 0;
    line-height: 1.2;
}

.section-title {
    font-size: 1.45rem;
    font-weight: 800;
    letter-spacing: -0.02em;
    color: var(--text-1);
    display: flex;
    align-items: center;
    gap: 0.75rem;
}

.section-title i {
    color: var(--accent);
}

/* Interactive Text Highlight Badges - INLINE FOR PERFECT FLOW */
.highlight-box {
    display: inline;
    border-radius: var(--r-xs);
    padding: 2px 5px;
    margin: 0 1px;
    transition: all 0.22s ease-in-out;
    cursor: pointer;
    box-decoration-break: clone;
    -webkit-box-decoration-break: clone;
}

.highlight-box.highlight-plain {
    background-color: transparent !important;
    border: none !important;
    color: inherit !important;
    box-shadow: none !important;
    padding: 0 !important;
    margin: 0 !important;
}

.highlight-box.highlight-plain strong {
    font-weight: inherit !important;
}

.highlight-box:not(.highlight-plain):hover {
    filter: brightness(1.22);
    box-shadow: 0 2px 12px rgba(224, 107, 58, 0.35);
}

.badge-entity-strong {
    background-color: rgba(59, 130, 246, 0.20);
    color: #93c5fd;
    border: 1px solid rgba(59, 130, 246, 0.45);
}

.badge-entity-weak {
    background-color: rgba(168, 85, 247, 0.20);
    color: #d8b4fe;
    border: 1px dashed rgba(168, 85, 247, 0.55);
}

.badge-key-pk {
    background-color: rgba(224, 107, 58, 0.24);
    color: #fdba74;
    border-bottom: 2px solid var(--accent);
    font-weight: 700;
}

.badge-key-candidate {
    background-color: rgba(245, 158, 11, 0.20);
    color: #fde68a;
    border-bottom: 2px dashed var(--accent-light);
}

.badge-key-partial {
    background-color: rgba(234, 179, 8, 0.20);
    color: #fef08a;
    border-bottom: 2px dashed rgba(234, 179, 8, 0.75);
}

.badge-attr-simple {
    background-color: rgba(16, 185, 129, 0.20);
    color: #86efac;
    border: 1px solid rgba(16, 185, 129, 0.45);
}

.badge-attr-composite {
    background-color: rgba(20, 184, 166, 0.20);
    color: #5eead4;
    border: 1px dashed rgba(20, 184, 166, 0.50);
}

.badge-attr-multi {
    background-color: rgba(217, 70, 239, 0.20);
    color: #f0abfc;
    border: 1px double rgba(217, 70, 239, 0.55);
}

.badge-rel {
    background-color: rgba(244, 63, 94, 0.20);
    color: #fda4af;
    border: 1px solid rgba(244, 63, 94, 0.45);
}

.tag-label {
    font-size: 0.65rem;
    font-weight: 800;
    padding: 1px 5px;
    border-radius: var(--r-xs);
    margin-left: 4px;
    margin-right: 2px;
    vertical-align: baseline;
    display: inline-block;
    letter-spacing: 0.03em;
}

/* Custom Scrollbars */
::-webkit-scrollbar {
    width: 7px;
    height: 7px;
}

::-webkit-scrollbar-track {
    background: var(--bg-deep);
}

::-webkit-scrollbar-thumb {
    background: rgba(224, 107, 58, 0.30);
    border-radius: 4px;
}

::-webkit-scrollbar-thumb:hover {
    background: var(--accent);
}

/* Dark Data Tables */
.dark-table {
    width: 100%;
    border-collapse: collapse;
    margin: 1rem 0;
    border-radius: var(--r-md);
    overflow: hidden;
    border: 1px solid var(--border);
    background: rgba(0, 0, 0, 0.25);
}

.dark-table th {
    background: rgba(255, 255, 255, 0.05);
    color: var(--text-1);
    font-weight: 700;
    padding: 12px 16px;
    font-size: 0.90rem;
    border-bottom: 1px solid var(--border);
    text-align: left;
}

.dark-table td {
    padding: 12px 16px;
    color: var(--text-2);
    font-size: 0.88rem;
    border-bottom: 1px solid rgba(255, 255, 255, 0.04);
}

.dark-table tr:hover {
    background: rgba(255, 255, 255, 0.03);
}

.dark-table code {
    font-family: 'JetBrains Mono', monospace;
    color: var(--accent-light);
    background: rgba(255, 255, 255, 0.06);
    padding: 2px 6px;
    border-radius: 4px;
    font-size: 0.84rem;
}

/* Filter Chips */
.filter-chip {
    padding: 6px 14px;
    border-radius: var(--r-sm);
    font-size: 0.82rem;
    font-weight: 700;
    cursor: pointer;
    transition: all 0.2s ease;
    border: 1px solid var(--border);
    background: var(--surface);
    color: var(--text-2);
}

.filter-chip:hover {
    background: var(--surface-hover);
    color: var(--text-1);
    border-color: var(--border-accent);
}

.filter-chip.active {
    background: linear-gradient(135deg, var(--accent) 0%, var(--amber) 100%);
    color: #141413;
    border-color: transparent;
    box-shadow: 0 2px 12px rgba(224, 107, 58, 0.35);
}

.filter-chip-danger.active {
    background: linear-gradient(135deg, #78756d 0%, #475569 100%);
    color: #f4f1ea;
}

/* Primary Gradient Button */
.btn-primary {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 0.5rem;
    padding: 10px 22px;
    border-radius: var(--r-sm);
    background: linear-gradient(135deg, #e06b3a 0%, #d97706 100%);
    color: #141413;
    font-weight: 800;
    font-size: 0.88rem;
    border: none;
    cursor: pointer;
    box-shadow: 0 4px 16px rgba(224, 107, 58, 0.35);
    transition: all 0.2s ease;
}

.btn-primary:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(224, 107, 58, 0.45);
}

.btn-secondary {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 0.5rem;
    padding: 10px 20px;
    border-radius: var(--r-sm);
    background: var(--surface-2);
    color: var(--text-1);
    font-weight: 600;
    font-size: 0.88rem;
    border: 1px solid var(--border);
    cursor: pointer;
    transition: all 0.2s ease;
}

.btn-secondary:hover {
    background: var(--surface-hover);
    border-color: var(--border-accent);
}

/* SVG ER Diagram Styling */
#er-svg-canvas {
    user-select: none;
    cursor: grab;
    background-color: #121211;
    background-image: radial-gradient(rgba(255, 255, 255, 0.08) 1.2px, transparent 1.2px);
    background-size: 24px 24px;
    border-radius: var(--r-lg);
}

#er-svg-canvas:active {
    cursor: grabbing;
}

.er-node {
    transition: filter 0.15s ease;
    cursor: pointer;
}

.er-node:hover {
    filter: drop-shadow(0 6px 16px rgba(224, 107, 58, 0.3));
}
"""
