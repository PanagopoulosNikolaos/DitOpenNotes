"""Theme configuration, design tokens, LaTeX support, and styling rules for Digital Electronics app.

Provides design tokens for Orange Light (default) and Soft Dark themes, KaTeX math
support, print-to-PDF styles, canvas highlight classes, and global JavaScript helpers.
"""

import re
import markdown2


def renderMathHtml(text: str) -> str:
    """Converts markdown text to HTML while preserving LaTeX math delimiters and expressions intact.

    Protects inline math ($...$) and display math ($$...$$) with collision-free
    alphanumeric tokens before passing to markdown2, preventing subscripts and underscores
    from being mangled into HTML emphasis tags.

    Args:
        text (str): The markdown string containing optional LaTeX blocks.

    Returns:
        str: Rendered HTML string with uncorrupted LaTeX delimiters.
    """
    if not text:
        return ""

    math_blocks: list[str] = []

    def saveMath(match: re.Match) -> str:
        idx = len(math_blocks)
        math_blocks.append(match.group(0))
        return f"QQMATHTOKEN{idx}ZZ"

    # Pattern matches $$...$$ display math or $...$ inline math
    pattern = re.compile(r"(\$\$.*?\$\$|\$[^\$\n]+?\$)", re.DOTALL)
    protected_text = pattern.sub(saveMath, text)

    html = markdown2.markdown(protected_text, extras=["fenced-code-blocks", "tables"])

    for idx, block in enumerate(math_blocks):
        html = html.replace(f"QQMATHTOKEN{idx}ZZ", block)

    return html


