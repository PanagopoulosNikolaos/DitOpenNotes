#!/usr/bin/env python3
"""
Modern Quiz Web App built with NiceGUI.

Loads question sets from data/questions.json and presents an interactive
quiz interface with topic selection, per-question feedback, and a results
review screen. Uses a soft dark theme with muted accent colors.
"""

import json
import pathlib
import time
from dataclasses import dataclass, field

from nicegui import ui

# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------

DATA_FILE = pathlib.Path(__file__).resolve().parent / "data" / "questions.json"

TOPIC_NAMES = {
    "1": "Network Edge",
    "2": "The Internet",
    "3": "Network Structure",
    "4": "Access Technologies",
    "5": "Communication Media",
    "6": "Data Switching and Routing",
    "7": "Basic Networking Issues",
    "8": "General Quick Review",
}

ALL_TOPICS_KEY = "all"


def loadQuestions():
    """
    Loads the question dataset from the JSON data file.

    Returns:
        dict: Mapping of topic string IDs to lists of question objects.
    """
    with open(DATA_FILE, encoding="utf-8") as handle:
        return json.load(handle)


QUESTIONS = loadQuestions()


# ---------------------------------------------------------------------------
# Theme configuration
# ---------------------------------------------------------------------------

def configureTheme():
    """
    Applies the soft dark color palette and global CSS overrides.
    """
    ui.colors(
        primary="#5B8DEF",
        secondary="#94A3B8",
        accent="#FBBF24",
        positive="#34D399",
        negative="#F87171",
        info="#5B8DEF",
        warning="#FBBF24",
    )
    ui.dark_mode(True)

    ui.add_head_html(
        """
        <style>
        :root {
            --q-dark: #12161A;
            --q-dark-page: #12161A;
            --q-surface: #1E242B;
            --q-border: #2D353F;
            --q-text: #E2E8F0;
            --q-text-secondary: #94A3B8;
            --q-correct: #34D399;
            --q-incorrect: #F87171;
            --q-warning: #FBBF24;
        }
        body {
            background-color: #12161A !important;
            font-family: 'Inter', 'Segoe UI', system-ui, sans-serif;
        }
        .q-card {
            background-color: #1E242B !important;
            border: 1px solid #2D353F !important;
            border-radius: 16px !important;
            box-shadow: 0 8px 30px rgba(0, 0, 0, 0.35) !important;
        }
        .q-btn {
            border-radius: 10px !important;
            text-transform: none !important;
            font-weight: 500 !important;
        }
        .option-btn {
            width: 100%;
            justify-content: flex-start;
            text-align: left;
            padding: 14px 18px !important;
            background-color: #252D37 !important;
            color: #E2E8F0 !important;
            border: 1px solid #2D353F !important;
            border-radius: 12px !important;
            transition: all 0.2s ease !important;
            font-size: 15px !important;
            line-height: 1.5 !important;
        }
        .option-btn:hover {
            background-color: #2D353F !important;
            border-color: #5B8DEF !important;
            transform: translateY(-1px);
        }
        .option-correct {
            background-color: rgba(52, 211, 153, 0.15) !important;
            border-color: #34D399 !important;
            color: #34D399 !important;
        }
        .option-incorrect {
            background-color: rgba(248, 113, 113, 0.15) !important;
            border-color: #F87171 !important;
            color: #F87171 !important;
        }
        .option-dimmed {
            opacity: 0.5 !important;
        }
        .explanation-box {
            background-color: #1A2332 !important;
            border: 1px solid #2D353F !important;
            border-radius: 12px !important;
            padding: 16px 20px !important;
        }
        .topic-card {
            cursor: pointer;
            transition: all 0.2s ease !important;
        }
        .topic-card:hover {
            border-color: #5B8DEF !important;
            transform: translateY(-3px);
            box-shadow: 0 12px 30px rgba(91, 141, 239, 0.15) !important;
        }
        .score-pill {
            background-color: #1E242B !important;
            border: 1px solid #2D353F !important;
            border-radius: 999px !important;
            padding: 6px 16px !important;
            font-weight: 600 !important;
            color: #E2E8F0 !important;
        }
        .progress-track {
            background-color: #2D353F !important;
            border-radius: 999px !important;
            height: 8px !important;
        }
        .progress-fill {
            background: linear-gradient(90deg, #5B8DEF, #7C9FF0) !important;
            border-radius: 999px !important;
            transition: width 0.3s ease !important;
        }
        .stat-card {
            background-color: #1E242B !important;
            border: 1px solid #2D353F !important;
            border-radius: 14px !important;
            padding: 20px !important;
            text-align: center;
        }
        .stat-value {
            font-size: 28px !important;
            font-weight: 700 !important;
            color: #E2E8F0 !important;
        }
        .stat-label {
            font-size: 13px !important;
            color: #94A3B8 !important;
            margin-top: 4px !important;
        }
        .review-item {
            background-color: #1E242B !important;
            border: 1px solid #2D353F !important;
            border-radius: 12px !important;
            padding: 16px !important;
            margin-bottom: 12px !important;
        }
        .code-block {
            background-color: #0F1419 !important;
            border: 1px solid #2D353F !important;
            border-radius: 8px !important;
            padding: 12px 16px !important;
            font-family: 'JetBrains Mono', 'Fira Code', monospace !important;
            font-size: 13px !important;
            color: #FBBF24 !important;
            white-space: pre-wrap !important;
            word-break: break-word !important;
        }
        .header-bar {
            background-color: #12161A !important;
            border-bottom: 1px solid #2D353F !important;
        }
        .logo-btn {
            transition: opacity 0.2s ease !important;
            border-radius: 8px !important;
            padding: 4px 8px !important;
            margin-left: -8px !important;
        }
        .logo-btn:hover {
            opacity: 0.75 !important;
            background-color: #1E242B !important;
        }
        .logo-icon {
            transition: transform 0.2s ease !important;
        }
        .logo-btn:hover .logo-icon {
            transform: scale(1.1);
        }
        .math-content {
            line-height: 1.5;
        }
        </style>
        <script>
        window.MathJax = {
            tex: {
                inlineMath: [['$', '$'], ['\\(', '\\)']],
                displayMath: [['$$', '$$'], ['\\[', '\\]']],
                processEscapes: true
            },
            options: {
                ignoreHtmlClass: 'escaped-latex',
                processHtmlClass: 'math-content'
            },
            startup: {
                ready: function () {
                    MathJax.startup.defaultReady();
                    MathJax.startup.promise.then(function () {
                        var typesetting = false;
                        var scheduled = false;
                        function maybeTypeset() {
                            if (typesetting) {
                                scheduled = true;
                                return;
                            }
                            typesetting = true;
                            MathJax.typesetPromise().finally(function () {
                                typesetting = false;
                                if (scheduled) {
                                    scheduled = false;
                                    maybeTypeset();
                                }
                            });
                        }
                        var observer = new MutationObserver(function (mutations) {
                            var relevant = mutations.some(function (m) {
                                return Array.prototype.some.call(m.addedNodes, function (node) {
                                    return node.nodeType === 1 &&
                                        (node.classList.contains('math-content') ||
                                         node.querySelector && node.querySelector('.math-content'));
                                });
                            });
                            if (relevant) {
                                maybeTypeset();
                            }
                        });
                        observer.observe(document.body, { childList: true, subtree: true });
                    });
                }
            }
        };
        </script>
        <script async
            src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js">
        </script>
        """
    )


