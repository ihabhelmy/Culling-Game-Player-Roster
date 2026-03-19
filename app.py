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

# --- CUSTOM CSS FOR DARK/JJK AESTHETIC ---
st.markdown(
    """
    <style>
    /* Main background */
    .stApp {
        background-color: #0e0e0e;
        color: #e0e0e0;
    }
    
    /* Headers */
    h1, h2, h3 {
        color: #ff3333 !important;
        font-family: 'Courier New', Courier, monospace;
        text-transform: uppercase;
        letter-spacing: 2px;
    }
    
    /* Button styling */
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
    }
    
    div.stButton > button:hover {
        background-color: #ff3333;
        color: #1a1a1a;
        border: 2px solid #ff3333;
        box-shadow: 0 0 15px #ff3333;
    }
    
    /* Container styling */
    .character-card {
        background-color: #1a1a1a;
        border: 1px solid #333;
        padding: 20px;
        border-radius: 5px;
        box-shadow: inset 0 0 10px #000;
        margin-top: 20px;
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
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- CHARACTER DATABASE ---
CHARACTERS = [
    {
        "name": "Ryomen Sukuna",
        "grade": "Special Grade",
        "technique": "Dismantle & Cleave / Malevolent Shrine",
        "quote": "Know your place, fool.",
        "threat_level": "extreme"
    },
    {
        "name": "Satoru Gojo",
        "grade": "Special Grade",
        "technique": "Limitless / Unlimited Void",
        "quote": "Throughout Heaven and Earth, I alone am the honored one.",
        "threat_level": "extreme"
    },
    {
        "name": "Yuta Okkotsu",
        "grade": "Special Grade",
        "technique": "Copy / Rika",
        "quote": "I'll kill Yuji Itadori myself.",
        "threat_level": "high"
    },
    {
        "name": "Hajime Kashimo",
        "grade": "Grade 1 (Equivalent)",
        "technique": "Mythical Beast Amber",
        "quote": "Turn up the volume! Because this is a funeral for the living!",
        "threat_level": "high"
    },
    {
        "name": "Hiromi Higuruma",
        "grade": "Grade 1 (Equivalent)",
        "technique": "Deadly Sentencing",
        "quote": "Ignorance of the law is no excuse.",
        "threat_level": "high"
    },
    {
        "name": "Megumi Fushiguro",
        "grade": "Grade 2",
        "technique": "Ten Shadows Technique",
        "quote": "I will save people unequally.",
        "threat_level": "medium"
    },
    {
        "name": "Kinji Hakari",
        "grade": "Grade 1 (Equivalent)",
        "technique": "Idle Death Gamble",
        "quote": "I love the fever.",
        "threat_level": "high"
    },
    {
        "name": "Fumihiko Takaba",
        "grade": "Unknown",
        "technique": "Comedian",
        "quote": "Wouldn't it be funny if...",
        "threat_level": "unpredictable"
    },
    {
        "name": "Maki Zenin",
        "grade": "Grade 4 (Officially) / Special Grade (Equivalent)",
        "technique": "Heavenly Restriction",
        "quote": "I'm going to destroy everything.",
        "threat_level": "extreme"
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
                time.sleep(0.8) # Add a slight delay for dramatic effect
                st.session_state.current_character = random.choice(CHARACTERS)

    # Display character
    if st.session_state.current_character:
        char = st.session_state.current_character
        
        st.markdown('<div class="character-card">', unsafe_allow_html=True)
        
        # Header row with Name
        st.subheader(f"Name: {char['name']}")
        
        # Threat level indicators (using Streamlit's colored message boxes)
        if char['threat_level'] == 'extreme':
            st.error(f"⚠️ **THREAT LEVEL: EXTREME** - Proceed with absolute caution.")
        elif char['threat_level'] == 'high':
            st.warning(f"⚡ **THREAT LEVEL: HIGH** - Engaging is dangerous.")
        elif char['threat_level'] == 'unpredictable':
            st.info(f"🃏 **THREAT LEVEL: UNPREDICTABLE** - Cannot calculate cursed energy output.")
        else:
            st.success(f"🛡️ **THREAT LEVEL: MODERATE**")

        # Details
        st.markdown(f"**Grade:** {char['grade']}")
        st.markdown(f"**Cursed Technique:** <span class='technique-text'>{char['technique']}</span>", unsafe_allow_html=True)
        
        st.markdown("---")
        st.markdown(f"<div class='quote-text'>\"{char['quote']}\"</div>", unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Add some decorative elements based on character
        if char['name'] == "Ryomen Sukuna":
            st.toast("Malevolent Shrine activated...", icon="🔪")
        elif char['name'] == "Satoru Gojo":
            st.toast("Domain Expansion: Unlimited Void.", icon="♾️")
        elif char['name'] == "Kinji Hakari":
            st.toast("JACKPOT!", icon="🎰")
            st.balloons()
            
if __name__ == "__main__":
    main()
