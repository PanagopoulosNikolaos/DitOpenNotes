"""Theme configuration and styling rules for the Discrete Mathematics application.

Provides design tokens, color constants, custom CSS, KaTeX mathematical typography,
and theme switching logic adhering to the Orange Light (default) and Soft Dark specifications.
"""

# Universal CSS design tokens for Course 203: Discrete Mathematics
CUSTOM_CSS = r"""
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600;700&display=swap');
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css');
@import url('https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css');

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
    --surface: rgba(255, 255, 255, 0.92);
    --surface-2: #f1f3f6;
    --surface-hover: #e5e7eb;
    --border: rgba(0, 0, 0, 0.09);
    --border-accent: rgba(224, 107, 58, 0.45);
    --border-focus: rgba(234, 88, 12, 0.75);
    --accent: #d9531e;
    --accent-light: #ea580c;
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

    /* Semantic Math & Logic Styling Tokens */
    --card-bg-subtle: #f8fafc;
    --card-border-subtle: #e2e8f0;
    --table-header-bg: #f1f5f9;
    --table-alt-bg: #f8fafc;
    --table-border: #e2e8f0;
    --code-bg: #f8fafc;
    --code-text: #0f172a;
    --code-border: rgba(0, 0, 0, 0.10);
    --header-bg: rgba(255, 255, 255, 0.90);
    --menu-bg: #ffffff;
    --menu-border: rgba(224, 107, 58, 0.35);
    --input-bg: #ffffff;
    --badge-bg: #f3f4f6;

    /* Discrete Graph & Automata SVG Canvas */
    --svg-canvas-bg: #ffffff;
    --svg-grid-dot: rgba(0, 0, 0, 0.08);
    --svg-node-fill: #f8fafc;
    --svg-node-stroke: #ea580c;
    --svg-node-active: #d9531e;
    --svg-node-text: #18181b;
    --svg-edge-stroke: #64748b;
    --svg-edge-active: #059669;

    /* Callouts */
    --callout-gotcha-bg: #fef2f2;
    --callout-gotcha-border: #f87171;
    --callout-gotcha-text: #991b1b;
    --callout-formula-bg: #eff6ff;
    --callout-formula-border: #60a5fa;
    --callout-formula-text: #1e40af;
    --callout-success-bg: #f0fdf4;
    --callout-success-border: #4ade80;
    --callout-success-text: #166534;
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
    --surface-hover: rgba(255, 255, 255, 0.11);
    --border: rgba(255, 255, 255, 0.08);
    --border-accent: rgba(249, 115, 22, 0.40);
    --border-focus: rgba(249, 115, 22, 0.70);
    --accent: #f97316;
    --accent-light: #fb923c;
    --accent-dark: #ea580c;
    --amber: #f59e0b;
    --orange: #f97316;
    --text-1: #f4f4f5;
    --text-2: #a1a1aa;
    --text-3: #71717a;
    --green-ok: #10b981;
    --green-light: #34d399;
    --red-err: #ef4444;
    --red-light: #f87171;
    --blue-action: #3b82f6;
    --blue-hover: #60a5fa;
    --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.35);
    --shadow-md: 0 4px 18px rgba(0, 0, 0, 0.45);
    --shadow-lg: 0 10px 32px rgba(0, 0, 0, 0.60);

    /* Semantic Math & Logic Styling Tokens */
    --card-bg-subtle: #1e1e20;
    --card-border-subtle: #2e2e32;
    --table-header-bg: #27272a;
    --table-alt-bg: #1f1f23;
    --table-border: #3f3f46;
    --code-bg: #18181b;
    --code-text: #f4f4f5;
    --code-border: rgba(255, 255, 255, 0.10);
    --header-bg: rgba(28, 27, 26, 0.90);
    --menu-bg: #201f1d;
    --menu-border: rgba(249, 115, 22, 0.40);
    --input-bg: #201f1d;
    --badge-bg: #27272a;

    /* Discrete Graph & Automata SVG Canvas */
    --svg-canvas-bg: #1a1a1c;
    --svg-grid-dot: rgba(255, 255, 255, 0.08);
    --svg-node-fill: #262629;
    --svg-node-stroke: #f97316;
    --svg-node-active: #fb923c;
    --svg-node-text: #f4f4f5;
    --svg-edge-stroke: #94a3b8;
    --svg-edge-active: #34d399;

    /* Callouts */
    --callout-gotcha-bg: rgba(239, 68, 68, 0.12);
    --callout-gotcha-border: #ef4444;
    --callout-gotcha-text: #fca5a5;
    --callout-formula-bg: rgba(59, 130, 246, 0.12);
    --callout-formula-border: #3b82f6;
    --callout-formula-text: #93c5fd;
    --callout-success-bg: rgba(16, 185, 129, 0.12);
    --callout-success-border: #10b981;
    --callout-success-text: #86efac;
}

/* ==========================================================================
   GLOBAL RESET & TYPOGRAPHY
   ========================================================================== */

* {
    box-sizing: border-box;
}

body {
    font-family: 'Outfit', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    background-color: var(--bg-deep);
    color: var(--text-1);
    transition: background-color 0.25s ease, color 0.25s ease;
    margin: 0;
    padding: 0;
}

code, pre, .font-mono {
    font-family: 'JetBrains Mono', monospace !important;
}

/* Gradient Title */
.gradient-title {
    background: linear-gradient(135deg, var(--accent) 0%, #ea580c 50%, #f59e0b 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* Card Surface Utility */
.dash-card {
    background-color: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: var(--r-md);
    box-shadow: var(--shadow-sm);
    transition: box-shadow 0.2s ease, border-color 0.2s ease;
}

.dash-card:hover {
    box-shadow: var(--shadow-md);
    border-color: var(--border-accent);
}

/* Metric / KPI Chip */
.kpi-badge {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.35rem 0.75rem;
    border-radius: var(--r-pill);
    font-size: 0.75rem;
    font-weight: 600;
    background: var(--surface-2);
    border: 1px solid var(--border);
    color: var(--text-1);
}

/* Button Secondary */
.btn-secondary {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.4rem 0.85rem;
    border-radius: var(--r-sm);
    font-size: 0.8rem;
    font-weight: 600;
    background: var(--surface-2);
    border: 1px solid var(--border);
    color: var(--text-1);
    cursor: pointer;
    transition: all 0.2s ease;
}

.btn-secondary:hover {
    background: var(--surface-hover);
    border-color: var(--border-accent);
}

/* Callout Blocks */
.callout-gotcha {
    background-color: var(--callout-gotcha-bg);
    border-left: 4px solid var(--callout-gotcha-border);
    color: var(--callout-gotcha-text);
    padding: 0.85rem 1.15rem;
    border-radius: 0 var(--r-sm) var(--r-sm) 0;
    font-size: 0.875rem;
    line-height: 1.45;
}

.callout-formula {
    background-color: var(--callout-formula-bg);
    border-left: 4px solid var(--callout-formula-border);
    color: var(--callout-formula-text);
    padding: 0.85rem 1.15rem;
    border-radius: 0 var(--r-sm) var(--r-sm) 0;
    font-size: 0.875rem;
    line-height: 1.45;
}

/* Truth Table Styles */
.truth-table {
    width: 100%;
    border-collapse: collapse;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.825rem;
}

.truth-table th {
    background-color: var(--table-header-bg);
    color: var(--text-1);
    padding: 0.6rem 0.85rem;
    border: 1px solid var(--table-border);
    font-weight: 700;
    text-align: center;
}

.truth-table td {
    padding: 0.5rem 0.85rem;
    border: 1px solid var(--table-border);
    text-align: center;
}

.truth-table tr:nth-child(even) td {
    background-color: var(--table-alt-bg);
}

.val-true {
    color: var(--green-ok);
    font-weight: bold;
}

.val-false {
    color: var(--red-err);
    font-weight: bold;
}

/* Print Styles */
@media print {
    body {
        background: #ffffff !important;
        color: #000000 !important;
    }
    .no-print {
        display: none !important;
    }
    .dash-card {
        box-shadow: none !important;
        border: 1px solid #cccccc !important;
        break-inside: avoid;
    }
}
"""

THEME_HEAD_SCRIPT = """
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"></script>
<script>
    function renderKaTeX() {
        if (typeof renderMathInElement === 'function') {
            try {
                renderMathInElement(document.body, {
                    delimiters: [
                        {left: '$$', right: '$$', display: true},
                        {left: '$', right: '$', display: false}
                    ],
                    throwOnError: false
                });
            } catch (err) {
                console.warn('KaTeX render error:', err);
            }
        }
    }

    function getAppTheme() {
        return localStorage.getItem('discrete_math_theme') || 'light';
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
        localStorage.setItem('discrete_math_theme', isDark ? 'dark' : 'light');

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

    function printDiscreteSection(sectionId) {
        window.print();
    }

    document.addEventListener('DOMContentLoaded', () => {
        setAppTheme(getAppTheme());
        renderKaTeX();
    });

    setTimeout(() => {
        setAppTheme(getAppTheme());
        renderKaTeX();
    }, 150);
</script>
"""