# ---------------------------------------------------------------------------
# State management
# ---------------------------------------------------------------------------

@dataclass
class QuizState:
    """
    Holds the reactive state for the quiz application.

    Attributes:
        active_topic (str): Selected topic key, or "all" for practice exam.
        questions (list): The list of question objects for the active quiz.
        current_index (int): Index of the currently displayed question.
        answers (dict): Maps question index to the selected option index.
        screen (str): Current screen: "topics", "quiz", or "results".
        start_time (float): Timestamp when the quiz started.
        review_index (int): Index of the question being reviewed in results.
    """
    active_topic: str = ALL_TOPICS_KEY
    questions: list = field(default_factory=list)
    current_index: int = 0
    answers: dict = field(default_factory=dict)
    screen: str = "topics"
    start_time: float = 0.0
    review_index: int = 0


state = QuizState()


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------

def getTopicQuestions(topic_key):
    """
    Returns the question list for a topic key.

    Args:
        topic_key (str): The topic identifier or ALL_TOPICS_KEY.

    Returns:
        list: The list of question objects.
    """
    if topic_key == ALL_TOPICS_KEY:
        combined = []
        for key in sorted(QUESTIONS.keys(), key=int):
            combined.extend(QUESTIONS[key])
        return combined
    return QUESTIONS.get(topic_key, [])


