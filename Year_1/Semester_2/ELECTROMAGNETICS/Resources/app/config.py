"""Theme configuration, design tokens, LaTeX support, and styling rules for Electromagnetics app.

Provides design tokens for Orange Light (default) and Soft Dark themes, KaTeX math
support, print-to-PDF styles, canvas highlight classes, and global JavaScript helpers.
"""

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
    --hl-field-bg: rgba(37, 99, 235, 0.12);
    --hl-field-color: #1d4ed8;
    --hl-field-border: #93c5fd;

    --hl-param-bg: rgba(217, 83, 30, 0.12);
    --hl-param-color: #c2410c;
    --hl-param-border: #fdba74;

    --hl-calc-bg: rgba(124, 58, 237, 0.12);
    --hl-calc-color: #6d28d9;
    --hl-calc-border: #c4b5fd;

    --hl-law-bg: rgba(5, 150, 105, 0.12);
    --hl-law-color: #047857;
    --hl-law-border: #6ee7b7;

    --hl-geom-bg: rgba(217, 119, 6, 0.12);
    --hl-geom-color: #b45309;
    --hl-geom-border: #fcd34d;
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
    --purple: #a78bfa;
    --shadow-sm: 0 4px 16px rgba(0, 0, 0, 0.40);
    --shadow-md: 0 6px 28px rgba(0, 0, 0, 0.50);
    --shadow-lg: 0 10px 48px rgba(0, 0, 0, 0.60);

    /* Component Semantics */
    --card-bg-subtle: #201f1d;
    --table-header-bg: rgba(255, 255, 255, 0.05);
    --table-alt-bg: rgba(255, 255, 255, 0.03);
    --canvas-bg: #1a1918;
    --canvas-header-bg: #121211;
    --canvas-legend-bg: #171615;
    --svg-canvas-bg: #121211;
    --svg-grid-dot: rgba(255, 255, 255, 0.08);
    --svg-stroke: #94a3b8;
    --svg-fill: #1e293b;
    --code-bg: #10100f;
    --code-text: #f4f1ea;
    --code-border: rgba(255, 255, 255, 0.08);
    --header-bg: rgba(20, 20, 19, 0.90);
    --menu-bg: #1c1b1a;
    --menu-border: rgba(224, 107, 58, 0.3);
    --input-bg: #201f1d;
    --badge-bg: #201f1d;

    /* Dark Theme Highlight Badges */
    --hl-field-bg: rgba(59, 130, 246, 0.20);
    --hl-field-color: #93c5fd;
    --hl-field-border: rgba(59, 130, 246, 0.45);

    --hl-param-bg: rgba(224, 107, 58, 0.24);
    --hl-param-color: #fdba74;
    --hl-param-border: var(--accent);

    --hl-calc-bg: rgba(168, 85, 247, 0.22);
    --hl-calc-color: #d8b4fe;
    --hl-calc-border: rgba(168, 85, 247, 0.50);

    --hl-law-bg: rgba(16, 185, 129, 0.20);
    --hl-law-color: #86efac;
    --hl-law-border: rgba(16, 185, 129, 0.45);

    --hl-geom-bg: rgba(245, 158, 11, 0.20);
    --hl-geom-color: #fde68a;
    --hl-geom-border: rgba(245, 158, 11, 0.50);
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

/* Background Gradients */
body.theme-light::before,
[data-theme="light"] body::before,
body:not(.theme-dark)::before {
    content: '';
    position: fixed;
    inset: 0;
    background:
        radial-gradient(ellipse 75% 55% at 15% 5%, rgba(217, 83, 30, 0.05) 0%, transparent 65%),
        radial-gradient(ellipse 55% 45% at 85% 95%, rgba(180, 83, 9, 0.04) 0%, transparent 60%),
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

/* Quasar Normalization */
.q-btn {
    text-transform: none !important;
    font-family: 'Outfit', sans-serif !important;
    cursor: pointer !important;
}

.q-field--dark .q-field__control {
    background: var(--input-bg) !important;
    border-radius: var(--r-sm) !important;
}

.q-menu {
    background: var(--menu-bg) !important;
    border: 1px solid var(--menu-border) !important;
    box-shadow: var(--shadow-lg) !important;
    border-radius: var(--r-md) !important;
    color: var(--text-1) !important;
}

.q-item--dark.q-item--active, .q-item--dark:hover,
.q-item:hover {
    background: rgba(217, 83, 30, 0.15) !important;
    color: var(--accent) !important;
}

/* Glass Panels */
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
    box-shadow: var(--shadow-lg), 0 0 24px rgba(217, 83, 30, 0.08);
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
    border-color: var(--border-accent);
}

/* Headers */
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
    font-size: 1.35rem;
    font-weight: 800;
    letter-spacing: -0.02em;
    color: var(--text-1);
    display: flex;
    align-items: center;
    gap: 0.75rem;
}

/* Highlight Badges & Hover Tooltips */
.highlight-badge {
    display: inline-block;
    padding: 1px 6px;
    border-radius: var(--r-xs);
    font-weight: 600;
    cursor: help;
    transition: all 0.2s ease;
    text-decoration: none;
    line-height: 1.35;
    margin: 1px 2px;
}

