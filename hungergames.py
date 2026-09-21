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
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ============================================================
# IMAGE HELPER
# ============================================================

def get_base64_image(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return ""


gaster_base64 = get_base64_image("gasterbg.jfif")
chewie_base64 = get_base64_image("chewie.jpeg")
tf_base64 = get_base64_image("tf.gif")
sansback_base64 = get_base64_image("sansback.jpeg")


# ============================================================
# CSS
# ============================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;500;600;700;800&family=Libre+Baskerville:wght@400;700&display=swap');

.stApp {
    background:
        radial-gradient(circle at center, rgba(70,20,20,0.18), transparent 50%),
        linear-gradient(135deg, #090909 0%, #161616 50%, #080808 100%);
    color: #e6e6e6;
}

.block-container {
    max-width: 1050px !important;
    padding-top: 3rem !important;
    padding-bottom: 3rem !important;
}

.shake-screen {
    animation: shake 0.15s infinite;
}

@keyframes shake {
    0% { transform: translate(0px, 0px); }
    25% { transform: translate(2px, -2px); }
    50% { transform: translate(-2px, 2px); }
    75% { transform: translate(2px, 2px); }
    100% { transform: translate(-2px, -2px); }
}

.spinning-chewie {
    width: 260px;
    height: 260px;
    object-fit: contain;
    animation: spin 3s linear infinite;
}

@keyframes spin {
    from { transform: rotate(0deg); }
    to { transform: rotate(360deg); }
}

.tf-gif {
    width: 260px;
    height: 260px;
    object-fit: contain;
}

.hg-title {
    font-family: 'Cinzel', serif;
    font-size: 3.2rem;
    font-weight: 800;
    text-align: center;
    color: #c52c2c;
    letter-spacing: 5px;
    text-shadow:
        0 0 10px rgba(197,44,44,0.5),
        0 0 30px rgba(197,44,44,0.2);
    margin-bottom: 0.5rem;
}

.hg-subtitle {
    font-family: 'Cinzel', serif;
    text-align: center;
    color: #d6aa4a;
    font-size: 1rem;
    letter-spacing: 6px;
    margin-bottom: 1.5rem;
}

.divider {
    width: 70%;
    height: 1px;
    background: linear-gradient(
        90deg,
        transparent,
        #c52c2c,
        transparent
    );
    margin: 0 auto 3rem auto;
}

.question-number {
    font-family: 'Cinzel', serif;
    color: #d6aa4a;
    font-size: 0.9rem;
    letter-spacing: 4px;
    text-align: center;
    margin-bottom: 1rem;
}

.question-text {
    font-family: 'Libre Baskerville', serif;
    font-size: 1.45rem;
    line-height: 1.65;
    text-align: center;
    color: #eeeeee;
    margin: 0 auto 2rem auto;
    max-width: 900px;
}

.progress-label {
    text-align: center;
    color: #777;
    font-family: 'Cinzel', serif;
    font-size: 0.75rem;
    letter-spacing: 2px;
    margin-bottom: 0.5rem;
}

.progress-container {
    width: 100%;
    height: 5px;
    background: #292929;
    border-radius: 5px;
    overflow: hidden;
    margin-bottom: 3rem;
}

.progress-bar {
    height: 100%;
    background: linear-gradient(90deg, #8d1717, #d6aa4a);
    transition: width 0.4s ease;
}

div[data-testid="stRadio"] > div {
    gap: 0.7rem;
}

div[data-testid="stRadio"] label {
    background: rgba(30,30,30,0.85);
    border: 1px solid #393939;
    border-radius: 4px;
    padding: 1rem 1.2rem;
    transition: all 0.2s ease;
}

div[data-testid="stRadio"] label:hover {
    border-color: #a83232;
    background: rgba(55,25,25,0.9);
}

div[data-testid="stRadio"] label p {
    font-family: 'Libre Baskerville', serif;
    color: #ddd;
    line-height: 1.5;
}

.stButton > button {
    width: 100%;
    border: 1px solid #8d2424;
    background: linear-gradient(135deg, #641818, #351010);
    color: #e6b84a;
    font-family: 'Cinzel', serif;
    font-weight: 700;
    letter-spacing: 2px;
    padding: 0.8rem 1rem;
    border-radius: 3px;
    transition: all 0.2s ease;
}

.stButton > button:hover {
    border-color: #d6aa4a;
    color: #fff0bd;
    box-shadow: 0 0 20px rgba(197,44,44,0.25);
    transform: translateY(-1px);
}

.name-container {
    text-align: center;
    margin-top: 8rem;
    margin-bottom: 2rem;
}

.name-title {
    font-family: 'Cinzel', serif;
    color: #c52c2c;
    font-size: 2.5rem;
    font-weight: 800;
    letter-spacing: 5px;
}

.name-subtitle {
    color: #aaa;
    font-family: 'Libre Baskerville', serif;
    font-size: 0.95rem;
    margin-top: 1rem;
}

.name-container + div {
    max-width: 500px;
    margin: auto;
}

.result-container {
    text-align: center;
    margin-top: 5rem;
}

.fire-symbol {
    font-size: 4rem;
    margin-bottom: 1rem;
}

.result-small {
    color: #d6aa4a;
    font-family: 'Cinzel', serif;
    font-size: 0.9rem;
    letter-spacing: 4px;
}

.result-title {
    color: #c52c2c;
    font-family: 'Cinzel', serif;
    font-size: 3rem;
    font-weight: 800;
    letter-spacing: 6px;
    margin-top: 0.5rem;
}

.result-card {
    max-width: 700px;
    margin: 3rem auto;
    padding: 3rem;
    text-align: center;
    background:
        linear-gradient(
            rgba(25,25,25,0.95),
            rgba(12,12,12,0.95)
        );
    border: 1px solid #6e2727;
    box-shadow:
        0 0 40px rgba(0,0,0,0.6),
        inset 0 0 30px rgba(120,20,20,0.08);
}

.result-capitol {
    font-family: 'Cinzel', serif;
    color: #888;
    letter-spacing: 3px;
    font-size: 0.8rem;
}

.result-name {
    font-family: 'Cinzel', serif;
    color: #d6aa4a;
    font-size: 4rem;
    font-weight: 800;
    letter-spacing: 6px;
    margin: 1rem 0;
}

.result-score {
    color: #aaa;
    font-family: 'Libre Baskerville', serif;
}

.pct-container {
    margin-top: 1.5rem;
}

.pct-row {
    display: grid;
    grid-template-columns: 110px 1fr 70px;
    align-items: center;
    gap: 10px;
    margin: 0.7rem 0;
}

.pct-label {
    font-family: 'Cinzel', serif;
    color: #ddd;
    font-size: 0.8rem;
}

.pct-bar-bg {
    height: 12px;
    background: #292929;
    border-radius: 10px;
    overflow: hidden;
}

.pct-bar-fill {
    height: 100%;
    background: linear-gradient(90deg, #731b1b, #d6aa4a);
}

.pct-value {
    text-align: right;
    color: #aaa;
    font-family: 'Cinzel', serif;
    font-size: 0.75rem;
}

.restart-btn {
    opacity: 0.7;
}

.restart-btn .stButton > button {
    background: transparent;
    border-color: #444;
    color: #777;
    font-size: 0.75rem;
    letter-spacing: 1px;
}

.restart-btn .stButton > button:hover {
    color: #c52c2c;
    border-color: #7d2424;
    box-shadow: none;
}

.hg-footer {
    text-align: center;
    color: #444;
    font-family: 'Cinzel', serif;
    font-size: 0.65rem;
    letter-spacing: 3px;
    margin-top: 4rem;
    padding-bottom: 1rem;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# CHARACTERS
# ============================================================

CHARACTERS = [
    "Katniss", "Peeta", "Gale", "Haymitch", "Prim", "Finnick",
    "Rue", "Snow", "Cinna", "Johanna", "Effie",
    "Plutarch", "Foxface", "Beetee"
]


# ============================================================
# QUESTIONS
# ============================================================

BASE_QUESTIONS = [

    {
        "question": "What are you most given to do if you have an upcoming test and wifi is down (for a long time)?",
        "options": [
            "You take to the bulletin, cast rightful blame, and delineate how things haven’t been improving, as a quasi-productive way of procrastination",
            "You already have the material downloaded, so it’s not of much consequence to you; you quietly get on while the rest scramble",
            "You switch to mobile data and take a hedonistic deepdive into your internet recesses of choice till the wifi comes back on (and then procrastinate for “10 more minutes” after it comes back on)",
            "You actively send your downloaded material on your class WhatsApp groups in this time of need, and prioritise sorting out people’s pre-test queries over locking in yourself",
            "You sneakily sit on your downloaded material because you believe in taking all the advantages life hands you"
        ],
        "scores": {
            "Katniss": [1,3,0,1,-1],
            "Peeta": [0,1,0,3,-2],
            "Gale": [3,1,0,1,2],
            "Haymitch": [2,2,3,0,1],
            "Prim": [0,2,0,3,-2],
            "Finnick": [0,1,3,2,1],
            "Rue": [1,3,1,2,-1],
            "Snow": [1,1,0,-1,3],
            "Cinna": [0,2,0,2,-1],
            "Johanna": [2,0,1,0,2],
            "Effie": [1,3,-1,1,1],
            "Plutarch": [0,0,0,0,0],
            "Foxface": [0,0,0,0,0],
            "Beetee": [0,0,0,0,0]
        }
    },

    {
        "question": "You have your D&I major project on your hands — what kind of teammate do you think you will be?",
        "options": [
            "The one who attempts to do just as much as is required to be considered an ‘active contributor’ and save their score in the peer-grading",
            "The one who considers themselves inexperienced and unskilled, but is there to learn and constructively contribute, and is unabashed about it",
            "The one who somewhat does care about his grade, and his skillset, but just cannot be arsed",
            "The one who quietly works on an important chunk of the project independently instead of being the supervisor or coordinator",
            "The one who inevitably ends up organizing the group, dividing the work, setting deadlines, and chasing people",
            "The “you don't sell the steak, you sell the sizzle” guy — you come up with the interesting angle, make the presentation compelling, and are the voice of the group"
        ],
        "scores": {
            "Katniss": [1,1,0,3,1,0],
            "Peeta": [-1,3,0,1,1,3],
            "Gale": [1,1,0,2,3,2],
            "Haymitch": [3,0,3,1,1,1],
            "Prim": [-1,3,0,1,1,2],
            "Finnick": [1,1,2,0,1,3],
            "Rue": [1,3,1,2,1,1],
            "Snow": [3,-1,1,1,3,2],
            "Cinna": [0,2,0,3,1,3],
            "Johanna": [3,0,2,2,1,1],
            "Effie": [1,1,-1,0,3,2],
            "Plutarch": [0,0,0,0,0,0],
            "Foxface": [0,0,0,0,0,0],
            "Beetee": [0,0,0,0,0,0]
        }
    },

    {
        "question": "You’re a sophomore, and the incoming batch has arrived. What kind of a senior are you to the new freshmen?",
        "options": [
            "You’re pretty ambivalent about the whole “senior” thing — you’ll talk to them if the situation calls for it, but you won’t particularly seek them out or feel the need to establish yourself as a senior",
            "You can’t wait to become a mentor or older-sibling-figure to them, and want to speak to as many as possible",
            "You are somewhat looking forward to interacting with them, and would potentially like to be close to a few juniors who strike you as kindred",
            "You want to be the cool senior that all the juniors know the name of, and admire from a distance",
            "You’d like to be the cool senior too, but not at the cost of deep connection and proximity with the juniors"
        ],
        "scores": {
            "Katniss": [3,1,2,-1,1],
            "Peeta": [0,3,3,-1,1],
            "Gale": [2,1,2,1,3],
            "Haymitch": [3,-1,1,0,-1],
            "Prim": [1,3,3,-1,1],
            "Finnick": [0,2,2,3,3],
            "Rue": [2,2,3,-1,1],
            "Snow": [1,-1,0,3,2],
            "Cinna": [2,1,2,1,3],
            "Johanna": [3,-1,1,2,0],
            "Effie": [0,2,1,3,2],
            "Plutarch": [0,0,0,0,0],
            "Foxface": [0,0,0,0,0],
            "Beetee": [0,0,0,0,0]
        }
    },

    {
        "question": "It’s peak lunch hour in the mess, and you run into that senior who rejected you from their club, the ilgc teammate you’ve had a spat with, your ex-situationship, and your week 1 ‘friend’ you don’t talk to anymore, because Plaksha is the smallest godforsaken place on Earth; what do you do next?",
        "options": [
            "You acknowledge everyone politely, act like nothing happened, and proceed with your lunch — you’re a chill dude",
            "You make a banger joke about the sheer absurdity of all four of them being here at the same time, successfully break the tension for a second, and then have no idea what to do next",
            "You assess the situation and talk to anyone if they’re worth engaging with — you don’t believe in severing ties for trifling reasons",
            "You make no effort to hide the instinctual eyeroll, and sit on an empty seat confidently even if it’s close to them",
            "You desert the social minefield immediately to go to Tonnies or skip lunch entirely",
            "You try to break the ice with someone as you find it uncomfortable or unnecessary to awkwardly orbit a person you have interacted with in the past"
        ],
        "scores": {
            "Katniss": [3,1,2,3,1,1],
            "Peeta": [2,3,2,0,-1,3],
            "Gale": [2,1,3,2,0,1],
            "Haymitch": [3,3,2,1,2,-1],
            "Prim": [3,1,2,0,-1,3],
            "Finnick": [3,3,2,2,1,3],
            "Rue": [3,1,2,1,2,1],
            "Snow": [3,1,3,2,0,1],
            "Cinna": [3,2,2,1,1,3],
            "Johanna": [1,3,2,3,2,1],
            "Effie": [3,1,3,1,1,2],
            "Plutarch": [0,0,0,0,0,0],
            "Foxface": [0,0,0,0,0,0],
            "Beetee": [0,0,0,0,0,0]
        }
    },

    {
        "question": "What has been your personal strategy to grapple with the recent Plaksha mess scandals?",
        "options": [
            "You’re a careful consumer who sifts through the food before eating it, but you cannot be arsed to find alternative sources of food 3 times a day",
            "You’re also one of the mess regulars, but you don’t really think much about what could go wrong and are about that devil-may-care life",
            "You order out quite often (not really because of safety concerns, but because concerned parents send you extra money for food, which you gladly accept)",
            "You take to bulletin with evidence as a truly concerned member of the university, with sincere hopes that someone will bring about change",
            "You actively suggest potential solutions and contact relevant authority members / student activists to catalyse change firsthand"
        ],
        "scores": {
            "Katniss": [3,1,1,2,3],
            "Peeta": [2,0,1,3,2],
            "Gale": [1,0,1,3,3],
            "Haymitch": [2,3,2,1,1],
            "Prim": [3,-1,1,3,2],
            "Finnick": [1,2,3,1,2],
            "Rue": [3,1,1,2,2],
            "Snow": [2,1,3,2,3],
            "Cinna": [1,0,1,3,3],
            "Johanna": [1,2,1,3,2],
            "Effie": [2,-1,2,3,2],
            "Plutarch": [0,0,0,0,0],
            "Foxface": [0,0,0,0,0],
            "Beetee": [0,0,0,0,0]
        }
    },

    {
        "question": "You discover your alliance has been stealing your food. What do you do?",
        "options": [
            "Confront them immediately.",
            "Say nothing. Now you know who not to trust.",
            "Replace the food with something they'll regret eating.",
            "Ask them why they did it before deciding what to do.",
            "Pretend you haven't noticed and feed them false information.",
            "Honestly? Impressive. You join them."
        ],
        "scores": {
            "Katniss": [1,3,0,0,0,0],
            "Peeta": [0,0,0,3,0,0],
            "Gale": [0,0,0,0,0,0],
            "Haymitch": [0,0,3,0,0,2],
            "Prim": [0,0,0,0,0,0],
            "Finnick": [0,0,0,1,0,2],
            "Rue": [0,0,0,0,0,0],
            "Snow": [0,0,0,0,0,0],
            "Cinna": [0,0,0,0,0,0],
            "Johanna": [3,0,2,0,0,0],
            "Effie": [0,0,0,0,0,0],
            "Plutarch": [0,0,0,0,3,0],
            "Foxface": [0,2,0,0,3,0],
            "Beetee": [0,0,0,0,0,0]
        }
    },

    {
        "question": "You're on the Capitol train and dinner arrives. There are approximately 47 dishes in front of you. You have no idea what half of them are.",
        "options": [
            "Try everything. You may never get food like this again.",
            "Take the things that look like they'll actually be useful later.",
            "Spend the entire meal trying to figure out which dishes are ridiculously expensive.",
            "Don't touch anything until you've established whether it's safe.",
            "“Finally. A civilisation with standards.”"
        ],
        "scores": {
            "Katniss": [0,3,0,0,0],
            "Peeta": [3,0,0,0,0],
            "Gale": [0,0,0,0,0],
            "Haymitch": [0,2,2,0,0],
            "Prim": [0,0,0,0,0],
            "Finnick": [0,0,0,0,1],
            "Rue": [0,0,0,0,0],
            "Snow": [0,0,0,0,0],
            "Cinna": [0,0,0,0,0],
            "Johanna": [0,0,0,0,0],
            "Effie": [1,0,0,0,3],
            "Plutarch": [0,0,2,0,0],
            "Foxface": [0,0,0,3,0],
            "Beetee": [0,0,0,1,0]
        }
    },

    {
        "question": "You're given 30 seconds at the Cornucopia. What's taking?",
        "options": [
            "A weapon.",
            "Medicine.",
            "Food and water.",
            "Something nobody else seems interested in.",
            "Whatever looks most expensive.",
            "Whatever I can dismantle into something more useful."
        ],
        "scores": {
            "Katniss": [3,2,1,0,0,0],
            "Peeta": [0,2,0,0,0,0],
            "Gale": [0,0,0,0,0,0],
            "Haymitch": [0,0,3,0,0,1],
            "Prim": [0,0,0,0,0,0],
            "Finnick": [0,0,0,0,1,0],
            "Rue": [0,0,0,0,0,0],
            "Snow": [0,0,0,0,0,0],
            "Cinna": [0,0,0,0,0,0],
            "Johanna": [1,0,0,0,0,0],
            "Effie": [0,0,0,0,3,0],
            "Plutarch": [0,0,0,1,0,0],
            "Foxface": [0,0,0,3,0,0],
            "Beetee": [0,0,0,0,0,3]
        }
    },

    {
        "question": "You have one hour to prepare for the arena. What are you doing?",
        "options": [
            "Learning the layout.",
            "Practising with your weapon.",
            "Figuring out who is likely to form alliances.",
            "Finding out what the audience likes about you.",
            "Looking for weaknesses in the arena itself.",
            "Taking a nap."
        ],
        "scores": {
            "Katniss": [0,3,0,0,0,0],
            "Peeta": [0,0,0,3,0,0],
            "Gale": [0,0,0,0,0,0],
            "Haymitch": [0,0,0,0,0,3],
            "Prim": [0,0,0,0,0,0],
            "Finnick": [0,0,3,2,0,0],
            "Rue": [0,0,0,0,0,0],
            "Snow": [0,0,0,0,0,0],
            "Cinna": [0,0,0,0,0,0],
            "Johanna": [0,2,0,0,0,1],
            "Effie": [0,0,0,0,0,0],
            "Plutarch": [2,0,2,0,0,0],
            "Foxface": [0,0,0,0,2,0],
            "Beetee": [3,0,0,0,3,0]
        }
    }
]


# ============================================================
# SESSION STATE
# ============================================================

if "page" not in st.session_state:
    st.session_state.page = 0

if "answers" not in st.session_state:
    st.session_state.answers = []

if "finished" not in st.session_state:
    st.session_state.finished = False

if "access_denied" not in st.session_state:
    st.session_state.access_denied = False

if "chewie_mode" not in st.session_state:
    st.session_state.chewie_mode = False

if "result" not in st.session_state:
    st.session_state.result = None

if "scores" not in st.session_state:
    st.session_state.scores = None

if "name" not in st.session_state:
    st.session_state.name = ""

if "name_submitted" not in st.session_state:
    st.session_state.name_submitted = False

if "haunted" not in st.session_state:
    st.session_state.haunted = False

if "shuffled_questions" not in st.session_state:
    st.session_state.shuffled_questions = random.sample(
        BASE_QUESTIONS,
        len(BASE_QUESTIONS)
    )

QUESTIONS = st.session_state.shuffled_questions


# ============================================================
# HAUNTED MODE BACKGROUND
# ============================================================

if st.session_state.haunted and sansback_base64:
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-color: #000000 !important;
            background-image:
                linear-gradient(
                    rgba(0,0,0,0.72),
                    rgba(0,0,0,0.78)
                ),
                url("data:image/jpeg;base64,{sansback_base64}") !important;
            background-size: 85% auto !important;
            background-position: center center !important;
            background-repeat: no-repeat !important;
            background-attachment: fixed !important;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# HEADER
# ============================================================

if not st.session_state.haunted:
    st.markdown(
        '<div class="hg-title">WHO IS YOUR HUNGER GAMES CHARACTER?</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="hg-subtitle">MAY THE ODDS BE EVER IN YOUR FAVOUR</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="divider"></div>',
        unsafe_allow_html=True
    )


# ============================================================
# SCORING
# ============================================================

def calculate_scores(answers):
    scores = Counter()

    for q_index, answer_index in enumerate(answers):
        question = QUESTIONS[q_index]

        for character in CHARACTERS:
            scores[character] += question["scores"][character][answer_index]

    return scores


def determine_character(scores):
    if not scores:
        return None, []

    highest = max(scores.values())

    tied = [
        character
        for character, score in scores.items()
        if score == highest
    ]

    if len(tied) == 1:
        return tied[0], tied

    return random.choice(tied), tied


# ============================================================
# ACCESS DENIED
# ============================================================

def show_access_denied():

    st.markdown(
        f"""
        <style>
        .stApp {{
            background:
                linear-gradient(
                    rgba(0,0,0,0.7),
                    rgba(0,0,0,0.7)
                ),
                url("data:image/jfif;base64,{gaster_base64}") !important;
            background-size: cover !important;
            background-position: center !important;
            background-repeat: no-repeat !important;
        }}
        </style>

        <div
            class="shake-screen"
            style="
                display:flex;
                flex-direction:column;
                align-items:center;
                justify-content:center;
                height:60vh;
                text-align:center;
            "
        >

            <div style="
                font-size:5rem;
                margin-bottom:1rem;
            ">
                ⚠️
            </div>

            <div style="
                font-family:'Cinzel',serif;
                color:#c52c2c;
                font-size:2.5rem;
                font-weight:800;
                letter-spacing:4px;
                margin-bottom:1rem;
            ">
                ACCESS DENIED
            </div>

            <div style="
                font-family:'Cinzel',serif;
                color:#e6b84a;
                font-size:1.4rem;
                letter-spacing:2px;
                margin-bottom:2rem;
            ">
                you cannot play as me
            </div>

            <div style="
                color:#bbb;
                font-size:0.9rem;
                letter-spacing:1px;
                text-transform:uppercase;
            ">
                The Capitol rejects this intrusion.
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:

        if st.button("RETURN TO REAPING"):

            st.session_state.access_denied = False
            st.session_state.name = ""
            st.session_state.name_submitted = False

            st.rerun()


# ============================================================
# CHEWIE MODE
# ============================================================

def show_chewie():

    st.markdown(
        f"""
        <style>

        .stApp {{
            background: #000000 !important;
        }}

        .block-container {{
            max-width: 100% !important;
            padding-top: 0 !important;
        }}

        </style>

        <div style="
            display:flex;
            flex-direction:column;
            align-items:center;
            justify-content:center;
            height:85vh;
            gap:2.5rem;
        ">

            <div style="
                display:flex;
                align-items:center;
                justify-content:center;
                gap:4rem;
                flex-wrap:wrap;
            ">

                <img
                    src="data:image/jpeg;base64,{chewie_base64}"
                    class="spinning-chewie"
                    alt="Chewie"
                >

                <img
                    src="data:image/gif;base64,{tf_base64}"
                    class="tf-gif"
                    alt="TF"
                >

            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:

        if st.button("RETURN TO REAPING"):

            st.session_state.chewie_mode = False
            st.session_state.name = ""
            st.session_state.name_submitted = False

            st.rerun()


# ============================================================
# RESULT
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

    st.markdown(
        f"""
        <div class="result-card">

            <div class="result-capitol">
                THE CAPITOL HAS SPOKEN
            </div>

            <div class="result-name">
                {character.upper()}
            </div>

            <div class="result-score">
                Final score: {scores[character]}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    with st.expander("VIEW ALIGNMENT"):

        score_dict = dict(scores)

        min_s = (
            min(score_dict.values())
            if score_dict
            else 0
        )

        shifted = {
            key: value - min_s
            for key, value in score_dict.items()
        }

        total = sum(shifted.values()) or 1

        ranked = sorted(
            shifted.items(),
            key=lambda x: x[1],
            reverse=True
        )

        rows = []

        for char, val in ranked:

            pct = (val / total) * 100

            if pct < 1.0:
                continue

            row = (
                f'<div class="pct-row">'
                f'<div class="pct-label">{char}</div>'
                f'<div class="pct-bar-bg">'
                f'<div class="pct-bar-fill" '
                f'style="width:{pct:.1f}%;"></div>'
                f'</div>'
                f'<div class="pct-value">{pct:.1f}%</div>'
                f'</div>'
            )

            rows.append(row)

        bars_html = (
            '<div class="pct-container">'
            + "".join(rows)
            + '</div>'
        )

        st.markdown(
            bars_html,
            unsafe_allow_html=True
        )

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("RE-ENTER THE ARENA"):

        st.session_state.page = 0
        st.session_state.answers = []
        st.session_state.finished = False
        st.session_state.result = None
        st.session_state.scores = None
        st.session_state.name = ""
        st.session_state.name_submitted = False

        # Haunted mode intentionally remains active.
        st.rerun()


# ============================================================
# ROUTING
# ============================================================

if st.session_state.access_denied:

    show_access_denied()
    st.stop()


if st.session_state.chewie_mode:

    show_chewie()
    st.stop()


if st.session_state.finished:

    show_result()
    st.stop()


# ============================================================
# NAME SCREEN
#
# IMPORTANT:
# Haunted mode skips ONLY this screen.
# It does NOT stop the rest of the application.
# ============================================================

if (
    not st.session_state.name_submitted
    and not st.session_state.haunted
):

    st.markdown(
        """
        <div class="name-container">

            <div class="name-title">
                STATE YOUR NAME
            </div>

            <div class="name-subtitle">
                Before you enter the arena, the Capitol requires your identity.
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    name = st.text_input(
        "Your name",
        key="name_input",
        placeholder="Enter your name...",
        label_visibility="collapsed"
    )

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("ENTER THE ARENA"):

        entered_name = name.strip()

        if not entered_name:

            st.error(
                "You must state your name before entering the arena."
            )

            st.stop()

        if "trinav" in entered_name.lower():

            st.session_state.access_denied = True
            st.rerun()

        if "chewie" in entered_name.lower():

            st.session_state.chewie_mode = True
            st.rerun()

        if entered_name.lower() in {
            character.lower()
            for character in CHARACTERS
        }:

            st.error(
                "you think you can choose your own fate?"
            )

            st.stop()

        st.session_state.name = entered_name
        st.session_state.name_submitted = True

        st.rerun()

    st.stop()


# ============================================================
# QUESTION
# ============================================================

q_index = st.session_state.page

question = QUESTIONS[q_index]

total_questions = len(QUESTIONS)


st.markdown(
    f"""
    <div class="progress-label">
        Question {q_index + 1} of {total_questions}
    </div>
    """,
    unsafe_allow_html=True
)


progress = (
    (q_index + 1)
    / total_questions
)


st.markdown(
    f"""
    <div class="progress-container">

        <div
            class="progress-bar"
            style="width:{progress * 100}%"
        ></div>

    </div>
    """,
    unsafe_allow_html=True
)


st.markdown(
    f"""
    <div class="question-number">
        THE ARENA · QUESTION {q_index + 1}
    </div>
    """,
    unsafe_allow_html=True
)


st.markdown(
    f"""
    <div class="question-text">
        {question["question"]}
    </div>
    """,
    unsafe_allow_html=True
)


option_labels = [
    f"{chr(65 + i)}. {option}"
    for i, option in enumerate(question["options"])
]


selected = st.radio(
    "Choose your answer:",
    option_labels,
    index=None,
    key=f"question_{q_index}",
    label_visibility="collapsed"
)


st.markdown("<br>", unsafe_allow_html=True)


if selected is not None:

    selected_index = option_labels.index(selected)

    if q_index < total_questions - 1:

        if st.button("CONTINUE →"):

            st.session_state.answers.append(
                selected_index
            )

            st.session_state.page += 1

            st.rerun()

    else:

        if st.button("ENTER THE REAPING"):

            st.session_state.answers.append(
                selected_index
            )

            scores = calculate_scores(
                st.session_state.answers
            )

            character, _ = determine_character(
                scores
            )

            st.session_state.scores = scores
            st.session_state.result = character
            st.session_state.finished = True

            st.rerun()

else:

    st.markdown(
        """
        <div style="
            text-align:center;
            color:#666;
            font-size:0.8rem;
            letter-spacing:1px;
            margin-top:0.5rem;
        ">
            SELECT AN OPTION TO CONTINUE
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# RESTART BUTTON
# ============================================================

st.markdown("<br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])

with col2:

    st.markdown(
        '<div class="restart-btn">',
        unsafe_allow_html=True
    )

    if st.button(
        "Had a change of heart? Restart Quiz"
    ):

        st.session_state.page = 0
        st.session_state.answers = []
        st.session_state.finished = False
        st.session_state.result = None
        st.session_state.scores = None
        st.session_state.name = ""
        st.session_state.name_submitted = False

        # ====================================================
        # HAUNTED MODE ACTIVATION
        # ====================================================

        st.session_state.haunted = True

        # Reshuffle the questions on restart
        st.session_state.shuffled_questions = random.sample(
            BASE_QUESTIONS,
            len(BASE_QUESTIONS)
        )

        st.rerun()

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="hg-footer">
        PANEM · THE CAPITOL · MAY THE ODDS BE EVER IN YOUR FAVOUR
    </div>
    """,
    unsafe_allow_html=True
)
