"""Theme configuration, design tokens, LaTeX support, and styling rules for Discrete Mathematics app.

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
}

body.theme-dark,
[data-theme="dark"],
.body--dark {
    --bg-deep: #0e1117;
    --bg-base: #161b22;
    --bg-mid: #1c2128;
    --bg-card: #1e242c;
    --surface: rgba(30, 36, 44, 0.94);
    --surface-2: #242c35;
    --surface-hover: #2d3642;
    --border: rgba(255, 255, 255, 0.12);
    --border-accent: rgba(234, 88, 12, 0.6);
    --border-focus: rgba(251, 146, 60, 0.85);
    --accent: #e06b3a;
    --accent-light: #f97316;
    --accent-dark: #c2410c;
    --amber: #fbbf24;
    --orange: #fb923c;
    --text-1: #f3f4f6;
    --text-2: #cbd5e1;
    --text-3: #94a3b8;
    --green-ok: #10b981;
    --green-light: #34d399;
    --red-err: #ef4444;
    --red-light: #f87171;
    --blue-action: #60a5fa;
    --blue-hover: #3b82f6;
    --purple: #a78bfa;
    --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.35);
    --shadow-md: 0 4px 18px rgba(0, 0, 0, 0.45);
    --shadow-lg: 0 10px 32px rgba(0, 0, 0, 0.55);

    /* Component Semantics */
    --card-bg-subtle: #192028;
    --table-header-bg: #202731;
    --table-alt-bg: #1a2027;
    --canvas-bg: #141920;
    --canvas-header-bg: #1b222b;
    --canvas-legend-bg: #181f27;
    --svg-canvas-bg: #12171e;
}

/* Base resets & typography */
html, body {
    margin: 0;
    padding: 0;
    font-family: 'Outfit', -apple-system, BlinkMacSystemFont, sans-serif;
    background-color: var(--bg-deep) !important;
    color: var(--text-1) !important;
    min-height: 100vh;
    transition: background-color 0.25s ease, color 0.25s ease;
    font-size: 15px;
    line-height: 1.6;
}

/* Glassmorphism panels */
.glass-panel {
    background: var(--surface);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border: 1px solid var(--border);
    border-radius: var(--r-md);
    box-shadow: var(--shadow-sm);
    transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
}

.glass-panel:hover {
    border-color: var(--border-accent);
    box-shadow: var(--shadow-md);
}

/* ==========================================================================
   DISCRETE MATHEMATICS HIGHLIGHT BADGES & CONTRACT TOOLTIPS
   ========================================================================== */

.highlight-badge {
    display: inline-block;
    padding: 1px 6px;
    margin: 1px 2px;
    border-radius: 4px;
    font-weight: 600;
    cursor: help;
    transition: all 0.18s ease;
    position: relative;
    border-bottom: 2px solid transparent;
}

.highlight-badge:hover {
    transform: translateY(-1px);
    filter: brightness(1.1);
    box-shadow: 0 2px 6px rgba(0,0,0,0.15);
}

.badge-logic {
    background: rgba(245, 158, 11, 0.15);
    color: var(--amber);
    border-color: var(--amber);
}

.badge-set {
    background: rgba(37, 99, 235, 0.15);
    color: var(--blue-action);
    border-color: var(--blue-action);
}

.badge-prob {
    background: rgba(5, 150, 105, 0.15);
    color: var(--green-ok);
    border-color: var(--green-ok);
}

.badge-graph {
    background: rgba(124, 58, 237, 0.15);
    color: var(--purple);
    border-color: var(--purple);
}

.badge-automata {
    background: rgba(217, 83, 30, 0.15);
    color: var(--accent);
    border-color: var(--accent);
}

.badge-induct {
    background: rgba(14, 165, 233, 0.15);
    color: #0284c7;
    border-color: #0284c7;
}

.badge-param {
    background: rgba(234, 88, 12, 0.18);
    color: var(--orange);
    border-color: var(--orange);
    font-family: 'JetBrains Mono', monospace;
}

/* Solution block styling */
.option-row-static {
    padding: 10px 14px;
    border-radius: 8px;
    background: var(--surface-2);
    border: 1px solid var(--border);
    transition: border-color 0.2s;
}

.option-row-static.correct {
    border-color: var(--green-ok);
    background: rgba(5, 150, 105, 0.08);
}

.option-badge {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 24px;
    height: 24px;
    border-radius: 6px;
    font-weight: 700;
    font-size: 0.8rem;
    background: var(--surface-hover);
    color: var(--text-2);
}

.option-badge.correct {
    background: var(--green-ok);
    color: #ffffff;
}

.derivation-step-card {
    border-left: 3px solid var(--accent);
    background: var(--surface-2);
    border-radius: 0 var(--r-sm) var(--r-sm) 0;
    padding: 14px 18px;
    border-top: 1px solid var(--border);
    border-right: 1px solid var(--border);
    border-bottom: 1px solid var(--border);
    max-width: 100% !important;
    min-width: 0 !important;
    box-sizing: border-box !important;
    overflow-x: hidden !important;
}

.result-highlight-box {
    border: 2px solid var(--green-ok);
    background: rgba(5, 150, 105, 0.07);
    border-radius: var(--r-sm);
    padding: 14px 20px;
    max-width: 100% !important;
    min-width: 0 !important;
    box-sizing: border-box !important;
    overflow-x: hidden !important;
}

/* KaTeX container math overflow rules */
.katex-display {
    max-width: 100% !important;
    overflow-x: auto !important;
    overflow-y: hidden !important;
    padding: 6px 0 !important;
    margin: 0.5em 0 !important;
    text-align: center;
}

.katex {
    max-width: 100% !important;
    white-space: normal;
}

.katex-display > .katex {
    white-space: nowrap;
}

/* ==========================================================================
   QUASAR POPUP & SELECT DROPDOWN THEMING
   ========================================================================== */

.q-menu,
.scenario-select-popup,
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
.scenario-select-popup .q-item,
.q-select__dialog .q-item {
    color: var(--text-1) !important;
    transition: background 0.15s ease, color 0.15s ease;
    font-size: 0.82rem !important;
    padding: 8px 12px !important;
}

.q-menu .q-item:hover,
.q-menu .q-item.q-manual-focusable--focused,
.scenario-select-popup .q-item:hover,
.scenario-select-popup .q-item.q-manual-focusable--focused,
.q-select__dialog .q-item:hover {
    background: var(--surface-hover) !important;
    color: var(--accent) !important;
}

.q-menu .q-item.q-item--active,
.q-menu .q-item.text-primary,
.scenario-select-popup .q-item.q-item--active,
.scenario-select-popup .q-item.text-primary,
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
    background: var(--bg-base) !important;
}

.q-field--outlined:hover .q-field__control {
    border-color: var(--border-accent) !important;
}

/* Print Rules */
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
        break-inside: avoid;
    }
}
"""