.highlight-badge:hover {
    transform: translateY(-1px);
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
    filter: brightness(1.1);
}

.badge-field {
    background-color: var(--hl-field-bg);
    color: var(--hl-field-color);
    border: 1px solid var(--hl-field-border);
}

.badge-param {
    background-color: var(--hl-param-bg);
    color: var(--hl-param-color);
    border: 1px solid var(--hl-param-border);
}

.badge-calc {
    background-color: var(--hl-calc-bg);
    color: var(--hl-calc-color);
    border: 1px solid var(--hl-calc-border);
}

.badge-law {
    background-color: var(--hl-law-bg);
    color: var(--hl-law-color);
    border: 1px solid var(--hl-law-border);
}

.badge-geom {
    background-color: var(--hl-geom-bg);
    color: var(--hl-geom-color);
    border: 1px solid var(--hl-geom-border);
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
    background-color: rgba(0, 0, 0, 0.12);
    color: var(--text-1);
}

/* Filter Chips */
.filter-chip-btn {
    background: var(--surface);
    border: 1px solid var(--border);
    color: var(--text-2);
    padding: 0.35rem 0.85rem;
    border-radius: var(--r-pill);
    font-size: 0.82rem;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.2s ease;
    display: inline-flex;
    align-items: center;
    gap: 0.45rem;
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
    box-shadow: 0 2px 10px rgba(217, 83, 30, 0.30);
}

/* Static Multiple Choice Question Rows */
.option-row-static {
    display: flex;
    align-items: flex-start;
    gap: 0.85rem;
    padding: 0.75rem 1rem;
    border-radius: var(--r-md);
    border: 1px solid var(--border);
    background: var(--surface);
    margin-bottom: 0.5rem;
    transition: all 0.2s ease;
}

.option-row-static.correct {
    border-color: var(--green-ok) !important;
    background: rgba(5, 150, 105, 0.06) !important;
}

.option-badge {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 26px;
    height: 26px;
    border-radius: var(--r-pill);
    font-weight: 700;
    font-size: 0.85rem;
    background: var(--surface-2);
    color: var(--text-2);
    flex-shrink: 0;
}

.option-badge.correct {
    background: var(--green-ok) !important;
    color: #ffffff !important;
}

/* KaTeX Derivation Cards */
.derivation-step-card {
    background: var(--card-bg-subtle);
    border: 1px solid var(--border);
    border-left: 3px solid var(--accent);
    border-radius: var(--r-md);
    padding: 1rem 1.25rem;
    margin-bottom: 0.75rem;
}

.formula-highlight-box {
    background: rgba(217, 83, 30, 0.06);
    border: 1px solid var(--border-accent);
    border-radius: var(--r-md);
    padding: 0.85rem 1.25rem;
    margin: 0.75rem 0;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.15rem;
}

.result-highlight-box {
    background: rgba(5, 150, 105, 0.08);
    border: 1px solid var(--green-ok);
    border-radius: var(--r-md);
    padding: 0.85rem 1.25rem;
    margin-top: 0.75rem;
    font-weight: 700;
}

/* Tables */
.dark-table {
    width: 100%;
    border-collapse: collapse;
    margin: 1rem 0;
    border-radius: var(--r-md);
    overflow: hidden;
    border: 1px solid var(--border);
}

.dark-table th {
    background: var(--table-header-bg);
    color: var(--text-1);
    font-weight: 700;
    text-align: left;
    padding: 0.75rem 1rem;
    font-size: 0.85rem;
    border-bottom: 1px solid var(--border);
}

.dark-table td {
    padding: 0.75rem 1rem;
    border-bottom: 1px solid var(--border);
    font-size: 0.85rem;
    color: var(--text-2);
}

.dark-table tr:last-child td {
    border-bottom: none;
}

.dark-table tr:nth-child(even) td {
    background: var(--table-alt-bg);
}

/* Code container */
.code-wrapper {
    background: var(--code-bg);
    border: 1px solid var(--code-border);
    border-radius: var(--r-md);
    position: relative;
}

/* Print Rules */
@media print {
    body {
        background: #ffffff !important;
        color: #000000 !important;
    }
    .app-header, .no-print, .filter-chips-bar, .print-btn-menu {
        display: none !important;
    }
    .glass-panel, .glass-panel-subtle {
        box-shadow: none !important;
        border: 1px solid #d1d5db !important;
        page-break-inside: avoid !important;
    }
}
"""

KATEX_AND_SCRIPTS_HEAD = r"""
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"></script>