def getTopicTitle(topic_key):
    """
    Returns the display title for a topic key.

    Args:
        topic_key (str): The topic identifier or ALL_TOPICS_KEY.

    Returns:
        str: The human-readable topic title.
    """
    if topic_key == ALL_TOPICS_KEY:
        return "All Topics / Practice Exam"
    return TOPIC_NAMES.get(topic_key, f"Topic {topic_key}")


def getQuestionCount(topic_key):
    """
    Returns the number of questions for a topic key.

    Args:
        topic_key (str): The topic identifier or ALL_TOPICS_KEY.

    Returns:
        int: The question count.
    """
    return len(getTopicQuestions(topic_key))


def formatTime(seconds):
    """
    Formats a duration in seconds as MM:SS.

    Args:
        seconds (float): The elapsed time in seconds.

    Returns:
        str: The formatted time string.
    """
    total = int(seconds)
    minutes, secs = divmod(total, 60)
    return f"{minutes:02d}:{secs:02d}"


def isCodeQuestion(question):
    """
    Heuristic check for whether a question contains CLI or code content.

    Args:
        question (dict): The question object.

    Returns:
        bool: True if the question text looks like code/CLI content.
    """
    text = question.get("question", "")
    code_markers = [
        "enable", "configure terminal", "interface", "ip address",
        "show running-config", "ping", "traceroute", "switchport",
        "vlan", "router", "hostname", "no shutdown", "exit",
        ">", "#", "$", "cisco", "packet tracer", "cli",
    ]
    lowered = text.lower()
    return any(marker in lowered for marker in code_markers)


def renderQuestionText(question):
    """
    Renders question text, wrapping code-like content in a styled block.

    Args:
        question (dict): The question object.

    Returns:
        None: Adds UI elements directly.
    """
    text = question.get("question", "")
    if isCodeQuestion(question):
        with ui.column().classes("w-full gap-2"):
            ui.label(text).classes("text-lg text-[#E2E8F0] leading-relaxed math-content")
    else:
        ui.label(text).classes("text-lg text-[#E2E8F0] leading-relaxed math-content")


# ---------------------------------------------------------------------------
# Screen renderers
# ---------------------------------------------------------------------------

@ui.refreshable
def renderHeader():
    """
    Renders the top navigation bar with title, topic selector, and score.
    """
    with ui.row().classes("w-full items-center justify-between px-6 py-4 header-bar"):
        with ui.row().classes("items-center gap-3 cursor-pointer logo-btn").on(
            "click", goToTopics
        ):
            ui.icon("school").classes("text-[#5B8DEF] text-3xl logo-icon")
            ui.label("Network Notes Quiz").classes(
                "text-xl font-bold text-[#E2E8F0]"
            )

        with ui.row().classes("items-center gap-3"):
            if state.screen == "quiz":
                total = len(state.questions)
                answered = len(state.answers)
                correct = sum(
                    1
                    for idx, ans in state.answers.items()
                    if ans == state.questions[idx]["correct_index"]
                )
                pct = int((correct / total) * 100) if total else 0
                ui.label(f"{correct} / {answered}").classes(
                    "score-pill text-sm"
                )
                ui.label(f"{pct}%").classes(
                    "score-pill text-sm text-[#5B8DEF]"
                )


@ui.refreshable
def renderTopicSelection():
    """
    Renders the grid of topic selection cards.
    """
    with ui.column().classes("w-full max-w-5xl mx-auto px-6 py-10 gap-8"):
        ui.label("Select a Topic").classes(
            "text-3xl font-bold text-[#E2E8F0]"
        )
        ui.label(
            "Choose a topic to practice, or take a full practice exam across all topics."
        ).classes("text-[#94A3B8]")

        # All Topics card
        with ui.card().classes("topic-card w-full p-6").on(
            "click", lambda: startQuiz(ALL_TOPICS_KEY)
        ):
            with ui.row().classes("items-center justify-between w-full"):
                with ui.column().classes("gap-1"):
                    ui.label("All Topics / Practice Exam").classes(
                        "text-lg font-semibold text-[#E2E8F0]"
                    )
                    ui.label(
                        f"{getQuestionCount(ALL_TOPICS_KEY)} questions"
                    ).classes("text-sm text-[#94A3B8]")
                ui.button(
                    "Start Practice Exam",
                    on_click=lambda: startQuiz(ALL_TOPICS_KEY),
                ).props("flat color=primary")

        ui.label("Individual Topics").classes(
            "text-xl font-semibold text-[#E2E8F0] mt-4"
        )

        # Topic grid
        with ui.grid(columns=2).classes("w-full gap-4"):
            for key in sorted(QUESTIONS.keys(), key=int):
                title = TOPIC_NAMES[key]
                count = getQuestionCount(key)
                with ui.card().classes("topic-card p-6").on(
                    "click", lambda k=key: startQuiz(k)
                ):
                    with ui.column().classes("gap-2 w-full"):
                        ui.label(f"Topic {key}").classes(
                            "text-xs font-semibold text-[#5B8DEF] uppercase tracking-wide"
                        )
                        ui.label(title).classes(
                            "text-base font-semibold text-[#E2E8F0]"
                        )
                        ui.label(f"{count} questions").classes(
                            "text-sm text-[#94A3B8]"
                        )
                        ui.button(
                            "Start Topic Quiz",
                            on_click=lambda k=key: startQuiz(k),
                        ).props("flat color=primary").classes("mt-2")


