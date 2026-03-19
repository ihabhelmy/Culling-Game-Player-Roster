import streamlit as st
import random
import time

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Culling Game Player Roster",
    page_icon="🕸️",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# --- CUSTOM CSS FOR DARK/JJK AESTHETIC & ANIMATIONS ---
st.markdown(
    """
    <style>
    /* Main background */
    .stApp {
        background-color: #0e0e0e;
        color: #e0e0e0;
    }
    
    /* Glowing Headers */
    h1, h2, h3 {
        color: #ff3333 !important;
        font-family: 'Courier New', Courier, monospace;
        text-transform: uppercase;
        letter-spacing: 2px;
        text-shadow: 0 0 10px #ff3333, 0 0 20px #8a0303;
    }
    
    /* Breathing/Pulsating Animation for Button */
    @keyframes cursedEnergyPulse {
        0% { box-shadow: 0 0 5px #ff3333; transform: scale(1); }
        50% { box-shadow: 0 0 25px #ff3333, 0 0 10px #8a0303; transform: scale(1.02); }
        100% { box-shadow: 0 0 5px #ff3333; transform: scale(1); }
    }

    div.stButton > button {
        background-color: #1a1a1a;
        color: #ff3333;
        border: 2px solid #ff3333;
        border-radius: 0px;
        padding: 10px 24px;
        font-weight: bold;
        font-size: 18px;
        font-family: 'Courier New', Courier, monospace;
        transition: all 0.3s ease;
        width: 100%;
        animation: cursedEnergyPulse 2s infinite;
    }
    
    div.stButton > button:hover {
        background-color: #ff3333;
        color: #1a1a1a;
        border: 2px solid #ff3333;
        animation: none;
        box-shadow: 0 0 20px #ff3333;
    }
    
    /* Fade-in Animation for Character Card */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }

    .character-card {
        background-color: #1a1a1a;
        border: 1px solid #333;
        padding: 20px;
        border-radius: 5px;
        box-shadow: inset 0 0 15px #000;
        margin-top: 20px;
        animation: fadeIn 0.8s ease-out forwards;
    }
    
    .quote-text {
        font-style: italic;
        color: #b3b3b3;
        border-left: 3px solid #ff3333;
        padding-left: 10px;
        margin: 10px 0;
    }
    
    .technique-text {
        color: #8888ff;
        font-weight: bold;
        text-shadow: 0 0 5px #4444ff;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- EXPANDED CHARACTER DATABASE ---
CHARACTERS = [
    {
        "name": "Ryomen Sukuna",
        "grade": "Special Grade",
        "technique": "Shrine (Dismantle & Cleave) / Ten Shadows",
        "quote": "Know your place, fool.",
        "threat_level": "extreme"
    },
    {
        "name": "Satoru Gojo",
        "grade": "Special Grade",
        "technique": "Limitless / Six Eyes",
        "quote": "Throughout Heaven and Earth, I alone am the honored one.",
        "threat_level": "extreme"
    },
    {
        "name": "Yuta Okkotsu",
        "grade": "Special Grade",
        "technique": "Copy / Rika",
        "quote": "Don't you dare hurt my friends!",
        "threat_level": "extreme"
    },
    {
        "name": "Kinji Hakari",
        "grade": "Grade 1 (Equivalent)",
        "technique": "Idle Death Gamble",
        "quote": "Let's get feverish!",
        "threat_level": "high"
    },
    {
        "name": "Maki Zenin",
        "grade": "Special Grade (Equivalent)",
        "technique": "Heavenly Restriction",
        "quote": "I'm going to destroy everything. All of it.",
        "threat_level": "extreme"
    },
    {
        "name": "Hajime Kashimo",
        "grade": "Grade 1 (Equivalent) / Past Era",
        "technique": "Mythical Beast Amber",
        "quote": "Turn up the volume! Because this is a funeral for the living!",
        "threat_level": "extreme"
    },
    {
        "name": "Hiromi Higuruma",
        "grade": "Grade 1 (Equivalent)",
        "technique": "Deadly Sentencing",
        "quote": "Ignorance of the law is no excuse.",
        "threat_level": "high"
    },
    {
        "name": "Ryu Ishigori",
        "grade": "Grade 1 (Equivalent) / Past Era",
        "technique": "Cursed Energy Discharge",
        "quote": "I want a dessert that fills me up!",
        "threat_level": "high"
    },
    {
        "name": "Takako Uro",
        "grade": "Grade 1 (Equivalent) / Past Era",
        "technique": "Sky Manipulation",
        "quote": "You're just a kid who doesn't know their place.",
        "threat_level": "high"
    },
    {
        "name": "Hana Kurusu (Angel)",
        "grade": "Special Grade (Equivalent)",
        "technique": "Jacob's Ladder (Technique Extinguishment)",
        "quote": "We will purge all incarnated players.",
        "threat_level": "extreme"
    },
    {
        "name": "Fumihiko Takaba",
        "grade": "Special Grade (Equivalent Potential)",
        "technique": "Comedian",
        "quote": "Wouldn't it be hilarious if...",
        "threat_level": "unpredictable"
    },
    {
        "name": "Reggie Star",
        "grade": "Grade 1 (Equivalent) / Past Era",
        "technique": "Contract Reproduction",
        "quote": "Let me show you a real scam.",
        "threat_level": "medium"
    },
    {
        "name": "Charles Bernard",
        "grade": "Grade 2 (Equivalent)",
        "technique": "G-Warstaff (Future Sight)",
        "quote": "I will draw the perfect manga!",
        "threat_level": "low"
    },
    {
        "name": "Yorozu",
        "grade": "Special Grade (Equivalent) / Past Era",
        "technique": "Construction",
        "quote": "I will teach you about love!",
        "threat_level": "extreme"
    },
    {
        "name": "Megumi Fushiguro",
        "grade": "Grade 1 (Potential)",
        "technique": "Ten Shadows Technique",
        "quote": "I will save people unequally.",
        "threat_level": "high"
    },
    {
        "name": "Yuji Itadori",
        "grade": "Grade 1 (Equivalent)",
        "technique": "Divergent Fist / Black Flash / Shrine / Blood Manipulation",
        "quote": "I don't care if I'm a cog.",
        "threat_level": "high"
    }
]

# --- MAIN APP ---
def main():
    st.title("🩸 Culling Game: Player Roster")
    st.markdown("*" + "Enter the colonies. Survive the game." + "*")
    st.divider()

    # Session state to keep track of the current character
    if 'current_character' not in st.session_state:
        st.session_state.current_character = None

    # Summon button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("SUMMON PLAYER"):
            with st.spinner("Sensing Cursed Energy..."):
                time.sleep(1) # Dramatic delay for animation feel
                st.session_state.current_character = random.choice(CHARACTERS)

    # Display character with fade-in animation
    if st.session_state.current_character:
        char = st.session_state.current_character
        
        st.markdown('<div class="character-card">', unsafe_allow_html=True)
        
        # Header row with Name
        st.subheader(f"Name: {char['name']}")
        
        # Threat level indicators with Streamlit's colored boxes
        if char['threat_level'] == 'extreme':
            st.error("⚠️ **THREAT LEVEL: EXTREME** - Proceed with absolute caution. Special Grade anomaly detected.")
        elif char['threat_level'] == 'high':
            st.warning("⚡ **THREAT LEVEL: HIGH** - Engaging is dangerous. Grade 1 equivalent.")
        elif char['threat_level'] == 'unpredictable':
            st.info("🃏 **THREAT LEVEL: UNPREDICTABLE** - Cannot calculate cursed energy output. Proceed with extreme caution.")
        elif char['threat_level'] == 'medium':
            st.warning("⚔️ **THREAT LEVEL: MEDIUM** - Formidable opponent. Grade 2 equivalent.")
        else:
            st.success("🛡️ **THREAT LEVEL: LOW** - Minor threat detected.")

        # Details
        st.markdown(f"**Grade:** {char['grade']}")
        st.markdown(f"**Cursed Technique:** <span class='technique-text'>{char['technique']}</span>", unsafe_allow_html=True)
        
        st.markdown("---")
        st.markdown(f"<div class='quote-text'>\"{char['quote']}\"</div>", unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Decorative toasts
        if char['name'] == "Ryomen Sukuna":
            st.toast("Malevolent Shrine activated...", icon="🔪")
        elif char['name'] == "Satoru Gojo":
            st.toast("Domain Expansion: Unlimited Void.", icon="♾️")
        elif char['name'] == "Kinji Hakari":
            st.toast("JACKPOT! Restless Gambler activated!", icon="🎰")
            st.balloons()
        elif char['name'] == "Fumihiko Takaba":
            st.toast("A wild scenario appears!", icon="🎭")
            st.snow()
            
if __name__ == "__main__":
    main()