# Color tokens for Light and Dark themes
CUSTOM_CSS = r"""
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600;700&display=swap');
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css');

/* ==========================================================================
   THEME DESIGN TOKENS (ORANGE LIGHT DEFAULT & SOFT DARK)
   ========================================================================== */

:root,
body.theme-light,
[data-theme="light"] {
    --bg-deep: #f4f5f8;
    --bg-base: #ffffff;
    --bg-mid: #f9fafb;
    --bg-card: #ffffff;
    --surface: rgba(255, 255, 255, 0.94);
    --surface-2: #f1f3f6;
    --surface-hover: #e5e7eb;
    --border: rgba(0, 0, 0, 0.09);
    --border-accent: rgba(217, 83, 30, 0.45);
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
    --purple: #7c3aed;
    --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.07), 0 1px 2px rgba(0, 0, 0, 0.04);
    --shadow-md: 0 4px 18px rgba(0, 0, 0, 0.08);
    --shadow-lg: 0 10px 32px rgba(0, 0, 0, 0.12);
    --r-xs: 6px;
    --r-sm: 10px;
    --r-md: 16px;
    --r-lg: 22px;
    --r-xl: 28px;
    --r-pill: 9999px;

    /* Component Semantics */
    --card-bg-subtle: #f8fafc;
    --table-header-bg: #f1f5f9;
    --table-alt-bg: #f8fafc;
    --canvas-bg: #ffffff;
    --canvas-header-bg: #f8fafc;
    --canvas-legend-bg: #f1f5f9;
    --svg-canvas-bg: #ffffff;
    --svg-grid-dot: rgba(0, 0, 0, 0.08);
    --svg-stroke: #475569;
    --svg-fill: #f8fafc;
    --code-bg: #f8fafc;
    --code-text: #0f172a;
    --code-border: rgba(0, 0, 0, 0.10);
    --header-bg: rgba(255, 255, 255, 0.92);
    --menu-bg: #ffffff;
    --menu-border: rgba(217, 83, 30, 0.35);
    --input-bg: #ffffff;
    --badge-bg: #f3f4f6;

    /* Light Theme Highlight Badges */
    --hl-binary-bg: rgba(37, 99, 235, 0.12);
    --hl-binary-color: #1d4ed8;
    --hl-binary-border: #93c5fd;

    --hl-boolean-bg: rgba(217, 83, 30, 0.12);
    --hl-boolean-color: #c2410c;
    --hl-boolean-border: #fdba74;

    --hl-fsm-bg: rgba(124, 58, 237, 0.12);
    --hl-fsm-color: #6d28d9;
    --hl-fsm-border: #c4b5fd;

    --hl-vhdl-bg: rgba(5, 150, 105, 0.12);
    --hl-vhdl-color: #047857;
    --hl-vhdl-border: #6ee7b7;

    --hl-param-bg: rgba(217, 119, 6, 0.12);
    --hl-param-color: #b45309;
    --hl-param-border: #fcd34d;
}

body.theme-dark,
[data-theme="dark"] {
    --bg-deep: #090a0f;
    --bg-base: #0f111a;
    --bg-mid: #141724;
    --bg-card: #181b2e;
    --surface: rgba(24, 27, 46, 0.94);
    --surface-2: #1e2238;
    --surface-hover: #262b46;
    --border: rgba(255, 255, 255, 0.08);
    --border-accent: rgba(224, 107, 58, 0.50);
    --border-focus: rgba(249, 115, 22, 0.75);
    --accent: #e06b3a;
    --accent-light: #f97316;
    --accent-dark: #c2410c;
    --amber: #f59e0b;
    --orange: #f97316;
    --text-1: #f1f5f9;
    --text-2: #cbd5e1;
    --text-3: #94a3b8;
    --green-ok: #10b981;
    --green-light: #34d399;
    --red-err: #ef4444;
    --red-light: #f87171;
    --blue-action: #3b82f6;
    --blue-hover: #60a5fa;
    --purple: #a855f7;
    --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.40);
    --shadow-md: 0 4px 18px rgba(0, 0, 0, 0.45);
    --shadow-lg: 0 10px 32px rgba(0, 0, 0, 0.55);

    /* Component Semantics */
    --card-bg-subtle: #141724;
    --table-header-bg: #1a1e33;
    --table-alt-bg: #141724;
    --canvas-bg: #0f111a;
    --canvas-header-bg: #141724;
    --canvas-legend-bg: #1a1e33;
    --svg-canvas-bg: #0b0d14;
    --svg-grid-dot: rgba(255, 255, 255, 0.08);
    --svg-stroke: #94a3b8;
    --svg-fill: #141724;
    --code-bg: #0b0d14;
    --code-text: #e2e8f0;
    --code-border: rgba(255, 255, 255, 0.10);
    --header-bg: rgba(15, 17, 26, 0.92);
    --menu-bg: #181b2e;
    --menu-border: rgba(224, 107, 58, 0.40);
    --input-bg: #141724;
    --badge-bg: #1e2238;

    /* Dark Theme Highlight Badges */
    --hl-binary-bg: rgba(59, 130, 246, 0.20);
    --hl-binary-color: #93c5fd;
    --hl-binary-border: #3b82f6;

    --hl-boolean-bg: rgba(249, 115, 22, 0.20);
    --hl-boolean-color: #fdba74;
    --hl-boolean-border: #f97316;

    --hl-fsm-bg: rgba(168, 85, 247, 0.20);
    --hl-fsm-color: #d8b4fe;
    --hl-fsm-border: #a855f7;

    --hl-vhdl-bg: rgba(16, 185, 129, 0.20);
    --hl-vhdl-color: #6ee7b7;
    --hl-vhdl-border: #10b981;

    --hl-param-bg: rgba(245, 158, 11, 0.20);
    --hl-param-color: #fde68a;
    --hl-param-border: #f59e0b;
}

/* ==========================================================================
   GLOBAL RESET & TYPOGRAPHY
   ========================================================================== */

* {
    box-sizing: border-box;
}

body {
    font-family: 'Outfit', sans-serif;
    background-color: var(--bg-deep);
    color: var(--text-1);
    line-height: 1.6;
    margin: 0;
    padding: 0;
    transition: background-color 0.25s ease, color 0.25s ease;
}

code, pre, .font-mono {
    font-family: 'JetBrains Mono', monospace !important;
}

/* Glass panel */
.glass-panel {
    background: var(--surface);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border: 1px solid var(--border);
    border-radius: var(--r-md);
    box-shadow: var(--shadow-sm);
    transition: background 0.25s ease, border-color 0.25s ease;
}

/* Highlight badge styles */
.highlight-badge {
    position: relative;
    display: inline-flex;
    align-items: center;
    gap: 4px;
    padding: 2px 8px;
    border-radius: 6px;
    font-weight: 600;
    font-size: 0.9em;
    cursor: help;
    transition: all 0.2s ease;
    border: 1px solid transparent;
}

.highlight-badge:hover {
    transform: translateY(-1px);
    box-shadow: var(--shadow-md);
    filter: brightness(1.05);
}

.badge-binary {
    background-color: var(--hl-binary-bg);
    color: var(--hl-binary-color);
    border-color: var(--hl-binary-border);
}

.badge-boolean {
    background-color: var(--hl-boolean-bg);
    color: var(--hl-boolean-color);
    border-color: var(--hl-boolean-border);
}

.badge-fsm {
    background-color: var(--hl-fsm-bg);
    color: var(--hl-fsm-color);
    border-color: var(--hl-fsm-border);
}

.badge-vhdl {
    background-color: var(--hl-vhdl-bg);
    color: var(--hl-vhdl-color);
    border-color: var(--hl-vhdl-border);
}

.badge-param {
    background-color: var(--hl-param-bg);
    color: var(--hl-param-color);
    border-color: var(--hl-param-border);
}

.tag-label {
    font-size: 0.65em;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    opacity: 0.85;
    padding: 1px 4px;
    background: rgba(0, 0, 0, 0.08);
    border-radius: 4px;
    margin-left: 2px;
}

/* Filter chips */
.filter-chip-btn {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 6px 12px;
    border-radius: var(--r-pill);
    font-size: 0.75rem;
    font-weight: 600;
    background: var(--surface-2);
    color: var(--text-2);
    border: 1px solid var(--border);
    cursor: pointer;
    transition: all 0.2s ease;
}

.filter-chip-btn:hover {
    background: var(--surface-hover);
    color: var(--text-1);
    border-color: var(--border-accent);
}

.filter-chip-btn.active {
    background: var(--accent);
    color: #ffffff;
    border-color: var(--accent);
    box-shadow: 0 2px 8px rgba(217, 83, 30, 0.35);
}

/* Clean mode overrides */
.clean-text-mode .highlight-badge {
    background: transparent !important;
    border-color: transparent !important;
    color: inherit !important;
    padding: 0 !important;
    box-shadow: none !important;
    cursor: text !important;
}

.clean-text-mode .tag-label {
    display: none !important;
}

/* Multiple choice static rows */
.option-row-static {
    display: flex;
    align-items: flex-start;
    padding: 10px 14px;
    border-radius: var(--r-sm);
    background: var(--surface-2);
    border: 1px solid var(--border);
    transition: all 0.2s ease;
}

.option-row-static.correct {
    background: rgba(5, 150, 105, 0.10);
    border-color: var(--green-ok);
}

.option-badge {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 24px;
    height: 24px;
    border-radius: 6px;
    font-weight: 800;
    font-size: 0.75rem;
    background: var(--surface);
    color: var(--text-2);
    border: 1px solid var(--border);
    margin-right: 10px;
    flex-shrink: 0;
}

.option-badge.correct {
    background: var(--green-ok);
    color: #ffffff;
    border-color: var(--green-ok);
}

/* Derivation cards */
.derivation-step-card {
    background: var(--surface-2);
    border: 1px solid var(--border);
    border-radius: var(--r-md);
    padding: 16px;
    transition: all 0.2s ease;
}

.result-highlight-box {
    background: rgba(5, 150, 105, 0.12);
    border: 2px solid var(--green-ok);
    border-radius: var(--r-md);
    padding: 14px 18px;
}

/* Code wrapper */
.code-wrapper {
    background: var(--code-bg);
    border: 1px solid var(--code-border);
    border-radius: var(--r-md);
}

/* ==========================================================================
   QUASAR POPUP & SELECT DROPDOWN THEMING
   ========================================================================== */

.q-menu,
.app-select-popup,
.q-select__dialog,
.q-menu--square,
.q-popup {
    background-color: var(--bg-card) !important;
    background: var(--bg-card) !important;
    color: var(--text-1) !important;
    border: 1px solid var(--border) !important;
    box-shadow: var(--shadow-lg) !important;
    border-radius: var(--r-sm) !important;
}

.q-menu .q-item,
.app-select-popup .q-item,
.q-select__dialog .q-item {
    color: var(--text-1) !important;
    transition: background 0.15s ease, color 0.15s ease;
    font-size: 0.82rem !important;
    padding: 8px 12px !important;
}

.q-menu .q-item:hover,
.q-menu .q-item.q-manual-focusable--focused,
.app-select-popup .q-item:hover,
.app-select-popup .q-item.q-manual-focusable--focused,
.q-select__dialog .q-item:hover {
    background: var(--surface-hover) !important;
    color: var(--accent) !important;
}

.q-menu .q-item.q-item--active,
.q-menu .q-item.text-primary,
.app-select-popup .q-item.q-item--active,
.app-select-popup .q-item.text-primary,
.q-select__dialog .q-item.q-item--active {
    background: rgba(217, 83, 30, 0.18) !important;
    color: var(--accent) !important;
    font-weight: 700 !important;
}

.q-item__label {
    color: inherit !important;
}

.q-select .q-field__native,
.q-select .q-field__prefix,
.q-select .q-field__suffix,
.q-select .q-field__input {
    color: var(--text-1) !important;
}

.q-field--outlined .q-field__control {
    border-color: var(--border) !important;
    background: var(--input-bg) !important;
}

.q-field--outlined:hover .q-field__control {
    border-color: var(--border-accent) !important;
}

.q-field--outlined.q-field--focused .q-field__control {
    border-color: var(--border-focus) !important;
}

/* Print CSS */
@media print {
    body {
        background: #ffffff !important;
        color: #000000 !important;
    }
    .no-print {
        display: none !important;
    }
    .glass-panel {
        box-shadow: none !important;
        border: 1px solid #cccccc !important;
        background: #ffffff !important;
    }
}
"""