<script>
/* KaTeX Auto-Render Helper */
function renderAllLatex() {
    if (typeof renderMathInElement !== 'function') {
        setTimeout(renderAllLatex, 100);
        return;
    }
    
    const selectors = [
        '.latex-target',
        '#interactive-text-canvas',
        '.analysis-section',
        '.derivation-step-card',
        '.formula-highlight-box',
        '.result-highlight-box',
        '.theory-container',
        '.nicegui-markdown',
        '.q-card'
    ];
    
    const targets = document.querySelectorAll(selectors.join(', '));
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
                    ignoredTags: ["script", "noscript", "style", "textarea", "pre", "code", "option"],
                    throwOnError: false
                });
            } catch (err) {
                console.warn('KaTeX render error:', err);
            }
        });
    } else {
        const root = document.getElementById('main-content-area') || document.body;
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
                    ignoredTags: ["script", "noscript", "style", "textarea", "pre", "code", "option"],
                    throwOnError: false
                });
            } catch (err) {}
        }
    }
}

/* Theme switching controller */
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
        try { window.Quasar.Dark.set(isDark); } catch (e) {}
    }
    localStorage.setItem('app_theme', isDark ? 'dark' : 'light');

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
}

function toggleAppTheme() {
    const current = getAppTheme();
    const next = current === 'dark' ? 'light' : 'dark';
    setAppTheme(next);
}

/* Canvas Highlight Filtering */
window.activeCategories = {
    field: true, param: true, calc: true, law: true, geom: true
};

function updateCanvasHighlights() {
    const badges = document.querySelectorAll('#interactive-text-canvas .highlight-badge');
    badges.forEach(badge => {
        const cat = badge.getAttribute('data-category');
        if (window.activeCategories[cat]) {
            badge.style.opacity = '1';
            badge.style.filter = 'none';
        } else {
            badge.style.opacity = '0.35';
            badge.style.filter = 'grayscale(80%)';
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
        if (btn) {
            isAll ? btn.classList.add('active') : btn.classList.remove('active');
        }
    }
    const allBtn = document.querySelector('button[data-filter="all"]');
    const cleanBtn = document.querySelector('button[data-filter="clean"]');
    if (allBtn && cleanBtn) {
        if (isAll) {
            allBtn.classList.add('active');
            cleanBtn.classList.remove('active');
        } else {
            allBtn.classList.remove('active');
            cleanBtn.classList.add('active');
        }
    }
    updateCanvasHighlights();
}

/* Printing & Standalone HTML Helpers */
function printSection(target) {
    if (target === 'all') {
        window.print();
        return;
    }
    const elem = document.getElementById(target);
    if (!elem) {
        window.print();
        return;
    }
    document.body.setAttribute('data-print-target', target);
    window.print();
    document.body.removeAttribute('data-print-target');
}

function downloadStandaloneHTML() {
    const content = document.documentElement.outerHTML;
    const blob = new Blob([content], { type: 'text/html;charset=utf-8' });
    const a = document.createElement('a');
    a.href = URL.createObjectURL(blob);
    a.download = 'electromagnetics_study_sheet.html';
    a.click();
}

/* EM Diagram Pan, Zoom & Interaction Handlers */
let emZoom = 1.0;
let emPanX = 0, emPanY = 0;
let isEmDragging = false;
let emStartX = 0, emStartY = 0;
let emShowDetails = true;

function applyEmTransform() {
    const layer = document.getElementById('em-diagram-layer');
    if (layer) {
        layer.style.transform = `translate(${emPanX}px, ${emPanY}px) scale(${emZoom})`;
    }
}

function zoomEmDiagram(factor) {
    emZoom = Math.min(Math.max(emZoom * factor, 0.4), 3.5);
    applyEmTransform();
}

function resetEmDiagramZoom() {
    emZoom = 1.0;
    emPanX = 0;
    emPanY = 0;
    applyEmTransform();
}

function toggleEmDiagramDetails() {
    emShowDetails = !emShowDetails;
    const detailsGroup = document.querySelectorAll('.em-diagram-detail');
    detailsGroup.forEach(el => {
        el.style.display = emShowDetails ? 'inline' : 'none';
    });
    const btn = document.getElementById('toggle-em-details-btn');
    if (btn) {
        btn.classList.toggle('active', emShowDetails);
    }
}

function startEmDrag(e) {
    isEmDragging = true;
    emStartX = e.clientX - emPanX;
    emStartY = e.clientY - emPanY;
    const vp = document.getElementById('em-diagram-viewport');
    if (vp) vp.style.cursor = 'grabbing';
    window.addEventListener('mousemove', handleEmDrag);
    window.addEventListener('mouseup', stopEmDrag);
}

function handleEmDrag(e) {
    if (!isEmDragging) return;
    emPanX = e.clientX - emStartX;
    emPanY = e.clientY - emStartY;
    applyEmTransform();
}

function stopEmDrag() {
    isEmDragging = false;
    const vp = document.getElementById('em-diagram-viewport');
    if (vp) vp.style.cursor = 'grab';
    window.removeEventListener('mousemove', handleEmDrag);
    window.removeEventListener('mouseup', stopEmDrag);
}

function handleEmWheel(e) {
    e.preventDefault();
    const delta = e.deltaY < 0 ? 1.1 : 0.9;
    zoomEmDiagram(delta);
}

document.addEventListener('DOMContentLoaded', () => {
    const savedTheme = getAppTheme();
    setAppTheme(savedTheme);
    setTimeout(renderAllLatex, 150);
});
</script>
"""

