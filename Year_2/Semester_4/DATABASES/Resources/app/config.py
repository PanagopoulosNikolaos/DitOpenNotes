"""Theme configuration and styling rules for the ER Analysis application.

This module provides design tokens, color constants, custom CSS, and theme
switching logic adhering to the Orange Light (default) and Soft Dark specifications.
"""

# Color tokens for Light and Dark themes
CUSTOM_CSS = """
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600;700&display=swap');
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css');

/* ==========================================================================
   THEME DESIGN TOKENS (LIGHT DEFAULT & DARK SOFT)
   ========================================================================== */

:root,
body.theme-light,
[data-theme="light"] {
    --bg-deep: #f4f5f8;
    --bg-base: #ffffff;
    --bg-mid: #f9fafb;
    --bg-card: #ffffff;
    --surface: rgba(255, 255, 255, 0.92);
    --surface-2: #f1f3f6;
    --surface-hover: #e5e7eb;
    --border: rgba(0, 0, 0, 0.09);
    --border-accent: rgba(224, 107, 58, 0.45);
    --border-focus: rgba(234, 88, 12, 0.75);
    --accent: #d9531e;
    --accent-light: #b45309;
    --accent-dark: #9a3412;
    --amber: #b45309;
    --orange: #c2410c;
    --text-1: #18181b;
    --text-2: #52525b;
    --text-3: #71717a;
    --green-ok: #059669;
    --green-light: #047857;
    --red-err: #dc2626;
    --red-light: #b91c1c;
    --blue-action: #2563eb;
    --blue-hover: #1d4ed8;
    --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.07), 0 1px 2px rgba(0, 0, 0, 0.04);
    --shadow-md: 0 4px 18px rgba(0, 0, 0, 0.08);
    --shadow-lg: 0 10px 32px rgba(0, 0, 0, 0.12);
    --r-xs: 6px;
    --r-sm: 10px;
    --r-md: 16px;
    --r-lg: 22px;
    --r-xl: 28px;
    --r-pill: 9999px;

    /* Semantic Component Backgrounds */
    --card-bg-subtle: #f8fafc;
    --card-bg-ent-strong: #eff6ff;
    --card-border-ent-strong: #bfdbfe;
    --card-bg-ent-weak: #faf5ff;
    --card-border-ent-weak: #e9d5ff;
    --card-bg-attr: #f0fdf4;
    --card-border-attr: #bbf7d0;
    --card-bg-rel-attr: #fff1f2;
    --card-border-rel-attr: #fecdd3;
    --card-bg-rel: #fff1f2;
    --card-border-rel: #fecdd3;
    --card-bg-rel-ident: #faf5ff;
    --card-border-rel-ident: #e9d5ff;
    --table-header-bg: #f1f5f9;
    --table-alt-bg: #f8fafc;
    --canvas-bg: #ffffff;
    --canvas-header-bg: #f8fafc;
    --canvas-legend-bg: #f1f5f9;
    --svg-canvas-bg: #ffffff;
    --svg-grid-dot: rgba(0, 0, 0, 0.07);
    --svg-node-bg: #ffffff;
    --svg-node-border: rgba(0, 0, 0, 0.14);
    --svg-node-header-bg: #f4f4f5;
    --svg-node-text: #18181b;
    --svg-node-row-alt: rgba(0, 0, 0, 0.025);
    --svg-edge-stroke: #4b5563;
    --svg-edge-bg: #ffffff;
    --svg-edge-text: #18181b;
    --code-bg: #f8fafc;
    --code-text: #0f172a;
    --code-border: rgba(0, 0, 0, 0.10);
    --header-bg: rgba(255, 255, 255, 0.90);
    --menu-bg: #ffffff;
    --menu-border: rgba(224, 107, 58, 0.35);
    --input-bg: #ffffff;
    --badge-bg: #f3f4f6;
}

body.theme-dark,
[data-theme="dark"],
body.body--dark {
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

    /* Semantic Component Backgrounds */
    --card-bg-subtle: #201f1d;
    --card-bg-ent-strong: #1c202a;
    --card-border-ent-strong: rgba(59, 130, 246, 0.3);
    --card-bg-ent-weak: #251f2d;
    --card-border-ent-weak: rgba(168, 85, 247, 0.5);
    --card-bg-attr: #1e231e;
    --card-border-attr: rgba(16, 185, 129, 0.25);
    --card-bg-rel-attr: #231e21;
    --card-border-rel-attr: rgba(244, 63, 94, 0.25);
    --card-bg-rel: #251d20;
    --card-border-rel: rgba(244, 63, 94, 0.3);
    --card-bg-rel-ident: #251f2d;
    --card-border-rel-ident: rgba(168, 85, 247, 0.4);
    --table-header-bg: rgba(255, 255, 255, 0.05);
    --table-alt-bg: rgba(255, 255, 255, 0.03);
    --canvas-bg: #1a1918;
    --canvas-header-bg: #121211;
    --canvas-legend-bg: #171615;
    --svg-canvas-bg: #121211;
    --svg-grid-dot: rgba(255, 255, 255, 0.08);
    --svg-node-bg: #1c1b1a;
    --svg-node-border: rgba(255, 255, 255, 0.12);
    --svg-node-header-bg: #26211e;
    --svg-node-text: #f4f1ea;
    --svg-node-row-alt: rgba(255, 255, 255, 0.025);
    --svg-edge-stroke: #b5b0a4;
    --svg-edge-bg: #141413;
    --svg-edge-text: #f4f1ea;
    --code-bg: #10100f;
    --code-text: #f4f1ea;
    --code-border: rgba(255, 255, 255, 0.08);
    --header-bg: rgba(20, 20, 19, 0.90);
    --menu-bg: #1c1b1a;
    --menu-border: rgba(224, 107, 58, 0.3);
    --input-bg: #201f1d;
    --badge-bg: #201f1d;
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
    transition: background-color 0.25s ease, color 0.25s ease;
}

/* Light & Dark Ambient Background Gradients */
body.theme-light::before,
[data-theme="light"] body::before,
body:not(.theme-dark)::before {
    content: '';
    position: fixed;
    inset: 0;
    background:
        radial-gradient(ellipse 75% 55% at 15% 5%, rgba(224, 107, 58, 0.05) 0%, transparent 65%),
        radial-gradient(ellipse 55% 45% at 85% 95%, rgba(217, 119, 6, 0.04) 0%, transparent 60%),
        linear-gradient(160deg, #f8f9fa 0%, #ffffff 45%, #f4f5f8 100%);
    pointer-events: none;
    z-index: -1;
}

body.theme-dark::before,
[data-theme="dark"] body::before {
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

/* Glassmorphism Card Containers */
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
    background: linear-gradient(135deg, var(--text-1) 30%, var(--accent) 100%);
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

/* Interactive Text Highlight Badges */
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
    filter: brightness(1.15);
    box-shadow: 0 2px 12px rgba(224, 107, 58, 0.35);
}

/* Light Mode Badges (Default) */
:root,
body.theme-light,
[data-theme="light"] {
    .badge-entity-strong {
        background-color: #eff6ff;
        color: #1d4ed8;
        border: 1px solid #93c5fd;
    }

    .badge-entity-weak {
        background-color: #faf5ff;
        color: #7e22ce;
        border: 1px dashed #c084fc;
    }

    .badge-key-pk {
        background-color: #ffedd5;
        color: #9a3412;
        border-bottom: 2px solid var(--accent);
        font-weight: 700;
    }

    .badge-key-candidate {
        background-color: #fef3c7;
        color: #92400e;
        border-bottom: 2px dashed var(--accent-light);
    }

    .badge-key-partial {
        background-color: #fef9c3;
        color: #854d0e;
        border-bottom: 2px dashed #ca8a04;
    }

    .badge-attr-simple {
        background-color: #ecfdf5;
        color: #047857;
        border: 1px solid #6ee7b7;
    }

    .badge-attr-composite {
        background-color: #f0fdfa;
        color: #0f766e;
        border: 1px dashed #5eead4;
    }

    .badge-attr-multi {
        background-color: #fdf4ff;
        color: #a21caf;
        border: 1px double #f0abfc;
    }

    .badge-attr-derived {
        background-color: #ecfeff;
        color: #0e7490;
        border: 1px dotted #67e8f9;
    }

    .badge-rel,
    .badge-rel-11,
    .badge-rel-1n,
    .badge-rel-nm {
        background-color: #fff1f2;
        color: #be123c;
        border: 1px solid #fda4af;
    }

    .tag-label {
        background-color: rgba(0, 0, 0, 0.08);
        color: var(--text-1);
    }
}

/* Dark Mode Badges */
body.theme-dark,
[data-theme="dark"] {
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

    .badge-attr-derived {
        background-color: rgba(6, 182, 212, 0.20);
        color: #67e8f9;
        border: 1px dotted rgba(6, 182, 212, 0.55);
    }

    .badge-rel,
    .badge-rel-11,
    .badge-rel-1n,
    .badge-rel-nm {
        background-color: rgba(244, 63, 94, 0.20);
        color: #fda4af;
        border: 1px solid rgba(244, 63, 94, 0.45);
    }

    .tag-label {
        background-color: rgba(0, 0, 0, 0.50);
        color: #f4f1ea;
    }
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

/* Data Tables */
.dark-table {
    width: 100%;
    border-collapse: collapse;
    margin: 1rem 0;
    border-radius: var(--r-md);
    overflow: hidden;
    border: 1px solid var(--border);
    background: var(--surface);
}

.dark-table th {
    background: var(--table-header-bg);
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
    border-bottom: 1px solid var(--border);
}

.dark-table tr:hover {
    background: var(--table-alt-bg);
}

.dark-table code {
    font-family: 'JetBrains Mono', monospace;
    color: var(--accent);
    background: var(--surface-2);
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
    background: var(--surface-2);
    color: var(--text-2);
}

.filter-chip:hover {
    background: var(--surface-hover);
    color: var(--text-1);
    border-color: var(--border-accent);
}

.filter-chip.active {
    background: linear-gradient(135deg, var(--accent) 0%, var(--amber) 100%);
    color: #ffffff !important;
    border-color: transparent;
    box-shadow: 0 2px 12px rgba(224, 107, 58, 0.35);
}

.filter-chip-danger.active {
    background: linear-gradient(135deg, #78756d 0%, #475569 100%);
    color: #ffffff !important;
}

/* Action Buttons */
.btn-primary {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 0.5rem;
    padding: 10px 22px;
    border-radius: var(--r-sm);
    background: linear-gradient(135deg, #e06b3a 0%, #d97706 100%);
    color: #ffffff;
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
    padding: 8px 16px;
    border-radius: var(--r-sm);
    background: var(--surface-2);
    color: var(--text-1);
    font-weight: 600;
    font-size: 0.84rem;
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
    background-color: var(--svg-canvas-bg);
    background-image: radial-gradient(var(--svg-grid-dot) 1.2px, transparent 1.2px);
    background-size: 24px 24px;
    border-radius: var(--r-lg);
    transition: background-color 0.25s ease;
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

/* Theme Adaptive Helpers for Hardcoded Classes */
body.theme-light .bg-\[\#201f1d\],
body.theme-light .bg-\[\#1c1b1a\],
body.theme-light .bg-\[\#171615\],
body.theme-light .bg-\[\#141413\],
body.theme-light .bg-\[\#121211\],
body.theme-light .bg-\[\#1a1918\],
body.theme-light .bg-\[\#242321\],
body.theme-light .bg-\[\#10100f\] {
    background-color: var(--bg-card) !important;
}

body.theme-light .text-\[\#f4f1ea\] {
    color: var(--text-1) !important;
}

body.theme-light .text-\[\#b5b0a4\] {
    color: var(--text-2) !important;
}

body.theme-light .text-\[\#78756d\] {
    color: var(--text-3) !important;
}

body.theme-light .text-\[\#fdba74\],
body.theme-light .text-\[\#fde68a\] {
    color: var(--accent-dark) !important;
}

body.theme-light .border-\[rgba\(255\,255\,255\,0\.08\)\],
body.theme-light .border-\[rgba\(255\,255\,255\,0\.06\)\],
body.theme-light .border-\[rgba\(255\,255\,255\,0\.04\)\] {
    border-color: var(--border) !important;
}

/* ==========================================================================
   INK-SAVING PRINT & A4 PDF EXPORT STYLES (ALWAYS CLEAN WHITE)
   ========================================================================== */
@media print {
    @page {
        size: A4 portrait;
        margin: 5mm 8mm 5mm 8mm;
    }

    *, *::before, *::after {
        -webkit-print-color-adjust: exact !important;
        print-color-adjust: exact !important;
        color-adjust: exact !important;
    }

    html, body {
        background-color: #ffffff !important;
        background-image: none !important;
        color: #18181b !important;
        font-size: 8.5pt !important;
        margin: 0 !important;
        padding: 0 !important;
        width: 100% !important;
    }

    /* Reset flex/scroll heights for clean multi-page print layout */
    #q-app, .q-layout, .q-page-container, .q-page, main, .nicegui-column {
        display: block !important;
        position: static !important;
        overflow: visible !important;
        height: auto !important;
        max-height: none !important;
        flex: none !important;
        float: none !important;
    }

    body::before {
        display: none !important;
    }

    /* Hide UI navigation, headers, footers, toolbars, and controls */
    header, nav, .q-header, .q-footer, .no-print {
        display: none !important;
    }

    /* Keep headings with their following content */
    h1, h2, h3, h4, .section-title, .print-header-banner {
        page-break-after: avoid !important;
        break-after: avoid !important;
        margin-top: 2px !important;
        margin-bottom: 4px !important;
        color: #18181b !important;
    }

    h2 {
        font-size: 11pt !important;
        color: #9a3412 !important;
    }

    h3 {
        font-size: 10pt !important;
        color: #c2410c !important;
    }

    /* Spacing container resets for print */
    .space-y-10 > :not([hidden]) ~ :not([hidden]),
    .space-y-4 > :not([hidden]) ~ :not([hidden]),
    .gap-6 {
        margin-top: 0 !important;
        margin-bottom: 0 !important;
        gap: 6px !important;
    }

    .glass-panel, .glass-panel-accent {
        background: #ffffff !important;
        border: 1px solid #d1d5db !important;
        box-shadow: none !important;
        backdrop-filter: none !important;
        -webkit-backdrop-filter: none !important;
        padding: 6px 10px !important;
        border-radius: 6px !important;
        margin-bottom: 6px !important;
        page-break-inside: auto !important;
        break-inside: auto !important;
    }

    /* Section Flow */
    .print-section {
        display: block !important;
        page-break-before: auto !important;
        break-before: auto !important;
        page-break-after: auto !important;
        break-after: auto !important;
        page-break-inside: auto !important;
        break-inside: auto !important;
        margin: 0 0 6px 0 !important;
        padding: 0 !important;
        width: 100% !important;
    }

    .print-avoid-break,
    .attr-card,
    .attr-card-rel,
    .rel-card {
        page-break-inside: avoid !important;
        break-inside: avoid !important;
    }

    .dark-table {
        page-break-inside: auto !important;
        break-inside: auto !important;
        background: #ffffff !important;
        border: 1px solid #d1d5db !important;
    }

    .dark-table th {
        background: #f3f4f6 !important;
        color: #111827 !important;
        border-bottom: 1px solid #d1d5db !important;
    }

    .dark-table td {
        background: #ffffff !important;
        color: #1f2937 !important;
        border-bottom: 1px solid #e5e7eb !important;
    }

    .dark-table tr {
        page-break-inside: avoid !important;
        break-inside: auto !important;
    }

    /* Single Section Print Filtering */
    body[data-print-target="canvas"] .print-section:not(.print-canvas),
    body[data-print-target="attributes"] .print-section:not(.print-attributes),
    body[data-print-target="keys"] .print-section:not(.print-keys),
    body[data-print-target="relationships"] .print-section:not(.print-relationships),
    body[data-print-target="er-diagram"] .print-section:not(.print-er-diagram),
    body[data-print-target="sql-ddl"] .print-section:not(.print-sql-ddl) {
        display: none !important;
    }

    /* Section 1: Canvas Print Layout */
    .print-canvas #canvas-text {
        background: #ffffff !important;
        padding: 6px 10px !important;
        font-size: 8.5pt !important;
        line-height: 1.35 !important;
        color: #18181b !important;
        border: 1px solid #e5e7eb !important;
        border-radius: 6px !important;
    }

    .print-canvas p {
        margin: 2px 0 !important;
    }

    .print-canvas .highlight-box {
        padding: 1px 3px !important;
        font-size: 8.5pt !important;
    }

    .print-canvas .tag-label {
        font-size: 6pt !important;
        padding: 0px 2px !important;
        background: #e5e7eb !important;
        color: #18181b !important;
    }

    /* Section 2: Attributes Print Layout */
    .print-attributes .attr-card-container {
        display: grid !important;
        grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
        gap: 6px !important;
    }

    .print-attributes .attr-card {
        margin-bottom: 0 !important;
        padding: 4px 8px !important;
        background: #f0fdf4 !important;
        border: 1px solid #86efac !important;
        color: #065f46 !important;
        border-radius: 5px !important;
    }

    .print-attributes .attr-card-rel {
        grid-column: span 2 !important;
        margin-bottom: 0 !important;
        padding: 4px 8px !important;
        background: #fff1f2 !important;
        border: 1px solid #fda4af !important;
        color: #9f1239 !important;
        border-radius: 5px !important;
    }

    .print-attributes ul {
        margin: 1px 0 0 0 !important;
        padding-left: 8px !important;
    }

    .print-attributes li {
        font-size: 7.5pt !important;
        margin-bottom: 1px !important;
        line-height: 1.2 !important;
        color: #374151 !important;
    }

    /* Section 3: Keys Analysis Table Layout */
    .print-keys .dark-table {
        font-size: 7.5pt !important;
        margin: 2px 0 !important;
        background: #ffffff !important;
        border-collapse: collapse !important;
        width: 100% !important;
    }

    .print-keys .dark-table th {
        padding: 3px 5px !important;
        font-size: 7.5pt !important;
        background: #f3f4f6 !important;
        color: #111827 !important;
    }

    .print-keys .dark-table td {
        padding: 3px 5px !important;
        font-size: 7pt !important;
        line-height: 1.2 !important;
        color: #1f2937 !important;
    }

    /* Section 4: Relationships Layout */
    .print-relationships .rel-card-container {
        display: grid !important;
        grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
        gap: 6px !important;
    }

    .print-relationships .rel-card {
        margin-bottom: 0 !important;
        padding: 4px 8px !important;
        border-radius: 5px !important;
        background: #fff1f2 !important;
        border: 1px solid #fda4af !important;
    }

    .print-relationships p,
    .print-relationships div,
    .print-relationships span {
        font-size: 7.5pt !important;
        line-height: 1.2 !important;
        color: #374151 !important;
    }

    /* Section 5: ER Diagram SVG Layout */
    .print-er-diagram {
        page-break-before: auto !important;
        break-before: auto !important;
        page-break-inside: avoid !important;
        break-inside: avoid !important;
        margin-top: 0 !important;
        margin-bottom: 4px !important;
    }

    .print-er-diagram #er-svg-canvas {
        height: 520px !important;
        max-height: 520px !important;
        width: 100% !important;
        background-color: #ffffff !important;
        border: 1px solid #d1d5db !important;
        border-radius: 6px !important;
    }

    body[data-print-target="er-diagram"] .print-er-diagram #er-svg-canvas {
        height: 540px !important;
        max-height: 540px !important;
    }

    /* Section 6: SQL DDL Schema Layout */
    .print-sql-ddl {
        page-break-before: auto !important;
        break-before: auto !important;
        page-break-inside: auto !important;
        break-inside: auto !important;
        margin-top: 0 !important;
        overflow: visible !important;
        width: 100% !important;
    }

    .print-sql-ddl .sql-code-container,
    .print-sql-ddl .q-card,
    .print-sql-ddl .nicegui-code {
        background: #f8fafc !important;
        border: 1px solid #d1d5db !important;
        border-radius: 6px !important;
        padding: 6px 10px !important;
        margin: 2px 0 !important;
        overflow: visible !important;
        width: 100% !important;
        box-sizing: border-box !important;
        page-break-inside: auto !important;
        break-inside: auto !important;
    }

    .print-sql-ddl pre,
    .print-sql-ddl code {
        font-family: 'JetBrains Mono', monospace !important;
        font-size: 7.5pt !important;
        line-height: 1.25 !important;
        white-space: pre-wrap !important;
        word-break: break-word !important;
        color: #0f172a !important;
        background: transparent !important;
        padding: 0 !important;
        margin: 0 !important;
        overflow: visible !important;
    }

    body[data-print-target="sql-ddl"] .print-sql-ddl pre,
    body[data-print-target="sql-ddl"] .print-sql-ddl code {
        font-size: 8pt !important;
        line-height: 1.3 !important;
    }
}
"""