@ui.refreshable
def renderQuiz():
    """
    Renders the active quiz question view.
    """
    if not state.questions:
        return

    total = len(state.questions)
    idx = state.current_index
    question = state.questions[idx]
    selected = state.answers.get(idx)
    revealed = selected is not None

    with ui.column().classes("w-full max-w-3xl mx-auto px-6 py-8 gap-6"):
        # Progress bar
        with ui.column().classes("w-full gap-2"):
            with ui.row().classes("w-full items-center justify-between"):
                ui.label(f"Question {idx + 1} of {total}").classes(
                    "text-sm text-[#94A3B8]"
                )
                ui.label(getTopicTitle(state.active_topic)).classes(
                    "text-sm text-[#94A3B8]"
                )
            ui.linear_progress(
                value=(idx + 1) / total,
                show_value=False,
            ).props("rounded").classes("w-full progress-track")

        # Question card
        with ui.card().classes("w-full p-8 gap-6"):
            renderQuestionText(question)

            # Options
            with ui.column().classes("w-full gap-3"):
                for opt_idx, option in enumerate(question["options"]):
                    is_correct = opt_idx == question["correct_index"]
                    is_selected = selected == opt_idx

                    classes = ["option-btn"]
                    if revealed:
                        if is_correct:
                            classes.append("option-correct")
                        elif is_selected:
                            classes.append("option-incorrect")
                        else:
                            classes.append("option-dimmed")

                    with ui.row().classes(
                        "w-full items-center gap-3 option-btn " + " ".join(
                            c for c in classes if c != "option-btn"
                        )
                    ).on("click", lambda o=opt_idx: selectAnswer(o)):
                        # Letter badge
                        letter = chr(65 + opt_idx)
                        with ui.row().classes(
                            "items-center justify-center w-8 h-8 rounded-full "
                            + (
                                "bg-[#34D399] text-[#12161A]"
                                if revealed and is_correct
                                else "bg-[#F87171] text-[#12161A]"
                                if revealed and is_selected
                                else "bg-[#2D353F] text-[#94A3B8]"
                            )
                        ):
                            ui.label(letter).classes("font-bold text-sm")

                        ui.label(option).classes("flex-1 math-content")

                        if revealed and is_correct:
                            ui.icon("check_circle").classes(
                                "text-[#34D399] text-xl"
                            )
                        elif revealed and is_selected:
                            ui.icon("cancel").classes(
                                "text-[#F87171] text-xl"
                            )

            # Explanation box
            if revealed:
                with ui.column().classes(
                    "w-full explanation-box gap-2 mt-2"
                ):
                    with ui.row().classes("items-center gap-2"):
                        ui.icon("lightbulb").classes(
                            "text-[#FBBF24] text-lg"
                        )
                        ui.label("Explanation").classes(
                            "font-semibold text-[#FBBF24]"
                        )
                    ui.label(question["explanation"]).classes(
                        "text-sm text-[#E2E8F0] leading-relaxed math-content"
                    )

        # Action footer
        with ui.row().classes("w-full items-center justify-between gap-3"):
            ui.button(
                "Previous",
                icon="arrow_back",
                on_click=goPrevious,
            ).props("flat").classes("text-[#94A3B8]").bind_enabled_from(
                state, "current_index", backward=lambda v: v > 0
            )

            with ui.row().classes("gap-3"):
                ui.button(
                    "Skip",
                    icon="skip_next",
                    on_click=skipQuestion,
                ).props("flat color=warning")

                if idx < total - 1:
                    ui.button(
                        "Next Question",
                        icon="arrow_forward",
                        on_click=goNext,
                    ).props("unelevated color=primary")
                else:
                    ui.button(
                        "Finish Quiz",
                        icon="flag",
                        on_click=finishQuiz,
                    ).props("unelevated color=positive")


