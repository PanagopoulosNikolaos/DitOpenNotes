"""Theme configuration, LaTeX support, and styling rules for Computer Networks application.

Provides design tokens, color constants, custom CSS, and KaTeX mathematical
rendering support adhering to the Orange and Dark Soft design specification.
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

KATEX_HEAD_HTML = """
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"></script>
<script>
function renderAllLatex() {
    if (typeof renderMathInElement !== 'function') return;
    
    // Target scoped containers only to prevent corrupting Vue 3 virtual DOM reconciliation
    const targets = document.querySelectorAll('.latex-target, .formula-box, #interactive-text-canvas, .analysis-content, .step-content');
    if (targets && targets.length > 0) {
        targets.forEach(el => {
            try {
                renderMathInElement(el, {
                    delimiters: [
                        {left: '$$$', right: '$$$', display: false},
                        {left: '$$', right: '$$', display: true},
                        {left: '$', right: '$', display: false},
                        {left: '\\\\[', right: '\\\\]', display: true},
                        {left: '\\\\(', right: '\\\\)', display: false}
                    ],
                    throwOnError: false
                });
            } catch (err) {
                console.warn('KaTeX render error:', err);
            }
        });
    } else {
        const root = document.getElementById('main-content-area');
        if (root) {
            try {
                renderMathInElement(root, {
                    delimiters: [
                        {left: '$$$', right: '$$$', display: false},
                        {left: '$$', right: '$$', display: true},
                        {left: '$', right: '$', display: false},
                        {left: '\\\\[', right: '\\\\]', display: true},
                        {left: '\\\\(', right: '\\\\)', display: false}
                    ],
                    throwOnError: false
                });
            } catch (err) {}
        }
    }
}

document.addEventListener('DOMContentLoaded', () => {
    setTimeout(renderAllLatex, 150);
});

// Interactive canvas highlight filter controller (loaded once at startup)
window.activeCategories = {
    delay: true, device: true, protocol: true, routing: true, error_check: true
};

function updateCanvasHighlights() {
    const badges = document.querySelectorAll('#interactive-text-canvas .highlight-badge');
    badges.forEach(badge => {
        const cat = badge.getAttribute('data-category');
        const badgeCls = badge.getAttribute('data-badge-class') || 'hl-' + cat;
        if (window.activeCategories[cat]) {
            badge.classList.add('highlight-active', badgeCls);
            badge.style.opacity = '1';
            badge.style.border = '';
        } else {
            badge.classList.remove('highlight-active', badgeCls);
            badge.style.opacity = '0.4';
            badge.style.border = '1px dashed rgba(255,255,255,0.15)';
        }
    });
}

function toggleCategory(cat) {
    window.activeCategories[cat] = !window.activeCategories[cat];
    const btn = document.querySelector(`button[data-category="${cat}"]`);
    if (btn) {
        window.activeCategories[cat] ? btn.classList.add('active') : btn.classList.remove('active');
    }
    updateCanvasHighlights();
}

