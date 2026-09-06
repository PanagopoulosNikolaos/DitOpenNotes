"""Theme configuration, design tokens, and global helper scripts for the
Computer Networks exam solutions application.

This module provides the Orange Light (default) and Soft Dark token sets,
custom CSS for the annotated solution sheet, KaTeX integration, and the
global JavaScript helpers (theme switching, targeted A4 printing, standalone
HTML export, and LaTeX rendering).
"""

# KaTeX CDN head block: required for the KaTeX derivations of Archetype B
# (computational exercises render their formulas through renderAllLatex()).
KATEX_HEAD = """
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css" crossorigin="anonymous">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js" crossorigin="anonymous"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js" crossorigin="anonymous"></script>
"""

CUSTOM_CSS = r"""
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600;700&display=swap');
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css');

/* ==========================================================================
   THEME DESIGN TOKENS (LIGHT DEFAULT & DARK SOFT)
   ========================================================================== */

/* Light tokens: applied to :root, the body's theme-light class, and the
   explicit data-theme="light" attribute. The :root selector is also used
   alone so the default (no attribute) loads in light mode. The dark block
   below uses :root[data-theme="dark"] (more specific than :root) to
   guarantee a complete override of every token. */
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
    --card-bg-term: #eff6ff;
    --card-border-term: #bfdbfe;
    --card-bg-given: #fffbeb;
    --card-border-given: #fde68a;
    --card-bg-proto: #f0fdf4;
    --card-border-proto: #bbf7d0;
    --card-bg-method: #faf5ff;
    --card-border-method: #e9d5ff;
    --card-bg-answer: #ecfdf5;
    --card-border-answer: #a7f3d0;
    --card-bg-question: #fff7ed;
    --card-border-question: #fed7aa;
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
    --svg-node-detail: #52525b;
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

/* Dark tokens: scoped to the most specific selector that always matches
   when dark mode is active (:root[data-theme="dark"] wins over :root at the
   same specificity because of the attribute selector), plus the body's
   theme-dark / body--dark classes for belt-and-braces coverage. */
:root[data-theme="dark"],
body.theme-dark,
body.body--dark,
[data-theme="dark"] {
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
    --card-bg-term: #1c202a;
    --card-border-term: rgba(59, 130, 246, 0.3);
    --card-bg-given: #262017;
    --card-border-given: rgba(245, 158, 11, 0.3);
    --card-bg-proto: #1e231e;
    --card-border-proto: rgba(16, 185, 129, 0.25);
    --card-bg-method: #251f2d;
    --card-border-method: rgba(168, 85, 247, 0.4);
    --card-bg-answer: #12241c;
    --card-border-answer: rgba(16, 185, 129, 0.4);
    --card-bg-question: #251d15;
    --card-border-question: rgba(224, 107, 58, 0.3);
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
    --svg-node-detail: #b5b0a4;
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
    .badge-term {
        background-color: #eff6ff;
        color: #1d4ed8;
        border: 1px solid #93c5fd;
    }

    .badge-given {
        background-color: #fffbeb;
        color: #b45309;
        border: 1px solid #fcd34d;
    }

    .badge-proto {
        background-color: #ecfdf5;
        color: #047857;
        border: 1px solid #6ee7b7;
    }

    .badge-method {
        background-color: #faf5ff;
        color: #7e22ce;
        border: 1px dashed #c084fc;
    }

    .tag-label {
        background-color: rgba(0, 0, 0, 0.08);
        color: var(--text-1);
    }
}

/* Dark Mode Badges */
body.theme-dark,
[data-theme="dark"] {
    .badge-term {
        background-color: rgba(59, 130, 246, 0.20);
        color: #93c5fd;
        border: 1px solid rgba(59, 130, 246, 0.45);
    }

    .badge-given {
        background-color: rgba(245, 158, 11, 0.20);
        color: #fde68a;
        border: 1px solid rgba(245, 158, 11, 0.45);
    }

    .badge-proto {
        background-color: rgba(16, 185, 129, 0.20);
        color: #86efac;
        border: 1px solid rgba(16, 185, 129, 0.45);
    }

    .badge-method {
        background-color: rgba(168, 85, 247, 0.20);
        color: #d8b4fe;
        border: 1px dashed rgba(168, 85, 247, 0.55);
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

/* Themata banner inside the exam paper canvas */
.thema-banner {
    display: inline-flex;
    align-items: center;
    gap: 0.6rem;
    font-weight: 800;
    font-size: 1.02rem;
    color: var(--accent-dark);
    background: var(--card-bg-question);
    border: 1px solid var(--card-border-question);
    border-left: 4px solid var(--accent);
    border-radius: var(--r-sm);
    padding: 8px 14px;
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
    vertical-align: top;
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

/* KaTeX sizing harmonized with the sheet typography */
.katex {
    font-size: 1.02em;
}

.katex-display {
    margin: 0.35rem 0;
    overflow-x: auto;
    overflow-y: hidden;
    padding: 2px 0;
}

/* Question solution blocks (open, sequential; zero accordions) */
.thema-divider {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    padding: 14px 18px;
    border-radius: var(--r-md);
    background: linear-gradient(135deg, var(--card-bg-question) 0%, var(--surface) 100%);
    border: 1px solid var(--card-border-question);
    border-left: 5px solid var(--accent);
}

.thema-divider .thema-text {
    font-weight: 900;
    font-size: 1.05rem;
    color: var(--accent-dark);
}

.qtype-badge {
    font-size: 0.62rem;
    font-weight: 800;
    letter-spacing: 0.04em;
    padding: 2px 8px;
    border-radius: var(--r-pill);
    text-transform: uppercase;
}

.qtype-mcq {
    background: var(--card-bg-term);
    color: var(--blue-action);
    border: 1px solid var(--card-border-term);
}

.qtype-computational {
    background: var(--card-bg-given);
    color: var(--amber);
    border: 1px solid var(--card-border-given);
}

.qtype-theory {
    background: var(--card-bg-method);
    color: #9333ea;
    border: 1px solid var(--card-border-method);
}

body.theme-dark .qtype-theory {
    color: #d8b4fe;
}

.qtype-comparison {
    background: var(--card-bg-proto);
    color: var(--green-ok);
    border: 1px solid var(--card-border-proto);
}

/* Prompt (ekfwnosi) box */
.prompt-box {
    background: var(--card-bg-question);
    border: 1px solid var(--card-border-question);
    border-radius: var(--r-sm);
    padding: 12px 16px;
    color: var(--text-1);
    font-size: 0.95rem;
    line-height: 1.65;
}

/* MCQ static option rows */
.option-row {
    display: flex;
    align-items: flex-start;
    gap: 0.75rem;
    padding: 10px 14px;
    border: 1px solid var(--border);
    border-radius: var(--r-sm);
    background: var(--surface);
    transition: border-color 0.2s ease;
}

.option-row.option-correct {
    border: 1px solid var(--green-ok);
    background: var(--card-bg-answer);
}

.option-letter {
    flex: 0 0 auto;
    width: 28px;
    height: 28px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    font-weight: 800;
    font-size: 0.8rem;
    border-radius: var(--r-pill);
    background: var(--surface-2);
    color: var(--text-2);
    border: 1px solid var(--border);
}

.option-row.option-correct .option-letter {
    background: var(--green-ok);
    color: #ffffff;
    border-color: var(--green-ok);
}

.option-correct-tag {
    display: inline-flex;
    align-items: center;
    gap: 0.35rem;
    color: var(--green-ok);
    font-weight: 800;
    font-size: 0.72rem;
    letter-spacing: 0.04em;
    white-space: nowrap;
}

.option-why {
    font-size: 0.78rem;
    color: var(--text-3);
    margin-top: 2px;
    line-height: 1.45;
}

/* Given parameters box */
.given-box {
    background: var(--card-bg-given);
    border: 1px solid var(--card-border-given);
    border-radius: var(--r-sm);
    padding: 12px 16px;
}

.given-row {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    align-items: baseline;
    font-size: 0.88rem;
    color: var(--text-1);
    padding: 3px 0;
}

.given-label {
    font-weight: 700;
    color: var(--amber);
    min-width: 210px;
}

.given-value {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.84rem;
}

/* Calculation step cards */
.calc-step {
    display: flex;
    flex-direction: column;
    gap: 0.3rem;
    padding: 12px 16px;
    border: 1px solid var(--border);
    border-left: 4px solid var(--amber);
    border-radius: var(--r-sm);
    background: var(--surface);
}

.step-chip {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    font-size: 0.68rem;
    font-weight: 800;
    letter-spacing: 0.05em;
    color: var(--amber);
    text-transform: uppercase;
}

.step-desc {
    font-size: 0.9rem;
    color: var(--text-2);
    line-height: 1.55;
}

.step-result {
    font-size: 0.88rem;
    font-weight: 700;
    color: var(--text-1);
    font-family: 'JetBrains Mono', monospace;
}

/* Final answer box */
.answer-final {
    display: flex;
    align-items: flex-start;
    gap: 0.75rem;
    padding: 14px 18px;
    border: 1px solid var(--green-ok);
    border-left: 5px solid var(--green-ok);
    border-radius: var(--r-sm);
    background: var(--card-bg-answer);
    color: var(--text-1);
    font-size: 0.95rem;
    line-height: 1.6;
}

.answer-final i {
    color: var(--green-ok);
    font-size: 1.1rem;
    margin-top: 3px;
}

/* Tip list */
.tip-item {
    display: flex;
    align-items: flex-start;
    gap: 0.5rem;
    font-size: 0.8rem;
    color: var(--text-2);
    line-height: 1.5;
    padding: 2px 0;
}

.tip-item i {
    color: var(--amber);
    margin-top: 3px;
}

/* SVG diagram styling */
#exam-svg-canvas {
    user-select: none;
    cursor: grab;
    background-color: var(--svg-canvas-bg);
    background-image: radial-gradient(var(--svg-grid-dot) 1.2px, transparent 1.2px);
    background-size: 24px 24px;
    border-radius: var(--r-lg);
    transition: background-color 0.25s ease;
}

#exam-svg-canvas:active {
    cursor: grabbing;
}

.svg-node-rect {
    fill: var(--svg-node-bg);
    stroke: var(--svg-node-border);
    stroke-width: 1.4;
}

.svg-node-rect.svg-node-hl {
    stroke: var(--accent);
    stroke-width: 2;
}

.svg-node-header {
    fill: var(--svg-node-header-bg);
}

.svg-node-title {
    fill: var(--svg-node-text);
    font-family: 'Outfit', system-ui, sans-serif;
    font-size: 13px;
    font-weight: 700;
}

.svg-node-detail {
    fill: var(--svg-node-detail);
    font-family: 'JetBrains Mono', monospace;
    font-size: 10.5px;
}

.svg-edge-line {
    fill: none;
    stroke: var(--svg-edge-stroke);
    stroke-width: 2;
}

.svg-edge-dashed {
    stroke-dasharray: 6 5;
}

.svg-edge-label-bg {
    fill: var(--svg-edge-bg);
    stroke: var(--svg-edge-stroke);
    stroke-width: 0.8;
}

.svg-edge-label {
    fill: var(--svg-edge-text);
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    font-weight: 600;
}

.svg-arrow-path {
    fill: var(--svg-edge-stroke);
}

/* Quasar Select Dropdown, Menu & Dialog Theming (Light & Dark Support) */
.q-menu,
.q-select__popup,
.app-select-popup,
.q-dialog__inner > div {
    background-color: var(--menu-bg) !important;
    background: var(--menu-bg) !important;
    color: var(--text-1) !important;
    border: 1px solid var(--border-accent) !important;
    border-radius: var(--r-sm) !important;
    box-shadow: var(--shadow-lg) !important;
    backdrop-filter: blur(16px) saturate(1.4) !important;
    -webkit-backdrop-filter: blur(16px) saturate(1.4) !important;
}

.q-menu .q-item,
.q-select__popup .q-item,
.app-select-popup .q-item {
    color: var(--text-1) !important;
    font-family: 'Outfit', system-ui, -apple-system, sans-serif !important;
    font-size: 0.84rem !important;
    transition: background-color 0.18s ease, color 0.18s ease;
    padding: 8px 14px !important;
    min-height: 38px !important;
}

.q-menu .q-item:hover,
.q-menu .q-item.q-manual-focusable--focused,
.q-select__popup .q-item:hover,
.q-select__popup .q-item.q-manual-focusable--focused,
.app-select-popup .q-item:hover,
.app-select-popup .q-item.q-manual-focusable--focused {
    background-color: var(--surface-hover) !important;
    color: var(--text-1) !important;
}

.q-menu .q-item.q-item--active,
.q-select__popup .q-item.q-item--active,
.app-select-popup .q-item.q-item--active,
.q-menu .q-item.q-item--active .q-item__label,
.q-select__popup .q-item.q-item--active .q-item__label,
.app-select-popup .q-item.q-item--active .q-item__label {
    background-color: rgba(224, 107, 58, 0.18) !important;
    color: var(--accent) !important;
    font-weight: 700 !important;
}

.q-menu .q-item__label,
.q-select__popup .q-item__label,
.app-select-popup .q-item__label {
    color: inherit !important;
}

.q-menu .q-item__label--caption,
.q-select__popup .q-item__label--caption,
.app-select-popup .q-item__label--caption {
    color: var(--text-2) !important;
}

/* Quasar Select Field Controls */
.q-field--outlined .q-field__control {
    background-color: var(--input-bg) !important;
    border-color: var(--border-accent) !important;
    color: var(--text-1) !important;
    border-radius: var(--r-sm) !important;
}

.q-field--outlined .q-field__control::before {
    border-color: var(--border-accent) !important;
}

.q-field--outlined:hover .q-field__control::before {
    border-color: var(--accent) !important;
}

.q-field--outlined.q-field--focused .q-field__control::after {
    border-color: var(--accent) !important;
}

.q-field__native,
.q-field__input {
    color: var(--text-1) !important;
    font-family: 'Outfit', system-ui, -apple-system, sans-serif !important;
    font-size: 0.84rem !important;
    font-weight: 500 !important;
}

.q-field__marginal,
.q-field__append {
    color: var(--text-2) !important;
}

.q-field--focused .q-field__marginal,
.q-field--focused .q-field__append {
    color: var(--accent) !important;
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
    h1, h2, h3, h4, .section-title, .thema-divider {
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

    .glass-panel {
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

    /* Section flow */
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
    .calc-step,
    .option-row,
    .answer-final,
    .given-box,
    .prompt-box {
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

    /* Single section print filtering */
    body[data-print-target="canvas"] .print-section:not(.print-canvas),
    body[data-print-target="solutions"] .print-section:not(.print-solutions),
    body[data-print-target="tables"] .print-section:not(.print-tables),
    body[data-print-target="diagram"] .print-section:not(.print-diagram),
    body[data-print-target="code"] .print-section:not(.print-code) {
        display: none !important;
    }

    /* Section 1: exam canvas print layout */
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

    .print-canvas .thema-banner {
        background: #fff7ed !important;
        border-color: #fed7aa !important;
        color: #9a3412 !important;
    }

    /* Section 2: question solutions print layout */
    .print-solutions .prompt-box {
        background: #ffffff !important;
        border: 1px solid #e5e7eb !important;
        color: #1f2937 !important;
    }

    .print-solutions .option-row {
        background: #ffffff !important;
        border: 1px solid #e5e7eb !important;
    }

    .print-solutions .option-row.option-correct {
        background: #ecfdf5 !important;
        border-color: #059669 !important;
    }

    .print-solutions .calc-step {
        background: #ffffff !important;
        border: 1px solid #d1d5db !important;
        border-left: 4px solid #b45309 !important;
    }

    .print-solutions .answer-final {
        background: #ecfdf5 !important;
        border-color: #059669 !important;
    }

    .print-solutions .given-box {
        background: #fffbeb !important;
        border-color: #fde68a !important;
    }

    /* Section 3: analysis tables print layout */
    .print-tables .dark-table {
        font-size: 7.5pt !important;
        margin: 2px 0 !important;
        background: #ffffff !important;
        border-collapse: collapse !important;
        width: 100% !important;
    }

    .print-tables .dark-table th {
        padding: 3px 5px !important;
        font-size: 7.5pt !important;
        background: #f3f4f6 !important;
        color: #111827 !important;
    }

    .print-tables .dark-table td {
        padding: 3px 5px !important;
        font-size: 7pt !important;
        line-height: 1.2 !important;
        color: #1f2937 !important;
    }

    /* Section 4: diagram SVG layout */
    .print-diagram {
        page-break-before: auto !important;
        break-before: auto !important;
        page-break-inside: avoid !important;
        break-inside: avoid !important;
        margin-top: 0 !important;
        margin-bottom: 4px !important;
    }

    .print-diagram #exam-svg-canvas {
        height: 520px !important;
        max-height: 520px !important;
        width: 100% !important;
        background-color: #ffffff !important;
        border: 1px solid #d1d5db !important;
        border-radius: 6px !important;
    }

    body[data-print-target="diagram"] .print-diagram #exam-svg-canvas {
        height: 540px !important;
        max-height: 540px !important;
    }

    /* Section 5: verification code layout */
    .print-code {
        page-break-before: auto !important;
        break-before: auto !important;
        page-break-inside: auto !important;
        break-inside: auto !important;
        margin-top: 0 !important;
        overflow: visible !important;
        width: 100% !important;
    }

    .print-code .code-container,
    .print-code .q-card,
    .print-code .nicegui-code {
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

    .print-code pre,
    .print-code code {
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
}
"""