@ui.refreshable
def renderResults():
    """
    Renders the quiz completion and results review screen.
    """
    total = len(state.questions)
    correct = 0
    incorrect = 0
    skipped = 0
    for idx, question in enumerate(state.questions):
        ans = state.answers.get(idx)
        if ans is None:
            skipped += 1
        elif ans == question["correct_index"]:
            correct += 1
        else:
            incorrect += 1

    pct = int((correct / total) * 100) if total else 0
    elapsed = time.time() - state.start_time

    with ui.column().classes("w-full max-w-3xl mx-auto px-6 py-10 gap-8"):
        # Header
        ui.label("Quiz Complete!").classes(
            "text-3xl font-bold text-[#E2E8F0]"
        )
        ui.label(getTopicTitle(state.active_topic)).classes(
            "text-[#94A3B8]"
        )

        # Score summary
        with ui.row().classes("w-full gap-4"):
            with ui.card().classes("stat-card flex-1"):
                ui.label(f"{pct}%").classes("stat-value text-[#5B8DEF]")
                ui.label("Accuracy").classes("stat-label")

            with ui.card().classes("stat-card flex-1"):
                ui.label(str(correct)).classes("stat-value text-[#34D399]")
                ui.label("Correct").classes("stat-label")

            with ui.card().classes("stat-card flex-1"):
                ui.label(str(incorrect)).classes("stat-value text-[#F87171]")
                ui.label("Incorrect").classes("stat-label")

            with ui.card().classes("stat-card flex-1"):
                ui.label(str(skipped)).classes("stat-value text-[#FBBF24]")
                ui.label("Skipped").classes("stat-label")

            with ui.card().classes("stat-card flex-1"):
                ui.label(formatTime(elapsed)).classes(
                    "stat-value text-[#94A3B8]"
                )
                ui.label("Time Spent").classes("stat-label")

        # Performance breakdown
        ui.label("Performance Breakdown").classes(
            "text-xl font-semibold text-[#E2E8F0] mt-4"
        )

        # Correct questions
        correct_indices = [
            idx
            for idx, q in enumerate(state.questions)
            if state.answers.get(idx) == q["correct_index"]
        ]
        incorrect_indices = [
            idx
            for idx, q in enumerate(state.questions)
            if state.answers.get(idx) is not None
            and state.answers.get(idx) != q["correct_index"]
        ]
        skipped_indices = [
            idx
            for idx in range(total)
            if state.answers.get(idx) is None
        ]

        with ui.tabs().classes("w-full") as tabs:
            correct_tab = ui.tab("Correct", icon="check_circle")
            incorrect_tab = ui.tab("Incorrect", icon="cancel")
            skipped_tab = ui.tab("Skipped", icon="skip_next")

        with ui.tab_panels(tabs, value=correct_tab).classes("w-full"):
            with ui.tab_panel(correct_tab):
                renderReviewList(correct_indices, "correct")
            with ui.tab_panel(incorrect_tab):
                renderReviewList(incorrect_indices, "incorrect")
            with ui.tab_panel(skipped_tab):
                renderReviewList(skipped_indices, "skipped")

        # Action buttons
        with ui.row().classes("w-full items-center justify-center gap-4 mt-6"):
            ui.button(
                "Retry Topic",
                icon="refresh",
                on_click=lambda: startQuiz(state.active_topic),
            ).props("unelevated color=primary")

            ui.button(
                "Select New Topic",
                icon="menu_book",
                on_click=goToTopics,
            ).props("outline color=primary")

            ui.button(
                "Export Review",
                icon="download",
                on_click=exportReview,
            ).props("flat color=secondary")