function setFilterMode(mode) {
    const isAll = (mode === 'all');
    for (let cat in window.activeCategories) {
        window.activeCategories[cat] = isAll;
        const btn = document.querySelector(`button[data-category="${cat}"]`);
        if (btn) { isAll ? btn.classList.add('active') : btn.classList.remove('active'); }
    }
    const allBtn  = document.querySelector('button[data-filter="all"]');
    const noneBtn = document.querySelector('button[data-filter="none"]');
    if (allBtn && noneBtn) {
        if (isAll) { allBtn.classList.add('active');  noneBtn.classList.remove('active'); }
        else       { allBtn.classList.remove('active'); noneBtn.classList.add('active'); }
    }
    updateCanvasHighlights();
}
</script>
"""

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

/* Quasar Component Enhancements & Hitbox Normalization */
.q-btn {
    text-transform: none !important;
    font-family: 'Outfit', sans-serif !important;
    cursor: pointer !important;
}

.q-btn .q-btn__wrapper {
    padding: 0.35rem 0.85rem !important;
    min-height: unset !important;
    width: 100% !important;
}

.q-btn .q-btn__content {
    width: 100% !important;
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;
    gap: 0.45rem !important;
}

.q-btn .q-icon {
    font-size: 1.15em !important;
}

.q-field--dark .q-field__control {
    background: #201f1d !important;
    border-radius: var(--r-sm) !important;
}

.q-menu {
    background: #1c1b1a !important;
    border: 1px solid rgba(224, 107, 58, 0.35) !important;
    box-shadow: 0 12px 40px rgba(0, 0, 0, 0.75) !important;
    border-radius: var(--r-md) !important;
}

.q-item--dark.q-item--active, .q-item--dark:hover {
    background: rgba(224, 107, 58, 0.2) !important;
    color: #fed7aa !important;
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

.glass-panel-subtle {
    background: var(--surface);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border: 1px solid var(--border);
    border-radius: var(--r-lg);
    padding: 1.25rem;
    transition: all 0.2s ease;
}

.glass-panel-subtle:hover {
    background: var(--surface-2);
    border-color: rgba(224, 107, 58, 0.25);
}

/* Header Styles */
.app-header {
    position: sticky;
    top: 0;
    z-index: 50;
    backdrop-filter: blur(20px) saturate(1.5);
    -webkit-backdrop-filter: blur(20px) saturate(1.5);
    background: rgba(20, 20, 19, 0.92);
    border-bottom: 1px solid var(--border-accent);
    box-shadow: 0 4px 24px rgba(0, 0, 0, 0.4);
}

/* Typography Enhancements */
.font-mono {
    font-family: 'JetBrains Mono', monospace !important;
}

.text-glow {
    text-shadow: 0 0 20px rgba(224, 107, 58, 0.4);
}

.gradient-title {
    background: linear-gradient(135deg, #f4f1ea 0%, #e06b3a 60%, #f59e0b 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

/* KaTeX Custom Math Styling */
.katex {
    font-size: 1.05em !important;
    color: #fed7aa !important;
}

.katex-display {
    margin: 0.75rem 0 !important;
    padding: 0.5rem 1rem !important;
    background: rgba(0, 0, 0, 0.3) !important;
    border-radius: 8px !important;
    border-left: 3px solid var(--accent) !important;
    overflow-x: auto !important;
}

/* Interactive Text Highlighter & Badges */
.highlight-badge {
    display: inline-flex;
    align-items: center;
    gap: 0.35rem;
    padding: 0.2rem 0.6rem;
    margin: 0 0.2rem;
    border-radius: var(--r-sm);
    font-weight: 600;
    font-size: 0.88rem;
    cursor: pointer;
    transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
    position: relative;
    border: 1px solid transparent;
}

.highlight-badge:hover {
    transform: translateY(-2px);
    box-shadow: var(--shadow-sm);
}

/* Highlight Categories */
.hl-delay {
    background: rgba(224, 107, 58, 0.18);
    color: #f97316;
    border-color: rgba(224, 107, 58, 0.45);
}
.hl-delay:hover {
    background: rgba(224, 107, 58, 0.28);
    box-shadow: 0 0 16px rgba(224, 107, 58, 0.35);
}

.hl-device {
    background: rgba(245, 158, 11, 0.18);
    color: #fbbf24;
    border-color: rgba(245, 158, 11, 0.45);
}
.hl-device:hover {
    background: rgba(245, 158, 11, 0.28);
    box-shadow: 0 0 16px rgba(245, 158, 11, 0.35);
}

.hl-protocol {
    background: rgba(79, 142, 201, 0.18);
    color: #60a5fa;
    border-color: rgba(79, 142, 201, 0.45);
}
.hl-protocol:hover {
    background: rgba(79, 142, 201, 0.28);
    box-shadow: 0 0 16px rgba(79, 142, 201, 0.35);
}

.hl-routing {
    background: rgba(16, 185, 129, 0.18);
    color: #34d399;
    border-color: rgba(16, 185, 129, 0.45);
}
.hl-routing:hover {
    background: rgba(16, 185, 129, 0.28);
    box-shadow: 0 0 16px rgba(16, 185, 129, 0.35);
}

.hl-error_check {
    background: rgba(239, 68, 68, 0.18);
    color: #f87171;
    border-color: rgba(239, 68, 68, 0.45);
}
.hl-error_check:hover {
    background: rgba(239, 68, 68, 0.28);
    box-shadow: 0 0 16px rgba(239, 68, 68, 0.35);
}

/* Custom Tag Pill inside Badge */
.tag-pill {
    font-size: 0.65rem;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    padding: 0.1rem 0.35rem;
    border-radius: 4px;
    background: rgba(0, 0, 0, 0.35);
    font-family: 'JetBrains Mono', monospace;
}

/* Filter Chip Buttons */
.filter-chip {
    padding: 0.45rem 0.95rem;
    border-radius: var(--r-pill);
    font-size: 0.85rem;
    font-weight: 500;
    cursor: pointer;
    background: var(--surface);
    border: 1px solid var(--border);
    color: var(--text-2);
    transition: all 0.2s ease;
    display: inline-flex;
    align-items: center;
    gap: 0.45rem;
}

.filter-chip:hover {
    background: var(--surface-2);
    color: var(--text-1);
    border-color: var(--border-accent);
}

.filter-chip.active {
    background: linear-gradient(135deg, rgba(224, 107, 58, 0.25), rgba(217, 119, 6, 0.25));
    border-color: var(--accent);
    color: var(--text-1);
    box-shadow: 0 0 14px rgba(224, 107, 58, 0.25);
}

/* Question and Option Cards */
.option-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--r-md);
    padding: 1rem 1.25rem;
    transition: all 0.2s ease;
    cursor: pointer;
    width: 100%;
}

.option-card:hover {
    background: var(--surface-2);
    border-color: rgba(224, 107, 58, 0.4);
    transform: translateY(-1px);
}

.option-card.correct {
    background: rgba(16, 185, 129, 0.15) !important;
    border-color: var(--green-ok) !important;
}

.option-card.incorrect {
    background: rgba(239, 68, 68, 0.15) !important;
    border-color: var(--red-err) !important;
}

/* Calculation Steps Timeline */
.step-node {
    position: relative;
    padding-left: 2.2rem;
    padding-bottom: 1.5rem;
}

.step-node::before {
    content: '';
    position: absolute;
    left: 0.75rem;
    top: 1.75rem;
    bottom: 0;
    width: 2px;
    background: rgba(255, 255, 255, 0.08);
}

.step-node:last-child::before {
    display: none;
}

.step-bullet {
    position: absolute;
    left: 0;
    top: 0.15rem;
    width: 1.6rem;
    height: 1.6rem;
    border-radius: 50%;
    background: var(--accent);
    color: #fff;
    font-weight: 700;
    font-size: 0.75rem;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 0 12px rgba(224, 107, 58, 0.4);
}

/* Formula Highlight Box */
.formula-box {
    background: rgba(0, 0, 0, 0.35);
    border-left: 3px solid var(--accent);
    padding: 0.85rem 1.15rem;
    border-radius: 0 var(--r-sm) var(--r-sm) 0;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.92rem;
    color: #fed7aa;
}

/* Custom Scrollbars */
::-webkit-scrollbar {
    width: 8px;
    height: 8px;
}

::-webkit-scrollbar-track {
    background: var(--bg-deep);
}

::-webkit-scrollbar-thumb {
    background: rgba(255, 255, 255, 0.15);
    border-radius: 4px;
}

::-webkit-scrollbar-thumb:hover {
    background: rgba(224, 107, 58, 0.4);
}
"""
