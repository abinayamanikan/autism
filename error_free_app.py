import streamlit as st
import random
from datetime import datetime

# Error-free page config
st.set_page_config(
    page_title="Autism Helper App",
    page_icon="🌟",
    layout="wide"
)

# Simple CSS
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(45deg, #ff9a9e 0%, #fecfef 100%);
        font-family: 'Comic Sans MS', cursive;
    }
    
    .main-card {
        background: white;
        padding: 2rem;
        border-radius: 20px;
        margin: 1rem 0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    
    .game-button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1rem 2rem;
        border-radius: 15px;
        border: none;
        font-size: 1.1rem;
        margin: 0.5rem;
        cursor: pointer;
    }
    
    .result-box {
        padding: 1.5rem;
        border-radius: 15px;
        text-align: center;
        margin: 1rem 0;
        font-weight: bold;
    }
    
    .correct {
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        color: white;
    }
    
    .wrong {
        background: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state safely
def init_session_state():
    if 'scores' not in st.session_state:
        st.session_state.scores = []
    if 'current_score' not in st.session_state:
        st.session_state.current_score = 0
    if 'total_questions' not in st.session_state:
        st.session_state.total_questions = 0

init_session_state()

# Header
st.markdown("""
<div class="main-card">
    <h1 style="text-align: center; color: #667eea;">🌟 Autism Helper App</h1>
    <p style="text-align: center; font-size: 1.2rem;">Safe, Simple, and Fun!</p>
</div>
""", unsafe_allow_html=True)

# Navigation
page = st.selectbox("Choose Section:", ["🏠 Home", "🎮 Games", "📊 Results"])

if page == "🏠 Home":
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.markdown("### Welcome! 🌈")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **What we do:**
        - 🎮 Fun learning games
        - 📊 Track your progress
        - 🌟 Celebrate achievements
        - 🛡️ Keep you safe
        """)
    
    with col2:
        st.markdown("""
        **How to play:**
        1. Go to Games section
        2. Choose a game
        3. Answer questions
        4. See your results!
        """)
    
    st.markdown('</div>', unsafe_allow_html=True)

elif page == "🎮 Games":
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.markdown("### 🎮 Choose Your Game")
    
    game_type = st.radio("Pick a game:", ["🌈 Color Game", "😊 Emotion Game"])
    
    if game_type == "🌈 Color Game":
        st.markdown("#### 🌈 Color Matching Game")
        
        if st.button("🚀 Start Color Game"):
            colors = ["Red 🔴", "Blue 🔵", "Green 🟢", "Yellow 🟡"]
            target_color = random.choice(colors)
            
            st.markdown(f"**Find this color: {target_color}**")
            
            # Create options
            options = random.sample(colors, 3)
            if target_color not in options:
                options[0] = target_color
            random.shuffle(options)
            
            selected = st.radio("Choose:", options, key="color_choice")
            
            if st.button("Check Answer"):
                st.session_state.total_questions += 1
                
                if selected == target_color:
                    st.session_state.current_score += 1
                    st.markdown('<div class="result-box correct">🎉 Correct! Great job!</div>', unsafe_allow_html=True)
                    st.balloons()
                else:
                    st.markdown(f'<div class="result-box wrong">Good try! Answer was {target_color}</div>', unsafe_allow_html=True)
                
                # Save result
                result = {
                    'game': 'Color Game',
                    'correct': selected == target_color,
                    'score': st.session_state.current_score,
                    'total': st.session_state.total_questions,
                    'time': datetime.now().strftime('%H:%M:%S')
                }
                st.session_state.scores.append(result)
    
    elif game_type == "😊 Emotion Game":
        st.markdown("#### 😊 Emotion Recognition Game")
        
        if st.button("🚀 Start Emotion Game"):
            emotions = {
                "😊": "Happy",
                "😢": "Sad", 
                "😠": "Angry",
                "😴": "Sleepy"
            }
            
            emoji, emotion_name = random.choice(list(emotions.items()))
            st.markdown(f"**What emotion is this? {emoji}**")
            
            # Create options
            emotion_options = list(emotions.values())
            selected_emotion = st.radio("Choose emotion:", emotion_options, key="emotion_choice")
            
            if st.button("Check Emotion"):
                st.session_state.total_questions += 1
                
                if selected_emotion == emotion_name:
                    st.session_state.current_score += 1
                    st.markdown('<div class="result-box correct">🎉 Perfect! You know emotions!</div>', unsafe_allow_html=True)
                    st.balloons()
                else:
                    st.markdown(f'<div class="result-box wrong">Good guess! That was {emotion_name}</div>', unsafe_allow_html=True)
                
                # Save result
                result = {
                    'game': 'Emotion Game',
                    'correct': selected_emotion == emotion_name,
                    'score': st.session_state.current_score,
                    'total': st.session_state.total_questions,
                    'time': datetime.now().strftime('%H:%M:%S')
                }
                st.session_state.scores.append(result)
    
    # Current score display
    if st.session_state.total_questions > 0:
        percentage = (st.session_state.current_score / st.session_state.total_questions) * 100
        st.markdown(f"""
        <div class="main-card">
            <h4>Your Current Score: {st.session_state.current_score}/{st.session_state.total_questions} ({percentage:.0f}%)</h4>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

elif page == "📊 Results":
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.markdown("### 📊 Your Results")
    
    if st.session_state.scores:
        # Overall stats
        total_games = len(st.session_state.scores)
        correct_answers = sum(1 for score in st.session_state.scores if score['correct'])
        success_rate = (correct_answers / total_games) * 100 if total_games > 0 else 0
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("🎮 Games Played", total_games)
        with col2:
            st.metric("✅ Correct Answers", correct_answers)
        with col3:
            st.metric("📈 Success Rate", f"{success_rate:.0f}%")
        
        # Recent results
        st.markdown("#### 📋 Recent Games")
        for i, result in enumerate(st.session_state.scores[-5:]):  # Last 5 results
            status = "✅" if result['correct'] else "❌"
            color = "#4facfe" if result['correct'] else "#fa709a"
            
            st.markdown(f"""
            <div style="background: {color}20; border-left: 4px solid {color}; 
                        padding: 1rem; margin: 0.5rem 0; border-radius: 8px;">
                {status} <strong>{result['game']}</strong><br>
                Score: {result['score']}/{result['total']} at {result['time']}
            </div>
            """, unsafe_allow_html=True)
        
        # Performance message
        if success_rate >= 80:
            st.success("🌟 Excellent work! You're doing amazing!")
        elif success_rate >= 60:
            st.info("👍 Good job! Keep practicing!")
        else:
            st.warning("💪 Keep trying! Every attempt makes you better!")
        
        # Reset button
        if st.button("🔄 Reset Scores"):
            st.session_state.scores = []
            st.session_state.current_score = 0
            st.session_state.total_questions = 0
            st.success("Scores reset! Ready for new games!")
            st.rerun()
    
    else:
        st.info("🎮 Play some games to see your results here!")
    
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 1rem; color: #667eea;">
    <strong>🌟 Autism Helper App</strong><br>
    <small>Safe • Fun • Educational</small>
</div>
""", unsafe_allow_html=True)