def renderReviewList(indices, status):
    """
    Renders a list of review items for the given question indices.

    Args:
        indices (list): List of question indices to display.
        status (str): One of "correct", "incorrect", or "skipped".
    """
    if not indices:
        ui.label("No questions in this category.").classes(
            "text-[#94A3B8] py-4"
        )
        return

    for idx in indices:
        question = state.questions[idx]
        selected = state.answers.get(idx)
        correct_idx = question["correct_index"]

        with ui.card().classes("review-item w-full gap-3"):
            with ui.row().classes("w-full items-start justify-between gap-3"):
                ui.label(f"Q{idx + 1}").classes(
                    "text-sm font-semibold text-[#5B8DEF]"
                )
                if status == "correct":
                    ui.icon("check_circle").classes("text-[#34D399]")
                elif status == "incorrect":
                    ui.icon("cancel").classes("text-[#F87171]")
                else:
                    ui.icon("skip_next").classes("text-[#FBBF24]")

            ui.label(question["question"]).classes(
                "text-sm text-[#E2E8F0] leading-relaxed math-content"
            )

            with ui.column().classes("w-full gap-1 mt-1"):
                for opt_idx, option in enumerate(question["options"]):
                    if opt_idx == correct_idx:
                        ui.label(
                            f"Correct: {option}"
                        ).classes("text-sm text-[#34D399] math-content")
                    elif opt_idx == selected:
                        ui.label(
                            f"Your answer: {option}"
                        ).classes("text-sm text-[#F87171] math-content")

            if status != "correct":
                ui.label(question["explanation"]).classes(
                    "text-xs text-[#94A3B8] leading-relaxed mt-1 math-content"
                )


# ---------------------------------------------------------------------------
# Actions
# ---------------------------------------------------------------------------

def startQuiz(topic_key):
    """
    Starts a quiz for the given topic key.

    Args:
        topic_key (str): The topic identifier or ALL_TOPICS_KEY.
    """
    state.active_topic = topic_key
    state.questions = getTopicQuestions(topic_key)
    state.current_index = 0
    state.answers = {}
    state.start_time = time.time()
    state.screen = "quiz"
    refreshAll()


def selectAnswer(option_index):
    """
    Records the selected answer for the current question.

    Args:
        option_index (int): The index of the selected option.
    """
    if state.answers.get(state.current_index) is not None:
        return
    state.answers[state.current_index] = option_index
    refreshAll()


def goNext():
    """
    Advances to the next question if available.
    """
    if state.current_index < len(state.questions) - 1:
        state.current_index += 1
        refreshAll()


def goPrevious():
    """
    Moves back to the previous question if available.
    """
    if state.current_index > 0:
        state.current_index -= 1
        refreshAll()


def skipQuestion():
    """
    Skips the current question and advances to the next one.
    """
    if state.current_index < len(state.questions) - 1:
        state.current_index += 1
        refreshAll()


def finishQuiz():
    """
    Transitions to the results screen.
    """
    state.screen = "results"
    refreshAll()


def goToTopics():
    """
    Returns to the topic selection screen.
    """
    state.screen = "topics"
    refreshAll()


def exportReview():
    """
    Exports the review data as a downloadable JSON file.
    """
    export_data = {
        "topic": getTopicTitle(state.active_topic),
        "total_questions": len(state.questions),
        "answers": [],
    }
    for idx, question in enumerate(state.questions):
        selected = state.answers.get(idx)
        export_data["answers"].append(
            {
                "question_index": idx,
                "question": question["question"],
                "selected_index": selected,
                "correct_index": question["correct_index"],
                "is_correct": selected == question["correct_index"],
            }
        )

    ui.download(
        json.dumps(export_data, ensure_ascii=False, indent=2),
        filename="quiz_review.json",
    )


def refreshAll():
    """
    Refreshes all dynamic UI sections based on the current state.
    """
    renderHeader.refresh()
    renderTopicSelection.refresh()
    renderQuiz.refresh()
    renderResults.refresh()


# ---------------------------------------------------------------------------
# Main layout
# ---------------------------------------------------------------------------

def buildLayout():
    """
    Builds the main application layout with header and screen containers.
    """
    configureTheme()

    renderHeader()

    with ui.column().classes("w-full"):
        with ui.column().bind_visibility_from(
            state, "screen", value="topics"
        ).classes("w-full"):
            renderTopicSelection()

        with ui.column().bind_visibility_from(
            state, "screen", value="quiz"
        ).classes("w-full"):
            renderQuiz()

        with ui.column().bind_visibility_from(
            state, "screen", value="results"
        ).classes("w-full"):
            renderResults()


ui.page("/", title="Network Notes Quiz")(buildLayout)

if __name__ in {"__main__", "__mp_main__"}:
    ui.run(
        title="Network Notes Quiz",
        dark=True,
        port=8080,
        reload=False,
    )