# Global JavaScript helpers: theme switching, KaTeX rendering, targeted A4
# printing, and standalone HTML export. Content-level interaction remains
# hover-to-explain only (the whitelist of Section 2.3 of the generator spec).
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
            document.body.classList.add('body--dark');
        } else {
            document.body.classList.add('theme-light');
            document.body.classList.remove('theme-dark');
            document.body.classList.remove('body--dark');
        }
        if (window.Quasar && window.Quasar.Dark) {
            try {
                window.Quasar.Dark.set(isDark);
            } catch (e) {}
        }
        localStorage.setItem('app_theme', isDark ? 'dark' : 'light');

        // Update theme toggle icon and label in the UI
        const themeBtn = document.getElementById('theme-toggle-btn');
        if (themeBtn) {
            const icon = themeBtn.querySelector('i');
            const label = themeBtn.querySelector('.theme-btn-label');
            if (icon) {
                icon.className = isDark ? 'fa-solid fa-sun text-amber-500' : 'fa-solid fa-moon text-slate-500';
            }
            if (label) {
                label.textContent = isDark ? 'Φωτεινό' : 'Σκοτεινό';
            }
        }

        // Re-render the exam diagram with the active theme palette
        if (typeof initExamDiagram === 'function') {
            initExamDiagram();
        }
    }

    function toggleAppTheme() {
        const current = getAppTheme();
        const next = current === 'dark' ? 'light' : 'dark';
        setAppTheme(next);
    }

    // Re-invoked after every content re-render so KaTeX derivations appear.
    function renderAllLatex() {
        if (typeof renderMathInElement === 'function') {
            try {
                renderMathInElement(document.body, {
                    delimiters: [
                        {left: '$$', right: '$$', display: true},
                        {left: '\\\\[', right: '\\\\]', display: true},
                        {left: '\\\\(', right: '\\\\)', display: false}
                    ],
                    throwOnError: false
                });
            } catch (e) {}
        }
    }

    // Targeted A4 printing: 'all' prints every visible print section.
    function printExamSection(target) {
        if (!target || target === 'all') {
            document.body.removeAttribute('data-print-target');
        } else {
            document.body.setAttribute('data-print-target', target);
        }

        // Ensure every highlight category is enabled for clean print output
        if (typeof setFilterMode === 'function') {
            setFilterMode('all');
        }

        // Reset diagram zoom and re-center before printing
        if (typeof resetExamZoom === 'function') {
            resetExamZoom();
        }

        setTimeout(() => {
            window.print();
            setTimeout(() => {
                document.body.removeAttribute('data-print-target');
            }, 500);
        }, 150);
    }

    // Export of a self-contained standalone HTML study guide.
    function downloadStandaloneHTML() {
        const title = document.querySelector('h1')?.innerText || 'Λυμένο Θέμα Εξετάσεων Δικτύων';
        const subTitle = document.querySelector('header label')?.innerText || '';
        const printSections = document.querySelectorAll('.print-section');
        let sectionsHTML = '';

        printSections.forEach(sec => {
            const clone = sec.cloneNode(true);
            clone.querySelectorAll('.no-print').forEach(el => el.remove());
            sectionsHTML += `<div class="section-wrapper">${clone.outerHTML}</div>`;
        });

        const fullHTML = `<!DOCTYPE html>
<html lang="el">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>${title}</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
    <style>
        * { box-sizing: border-box; -webkit-print-color-adjust: exact !important; print-color-adjust: exact !important; color-adjust: exact !important; }
        body { background-color: #ffffff; color: #18181b; font-family: system-ui, -apple-system, sans-serif; font-size: 13px; line-height: 1.5; margin: 0; padding: 24px; }
        .header-banner { border-bottom: 2px solid rgba(224, 107, 58, 0.4); padding-bottom: 12px; margin-bottom: 20px; }
        .header-banner h1 { margin: 0; font-size: 22px; color: #c2410c; }
        .glass-panel { background: #ffffff; border: 1px solid #d1d5db; border-radius: 8px; padding: 16px; margin-bottom: 16px; }
        h2, h3 { color: #9a3412; margin-top: 0; }
        .thema-divider { border-left: 5px solid #c2410c; background: #fff7ed; padding: 10px 14px; border-radius: 6px; margin-bottom: 10px; font-weight: 800; color: #9a3412; }
        .prompt-box { background: #fff7ed; border: 1px solid #fed7aa; border-radius: 6px; padding: 10px 14px; margin: 8px 0; }
        .calc-step { border: 1px solid #d1d5db; border-left: 4px solid #b45309; border-radius: 6px; padding: 10px 14px; margin: 8px 0; }
        .answer-final { border: 1px solid #059669; border-left: 5px solid #059669; background: #ecfdf5; border-radius: 6px; padding: 10px 14px; margin: 8px 0; }
        .option-row { border: 1px solid #e5e7eb; border-radius: 6px; padding: 8px 12px; margin: 6px 0; }
        .option-row.option-correct { border-color: #059669; background: #ecfdf5; }
        .dark-table { width: 100%; border-collapse: collapse; margin-top: 8px; }
        .dark-table th, .dark-table td { border: 1px solid #d1d5db; padding: 6px 10px; font-size: 12px; text-align: left; }
        .dark-table th { background: #f3f4f6; color: #111827; }
        .given-box { background: #fffbeb; border: 1px solid #fde68a; border-radius: 6px; padding: 10px 14px; margin: 8px 0; }
        #exam-svg-canvas { width: 100%; height: 500px; background: #ffffff; border: 1px solid #d1d5db; border-radius: 8px; }
        pre, code { font-family: monospace; font-size: 11px; white-space: pre-wrap; word-break: break-word; }
        .code-container { background: #f8fafc; border: 1px solid #d1d5db; padding: 14px; border-radius: 8px; color: #0f172a; }
        @media print {
            @page { size: A4 portrait; margin: 6mm 8mm; }
            body { padding: 0; font-size: 8.5pt; background: #ffffff !important; color: #18181b !important; }
            .dark-table th, .dark-table td { padding: 3px 5px; font-size: 7.5pt; }
            .code-container pre { font-size: 7.5pt; line-height: 1.25; }
        }
    </style>
</head>
<body>
    <div class="header-banner">
        <h1>${title}</h1>
        <p style="color:#52525b; margin: 4px 0 0 0; font-size: 12px;">${subTitle}</p>
    </div>
    ${sectionsHTML}
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"></script>
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            if (typeof renderMathInElement === 'function') {
                renderMathInElement(document.body, {
                    delimiters: [
                        {left: '$$', right: '$$', display: true},
                        {left: '\\\\[', right: '\\\\]', display: true},
                        {left: '\\\\(', right: '\\\\)', display: false}
                    ],
                    throwOnError: false
                });
            }
        });
    </script>
</body>
</html>`;

        const blob = new Blob([fullHTML], { type: 'text/html;charset=utf-8;' });
        const url = URL.createObjectURL(blob);
        const link = document.createElement('a');
        link.href = url;
        link.download = `NetExam_Report_${new Date().toISOString().slice(0,10)}.html`;
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
        URL.revokeObjectURL(url);
    }

    document.addEventListener('DOMContentLoaded', () => {
        const savedTheme = getAppTheme();
        setAppTheme(savedTheme);
        renderAllLatex();
    });

    setTimeout(() => {
        const savedTheme = getAppTheme();
        setAppTheme(savedTheme);
        renderAllLatex();
    }, 50);
</script>
"""
