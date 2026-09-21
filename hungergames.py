import streamlit as st
import random
from collections import Counter
import base64
import os


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="WHO IS YOUR HUNGER GAMES CHARACTER?",
    page_icon="🔥",
    layout="centered"
)


# ============================================================
# BACKGROUND IMAGE
# ============================================================

def get_base64_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()


image_path = "gasterbg.jfif"

if os.path.exists(image_path):
    bg_base64 = get_base64_image(image_path)
else:
    bg_base64 = ""


# ============================================================
# SESSION STATE
# ============================================================

if "page" not in st.session_state:
    st.session_state.page = 0

if "answers" not in st.session_state:
    st.session_state.answers = []

if "finished" not in st.session_state:
    st.session_state.finished = False

if "result" not in st.session_state:
    st.session_state.result = None

if "scores" not in st.session_state:
    st.session_state.scores = None

if "name" not in st.session_state:
    st.session_state.name = ""

if "name_submitted" not in st.session_state:
    st.session_state.name_submitted = False

if "access_denied" not in st.session_state:
    st.session_state.access_denied = False


# ============================================================
# CSS
# ============================================================

st.markdown(
    f"""
    <style>

    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;500;600;700;800&family=Montserrat:wght@400;500;600;700&display=swap');

    html, body, [class*="css"] {{
        font-family: 'Montserrat', sans-serif;
    }}

    .stApp {{
        background:
            linear-gradient(
                rgba(0, 0, 0, 0.72),
                rgba(0, 0, 0, 0.72)
            ),
            url("data:image/jpeg;base64,{bg_base64}");

        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

    .block-container {{
        max-width: 850px;
        padding-top: 3rem;
        padding-bottom: 3rem;
    }}

    /* ========================================================
       TITLE
       ======================================================== */

    .main-title {{
        font-family: 'Cinzel', serif;
        text-align: center;
        font-size: 3rem;
        font-weight: 800;
        color: #e6b84a;
        letter-spacing: 4px;
        text-shadow:
            0 0 10px rgba(230, 184, 74, 0.5),
            0 0 25px rgba(230, 184, 74, 0.25);
        margin-bottom: 0.5rem;
    }}

    .subtitle {{
        text-align: center;
        font-family: 'Cinzel', serif;
        color: #aaa;
        font-size: 1rem;
        letter-spacing: 3px;
        margin-bottom: 3rem;
    }}

    /* ========================================================
       QUESTIONS
       ======================================================== */

    .question-number {{
        font-family: 'Cinzel', serif;
        color: #e6b84a;
        font-size: 0.9rem;
        letter-spacing: 3px;
        text-transform: uppercase;
        margin-bottom: 0.5rem;
    }}

    .question-text {{
        font-family: 'Cinzel', serif;
        color: #f0f0f0;
        font-size: 1.45rem;
        font-weight: 600;
        line-height: 1.5;
        margin-bottom: 1.5rem;
    }}

    /* ========================================================
       BUTTONS
       ======================================================== */

    .stButton > button {{
        width: 100%;
        background: rgba(20, 20, 20, 0.85);
        color: #ddd;
        border: 1px solid #555;
        border-radius: 2px;
        padding: 0.9rem 1rem;
        font-family: 'Montserrat', sans-serif;
        font-size: 0.95rem;
        transition: all 0.2s ease;
    }}

    .stButton > button:hover {{
        border-color: #e6b84a;
        color: #e6b84a;
        background: rgba(40, 35, 20, 0.9);
        transform: translateY(-1px);
    }}

    /* ========================================================
       PROGRESS
       ======================================================== */

    .progress-container {{
        width: 100%;
        height: 5px;
        background: #333;
        margin-bottom: 2.5rem;
        border-radius: 5px;
        overflow: hidden;
    }}

    .progress-bar {{
        height: 100%;
        background: #e6b84a;
        transition: width 0.3s ease;
    }}

    /* ========================================================
       RESULT
       ======================================================== */

    .result-container {{
        text-align: center;
        margin-bottom: 1rem;
    }}

    .fire-symbol {{
        font-size: 3rem;
        margin-bottom: 0.5rem;
    }}

    .result-small {{
        font-family: 'Cinzel', serif;
        font-size: 0.9rem;
        color: #aaa;
        letter-spacing: 4px;
    }}

    .result-title {{
        font-family: 'Cinzel', serif;
        font-size: 2rem;
        font-weight: 700;
        color: #f0f0f0;
        letter-spacing: 3px;
        margin-top: 0.5rem;
    }}

    .result-card {{
        background: rgba(10, 10, 10, 0.9);
        border: 1px solid #555;
        border-top: 3px solid #e6b84a;
        padding: 2.5rem;
        text-align: center;
        margin-top: 2rem;
        box-shadow:
            0 0 30px rgba(0, 0, 0, 0.6),
            inset 0 0 30px rgba(230, 184, 74, 0.03);
    }}

    .result-score {{
        font-family: 'Montserrat', sans-serif;
        color: #aaa;
        font-size: 1rem;
        letter-spacing: 1px;
    }}

    /* ========================================================
       NAME SCREEN
       ======================================================== */

    .name-container {{
        text-align: center;
        margin-top: 5rem;
    }}

    .name-title {{
        font-family: 'Cinzel', serif;
        color: #e6b84a;
        font-size: 2.5rem;
        font-weight: 800;
        letter-spacing: 4px;
        margin-bottom: 1rem;
    }}

    .name-subtitle {{
        font-family: 'Cinzel', serif;
        color: #aaa;
        font-size: 1rem;
        letter-spacing: 2px;
        margin-bottom: 2rem;
    }}

    /* ========================================================
       ACCESS DENIED
       ======================================================== */

    .access-denied {{
        text-align: center;
        min-height: 70vh;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }}

    .access-title {{
        font-family: 'Cinzel', serif;
        font-size: 4rem;
        font-weight: 800;
        color: #e60000;
        letter-spacing: 6px;
        text-shadow:
            0 0 10px rgba(255, 0, 0, 0.7),
            0 0 30px rgba(255, 0, 0, 0.4);
        animation: shake 0.4s infinite;
    }}

    .access-message {{
        font-family: 'Cinzel', serif;
        color: #fff;
        font-size: 1.5rem;
        letter-spacing: 3px;
        margin-top: 1rem;
    }}

    @keyframes shake {{
        0% {{ transform: translateX(0); }}
        25% {{ transform: translateX(-4px); }}
        50% {{ transform: translateX(4px); }}
        75% {{ transform: translateX(-4px); }}
        100% {{ transform: translateX(0); }}
    }}

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# QUESTIONS
# ============================================================

QUESTIONS = [

    {
        "question": "What are you most given to do if you have an upcoming test and wifi is down (for a long time)?",

        "options": [
            "you take to the bulletin, cast rightful blame, and delineate how things haven’t been improving, as a quasi-productive way of procrastination",
            "you already have the material downloaded, so it’s not of much consequence to you;",
            "you take the opportunity to sleep. you’ll deal with the test later",
            "you try to fix the wifi yourself because someone has to do something",
            "you start panicking and immediately try every possible solution",
        ],

        "scores": [
            {
                "Katniss": 3,
                "Peeta": 1,
                "Gale": 1,
                "Haymitch": 2,
                "Prim": 0,
                "Finnick": 1,
                "Rue": 1,
                "Snow": 0,
                "Cinna": 1,
                "Johanna": 3,
                "Effie": 2
            },

            {
                "Katniss": 1,
                "Peeta": 2,
                "Gale": 2,
                "Haymitch": 3,
                "Prim": 1,
                "Finnick": 2,
                "Rue": 2,
                "Snow": 1,
                "Cinna": 2,
                "Johanna": 0,
                "Effie": 1
            },

            {
                "Katniss": 0,
                "Peeta": 1,
                "Gale": 0,
                "Haymitch": 3,
                "Prim": 2,
                "Finnick": 2,
                "Rue": 1,
                "Snow": 1,
                "Cinna": 0,
                "Johanna": 2,
                "Effie": 0
            },

            {
                "Katniss": 2,
                "Peeta": 1,
                "Gale": 3,
                "Haymitch": 1,
                "Prim": 1,
                "Finnick": 2,
                "Rue": 1,
                "Snow": 2,
                "Cinna": 2,
                "Johanna": 3,
                "Effie": 1
            },

            {
                "Katniss": 1,
                "Peeta": 2,
                "Gale": 1,
                "Haymitch": 0,
                "Prim": 3,
                "Finnick": 1,
                "Rue": 3,
                "Snow": 1,
                "Cinna": 1,
                "Johanna": 1,
                "Effie": 3
            }
        ]
    },

    {
        "question": "You are thrown into a completely unfamiliar situation. What do you do?",

        "options": [
            "Observe quietly and figure out what is happening before acting.",
            "Try to help whoever seems to need it most.",
            "Take charge and start figuring out a practical solution.",
            "Make a joke and pretend everything is completely fine.",
            "Stay calm, adapt, and work with whatever resources are available."
        ],

        "scores": [
            {
                "Katniss": 3,
                "Peeta": 1,
                "Gale": 2,
                "Haymitch": 2,
                "Prim": 1,
                "Finnick": 2,
                "Rue": 3,
                "Snow": 1,
                "Cinna": 2,
                "Johanna": 2,
                "Effie": 0
            },

            {
                "Katniss": 1,
                "Peeta": 3,
                "Gale": 1,
                "Haymitch": 1,
                "Prim": 3,
                "Finnick": 2,
                "Rue": 3,
                "Snow": 0,
                "Cinna": 2,
                "Johanna": 0,
                "Effie": 1
            },

            {
                "Katniss": 3,
                "Peeta": 2,
                "Gale": 3,
                "Haymitch": 1,
                "Prim": 1,
                "Finnick": 2,
                "Rue": 0,
                "Snow": 2,
                "Cinna": 2,
                "Johanna": 3,
                "Effie": 1
            },

            {
                "Katniss": 1,
                "Peeta": 2,
                "Gale": 1,
                "Haymitch": 3,
                "Prim": 0,
                "Finnick": 3,
                "Rue": 2,
                "Snow": 2,
                "Cinna": 2,
                "Johanna": 3,
                "Effie": 2
            },

            {
                "Katniss": 2,
                "Peeta": 3,
                "Gale": 3,
                "Haymitch": 3,
                "Prim": 2,
                "Finnick": 3,
                "Rue": 2,
                "Snow": 3,
                "Cinna": 3,
                "Johanna": 2,
                "Effie": 2
            }
        ]
    },

    {
        "question": "Someone insults you in front of everyone. How do you respond?",

        "options": [
            "Say nothing. You don't need to prove anything.",
            "Insult them back immediately.",
            "Laugh it off.",
            "Remember it and deal with it later.",
            "Ask them directly why they said it."
        ],

        "scores": [
            {
                "Katniss": 3,
                "Peeta": 2,
                "Gale": 1,
                "Haymitch": 2,
                "Prim": 1,
                "Finnick": 2,
                "Rue": 2,
                "Snow": 2,
                "Cinna": 2,
                "Johanna": 1,
                "Effie": 1
            },

            {
                "Katniss": 2,
                "Peeta": 1,
                "Gale": 3,
                "Haymitch": 2,
                "Prim": 0,
                "Finnick": 2,
                "Rue": 1,
                "Snow": 3,
                "Cinna": 1,
                "Johanna": 3,
                "Effie": 2
            },

            {
                "Katniss": 1,
                "Peeta": 3,
                "Gale": 1,
                "Haymitch": 3,
                "Prim": 1,
                "Finnick": 3,
                "Rue": 2,
                "Snow": 2,
                "Cinna": 2,
                "Johanna": 2,
                "Effie": 3
            },

            {
                "Katniss": 3,
                "Peeta": 1,
                "Gale": 3,
                "Haymitch": 3,
                "Prim": 1,
                "Finnick": 3,
                "Rue": 1,
                "Snow": 3,
                "Cinna": 2,
                "Johanna": 3,
                "Effie": 1
            },

            {
                "Katniss": 2,
                "Peeta": 3,
                "Gale": 2,
                "Haymitch": 1,
                "Prim": 3,
                "Finnick": 1,
                "Rue": 3,
                "Snow": 1,
                "Cinna": 3,
                "Johanna": 1,
                "Effie": 3
            }
        ]
    },

    {
        "question": "You discover that someone you care about is in danger. What is your first instinct?",

        "options": [
            "Go after them immediately, consequences be damned.",
            "Make a careful plan first.",
            "Find someone who can help.",
            "Try to negotiate or talk your way through the situation.",
            "Figure out who caused the problem and make them regret it."
        ],

        "scores": [
            {
                "Katniss": 3,
                "Peeta": 2,
                "Gale": 2,
                "Haymitch": 1,
                "Prim": 3,
                "Finnick": 2,
                "Rue": 3,
                "Snow": 1,
                "Cinna": 2,
                "Johanna": 3,
                "Effie": 1
            },

            {
                "Katniss": 2,
                "Peeta": 3,
                "Gale": 3,
                "Haymitch": 3,
                "Prim": 2,
                "Finnick": 3,
                "Rue": 1,
                "Snow": 3,
                "Cinna": 3,
                "Johanna": 2,
                "Effie": 2
            },

            {
                "Katniss": 2,
                "Peeta": 3,
                "Gale": 2,
                "Haymitch": 3,
                "Prim": 3,
                "Finnick": 2,
                "Rue": 2,
                "Snow": 1,
                "Cinna": 2,
                "Johanna": 1,
                "Effie": 3
            },

            {
                "Katniss": 1,
                "Peeta": 3,
                "Gale": 1,
                "Haymitch": 3,
                "Prim": 2,
                "Finnick": 3,
                "Rue": 3,
                "Snow": 3,
                "Cinna": 3,
                "Johanna": 2,
                "Effie": 3
            },

            {
                "Katniss": 3,
                "Peeta": 0,
                "Gale": 3,
                "Haymitch": 2,
                "Prim": 1,
                "Finnick": 2,
                "Rue": 1,
                "Snow": 3,
                "Cinna": 1,
                "Johanna": 3,
                "Effie": 1
            }
        ]
    },

    {
        "question": "What matters most to you?",

        "options": [
            "Protecting the people I love.",
            "Being a good person even when it is difficult.",
            "Freedom and independence.",
            "Power and control.",
            "Making the world more beautiful."
        ],

        "scores": [
            {
                "Katniss": 3,
                "Peeta": 2,
                "Gale": 3,
                "Haymitch": 1,
                "Prim": 3,
                "Finnick": 2,
                "Rue": 3,
                "Snow": 1,
                "Cinna": 2,
                "Johanna": 2,
                "Effie": 1
            },

            {
                "Katniss": 2,
                "Peeta": 3,
                "Gale": 1,
                "Haymitch": 2,
                "Prim": 3,
                "Finnick": 2,
                "Rue": 3,
                "Snow": 0,
                "Cinna": 3,
                "Johanna": 1,
                "Effie": 2
            },

            {
                "Katniss": 3,
                "Peeta": 1,
                "Gale": 3,
                "Haymitch": 2,
                "Prim": 1,
                "Finnick": 2,
                "Rue": 2,
                "Snow": 1,
                "Cinna": 2,
                "Johanna": 3,
                "Effie": 1
            },

            {
                "Katniss": 0,
                "Peeta": 0,
                "Gale": 1,
                "Haymitch": 2,
                "Prim": 0,
                "Finnick": 2,
                "Rue": 0,
                "Snow": 3,
                "Cinna": 1,
                "Johanna": 1,
                "Effie": 2
            },

            {
                "Katniss": 1,
                "Peeta": 3,
                "Gale": 0,
                "Haymitch": 1,
                "Prim": 2,
                "Finnick": 2,
                "Rue": 3,
                "Snow": 0,
                "Cinna": 3,
                "Johanna": 1,
                "Effie": 3
            }
        ]
    }
]


# ============================================================
# CHARACTERS
# ============================================================

CHARACTERS = [
    "Katniss",
    "Peeta",
    "Gale",
    "Haymitch",
    "Prim",
    "Finnick",
    "Rue",
    "Snow",
    "Cinna",
    "Johanna",
    "Effie"
]


# ============================================================
# DETERMINE CHARACTER
# ============================================================

def determine_character():

    scores = Counter()

    for question_index, answer_index in enumerate(st.session_state.answers):

        answer_score = QUESTIONS[question_index]["scores"][answer_index]

        for character, score in answer_score.items():
            scores[character] += score

    max_score = max(scores.values())

    winners = [
        character
        for character, score in scores.items()
        if score == max_score
    ]

    result = random.choice(winners)

    return result, scores


# ============================================================
# ACCESS DENIED
# ============================================================

def show_access_denied():

    st.markdown(
        f"""
        <div class="access-denied">

            <div class="access-title">
                ACCESS DENIED
            </div>

            <div class="access-message">
                you cannot play as me
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button("RE-ENTER THE ARENA"):

        st.session_state.access_denied = False
        st.session_state.page = 0
        st.session_state.answers = []
        st.session_state.finished = False
        st.session_state.result = None
        st.session_state.scores = None
        st.session_state.name = ""
        st.session_state.name_submitted = False

        st.rerun()


# ============================================================
# NAME SCREEN
# ============================================================

def show_name_screen():

    st.markdown(
        """
        <div class="name-container">

            <div class="name-title">
                ENTER YOUR NAME
            </div>

            <div class="name-subtitle">
                THE CAPITOL IS WATCHING
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    entered_name = st.text_input(
        "Name",
        value=st.session_state.name,
        label_visibility="collapsed",
        placeholder="Enter your name..."
    )

    if st.button("ENTER THE ARENA"):

        entered_name = entered_name.strip()

        if not entered_name:
            st.error("Please enter your name.")
            st.stop()

        if "trinav" in entered_name.lower():

            st.session_state.access_denied = True
            st.rerun()

        character_names = {
            character.lower()
            for character in CHARACTERS
        }

        if entered_name.lower() in character_names:

            st.error(
                "you think you can choose your own fate?"
            )
            st.stop()

        st.session_state.name = entered_name
        st.session_state.name_submitted = True
        st.session_state.page = 0

        st.rerun()


# ============================================================
# RESULT SCREEN
# ============================================================

def show_result():

    character = st.session_state.result
    scores = st.session_state.scores

    st.markdown(
        """
        <div class="result-container">

            <div class="fire-symbol">
                🔥
            </div>

            <div class="result-small">
                THE REAPING IS COMPLETE
            </div>

            <div class="result-title">
                YOUR CHARACTER
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    # FIX:
    # Use st.html() instead of st.markdown() so Streamlit
    # does not interpret the HTML as Markdown/text.

    st.html(
        f"""
        <div class="result-card">

            <div style="
                font-family: 'Cinzel', serif;
                font-size: 1rem;
                color: #999;
                letter-spacing: 4px;
                text-transform: uppercase;
            ">
                THE CAPITOL HAS SPOKEN
            </div>

            <div style="
                font-family: 'Cinzel', serif;
                font-size: 3.5rem;
                font-weight: 800;
                color: #e6b84a;
                margin: 1rem 0;
                letter-spacing: 3px;
            ">
                {character.upper()}
            </div>

            <div class="result-score">
                Final score: {scores[character]}
            </div>

        </div>
        """
    )

    with st.expander("View your scores"):

        sorted_scores = sorted(
            scores.items(),
            key=lambda x: x[1],
            reverse=True
        )

        for char, score in sorted_scores:
            st.write(f"**{char}** — {score}")

    st.markdown(
        "<br>",
        unsafe_allow_html=True
    )

    if st.button("RE-ENTER THE ARENA"):

        st.session_state.page = 0
        st.session_state.answers = []
        st.session_state.finished = False
        st.session_state.result = None
        st.session_state.scores = None
        st.session_state.name = ""
        st.session_state.name_submitted = False

        st.rerun()


# ============================================================
# MAIN ROUTING
# ============================================================

if st.session_state.access_denied:

    show_access_denied()
    st.stop()


if not st.session_state.name_submitted:

    show_name_screen()
    st.stop()


if st.session_state.finished:

    show_result()
    st.stop()


# ============================================================
# QUIZ HEADER
# ============================================================

st.markdown(
    """
    <div class="main-title">
        WHO IS YOUR HUNGER GAMES CHARACTER?
    </div>

    <div class="subtitle">
        MAY THE ODDS BE EVER IN YOUR FAVOR
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# CURRENT QUESTION
# ============================================================

question_index = st.session_state.page

question = QUESTIONS[question_index]

progress = (
    question_index / len(QUESTIONS)
) * 100

st.markdown(
    f"""
    <div class="progress-container">
        <div
            class="progress-bar"
            style="width: {progress}%;">
        </div>
    </div>
    """,
    unsafe_allow_html=True
)


st.markdown(
    f"""
    <div class="question-number">
        QUESTION {question_index + 1} OF {len(QUESTIONS)}
    </div>

    <div class="question-text">
        {question["question"]}
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# ANSWERS
# ============================================================

for answer_index, option in enumerate(question["options"]):

    if st.button(
        option,
        key=f"question_{question_index}_answer_{answer_index}"
    ):

        st.session_state.answers.append(answer_index)

        if question_index + 1 >= len(QUESTIONS):

            result, scores = determine_character()

            st.session_state.result = result
            st.session_state.scores = scores
            st.session_state.finished = True

        else:

            st.session_state.page += 1

        st.rerun()