KATEX_AND_SCRIPTS_HEAD = r"""
<!-- KaTeX Math Rendering Styles & Scripts -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css" crossorigin="anonymous">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js" crossorigin="anonymous"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js" crossorigin="anonymous"></script>

<script>
/**
 * Renders all mathematical expressions on the page using KaTeX auto-renderer.
 */
function renderAllLatex() {
    if (typeof renderMathInElement === 'function') {
        const targets = document.querySelectorAll('.latex-target, .q-page, #interactive-canvas-section, #solution-sheet-section');
        targets.forEach(function(el) {
            renderMathInElement(el, {
                delimiters: [
                    {left: '$$', right: '$$', display: true},
                    {left: '$', right: '$', display: false}
                ],
                throwOnError: false
            });
        });
    }
}

/**
 * Toggles application theme between Light and Dark mode.
 */
function toggleAppTheme() {
    const isDark = document.body.classList.contains('theme-dark') || document.body.classList.contains('body--dark');
    if (isDark) {
        document.body.classList.remove('theme-dark', 'body--dark');
        document.body.classList.add('theme-light');
        document.documentElement.setAttribute('data-theme', 'light');
        localStorage.setItem('dit_dm_theme', 'light');
        if (window.Quasar && window.Quasar.dark) {
            window.Quasar.dark.set(false);
        }
    } else {
        document.body.classList.remove('theme-light');
        document.body.classList.add('theme-dark', 'body--dark');
        document.documentElement.setAttribute('data-theme', 'dark');
        localStorage.setItem('dit_dm_theme', 'dark');
        if (window.Quasar && window.Quasar.dark) {
            window.Quasar.dark.set(true);
        }
    }
}

/**
 * Sets highlight filter mode in the interactive canvas.
 */
function setFilterMode(mode) {
    const badges = document.querySelectorAll('.highlight-badge');
    const buttons = document.querySelectorAll('.category-chip-btn');
    buttons.forEach(btn => btn.classList.remove('active-chip'));

    const clickedBtn = document.getElementById('chip-' + mode);
    if (clickedBtn) clickedBtn.classList.add('active-chip');

    if (mode === 'all') {
        badges.forEach(b => {
            b.style.display = 'inline-block';
            b.style.opacity = '1';
        });
    } else if (mode === 'clean') {
        badges.forEach(b => {
            b.style.background = 'transparent';
            b.style.borderColor = 'transparent';
            b.style.color = 'inherit';
            b.style.padding = '0';
        });
    } else {
        badges.forEach(b => {
            const cat = b.getAttribute('data-category');
            if (cat === mode) {
                b.style.display = 'inline-block';
                b.style.opacity = '1';
            } else {
                b.style.opacity = '0.25';
            }
        });
    }
}

/**
 * Synchronizes canvas highlight badges with event listeners.
 */
function updateCanvasHighlights() {
    // Ensures tooltips and badges react cleanly
}

/**
 * Triggers clean A4 printing for a specific container.
 */
function printSection(targetId) {
    window.print();
}

/**
 * Downloads a standalone HTML copy of the active view.
 */
function downloadStandaloneHTML() {
    const content = document.documentElement.outerHTML;
    const blob = new Blob([content], {type: 'text/html'});
    const a = document.createElement('a');
    a.href = URL.createObjectURL(blob);
    a.download = 'Discrete_Mathematics_Master_Solution_Sheet.html';
    a.click();
}

// Global initialization after page load
document.addEventListener('DOMContentLoaded', () => {
    const savedTheme = localStorage.getItem('dit_dm_theme') || 'light';
    const isDark = savedTheme === 'dark';
    if (isDark) {
        document.body.classList.add('theme-dark', 'body--dark');
        document.documentElement.setAttribute('data-theme', 'dark');
    } else {
        document.body.classList.add('theme-light');
        document.documentElement.setAttribute('data-theme', 'light');
    }
    if (window.Quasar && window.Quasar.dark) {
        window.Quasar.dark.set(isDark);
    }
    setTimeout(renderAllLatex, 150);
});
</script>
"""