# KaTeX CDN and Scripts head injection
KATEX_AND_SCRIPTS_HEAD = r"""
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"></script>

<script>
// Global Theme Switcher
function toggleAppTheme() {
    const isDark = document.body.classList.contains('theme-dark') || document.body.classList.contains('body--dark');
    if (isDark) {
        document.body.classList.remove('theme-dark', 'body--dark');
        document.body.classList.add('theme-light');
        document.documentElement.setAttribute('data-theme', 'light');
        localStorage.setItem('de_theme', 'light');
        if (window.Quasar && window.Quasar.dark) {
            window.Quasar.dark.set(false);
        }
    } else {
        document.body.classList.remove('theme-light');
        document.body.classList.add('theme-dark', 'body--dark');
        document.documentElement.setAttribute('data-theme', 'dark');
        localStorage.setItem('de_theme', 'dark');
        if (window.Quasar && window.Quasar.dark) {
            window.Quasar.dark.set(true);
        }
    }
}

// Global KaTeX Render Helper
function renderAllLatex() {
    if (typeof renderMathInElement === 'function') {
        const targets = document.querySelectorAll('.latex-target');
        targets.forEach(el => {
            renderMathInElement(el, {
                delimiters: [
                    {left: '$$', right: '$$', display: true},
                    {left: '$', right: '$', display: false},
                    {left: '\\(', right: '\\)', display: false},
                    {left: '\\[', right: '\\]', display: true}
                ],
                throwOnError: false
            });
        });
    } else {
        setTimeout(renderAllLatex, 100);
    }
}

// Canvas Highlight Category Filter State
let currentFilterMode = 'all';
let activeCategories = new Set(['binary', 'boolean', 'fsm', 'vhdl', 'param']);

function setFilterMode(mode) {
    currentFilterMode = mode;
    const canvas = document.getElementById('interactive-text-canvas');
    const buttons = document.querySelectorAll('.filter-chip-btn[data-filter]');

    buttons.forEach(btn => {
        if (btn.getAttribute('data-filter') === mode) {
            btn.classList.add('active');
        } else {
            btn.classList.remove('active');
        }
    });

    if (!canvas) return;

    if (mode === 'clean') {
        canvas.classList.add('clean-text-mode');
        document.querySelectorAll('.filter-chip-btn[data-category]').forEach(btn => {
            btn.classList.remove('active');
        });
    } else {
        canvas.classList.remove('clean-text-mode');
        activeCategories = new Set(['binary', 'boolean', 'fsm', 'vhdl', 'param']);
        document.querySelectorAll('.filter-chip-btn[data-category]').forEach(btn => {
            btn.classList.add('active');
        });
    }
    updateCanvasHighlights();
}

function toggleCategory(cat) {
    const canvas = document.getElementById('interactive-text-canvas');
    if (canvas) canvas.classList.remove('clean-text-mode');

    document.querySelectorAll('.filter-chip-btn[data-filter]').forEach(btn => {
        btn.classList.remove('active');
    });

    const btn = document.querySelector(`.filter-chip-btn[data-category="${cat}"]`);
    if (activeCategories.has(cat)) {
        activeCategories.delete(cat);
        if (btn) btn.classList.remove('active');
    } else {
        activeCategories.add(cat);
        if (btn) btn.classList.add('active');
    }
    updateCanvasHighlights();
}

function updateCanvasHighlights() {
    const canvas = document.getElementById('interactive-text-canvas');
    if (!canvas) return;

    if (canvas.classList.contains('clean-text-mode')) {
        return;
    }

    const badges = canvas.querySelectorAll('.highlight-badge');
    badges.forEach(badge => {
        const cat = badge.getAttribute('data-category');
        if (activeCategories.has(cat)) {
            badge.style.display = 'inline-flex';
        } else {
            badge.style.display = 'inline';
            badge.style.background = 'transparent';
            badge.style.border = 'none';
            badge.style.padding = '0';
            const tag = badge.querySelector('.tag-label');
            if (tag) tag.style.display = 'none';
        }
    });
}

// Diagram Zoom, Pan and Details Helpers
let deZoomScale = 1.0;
let dePanX = 0;
let dePanY = 0;
let isDeDragging = false;
let deStartX = 0;
let deStartY = 0;

function zoomDeDiagram(factor) {
    deZoomScale *= factor;
    deZoomScale = Math.min(Math.max(0.4, deZoomScale), 3.0);
    applyDeTransform();
}

function resetDeDiagramZoom() {
    deZoomScale = 1.0;
    dePanX = 0;
    dePanY = 0;
    applyDeTransform();
}

function applyDeTransform() {
    const layer = document.getElementById('de-diagram-layer');
    if (layer) {
        layer.style.transform = `translate(${dePanX}px, ${dePanY}px) scale(${deZoomScale})`;
    }
}

function toggleDeDiagramDetails() {
    const details = document.querySelectorAll('.de-diagram-detail');
    const btn = document.getElementById('toggle-de-details-btn');
    details.forEach(el => {
        el.style.display = (el.style.display === 'none') ? '' : 'none';
    });
    if (btn) btn.classList.toggle('active');
}

function startDeDrag(e) {
    isDeDragging = true;
    deStartX = e.clientX - dePanX;
    deStartY = e.clientY - dePanY;
    const viewport = document.getElementById('de-diagram-viewport');
    if (viewport) viewport.style.cursor = 'grabbing';
    window.addEventListener('mousemove', handleDeDrag);
    window.addEventListener('mouseup', stopDeDrag);
}

function handleDeDrag(e) {
    if (!isDeDragging) return;
    dePanX = e.clientX - deStartX;
    dePanY = e.clientY - deStartY;
    applyDeTransform();
}

function stopDeDrag() {
    isDeDragging = false;
    const viewport = document.getElementById('de-diagram-viewport');
    if (viewport) viewport.style.cursor = 'grab';
    window.removeEventListener('mousemove', handleDeDrag);
    window.removeEventListener('mouseup', stopDeDrag);
}

function handleDeWheel(e) {
    e.preventDefault();
    const factor = e.deltaY < 0 ? 1.1 : 0.9;
    zoomDeDiagram(factor);
}

// Print and Export Helpers
function printSection(sectionId) {
    if (!sectionId || sectionId === 'all') {
        window.print();
        return;
    }
    const elem = document.getElementById(sectionId);
    if (!elem) {
        window.print();
        return;
    }
    window.print();
}

function downloadStandaloneHTML() {
    const htmlContent = document.documentElement.outerHTML;
    const blob = new Blob([htmlContent], {type: 'text/html;charset=utf-8'});
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'digital_electronics_study_guide.html';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
}

// Initialize on Load
document.addEventListener('DOMContentLoaded', () => {
    const savedTheme = localStorage.getItem('de_theme') || 'light';
    if (savedTheme === 'dark') {
        document.body.classList.add('theme-dark', 'body--dark');
        document.documentElement.setAttribute('data-theme', 'dark');
        if (window.Quasar && window.Quasar.dark) {
            window.Quasar.dark.set(true);
        }
    } else {
        document.body.classList.add('theme-light');
        document.documentElement.setAttribute('data-theme', 'light');
        if (window.Quasar && window.Quasar.dark) {
            window.Quasar.dark.set(false);
        }
    }
    renderAllLatex();
});
</script>
"""

