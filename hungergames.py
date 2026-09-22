import streamlit as st
import random
from collections import Counter
import base64
import os
import streamlit.components.v1 as components
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
# HELPER TO ENCODE BACKGROUND IMAGE
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
# Character images
katniss_img = get_base64_image("Katniss.png")
peeta_img = get_base64_image("Peeta.jfif")
gale_img = get_base64_image("Gale.jfif")
haymitch_img = get_base64_image("Haymitch.jfif")
prim_img = get_base64_image("Prim.png")
finnick_img = get_base64_image("Finnick.jfif")
rue_img = get_base64_image("Rue.png")
snow_img = get_base64_image("Snow.webp")
cinna_img = get_base64_image("Cinna.jpg")
johanna_img = get_base64_image("Johanna.jpg")
effie_img = get_base64_image("Effie.jfif")

CHARACTER_IMAGES = {
    "Katniss": katniss_img,
    "Peeta": peeta_img,
    "Gale": gale_img,
    "Haymitch": haymitch_img,
    "Prim": prim_img,
    "Finnick": finnick_img,
    "Rue": rue_img,
    "Snow": snow_img,
    "Cinna": cinna_img,
    "Johanna": johanna_img,
    "Effie": effie_img,
}

# ============================================================
# HUNGER GAMES INSPIRED STYLING
# ============================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;500;600;700;800&family=Inter:wght@400;500;600;700&display=swap');
html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}
.stApp {
    background:
        radial-gradient(circle at 50% 0%, rgba(145, 20, 20, 0.22), transparent 35%),
        linear-gradient(180deg, #080808 0%, #111111 45%, #070707 100%);
    color: #eeeeee;
}
.block-container {
    padding-top: 2rem;
    padding-bottom: 4rem;
    max-width: 1050px;
}
@keyframes shake-violent {
  0% { transform: translate(0, 0) rotate(0deg); }
  10% { transform: translate(-15px, -10px) rotate(-3deg); }
  20% { transform: translate(15px, 8px) rotate(3deg); }
  30% { transform: translate(-12px, 12px) rotate(-2deg); }
  40% { transform: translate(12px, -8px) rotate(2deg); }
  50% { transform: translate(-15px, 5px) rotate(-3deg); }
  60% { transform: translate(10px, -12px) rotate(2deg); }
  70% { transform: translate(-10px, 10px) rotate(-1deg); }
  80% { transform: translate(8px, -5px) rotate(1deg); }
  90% { transform: translate(-5px, 8px) rotate(0deg); }
  100% { transform: translate(0, 0) rotate(0deg); }
}
.shake-screen {
  animation: shake-violent 0.4s cubic-bezier(.36,.07,.19,.97) both;
}
@keyframes spin {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}
.spinning-chewie {
  animation: spin 2.5s linear infinite;
  width: 320px;
  height: auto;
  border-radius: 12px;
  box-shadow: 0 0 40px rgba(255, 255, 255, 0.15);
}
.tf-gif {
  width: 320px;
  height: auto;
  border-radius: 12px;
}
.hg-title {
    text-align: center;
    font-family: 'Cinzel', serif;
    font-size: 3.4rem;
    font-weight: 800;
    letter-spacing: 5px;
    color: #e6b84a;
    text-shadow:
        0 0 8px rgba(230,184,74,0.35),
        0 0 25px rgba(165,25,25,0.25);
    margin-bottom: 0;
}
.hg-subtitle {
    text-align: center;
    color: #b8b8b8;
    font-size: 1rem;
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-top: 0.4rem;
    margin-bottom: 2rem;
}
.divider {
    width: 70%;
    height: 1px;
    margin: 1.5rem auto 2rem auto;
    background: linear-gradient(90deg, transparent, #a91d1d, #e6b84a, #a91d1d, transparent);
}
.question-number {
    text-align: center;
    font-family: 'Cinzel', serif;
    color: #b52a2a;
    font-size: 0.95rem;
    font-weight: 700;
    letter-spacing: 4px;
    text-transform: uppercase;
}
.question-text {
    text-align: center;
    font-family: 'Cinzel', serif;
    font-size: 1.65rem;
    line-height: 1.45;
    font-weight: 600;
    color: #f1f1f1;
    margin: 0.7rem auto 1.7rem auto;
    max-width: 900px;
}
div[data-testid="stRadio"] > div {
    gap: 0.7rem;
}
div[data-testid="stRadio"] label {
    background: #181818;
    border: 1px solid #353535;
    border-left: 3px solid #5c5c5c;
    border-radius: 2px;
    padding: 0.8rem 1rem;
    transition: all 0.15s ease;
}
div[data-testid="stRadio"] label:hover {
    border-left-color: #c48b2c;
    background: #202020;
    box-shadow: 0 0 12px rgba(196,139,44,0.08);
}
div[data-testid="stRadio"] label p {
    color: #dedede !important;
    font-size: 0.95rem !important;
    line-height: 1.5 !important;
}
.stButton > button {
    width: 100%;
    background: linear-gradient(180deg, #a32626, #721515);
    color: white;
    border: 1px solid #c33a3a;
    border-radius: 2px;
    padding: 0.8rem 1.5rem;
    font-family: 'Cinzel', serif;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    transition: all 0.2s ease;
}
.stButton > button:hover {
    background: linear-gradient(180deg, #c33232, #8b1919);
    border-color: #e6b84a;
    box-shadow: 0 0 18px rgba(190,35,35,0.35);
    color: white;
}
.progress-label {
    text-align: center;
    font-size: 0.8rem;
    color: #888888;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 0.4rem;
}
.progress-container {
    height: 5px;
    background: #252525;
    width: 100%;
    margin-bottom: 2rem;
}
.progress-bar {
    height: 5px;
    background: linear-gradient(90deg, #781717, #d29a32, #e6b84a);
    box-shadow: 0 0 8px rgba(230,184,74,0.35);
}
.result-container {
    text-align: center;
    padding: 2rem 1rem 3rem 1rem;
}
.result-small {
    font-family: 'Cinzel', serif;
    color: #b52a2a;
    font-size: 1rem;
    font-weight: 700;
    letter-spacing: 5px;
    text-transform: uppercase;
}
.result-title {
    font-family: 'Cinzel', serif;
    color: #e6b84a;
    font-size: 2.8rem;
    font-weight: 800;
    letter-spacing: 3px;
    margin: 1rem 0;
    text-shadow: 0 0 15px rgba(230,184,74,0.3), 0 0 35px rgba(150,20,20,0.2);
}
.result-card {
    max-width: 750px;
    margin: 2rem auto;
    padding: 3rem 2rem;
    background: radial-gradient(circle at center, rgba(150,25,25,0.13), transparent 65%), #111111;
    border: 1px solid #4b4b4b;
    border-top: 3px solid #e6b84a;
    border-bottom: 3px solid #9e2020;
    box-shadow: 0 15px 50px rgba(0,0,0,0.65), 0 0 30px rgba(130,20,20,0.08);
}
.result-capitol {
    font-family: 'Cinzel', serif;
    font-size: 1rem;
    color: #999;
    letter-spacing: 4px;
    text-transform: uppercase;
}
.result-name {
    font-family: 'Cinzel', serif;
    font-size: 3.5rem;
    font-weight: 800;
    color: #e6b84a;
    margin: 1rem 0;
    letter-spacing: 3px;
}
.result-score {
    color: #999999;
    font-size: 0.9rem;
    letter-spacing: 2px;
    text-transform: uppercase;
}
.fire-symbol {
    font-size: 4rem;
    margin-bottom: 0.5rem;
    filter: drop-shadow(0 0 12px rgba(220,80,20,0.35));
}
.pct-container {
    max-width: 720px;
    margin: 0 auto 1rem auto;
    padding: 1.8rem 2rem;
    background: #111111;
    border: 1px solid #3a3a3a;
    border-top: 2px solid #e6b84a;
}
.pct-row {
    display: flex;
    align-items: center;
    margin-bottom: 1.15rem;
}
.pct-label {
    width: 110px;
    font-family: 'Cinzel', serif;
    font-size: 0.95rem;
    color: #e6b84a;
    letter-spacing: 1px;
    flex-shrink: 0;
}
.pct-bar-bg {
    flex: 1;
    height: 18px;
    background: #1e1e1e;
    border-radius: 2px;
    overflow: hidden;
    margin: 0 14px;
}
.pct-bar-fill {
    height: 100%;
    background: linear-gradient(90deg, #781717, #d29a32, #e6b84a);
    border-radius: 2px;
}
.pct-value {
    width: 58px;
    text-align: right;
    font-size: 0.9rem;
    color: #ccc;
    font-family: 'Cinzel', serif;
    flex-shrink: 0;
}
.name-container {
    max-width: 650px;
    margin: 4rem auto;
    padding: 3rem 2.5rem;
    text-align: center;
    background: radial-gradient(circle at center, rgba(150,25,25,0.12), transparent 70%), #111111;
    border: 1px solid #4b4b4b;
    border-top: 3px solid #e6b84a;
    border-bottom: 3px solid #9e2020;
    box-shadow: 0 15px 50px rgba(0,0,0,0.65), 0 0 30px rgba(130,20,20,0.08);
}
.name-title {
    font-family: 'Cinzel', serif;
    color: #e6b84a;
    font-size: 2rem;
    font-weight: 800;
    letter-spacing: 3px;
    margin-bottom: 1rem;
}
.name-subtitle {
    color: #999999;
    font-size: 0.9rem;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 2rem;
}
.hg-footer {
    text-align: center;
    color: #555555;
    font-size: 0.72rem;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-top: 3rem;
}
/* Restart button styling */
.restart-btn button {
    background: transparent !important;
    border: 1px solid #555 !important;
    color: #999 !important;
    font-size: 0.85rem !important;
    letter-spacing: 1px !important;
    margin-top: 1.5rem !important;
}
.restart-btn button:hover {
    border-color: #e6b84a !important;
    color: #e6b84a !important;
}
</style>
""", unsafe_allow_html=True)

# ============================================================
# GASTER MODE (Wingdings + mobile fallback)
# ============================================================
if "gaster_mode" not in st.session_state:
    st.session_state.gaster_mode = False

if st.session_state.gaster_mode:
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Symbols+2&display=swap');
    html, body, [class*="css"], .stApp, .stMarkdown, p, div, span, label, 
    button, input, textarea, h1, h2, h3, h4, h5, h6, 
    .stButton > button, .stRadio label, .stTextInput input {
        font-family: 'Wingdings', 'Noto Sans Symbols 2', 'Segoe UI Symbol', 'Apple Symbols', sans-serif !important;
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
# CHARACTER DESCRIPTIONS
# ============================================================
DESCRIPTIONS = {
    "Katniss": "Katniss (named after katniss) is fiercely independent and takes on the protector role in her relationships. Having lost her father at a young age, she’s an avoidant self-sufficient and works hard to keep her family afloat. She’s determined and goal oriented, but also incredibly compassionate. She also lets her intrusive thoughts win (hello mr seneca crane). In a revolution, she represents most people; wanting to keep her head low and survive the oppressive system. She has plenty of fire herself.",
    
    "Peeta": "Soft and loving, Peeta is the ultimate green flag. He cares deeply and unforgivingly. Peeta is the rare type in a revolution; kind, charismatic and displays a refusal to play by the system’s violence. Hardly jumps to conclusions and tries to understand everyone. Mature and selfless, he rarely complains even when he has plenty of reason to. He is the dandelion in the spring.",
    
    "Gale": "Gale is the typical revolutionary; angry, brave and willing to fight for freedom even through violent means. Gale gives in to his anger and need for revenge as time goes on. Similar to Katniss, he has a lot of fire in him. He respected anyone for their skills and resilience and carried resentment to those more privileged than him. His bravery saved hundreds of lives from being killed.",
    
    "Effie": "Effie is a perfectionist and extremely punctual (a five-minute train delay will hugely affect her schedule). She is bright and bubbly at times. She sees the hunger games as just fun entertainment. Out of touch from reality, but loving nonetheless. She grows fond of her loving victors.",
    
    "Haymitch": "Everyone assumes Haymitch is simply the town drunk. But Haymitch is complex and has had a tough life. He’s a good mentor figure to Katniss and Peeta, but he’s not really an amazing father figure. Haymitch is incredibly intelligent, orchestrates a rebellion against the capitol and manages to communicate with Katniss in her manner.",
    
    "Finnick": "The youngest victor of the hunger games, and a fan favourite. Loved by all, and fantasized by a lot in the capitol, he still has his one true love at home. His love for Annie grounds him in a way, because their love makes everything he has ever endured worth it. He is known for his charm and exceptional skill with a trident. He’s extremely popular among the capitol crowd.",
    
    "Prim": "Prim’s innocence, kindness and gentle nature serves as the backbone of this story. A young healer, she is sheltered from a lot because of her elder sisters work. She grows up to be caring and a wonderful doctor. She loves her stupid cat. Like Peeta, she is not inclined towards violence.",
    
    "Rue": "Being reaped for the hunger games at the young age of 12, Rue is the symbolism of innocence and youth. Katniss saw Rue as someone to protect and take care of. Katniss and Rue cling onto each other. Rue tells stories about her life, and they sing. Though not a fighter, Rue is nimble, clever and resourceful. She is the beginning of the rebellion.",
    
    "Snow": "Beginning as an ambitious, impoverished Capitol orphan, Snow practically morphs into a psychopath. He’s calculated and manipulative and is in fear of losing his power, leading him to poison any threats. His charm is his currency. Ambitious and intelligent, he never lies. But he’s still a psychopath.",
    
    "Cinna": "Cinna is Katniss’s empathetic and brilliant stylist. He's a key underground rebellion leader and proves that rebellion doesn’t always mean heavy shots and elaborate plans, but can be depicted through small acts of resistance, such as a twirl. He believes fully in Katniss and knows she can win. He coins the term ‘girl on fire’.",
    
    "Johanna": "A fucking rebel through and through. Tough and says whats on everyone’s mind. That being said, she’s only the way she is because the capitol’s already taken everyone she can care for. She openly hates the Capitol and Snow and shows no desire to hold that back. Not everyone’s favourite, but she’s exactly who she says she is and doesn’t really care whether people like her.",
    
    "Plutarch": "A master strategist and political chameleon. He plays the long game and is always three steps ahead.",
    "Foxface": "Quiet, observant and extremely clever. She survives by staying invisible and using her intelligence rather than force.",
    "Beetee": "The quiet genius. He sees systems, patterns and weaknesses that others miss, and uses technology as his weapon."
}

# ============================================================
# ALL 9 QUESTIONS (base list)
# ============================================================
BASE_QUESTIONS = [
    # ===== HUNGER GAMES QUESTIONS =====
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
            "Katniss":  [0, 3, 0, 0, 0],
            "Peeta":    [3, 0, 0, 0, 0],
            "Gale":     [0, 0, 0, 0, 0],
            "Haymitch": [0, 2, 2, 0, 0],
            "Prim":     [0, 0, 0, 0, 0],
            "Finnick":  [0, 0, 0, 0, 1],
            "Rue":      [0, 0, 0, 0, 0],
            "Snow":     [0, 0, 0, 0, 0],
            "Cinna":    [0, 0, 0, 0, 0],
            "Johanna":  [0, 0, 0, 0, 0],
            "Effie":    [1, 0, 0, 0, 3],
            "Plutarch": [0, 0, 2, 0, 0],
            "Foxface":  [0, 0, 0, 3, 0],
            "Beetee":   [0, 0, 0, 1, 0]
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
            "Katniss":  [1, 3, 0, 0, 0, 0],
            "Peeta":    [0, 0, 0, 3, 0, 0],
            "Gale":     [0, 0, 0, 0, 0, 0],
            "Haymitch": [0, 0, 3, 0, 0, 2],
            "Prim":     [0, 0, 0, 0, 0, 0],
            "Finnick":  [0, 0, 0, 1, 0, 2],
            "Rue":      [0, 0, 0, 0, 0, 0],
            "Snow":     [0, 0, 0, 0, 0, 0],
            "Cinna":    [0, 0, 0, 0, 0, 0],
            "Johanna":  [3, 0, 2, 0, 0, 0],
            "Effie":    [0, 0, 0, 0, 0, 0],
            "Plutarch": [0, 0, 0, 0, 3, 0],
            "Foxface":  [0, 2, 0, 0, 3, 0],
            "Beetee":   [0, 0, 0, 0, 0, 0]
        }
    },
    {
        "question": "You're given 30 seconds at the Cornucopia. What are you taking?",
        "options": [
            "A weapon.",
            "Medicine.",
            "Food and water.",
            "Something nobody else seems interested in.",
            "Whatever looks most expensive.",
            "Whatever I can dismantle into something more useful."
        ],
        "scores": {
            "Katniss":  [3, 2, 1, 0, 0, 0],
            "Peeta":    [0, 2, 0, 0, 0, 0],
            "Gale":     [0, 0, 0, 0, 0, 0],
            "Haymitch": [0, 0, 3, 0, 0, 1],
            "Prim":     [0, 0, 0, 0, 0, 0],
            "Finnick":  [0, 0, 0, 0, 1, 0],
            "Rue":      [0, 0, 0, 0, 0, 0],
            "Snow":     [0, 0, 0, 0, 0, 0],
            "Cinna":    [0, 0, 0, 0, 0, 0],
            "Johanna":  [1, 0, 0, 0, 0, 0],
            "Effie":    [0, 0, 0, 0, 3, 0],
            "Plutarch": [0, 0, 0, 1, 0, 0],
            "Foxface":  [0, 0, 0, 3, 0, 0],
            "Beetee":   [0, 0, 0, 0, 0, 3]
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
            "Katniss":  [0, 3, 0, 0, 0, 0],
            "Peeta":    [0, 0, 0, 3, 0, 0],
            "Gale":     [0, 0, 0, 0, 0, 0],
            "Haymitch": [0, 0, 0, 0, 0, 3],
            "Prim":     [0, 0, 0, 0, 0, 0],
            "Finnick":  [0, 0, 3, 2, 0, 0],
            "Rue":      [0, 0, 0, 0, 0, 0],
            "Snow":     [0, 0, 0, 0, 0, 0],
            "Cinna":    [0, 0, 0, 0, 0, 0],
            "Johanna":  [0, 2, 0, 0, 0, 1],
            "Effie":    [0, 0, 0, 0, 0, 0],
            "Plutarch": [2, 0, 2, 0, 0, 0],
            "Foxface":  [0, 0, 0, 0, 2, 0],
            "Beetee":   [3, 0, 0, 0, 3, 0]
        }
    },
    # ===== ORIGINAL PLAKSHA QUESTIONS =====
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
            "Katniss":  [1, 3, 0, 1, -1],
            "Peeta":    [0, 1, 0, 3, -2],
            "Gale":     [3, 1, 0, 1, 2],
            "Haymitch": [2, 2, 3, 0, 1],
            "Prim":     [0, 2, 0, 3, -2],
            "Finnick":  [0, 1, 3, 2, 1],
            "Rue":      [1, 3, 1, 2, -1],
            "Snow":     [1, 1, 0, -1, 3],
            "Cinna":    [0, 2, 0, 2, -1],
            "Johanna":  [2, 0, 1, 0, 2],
            "Effie":    [1, 3, -1, 1, 1],
            "Plutarch": [0, 0, 0, 0, 0],
            "Foxface":  [0, 0, 0, 0, 0],
            "Beetee":   [0, 0, 0, 0, 0]
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
            "Katniss":  [1, 1, 0, 3, 1, 0],
            "Peeta":    [-1, 3, 0, 1, 1, 3],
            "Gale":     [1, 1, 0, 2, 3, 2],
            "Haymitch": [3, 0, 3, 1, 1, 1],
            "Prim":     [-1, 3, 0, 1, 1, 2],
            "Finnick":  [1, 1, 2, 0, 1, 3],
            "Rue":      [1, 3, 1, 2, 1, 1],
            "Snow":     [3, -1, 1, 1, 3, 2],
            "Cinna":    [0, 2, 0, 3, 1, 3],
            "Johanna":  [3, 0, 2, 2, 1, 1],
            "Effie":    [1, 1, -1, 0, 3, 2],
            "Plutarch": [0, 0, 0, 0, 0, 0],
            "Foxface":  [0, 0, 0, 0, 0, 0],
            "Beetee":   [0, 0, 0, 0, 0, 0]
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
            "Katniss":  [3, 1, 2, -1, 1],
            "Peeta":    [0, 3, 3, -1, 1],
            "Gale":     [2, 1, 2, 1, 3],
            "Haymitch": [3, -1, 1, 0, -1],
            "Prim":     [1, 3, 3, -1, 1],
            "Finnick":  [0, 2, 2, 3, 3],
            "Rue":      [2, 2, 3, -1, 1],
            "Snow":     [1, -1, 0, 3, 2],
            "Cinna":    [2, 1, 2, 1, 3],
            "Johanna":  [3, -1, 1, 2, 0],
            "Effie":    [0, 2, 1, 3, 2],
            "Plutarch": [0, 0, 0, 0, 0],
            "Foxface":  [0, 0, 0, 0, 0],
            "Beetee":   [0, 0, 0, 0, 0]
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
            "Katniss":  [3, 1, 2, 3, 1, 1],
            "Peeta":    [2, 3, 2, 0, -1, 3],
            "Gale":     [2, 1, 3, 2, 0, 1],
            "Haymitch": [3, 3, 2, 1, 2, -1],
            "Prim":     [3, 1, 2, 0, -1, 3],
            "Finnick":  [3, 3, 2, 2, 1, 3],
            "Rue":      [3, 1, 2, 1, 2, 1],
            "Snow":     [3, 1, 3, 2, 0, 1],
            "Cinna":    [3, 2, 2, 1, 1, 3],
            "Johanna":  [1, 3, 2, 3, 2, 1],
            "Effie":    [3, 1, 3, 1, 1, 2],
            "Plutarch": [0, 0, 0, 0, 0, 0],
            "Foxface":  [0, 0, 0, 0, 0, 0],
            "Beetee":   [0, 0, 0, 0, 0, 0]
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
            "Katniss":  [3, 1, 1, 2, 3],
            "Peeta":    [2, 0, 1, 3, 2],
            "Gale":     [1, 0, 1, 3, 3],
            "Haymitch": [2, 3, 2, 1, 1],
            "Prim":     [3, -1, 1, 3, 2],
            "Finnick":  [1, 2, 3, 1, 2],
            "Rue":      [3, 1, 1, 2, 2],
            "Snow":     [2, 1, 3, 2, 3],
            "Cinna":    [1, 0, 1, 3, 3],
            "Johanna":  [1, 2, 1, 3, 2],
            "Effie":    [2, -1, 2, 3, 2],
            "Plutarch": [0, 0, 0, 0, 0],
            "Foxface":  [0, 0, 0, 0, 0],
            "Beetee":   [0, 0, 0, 0, 0]
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
if "show_credits" not in st.session_state:
    st.session_state.show_credits = False

# Shuffle questions once per session
if "shuffled_questions" not in st.session_state:
    st.session_state.shuffled_questions = random.sample(BASE_QUESTIONS, len(BASE_QUESTIONS))
QUESTIONS = st.session_state.shuffled_questions

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
    tied = [c for c, s in scores.items() if s == highest]
    if len(tied) == 1:
        return tied[0], tied
    return random.choice(tied), tied

# ============================================================
# CREDITS (static version that works)
# ============================================================
def show_credits():
    # Force the page to the very top when credits appear
    components.html("""
    <script>
    function forceTop() {
        try {
            window.parent.scrollTo(0, 0);
            window.parent.document.documentElement.scrollTop = 0;
            window.parent.document.body.scrollTop = 0;

            const parentDoc = window.parent.document;
            const elements = parentDoc.querySelectorAll(
                'section, main, [data-testid="stAppViewContainer"], ' +
                '[data-testid="stAppViewBlockContainer"], ' +
                '[data-testid="stVerticalBlockBorderWrapper"]'
            );

            elements.forEach(function(el) {
                if (el.scrollTop > 0) {
                    el.scrollTop = 0;
                }
            });
        } catch (e) {}
    }

    forceTop();
    setTimeout(forceTop, 50);
    setTimeout(forceTop, 150);
    setTimeout(forceTop, 300);
    setTimeout(forceTop, 500);
    setTimeout(forceTop, 800);
    </script>
    """, height=1)

    st.markdown("""
<div style="max-width:700px;margin:2rem auto 3rem auto;padding:3.5rem 2.5rem;text-align:center;background:radial-gradient(circle at top,#0a0a0a,#000000);border:2px solid #e6b84a;border-radius:12px;box-shadow:0 0 40px rgba(230,184,74,0.12);">
<div style="font-family:'Cinzel',serif;font-size:2.4rem;color:#e6b84a;letter-spacing:6px;margin-bottom:3.5rem;text-transform:uppercase;">CREDITS</div>
<div style="margin-bottom:2.8rem;">
<div style="font-family:'Cinzel',serif;font-size:0.9rem;color:#888;letter-spacing:2px;text-transform:uppercase;margin-bottom:0.4rem;">Made with DETERMINATION by</div>
<div style="font-family:'Cinzel',serif;font-size:1.5rem;color:#f1f1f1;letter-spacing:1px;">members of The Spine</div>
<div style="font-family:'Cinzel',serif;font-size:1.05rem;color:#e6b84a;margin-top:0.6rem;">(scroll till the end for secrets 👀)</div>
</div>
<div style="margin-bottom:2.8rem;">
<div style="font-family:'Cinzel',serif;font-size:0.9rem;color:#888;letter-spacing:2px;text-transform:uppercase;margin-bottom:0.4rem;">Questions Made by</div>
<div style="font-family:'Cinzel',serif;font-size:1.45rem;color:#f1f1f1;">Simran and Zaina</div>
</div>
<div style="margin-bottom:2.8rem;">
<div style="font-family:'Cinzel',serif;font-size:0.9rem;color:#888;letter-spacing:2px;text-transform:uppercase;margin-bottom:0.4rem;">Character Descriptions written by</div>
<div style="font-family:'Cinzel',serif;font-size:1.45rem;color:#f1f1f1;">Avani</div>
</div>
<div style="margin-bottom:2.8rem;">
<div style="font-family:'Cinzel',serif;font-size:0.9rem;color:#888;letter-spacing:2px;text-transform:uppercase;margin-bottom:0.4rem;">Site Dev and stupid Undertale references</div>
<div style="font-family:'Cinzel',serif;font-size:1.45rem;color:#f1f1f1;">Trinav</div>
</div>
<div style="margin-bottom:2.8rem;">
<div style="font-family:'Cinzel',serif;font-size:0.9rem;color:#888;letter-spacing:2px;text-transform:uppercase;margin-bottom:0.4rem;">Poster Design</div>
<div style="font-family:'Cinzel',serif;font-size:1.45rem;color:#f1f1f1;">Sara</div>
</div>
<div style="margin-bottom:2.8rem;">
<div style="font-family:'Cinzel',serif;font-size:0.9rem;color:#888;letter-spacing:2px;text-transform:uppercase;margin-bottom:0.4rem;">Names you should not enter</div>
<div style="font-family:'Cinzel',serif;font-size:1.45rem;color:#c52c2c;">Trinav<br>Gaster (if you're on your laptop)</div>
</div>
<div style="margin-bottom:2.8rem;">
<div style="font-family:'Cinzel',serif;font-size:0.9rem;color:#888;letter-spacing:2px;text-transform:uppercase;margin-bottom:0.4rem;">Names you should enter</div>
<div style="font-family:'Cinzel',serif;font-size:1.45rem;color:#f1f1f1;">Chewie<br>your own name =)</div>
</div>
<div style="font-family:'Cinzel',serif;font-size:1.15rem;color:#c52c2c;margin-top:3.5rem;letter-spacing:1px;line-height:1.6;">
...you really scrolled till the end?<br>EXCELLENT. TRULY EXCELLENT. not like you had a choice...
</div>
</div>
""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("CLOSE CREDITS", use_container_width=True):
            st.session_state.show_credits = False
            st.rerun()

# ============================================================
# ERROR / CHEWIE / RESULT VIEWS
# ============================================================
def show_access_denied():
    st.markdown(f"""
        <style>
        .stApp {{
            background: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)), url("data:image/jfif;base64,{gaster_base64}") !important;
            background-size: cover !important;
            background-position: center !important;
            background-repeat: no-repeat !important;
        }}
        </style>
        <div class="shake-screen" style="display:flex;flex-direction:column;align-items:center;justify-content:center;height:60vh;text-align:center;">
            <div style="font-size:5rem;margin-bottom:1rem;">⚠️</div>
            <div style="font-family:'Cinzel',serif;color:#c52c2c;font-size:2.5rem;font-weight:800;letter-spacing:4px;margin-bottom:1rem;">ACCESS DENIED</div>
            <div style="font-family:'Cinzel',serif;color:#e6b84a;font-size:1.4rem;letter-spacing:2px;margin-bottom:2rem;">you cannot play as me</div>
            <div style="color:#bbb;font-size:0.9rem;letter-spacing:1px;text-transform:uppercase;">The Capitol rejects this intrusion.</div>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("RETURN TO REAPING"):
            st.session_state.access_denied = False
            st.session_state.name = ""
            st.session_state.name_submitted = False
            st.rerun()

def show_chewie():
    st.markdown(f"""
        <style>
        .stApp {{ background: #000000 !important; }}
        .block-container {{ max-width: 100% !important; padding-top: 0 !important; }}
        </style>
        <div style="display:flex;flex-direction:column;align-items:center;justify-content:center;height:85vh;gap:2.5rem;">
            <div style="display:flex;align-items:center;justify-content:center;gap:4rem;flex-wrap:wrap;">
                <img src="data:image/jpeg;base64,{chewie_base64}" class="spinning-chewie" alt="Chewie">
                <img src="data:image/gif;base64,{tf_base64}" class="tf-gif" alt="TF">
            </div>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("RETURN TO REAPING"):
            st.session_state.chewie_mode = False
            st.session_state.name = ""
            st.session_state.name_submitted = False
            st.rerun()

def show_result():
    # Force the browser to the very top of the page when results load.
    # This uses a real Streamlit HTML component because JavaScript inside
    # st.markdown() is not reliably executed.
    components.html("""
        <script>
        function forceTop() {
            try {
                // Main document
                window.parent.scrollTo(0, 0);
                window.parent.document.documentElement.scrollTop = 0;
                window.parent.document.body.scrollTop = 0;

                // Streamlit's main scrolling containers
                const parentDoc = window.parent.document;

                const elements = parentDoc.querySelectorAll(
                    'section, main, [data-testid="stAppViewContainer"], ' +
                    '[data-testid="stAppViewBlockContainer"], ' +
                    '[data-testid="stVerticalBlockBorderWrapper"]'
                );

                elements.forEach(function(el) {
                    if (el.scrollTop > 0) {
                        el.scrollTop = 0;
                    }
                });
            } catch (e) {
                // Ignore browser restrictions
            }
        }

        // Run several times because Streamlit may still be rendering
        // the result screen when the first scroll command happens.
        forceTop();
        setTimeout(forceTop, 50);
        setTimeout(forceTop, 150);
        setTimeout(forceTop, 300);
        setTimeout(forceTop, 500);
        setTimeout(forceTop, 800);
        </script>
    """, height=1)

    character = st.session_state.result
    scores = st.session_state.scores
    user_name = st.session_state.name

    st.markdown(f"""
        <div class="result-container">
            <div class="fire-symbol">🔥</div>
            <div class="result-small">THE REAPING IS COMPLETE</div>
            <div class="result-title">{user_name}, your character is</div>
        </div>
    """, unsafe_allow_html=True)

    # Character Image
    img_data = CHARACTER_IMAGES.get(character, "")
    if img_data:
        # Determine correct mime type
        if character in ["Katniss", "Prim", "Rue"]:
            mime = "image/png"
        elif character == "Snow":
            mime = "image/webp"
        elif character in ["Cinna", "Johanna"]:
            mime = "image/jpeg"
        else:
            mime = "image/jpeg"  # for .jfif

        st.markdown(f"""
            <div style="text-align:center; margin: 1.5rem 0 2rem 0;">
                <img src="data:{mime};base64,{img_data}"
                     style="max-width: 320px; width: 100%; height: auto;
                            border-radius: 12px;
                            box-shadow: 0 0 30px rgba(230,184,74,0.25);
                            border: 2px solid #e6b84a;">
            </div>
        """, unsafe_allow_html=True)

    st.markdown(f"""
        <div class="result-card">
            <div class="result-capitol">THE CAPITOL HAS SPOKEN</div>
            <div class="result-name">{character.upper()}</div>
            <div class="result-score">Final score: {scores[character]}</div>
        </div>
    """, unsafe_allow_html=True)

    # Character Description
    description = DESCRIPTIONS.get(character, "No description available.")
    st.markdown(f"""
        <div style="
            max-width: 750px;
            margin: 2rem auto;
            padding: 2rem 2.2rem;
            background: #111111;
            border: 1px solid #3a3a3a;
            border-top: 2px solid #e6b84a;
            color: #dddddd;
            font-size: 1.05rem;
            line-height: 1.7;
            text-align: left;
        ">
            {description}
        </div>
    """, unsafe_allow_html=True)

    with st.expander("VIEW ALIGNMENT"):
        score_dict = dict(scores)
        min_s = min(score_dict.values()) if score_dict else 0
        shifted = {k: v - min_s for k, v in score_dict.items()}
        total = sum(shifted.values()) or 1
        ranked = sorted(shifted.items(), key=lambda x: x[1], reverse=True)
        rows = []

        for char, val in ranked:
            pct = (val / total) * 100
            if pct < 1.0:
                continue

            row = (
                f'<div class="pct-row">'
                f'<div class="pct-label">{char}</div>'
                f'<div class="pct-bar-bg"><div class="pct-bar-fill" style="width:{pct:.1f}%;"></div></div>'
                f'<div class="pct-value">{pct:.1f}%</div>'
                f'</div>'
            )
            rows.append(row)

        bars_html = '<div class="pct-container">' + "".join(rows) + '</div>'
        st.markdown(bars_html, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        if st.button("RE-ENTER THE ARENA"):
            st.session_state.page = 0
            st.session_state.answers = []
            st.session_state.finished = False
            st.session_state.result = None
            st.session_state.scores = None
            st.session_state.name = ""
            st.session_state.name_submitted = False
            st.rerun()

    with col3:
        if st.button("CREDITS"):
            st.session_state.show_credits = True
            st.rerun()

# ============================================================
# MAIN HEADER  (hidden when haunted)
# ============================================================
if not st.session_state.haunted:
    st.markdown('<div class="hg-title">WHO IS YOUR HUNGER GAMES CHARACTER?</div>', unsafe_allow_html=True)
    st.markdown('<div class="hg-subtitle">MAY THE ODDS BE EVER IN YOUR FAVOUR</div>', unsafe_allow_html=True)
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ============================================================
# ROUTING
# ============================================================
if st.session_state.show_credits:
    show_credits()
    st.stop()

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
# NAME CHECK
# ============================================================
if not st.session_state.name_submitted:
    st.markdown("""
        <div class="name-container">
            <div class="name-title">STATE YOUR NAME</div>
            <div class="name-subtitle">Before you enter the arena, the Capitol requires your identity.</div>
        </div>
    """, unsafe_allow_html=True)

    if st.session_state.haunted and sansback_base64:
        st.markdown(f"""
            <div style="display:flex;justify-content:center;margin:1.5rem 0 2rem 0; overflow:hidden;">
                <img src="data:image/jpeg;base64,{sansback_base64}"
                     style="width: 1100px; max-width: 100%; height: auto;
                            transform: scale(1.6);
                            transform-origin: center center;
                            border-radius: 12px;
                            box-shadow: 0 0 40px rgba(197,44,44,0.35);">
            </div>
        """, unsafe_allow_html=True)

    name = st.text_input("Your name", key="name_input", placeholder="Enter your name...", label_visibility="collapsed")
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        if st.button("ENTER THE ARENA"):
            entered_name = name.strip()
            if not entered_name:
                st.error("You must state your name before entering the arena.")
                st.stop()

            # Special name checks
            if "trinav" in entered_name.lower():
                st.session_state.access_denied = True
                st.rerun()
            if "chewie" in entered_name.lower():
                st.session_state.chewie_mode = True
                st.rerun()
            if "gaster" in entered_name.lower():
                st.session_state.gaster_mode = True

            if entered_name.lower() in {c.lower() for c in CHARACTERS}:
                st.error("you think you can choose your own fate?")
                st.stop()

            st.session_state.name = entered_name
            st.session_state.name_submitted = True
            st.rerun()
    with col3:
        if st.button("CREDITS"):
            st.session_state.show_credits = True
            st.rerun()
    st.stop()

# ============================================================
# CURRENT QUESTION
# ============================================================
q_index = st.session_state.page
question = QUESTIONS[q_index]
total_questions = len(QUESTIONS)

st.markdown(f'<div class="progress-label">Question {q_index + 1} of {total_questions}</div>', unsafe_allow_html=True)
progress = (q_index + 1) / total_questions
st.markdown(f"""
    <div class="progress-container">
        <div class="progress-bar" style="width:{progress * 100}%"></div>
    </div>
""", unsafe_allow_html=True)

st.markdown(f'<div class="question-number">THE ARENA · QUESTION {q_index + 1}</div>', unsafe_allow_html=True)
st.markdown(f'<div class="question-text">{question["question"]}</div>', unsafe_allow_html=True)

option_labels = [f"{chr(65 + i)}. {option}" for i, option in enumerate(question["options"])]
selected = st.radio("Choose your answer:", option_labels, index=None, key=f"question_{q_index}", label_visibility="collapsed")

st.markdown("<br>", unsafe_allow_html=True)

if selected is not None:
    selected_index = option_labels.index(selected)
    if q_index < total_questions - 1:
        if st.button("CONTINUE →"):
            st.session_state.answers.append(selected_index)
            st.session_state.page += 1
            st.rerun()
    else:
        if st.button("ENTER THE REAPING"):
            st.session_state.answers.append(selected_index)
            scores = calculate_scores(st.session_state.answers)
            character, _ = determine_character(scores)
            st.session_state.scores = scores
            st.session_state.result = character
            st.session_state.finished = True
            st.rerun()
else:
    st.markdown("""
        <div style="text-align:center;color:#666;font-size:0.8rem;letter-spacing:1px;margin-top:0.5rem;">
            SELECT AN OPTION TO CONTINUE
        </div>
    """, unsafe_allow_html=True)

# ---------- RESTART BUTTON ----------
st.markdown("<br>", unsafe_allow_html=True)
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown('<div class="restart-btn">', unsafe_allow_html=True)
    if st.button("Had a change of heart? Restart Quiz"):
        st.session_state.page = 0
        st.session_state.answers = []
        st.session_state.finished = False
        st.session_state.result = None
        st.session_state.scores = None
        st.session_state.name = ""
        st.session_state.name_submitted = False
        st.session_state.haunted = True
        st.session_state.gaster_mode = False
        st.session_state.shuffled_questions = random.sample(BASE_QUESTIONS, len(BASE_QUESTIONS))
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="hg-footer">PANEM · THE CAPITOL · MAY THE ODDS BE EVER IN YOUR FAVOUR</div>', unsafe_allow_html=True)