THEME_HEAD_SCRIPT = """
<script>
    function getAppTheme() {
        return localStorage.getItem('app_theme') || 'light';
    }

    function setAppTheme(theme) {
        const isDark = (theme === 'dark');
        document.documentElement.setAttribute('data-theme', isDark ? 'dark' : 'light');
        if (isDark) {
            document.body.classList.add('theme-dark');
            document.body.classList.remove('theme-light');
        } else {
            document.body.classList.add('theme-light');
            document.body.classList.remove('theme-dark');
        }
        localStorage.setItem('app_theme', isDark ? 'dark' : 'light');

        // Update Theme Toggle Icon & Label in UI
        const themeBtn = document.getElementById('theme-toggle-btn');
        if (themeBtn) {
            const icon = themeBtn.querySelector('i');
            const label = themeBtn.querySelector('.theme-btn-label');
            if (icon) {
                icon.className = isDark ? 'fa-solid fa-sun text-[#f59e0b]' : 'fa-solid fa-moon text-[#71717a]';
            }
            if (label) {
                label.textContent = isDark ? 'Φωτεινό' : 'Σκοτεινό';
            }
        }

        // Re-render ER diagram with active theme palette
        if (typeof initERDiagram === 'function') {
            initERDiagram();
        }
    }

    function toggleAppTheme() {
        const current = getAppTheme();
        const next = current === 'dark' ? 'light' : 'dark';
        setAppTheme(next);
    }

    document.addEventListener('DOMContentLoaded', () => {
        const savedTheme = getAppTheme();
        setAppTheme(savedTheme);
    });

    setTimeout(() => {
        const savedTheme = getAppTheme();
        setAppTheme(savedTheme);
    }, 50);
</script>
"""
