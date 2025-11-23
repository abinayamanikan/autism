import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import joblib
import os
import time

# Super kid-friendly config
st.set_page_config(
    page_title="🌟 Magic Helper for Kids",
    page_icon="🦄",
    layout="wide"
)

# Super colorful CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Fredoka+One:wght@400&family=Nunito:wght@400;600;700&display=swap');
    
    .stApp {
        font-family: 'Nunito', sans-serif;
        background: linear-gradient(45deg, #ff9a9e 0%, #fecfef 25%, #fecfef 50%, #a8edea 75%, #fed6e3 100%);
        background-size: 400% 400%;
        animation: gradientShift 8s ease infinite;
    }
    
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    .magic-title {
        font-family: 'Fredoka One', cursive;
        background: linear-gradient(45deg, #ff6b6b, #4ecdc4, #45b7d1, #96ceb4, #feca57, #ff9ff3);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-size: 4rem;
        text-align: center;
        margin: 2rem 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        animation: bounce 2s ease-in-out infinite alternate;
    }
    
    @keyframes bounce {
        0% { transform: translateY(0px); }
        100% { transform: translateY(-10px); }
    }
    
    .fun-bubble {
        background: rgba(255,255,255,0.9);
        border-radius: 30px;
        padding: 2rem;
        margin: 1rem 0;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        border: 4px solid;
        border-image: linear-gradient(45deg, #ff6b6b, #4ecdc4, #feca57) 1;
        animation: float 3s ease-in-out infinite;
    }
    
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-5px); }
    }
    
    .question-magic {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 2rem;
        border-radius: 25px;
        margin: 1.5rem 0;
        box-shadow: 0 8px 25px rgba(102,126,234,0.4);
        font-size: 1.2rem;
        animation: pulse 2s ease-in-out infinite;
    }
    
    @keyframes pulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.02); }
    }
    
    .super-happy {
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        color: white;
        padding: 2.5rem;
        border-radius: 30px;
        text-align: center;
        margin: 2rem 0;
        box-shadow: 0 15px 35px rgba(79,172,254,0.4);
        animation: celebrate 1s ease-in-out;
    }
    
    @keyframes celebrate {
        0% { transform: scale(0.8); opacity: 0; }
        100% { transform: scale(1); opacity: 1; }
    }
    
    .super-careful {
        background: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
        color: white;
        padding: 2.5rem;
        border-radius: 30px;
        text-align: center;
        margin: 2rem 0;
        box-shadow: 0 15px 35px rgba(250,112,154,0.4);
        animation: celebrate 1s ease-in-out;
    }
    
    .stButton > button {
        background: linear-gradient(90deg, #ff6b6b, #4ecdc4, #feca57);
        color: white;
        border: none;
        padding: 1.5rem 3rem;
        border-radius: 50px;
        font-weight: bold;
        font-size: 1.5rem;
        font-family: 'Fredoka One', cursive;
        box-shadow: 0 8px 25px rgba(255,107,107,0.4);
        transition: all 0.3s;
        animation: buttonGlow 2s ease-in-out infinite alternate;
    }
    
    @keyframes buttonGlow {
        0% { box-shadow: 0 8px 25px rgba(255,107,107,0.4); }
        100% { box-shadow: 0 12px 35px rgba(255,107,107,0.6); }
    }
    
    .stButton > button:hover {
        transform: translateY(-5px) scale(1.05);
        box-shadow: 0 15px 40px rgba(255,107,107,0.6);
    }
    
    .emoji-huge {
        font-size: 5rem;
        text-align: center;
        margin: 2rem 0;
        animation: spin 3s linear infinite;
    }
    
    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    
    .magic-card {
        background: rgba(255,255,255,0.95);
        border-radius: 25px;
        padding: 2rem;
        text-align: center;
        margin: 1rem 0;
        border: 3px solid;
        border-image: linear-gradient(45deg, #4ecdc4, #44a08d) 1;
        box-shadow: 0 10px 30px rgba(78,205,196,0.3);
        animation: wiggle 4s ease-in-out infinite;
    }
    
    @keyframes wiggle {
        0%, 100% { transform: rotate(0deg); }
        25% { transform: rotate(1deg); }
        75% { transform: rotate(-1deg); }
    }
    
    .progress-rainbow {
        background: rgba(255,255,255,0.9);
        border-radius: 20px;
        padding: 2rem;
        margin: 1rem 0;
        border: 3px solid #feca57;
        animation: rainbow-border 3s linear infinite;
    }
    
    @keyframes rainbow-border {
        0% { border-color: #ff6b6b; }
        16% { border-color: #feca57; }
        33% { border-color: #48dbfb; }
        50% { border-color: #ff9ff3; }
        66% { border-color: #54a0ff; }
        83% { border-color: #5f27cd; }
        100% { border-color: #ff6b6b; }
    }
    
    h1, h2, h3 {
        font-family: 'Fredoka One', cursive;
        color: #ff6b6b;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

# Animated title
st.markdown('<h1 class="magic-title">🦄 Super Magic Helper for Amazing Kids! 🌟</h1>', unsafe_allow_html=True)

# Fun navigation with emojis
page = st.selectbox(
    "🎈 Pick Your Magical Adventure!",
    ["🏠 Magic Home", "🎯 Fun Question Game", "🤖 Train Magic Robot", "📚 Cool Stuff to Know"],
    index=0
)

if page == "🏠 Magic Home":
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="magic-card">
            <div class="emoji-huge">🎨</div>
            <h3>Super Colorful!</h3>
            <p>Everything is bright and fun just for you!</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="magic-card">
            <div class="emoji-huge">⚡</div>
            <h3>Lightning Fast!</h3>
            <p>Faster than eating your favorite candy!</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="magic-card">
            <div class="emoji-huge">🛡️</div>
            <h3>Super Safe!</h3>
            <p>Your answers are safe like a treasure chest!</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('<div class="fun-bubble">', unsafe_allow_html=True)
    st.markdown("""
    ### 🌟 Welcome to the Most Amazing Helper Ever!
    
    Hi there, awesome kid! This is a super special magical tool that helps grown-ups understand how incredible and unique you are! 
    
    **🎯 What Makes This So Cool:**
    - 🎮 It's like playing a fun question game!
    - 🤖 A smart robot friend helps figure things out
    - 🌈 Everything is colorful and exciting
    - ✨ You get to learn about yourself!
    
    **🦄 Super Important Stuff:**
    - You are AMAZING exactly as you are! 🌟
    - This is just a fun helper - not a doctor
    - Grown-ups will talk to real doctors about important things
    - You are the most special person in the whole world! 💖
    
    **🎈 Ready for an Adventure?**
    Click the big colorful button below to start your magical journey!
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    if st.button("🚀 Start My Magical Adventure!", key="home_start"):
        st.balloons()
        time.sleep(1)
        st.snow()

elif page == "🎯 Fun Question Game":
    st.markdown("### 🎯 Let's Play the Super Fun Question Game!")
    st.markdown("*Answer these magical questions about how you like to play and explore the world!*")
    
    with st.form("super_kids_game"):
        # Kid info with fun styling
        st.markdown('<div class="fun-bubble">', unsafe_allow_html=True)
        st.markdown("#### 🎂 Tell Me About You!")
        
        col1, col2 = st.columns(2)
        with col1:
            child_age = st.number_input("🎂 How many candles on your birthday cake?", min_value=2, max_value=18, value=6)
        with col2:
            child_gender = st.selectbox("👦👧 Are you a...", ["Amazing Girl", "Awesome Boy", "Super Cool Kid"])
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Super fun questions with animations
        magical_questions = [
            ("🔊", "You hear tiny sounds that others might miss (like a mouse walking!)"),
            ("🖼️", "You like looking at the whole picture instead of tiny pieces"),
            ("🎪", "You can do lots of things at once (like drawing while singing!)"),
            ("🔄", "If someone stops you, you can jump right back to what you were doing"),
            ("💭", "You understand secret messages when people talk"),
            ("😴", "You know when someone is getting sleepy or bored"),
            ("📖", "When you read stories, it's hard to guess what characters are thinking"),
            ("📚", "You LOVE collecting cool facts about your favorite things"),
            ("😊", "You can tell how people feel just by looking at their faces"),
            ("🤔", "Sometimes it's tricky to know what people really want")
        ]
        
        answers = []
        for i, (emoji, question) in enumerate(magical_questions, 1):
            st.markdown(f"""
            <div class="question-magic">
                <strong>{emoji} Magic Question {i}:</strong><br>
                {question}
            </div>
            """, unsafe_allow_html=True)
            
            answer = st.radio(
                f"Q{i}",
                ["❌ Nope, not really!", "✅ Yes, that's totally me!"],
                key=f"magic_q{i}",
                horizontal=True,
                label_visibility="collapsed"
            )
            answers.append(1 if answer == "✅ Yes, that's totally me!" else 0)
        
        st.markdown("---")
        
        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown("### 🎉 Ready to See Your Magical Results?")
            st.markdown("Click the super sparkly button to discover your magic!")
        
        with col2:
            submitted = st.form_submit_button("✨ Show Me My Magic Results!", use_container_width=True)
        
        if submitted:
            if os.path.exists("model.pkl"):
                model = joblib.load("model.pkl")
                gender_code = 1 if child_gender == "Awesome Boy" else 0
                data = [answers + [child_age, gender_code]]
                
                prediction = model.predict(data)[0]
                probability = model.predict_proba(data)[0]
                
                st.markdown("---")
                st.markdown("### 🎊 Your Super Special Magic Results!")
                
                # Fun loading animation
                progress_bar = st.progress(0)
                for i in range(100):
                    progress_bar.progress(i + 1)
                    time.sleep(0.01)
                
                if prediction == 1:
                    st.markdown(f"""
                    <div class="super-careful">
                        <div class="emoji-huge">🌟</div>
                        <h2>You Are Extra Super Special!</h2>
                        <p><strong>🎯 Magic Score:</strong> {probability[1]:.0%} sparkles!</p>
                        <p><strong>🦄 What This Means:</strong> You have a wonderfully unique and magical way of seeing the world!</p>
                        <p><strong>🌈 Next Adventure:</strong> A friendly doctor who knows about special kids wants to meet you!</p>
                        <p><strong>✨ Remember:</strong> Being different makes you absolutely AMAZING! 🌟</p>
                        <p><strong>🎈 You Are:</strong> Creative, Smart, Wonderful, and Perfect just as you are!</p>
                    </div>
                    """, unsafe_allow_html=True)
                    st.balloons()
                else:
                    st.markdown(f"""
                    <div class="super-happy">
                        <div class="emoji-huge">🎈</div>
                        <h2>You Are Wonderfully Amazing!</h2>
                        <p><strong>🎯 Magic Score:</strong> {probability[0]:.0%} sparkles!</p>
                        <p><strong>🦄 What This Means:</strong> You have typical magical powers like many other awesome kids!</p>
                        <p><strong>🌈 Keep Doing:</strong> Being your incredible self and having fun every day!</p>
                        <p><strong>✨ Remember:</strong> You are special, loved, and absolutely perfect! 🌟</p>
                        <p><strong>🎪 You Are:</strong> Smart, Kind, Funny, and Amazing in every way!</p>
                    </div>
                    """, unsafe_allow_html=True)
                    st.snow()
                
                # Fun score display
                total_score = sum(answers)
                st.markdown(f"### 🌟 Your Awesome Score: {total_score}/10 Magic Stars! ⭐")
                
                # Celebration
                if total_score >= 5:
                    st.markdown("🎉 WOW! You got lots of stars! You're incredible!")
                else:
                    st.markdown("🎈 Great job answering all the questions! You're amazing!")
                
            else:
                st.error("🤖 Oops! Our magic robot friend needs to learn first! Let's go teach it!")

elif page == "🤖 Train Magic Robot":
    st.markdown("### 🤖 Let's Teach Our Robot Friend!")
    
    st.markdown('<div class="fun-bubble">', unsafe_allow_html=True)
    st.markdown("#### 🎓 Robot Learning School")
    
    col1, col2 = st.columns(2)
    with col1:
        if os.path.exists("model.pkl"):
            st.success("✅ **Robot Status:** Super smart and ready!")
            st.info("🧠 **Robot Brain:** Fully charged with knowledge!")
        else:
            st.warning("⚠️ **Robot Status:** Still in robot school...")
            st.error("🎯 **Mission:** Teach our robot friend!")
    
    with col2:
        st.markdown("""
        **🎪 How Our Robot Learns:**
        - 🧠 Robot has a super smart brain
        - 📚 We teach it with 1000 practice examples
        - 🎯 It gets really good at helping kids
        - ⚡ Then it can help you super fast!
        """)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    if st.button("🎪 Teach Our Robot Friend Everything!", use_container_width=True):
        st.markdown('<div class="progress-rainbow">', unsafe_allow_html=True)
        
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        # Super fun training messages
        messages = [
            "🎨 Creating rainbow practice examples...",
            "🦄 Teaching robot about unicorns and magic...",
            "🌟 Showing robot how amazing kids are...",
            "🎈 Robot is learning super fast...",
            "🤖 Robot brain getting smarter...",
            "💾 Saving robot's new superpowers..."
        ]
        
        np.random.seed(42)
        training_data, labels = [], []
        
        for i, message in enumerate(messages):
            status_text.text(message)
            progress_bar.progress((i + 1) * 15)
            time.sleep(0.5)
        
        for _ in range(1000):
            special_kid = np.random.choice([0, 1], p=[0.7, 0.3])
            
            if special_kid:
                features = [
                    np.random.choice([0, 1], p=[0.3, 0.7]),
                    np.random.choice([0, 1], p=[0.7, 0.3]),
                    np.random.choice([0, 1], p=[0.7, 0.3]),
                    np.random.choice([0, 1], p=[0.7, 0.3]),
                    np.random.choice([0, 1], p=[0.8, 0.2]),
                    np.random.choice([0, 1], p=[0.8, 0.2]),
                    np.random.choice([0, 1], p=[0.2, 0.8]),
                    np.random.choice([0, 1], p=[0.2, 0.8]),
                    np.random.choice([0, 1], p=[0.8, 0.2]),
                    np.random.choice([0, 1], p=[0.2, 0.8]),
                    np.random.randint(2, 18),
                    np.random.choice([0, 1])
                ]
            else:
                features = [
                    np.random.choice([0, 1], p=[0.7, 0.3]),
                    np.random.choice([0, 1], p=[0.3, 0.7]),
                    np.random.choice([0, 1], p=[0.3, 0.7]),
                    np.random.choice([0, 1], p=[0.3, 0.7]),
                    np.random.choice([0, 1], p=[0.2, 0.8]),
                    np.random.choice([0, 1], p=[0.2, 0.8]),
                    np.random.choice([0, 1], p=[0.8, 0.2]),
                    np.random.choice([0, 1], p=[0.7, 0.3]),
                    np.random.choice([0, 1], p=[0.2, 0.8]),
                    np.random.choice([0, 1], p=[0.8, 0.2]),
                    np.random.randint(2, 18),
                    np.random.choice([0, 1])
                ]
            
            training_data.append(features)
            labels.append(special_kid)
        
        progress_bar.progress(90)
        status_text.text("🎉 Robot graduated from school!")
        
        model = RandomForestClassifier(n_estimators=50, random_state=42)
        model.fit(training_data, labels)
        
        joblib.dump(model, "model.pkl")
        
        progress_bar.progress(100)
        status_text.text("🎊 Robot is now your super smart friend!")
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.success("🎉 **HOORAY!** Our robot friend learned everything and is ready to help!")
        st.balloons()
        time.sleep(1)
        st.snow()

else:  # Learn More page
    st.markdown("### 📚 Super Cool Stuff to Learn!")
    
    tab1, tab2, tab3 = st.tabs(["🌈 For Amazing Kids", "👨👩👧👦 For Super Parents", "⚠️ Grown-Up Stuff"])
    
    with tab1:
        st.markdown('<div class="fun-bubble">', unsafe_allow_html=True)
        st.markdown("""
        #### 🌟 Hey There, Awesome Kid!
        
        **🎯 What is this super cool thing?**
        - It's like the most fun game ever that asks about how you play!
        - A magical robot friend helps figure out what makes you special
        - It helps grown-ups understand how absolutely amazing you are!
        
        **🎨 Why are some kids different and that's AWESOME?**
        - Every kid's brain is like a unique snowflake - no two are the same! ❄️
        - Some kids are like detectives and notice EVERYTHING 🔍
        - Some kids become experts on dinosaurs, trains, or space! 🦕🚂🚀
        - Some kids need quiet time to recharge their superpowers 🔋
        - ALL kids make the world more colorful and amazing! 🌈
        
        **🤗 The Most Important Things to Remember:**
        - You are absolutely perfect exactly as you are! ✨
        - Being different is like having superpowers! 🦸‍♀️🦸‍♂️
        - Ask questions about anything - curiosity is awesome! 🤔
        - Grown-ups love you SO much and want to help you shine! 💖
        - You make the world a better place just by being YOU! 🌟
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with tab2:
        st.markdown('<div class="fun-bubble">', unsafe_allow_html=True)
        st.markdown("""
        #### 👨👩👧👦 Information for Families
        
        **🎯 Child-Centered Design Philosophy:**
        - Reduces assessment anxiety through playful presentation
        - Uses positive, strength-based language
        - Celebrates neurodiversity and individual differences
        - Creates safe, non-judgmental screening environment
        
        **🌈 What Makes This Kid-Friendly:**
        - Bright, engaging animations and colors
        - Simple, age-appropriate language
        - Gamified question format
        - Immediate positive reinforcement
        - Focus on uniqueness rather than deficits
        
        **📋 Assessment Areas (Kid-Friendly Version):**
        - Sensory experiences ("hearing tiny sounds")
        - Attention patterns ("whole picture vs details")
        - Cognitive flexibility ("doing lots of things at once")
        - Social communication ("understanding secret messages")
        - Special interests ("collecting cool facts")
        
        **🔍 Supporting Your Child:**
        - Participate together in a relaxed setting
        - Emphasize that there are no "wrong" answers
        - Celebrate their uniqueness regardless of results
        - Use results as starting point for understanding, not labeling
        - Follow up with professionals if indicated
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with tab3:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #fff3cd 0%, #ffeaa7 100%); border: 3px solid #fdcb6e; color: #2d3436; padding: 2rem; border-radius: 25px; margin: 1rem 0;">
            <h4>⚠️ IMPORTANT INFORMATION FOR CAREGIVERS</h4>
            
            <p><strong>🏥 This is a child-friendly screening tool only</strong></p>
            <ul>
                <li><strong>Educational Purpose:</strong> Designed to introduce autism awareness in age-appropriate way</li>
                <li><strong>Not Diagnostic:</strong> Professional evaluation required for any clinical decisions</li>
                <li><strong>Positive Framing:</strong> Emphasizes strengths and neurodiversity acceptance</li>
                <li><strong>Family Tool:</strong> Best used as conversation starter between families and professionals</li>
                <li><strong>Synthetic Training:</strong> Model uses simulated data - not clinically validated</li>
            </ul>
            
            <p><strong>🌟 Remember: Every child is wonderfully unique and deserves celebration!</strong></p>
        </div>
        """, unsafe_allow_html=True)

# Super fun footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; background: linear-gradient(90deg, #ff6b6b, #4ecdc4, #45b7d1, #feca57, #ff9ff3); color: white; padding: 2rem; border-radius: 30px; margin: 2rem 0; animation: rainbow-border 3s linear infinite;">
    <h2 style="font-family: 'Fredoka One', cursive; margin: 0;">🦄 Super Magic Helper for Amazing Kids! 🌟</h2>
    <p style="font-size: 18px; margin: 0.5rem 0;">Making learning about yourself the most fun adventure ever!</p>
    <p style="font-size: 16px; margin: 0;">Remember: You are magical, special, and absolutely perfect! ✨🌈✨</p>
</div>
""", unsafe_allow_html=True)