import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import time
import random
import json

# Perfect UI/UX Configuration
st.set_page_config(
    page_title="✨ Perfect Autism Helper",
    page_icon="🦄",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Ultra-Modern CSS with Perfect UX
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Fredoka+One:wght@400&display=swap');
    
    .stApp {
        font-family: 'Inter', sans-serif;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        background-attachment: fixed;
    }
    
    /* Glass Morphism Header */
    .glass-header {
        background: rgba(255, 255, 255, 0.25);
        backdrop-filter: blur(20px);
        border-radius: 30px;
        padding: 3rem 2rem;
        margin: 2rem 0;
        border: 1px solid rgba(255, 255, 255, 0.18);
        box-shadow: 0 8px 32px rgba(31, 38, 135, 0.37);
        text-align: center;
        color: white;
    }
    
    /* Floating Cards */
    .floating-card {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(20px);
        border-radius: 25px;
        padding: 2.5rem;
        margin: 1.5rem 0;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.1);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
    }
    
    .floating-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 25px 50px rgba(0, 0, 0, 0.15);
    }
    
    .floating-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.4), transparent);
        transition: left 0.5s;
    }
    
    .floating-card:hover::before {
        left: 100%;
    }
    
    /* Gradient Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 1rem 2.5rem;
        border-radius: 50px;
        font-weight: 600;
        font-size: 16px;
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.4);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
    }
    
    .stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 15px 40px rgba(102, 126, 234, 0.6);
        background: linear-gradient(135deg, #764ba2 0%, #667eea 100%);
    }
    
    /* Animated Navigation */
    .nav-container {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(20px);
        border-radius: 20px;
        padding: 1rem;
        margin: 1rem 0;
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    /* Progress Indicators */
    .progress-ring {
        width: 120px;
        height: 120px;
        margin: 1rem auto;
        position: relative;
    }
    
    .progress-ring svg {
        width: 100%;
        height: 100%;
        transform: rotate(-90deg);
    }
    
    .progress-ring circle {
        fill: none;
        stroke-width: 8;
        stroke-linecap: round;
    }
    
    .progress-ring .bg {
        stroke: rgba(255, 255, 255, 0.2);
    }
    
    .progress-ring .progress {
        stroke: #667eea;
        stroke-dasharray: 283;
        stroke-dashoffset: 283;
        animation: progress 2s ease-in-out forwards;
    }
    
    @keyframes progress {
        to {
            stroke-dashoffset: 0;
        }
    }
    
    /* Interactive Elements */
    .game-tile {
        background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%);
        border-radius: 20px;
        padding: 2rem;
        margin: 1rem;
        text-align: center;
        cursor: pointer;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        border: 2px solid transparent;
        position: relative;
        overflow: hidden;
    }
    
    .game-tile:hover {
        transform: scale(1.05);
        border-color: #667eea;
        box-shadow: 0 20px 40px rgba(255, 154, 158, 0.3);
    }
    
    .game-tile::after {
        content: '';
        position: absolute;
        top: 50%;
        left: 50%;
        width: 0;
        height: 0;
        background: rgba(255, 255, 255, 0.3);
        border-radius: 50%;
        transform: translate(-50%, -50%);
        transition: all 0.6s ease;
    }
    
    .game-tile:hover::after {
        width: 300px;
        height: 300px;
    }
    
    /* Status Indicators */
    .status-success {
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1rem 0;
        box-shadow: 0 10px 30px rgba(79, 172, 254, 0.3);
        animation: slideInUp 0.5s ease;
    }
    
    .status-warning {
        background: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1rem 0;
        box-shadow: 0 10px 30px rgba(250, 112, 154, 0.3);
        animation: slideInUp 0.5s ease;
    }
    
    @keyframes slideInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    /* Floating Action Button */
    .fab {
        position: fixed;
        bottom: 30px;
        right: 30px;
        width: 60px;
        height: 60px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-size: 24px;
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.4);
        cursor: pointer;
        transition: all 0.3s ease;
        z-index: 1000;
    }
    
    .fab:hover {
        transform: scale(1.1);
        box-shadow: 0 15px 40px rgba(102, 126, 234, 0.6);
    }
    
    /* Responsive Grid */
    .responsive-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 2rem;
        margin: 2rem 0;
    }
    
    /* Typography */
    h1, h2, h3 {
        font-weight: 600;
        color: #2d3748;
        margin-bottom: 1rem;
    }
    
    .title-gradient {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-family: 'Fredoka One', cursive;
        font-size: 3rem;
        text-align: center;
        margin: 2rem 0;
    }
    
    /* Loading Animation */
    .loading-spinner {
        width: 40px;
        height: 40px;
        border: 4px solid rgba(102, 126, 234, 0.3);
        border-top: 4px solid #667eea;
        border-radius: 50%;
        animation: spin 1s linear infinite;
        margin: 1rem auto;
    }
    
    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    
    /* Sidebar Styling */
    .css-1d391kg {
        background: linear-gradient(180deg, rgba(255, 255, 255, 0.1), rgba(255, 255, 255, 0.05));
        backdrop-filter: blur(20px);
    }
    
    /* Hide Streamlit Branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Custom Scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(135deg, #764ba2 0%, #667eea 100%);
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'home'
if 'user_data' not in st.session_state:
    st.session_state.user_data = {}
if 'game_progress' not in st.session_state:
    st.session_state.game_progress = {}
if 'game_results' not in st.session_state:
    st.session_state.game_results = []
if 'current_game_score' not in st.session_state:
    st.session_state.current_game_score = {'correct': 0, 'total': 0}

# Perfect Header
st.markdown("""
<div class="glass-header">
    <h1 class="title-gradient">🦄 Perfect Autism Helper</h1>
    <p style="font-size: 20px; margin: 0; opacity: 0.9;">Beautiful • Intuitive • Child-Friendly</p>
</div>
""", unsafe_allow_html=True)

# Navigation with Perfect UX
st.markdown('<div class="nav-container">', unsafe_allow_html=True)
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    if st.button("🏠 Home", key="nav_home"):
        st.session_state.current_page = 'home'

with col2:
    if st.button("👤 Profile", key="nav_profile"):
        st.session_state.current_page = 'profile'

with col3:
    if st.button("🎮 Games", key="nav_games"):
        st.session_state.current_page = 'games'

with col4:
    if st.button("📊 Results", key="nav_results"):
        st.session_state.current_page = 'results'

with col5:
    if st.button("🌟 Help", key="nav_help"):
        st.session_state.current_page = 'help'

st.markdown('</div>', unsafe_allow_html=True)

# Page Content with Perfect UX
if st.session_state.current_page == 'home':
    # Hero Section
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown('<div class="floating-card">', unsafe_allow_html=True)
        st.markdown("""
        <div style="text-align: center;">
            <div style="font-size: 4rem; margin: 1rem 0;">🌈</div>
            <h2>Welcome to Your Perfect Helper!</h2>
            <p style="font-size: 18px; color: #666; margin: 1rem 0;">
                A beautiful, safe space designed just for amazing kids like you!
            </p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Feature Grid
    st.markdown('<div class="responsive-grid">', unsafe_allow_html=True)
    
    # Feature 1
    st.markdown("""
    <div class="game-tile">
        <div style="font-size: 3rem; margin-bottom: 1rem;">🎨</div>
        <h3>Beautiful Design</h3>
        <p>Colorful, calming, and made just for you!</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Feature 2
    st.markdown("""
    <div class="game-tile">
        <div style="font-size: 3rem; margin-bottom: 1rem;">⚡</div>
        <h3>Super Fast</h3>
        <p>Lightning quick responses and smooth animations!</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Feature 3
    st.markdown("""
    <div class="game-tile">
        <div style="font-size: 3rem; margin-bottom: 1rem;">🛡️</div>
        <h3>Safe & Secure</h3>
        <p>Your privacy is protected like a treasure!</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.current_page == 'profile':
    st.markdown('<div class="floating-card">', unsafe_allow_html=True)
    st.markdown("### 👤 Create Your Perfect Profile")
    
    with st.form("perfect_profile"):
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Tell us about yourself! 🌟**")
            child_name = st.text_input("What's your name?", placeholder="Enter your beautiful name...")
            child_age = st.selectbox("How old are you?", [3, 4, 5, 6, 7, 8, 9, 10])
            favorite_color = st.selectbox("What's your favorite color?", [
                "💖 Pink", "💜 Purple", "💙 Blue", "💚 Green", "💛 Yellow", "🧡 Orange", "❤️ Red"
            ])
        
        with col2:
            st.markdown("**More about you! ✨**")
            favorite_animal = st.selectbox("Favorite animal?", [
                "🦄 Unicorn", "🐱 Cat", "🐶 Dog", "🐰 Bunny", "🦋 Butterfly", "🐸 Frog"
            ])
            favorite_activity = st.selectbox("What do you love doing?", [
                "🎨 Drawing", "📚 Reading", "🎵 Music", "🏃 Playing", "🧩 Puzzles", "🎮 Games"
            ])
            comfort_level = st.selectbox("How do you feel today?", [
                "😊 Super Happy", "🙂 Good", "😐 Okay", "😔 A bit sad", "😴 Sleepy"
            ])
        
        submitted = st.form_submit_button("🌈 Save My Perfect Profile!")
        
        if submitted:
            st.session_state.user_data = {
                'name': child_name,
                'age': child_age,
                'favorite_color': favorite_color,
                'favorite_animal': favorite_animal,
                'favorite_activity': favorite_activity,
                'comfort_level': comfort_level,
                'created_date': str(datetime.now())
            }
            
            st.markdown('<div class="status-success">', unsafe_allow_html=True)
            st.markdown(f"🎉 Welcome {child_name}! Your profile is perfect!")
            st.markdown('</div>', unsafe_allow_html=True)
            
            st.balloons()
    
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.current_page == 'games':
    if not st.session_state.user_data:
        st.markdown('<div class="floating-card">', unsafe_allow_html=True)
        st.markdown("### 🌟 Create your profile first to play games!")
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        child_name = st.session_state.user_data.get('name', 'Friend')
        
        st.markdown('<div class="floating-card">', unsafe_allow_html=True)
        st.markdown(f"### 🎮 Perfect Games for {child_name}!")
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Game Selection
        game_choice = st.selectbox("Choose your perfect game:", [
            "🌈 Color Matching Magic",
            "😊 Emotion Detective",
            "🔍 Shape Explorer",
            "🎵 Sound Safari"
        ])
        
        if game_choice == "🌈 Color Matching Magic":
            st.markdown('<div class="floating-card">', unsafe_allow_html=True)
            st.markdown("#### 🌈 Color Matching Magic")
            
            if st.button("✨ Start Color Magic!"):
                colors = ["💖 Pink", "💜 Purple", "💙 Blue", "💚 Green", "💛 Yellow"]
                target_color = random.choice(colors)
                
                st.markdown(f"### Find the color: {target_color}")
                
                # Create color options
                options = random.sample(colors, 3)
                if target_color not in options:
                    options[0] = target_color
                random.shuffle(options)
                
                selected = st.radio("Pick the matching color:", options, key="color_game")
                
                if st.button("🌟 Check My Answer!"):
                    correct = selected == target_color
                    
                    # Update game statistics
                    st.session_state.current_game_score['total'] += 1
                    if correct:
                        st.session_state.current_game_score['correct'] += 1
                    
                    # Store detailed result
                    game_result = {
                        'game': 'Color Matching',
                        'question': target_color,
                        'answer': selected,
                        'correct': correct,
                        'timestamp': str(datetime.now())
                    }
                    st.session_state.game_results.append(game_result)
                    
                    # Show immediate feedback with popup effect
                    if correct:
                        st.markdown('''
                        <div style="
                            position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%);
                            background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
                            color: white; padding: 2rem; border-radius: 20px;
                            box-shadow: 0 20px 60px rgba(79, 172, 254, 0.4);
                            z-index: 9999; text-align: center;
                            animation: popIn 0.5s ease;
                        ">
                            <div style="font-size: 3rem;">🎉</div>
                            <h2>CORRECT!</h2>
                            <p>You're a color wizard!</p>
                        </div>
                        <style>
                        @keyframes popIn {
                            0% { transform: translate(-50%, -50%) scale(0); }
                            100% { transform: translate(-50%, -50%) scale(1); }
                        }
                        </style>
                        ''', unsafe_allow_html=True)
                        st.balloons()
                    else:
                        st.markdown(f'''
                        <div style="
                            position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%);
                            background: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
                            color: white; padding: 2rem; border-radius: 20px;
                            box-shadow: 0 20px 60px rgba(250, 112, 154, 0.4);
                            z-index: 9999; text-align: center;
                            animation: popIn 0.5s ease;
                        ">
                            <div style="font-size: 3rem;">💭</div>
                            <h2>TRY AGAIN!</h2>
                            <p>The answer was {target_color}</p>
                            <p>You're learning great!</p>
                        </div>
                        ''', unsafe_allow_html=True)
                    
                    # Auto-hide popup after 3 seconds
                    time.sleep(3)
                    st.rerun()
            
            st.markdown('</div>', unsafe_allow_html=True)
        
        elif game_choice == "😊 Emotion Detective":
            st.markdown('<div class="floating-card">', unsafe_allow_html=True)
            st.markdown("#### 😊 Emotion Detective Game")
            
            if st.button("🕵️ Start Detective Work!"):
                emotions = {
                    "😊": "Happy",
                    "😢": "Sad",
                    "😠": "Angry",
                    "😨": "Scared",
                    "😴": "Sleepy"
                }
                
                emoji, emotion = random.choice(list(emotions.items()))
                st.markdown(f"### What emotion is this? {emoji}")
                
                emotion_options = list(emotions.values())
                selected_emotion = st.radio("Choose the emotion:", emotion_options, key="emotion_game")
                
                if st.button("🔍 Solve the Mystery!"):
                    correct = selected_emotion == emotion
                    
                    # Update game statistics
                    st.session_state.current_game_score['total'] += 1
                    if correct:
                        st.session_state.current_game_score['correct'] += 1
                    
                    # Store detailed result
                    game_result = {
                        'game': 'Emotion Detective',
                        'question': f"{emoji} - {emotion}",
                        'answer': selected_emotion,
                        'correct': correct,
                        'timestamp': str(datetime.now())
                    }
                    st.session_state.game_results.append(game_result)
                    
                    # Show immediate feedback with popup effect
                    if correct:
                        st.markdown('''
                        <div style="
                            position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%);
                            background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
                            color: white; padding: 2rem; border-radius: 20px;
                            box-shadow: 0 20px 60px rgba(79, 172, 254, 0.4);
                            z-index: 9999; text-align: center;
                            animation: popIn 0.5s ease;
                        ">
                            <div style="font-size: 3rem;">🕵️</div>
                            <h2>MYSTERY SOLVED!</h2>
                            <p>Amazing detective work!</p>
                        </div>
                        ''', unsafe_allow_html=True)
                        st.balloons()
                    else:
                        st.markdown(f'''
                        <div style="
                            position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%);
                            background: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
                            color: white; padding: 2rem; border-radius: 20px;
                            box-shadow: 0 20px 60px rgba(250, 112, 154, 0.4);
                            z-index: 9999; text-align: center;
                            animation: popIn 0.5s ease;
                        ">
                            <div style="font-size: 3rem;">🤔</div>
                            <h2>KEEP TRYING!</h2>
                            <p>That emotion was {emotion}</p>
                            <p>Great effort detective!</p>
                        </div>
                        ''', unsafe_allow_html=True)
                    
                    time.sleep(3)
                    st.rerun()
            
            st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.current_page == 'results':
    if not st.session_state.user_data:
        st.markdown('<div class="floating-card">', unsafe_allow_html=True)
        st.markdown("### 📊 Create your profile and play games to see results!")
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        child_name = st.session_state.user_data.get('name', 'Friend')
        
        st.markdown('<div class="floating-card">', unsafe_allow_html=True)
        st.markdown(f"### 📊 {child_name}'s Perfect Progress!")
        
        # Calculate honest results
        total_games = st.session_state.current_game_score['total']
        correct_answers = st.session_state.current_game_score['correct']
        success_rate = (correct_answers / total_games * 100) if total_games > 0 else 0
        
        # Progress Visualization with Real Data
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown(f"""
            <div style="text-align: center;">
                <div class="progress-ring">
                    <svg>
                        <circle class="bg" cx="60" cy="60" r="45"></circle>
                        <circle class="progress" cx="60" cy="60" r="45"></circle>
                    </svg>
                </div>
                <h4>🎮 Games Played</h4>
                <p style="font-size: 24px; font-weight: bold; color: #667eea;">{total_games}</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            color = "#4facfe" if success_rate >= 80 else "#fee140" if success_rate >= 60 else "#fa709a"
            st.markdown(f"""
            <div style="text-align: center;">
                <div class="progress-ring">
                    <svg>
                        <circle class="bg" cx="60" cy="60" r="45"></circle>
                        <circle class="progress" cx="60" cy="60" r="45"></circle>
                    </svg>
                </div>
                <h4>⭐ Success Rate</h4>
                <p style="font-size: 24px; font-weight: bold; color: {color};">{success_rate:.0f}%</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            achievements_earned = sum([total_games >= 1, success_rate >= 70, correct_answers >= 5])
            st.markdown(f"""
            <div style="text-align: center;">
                <div class="progress-ring">
                    <svg>
                        <circle class="bg" cx="60" cy="60" r="45"></circle>
                        <circle class="progress" cx="60" cy="60" r="45"></circle>
                    </svg>
                </div>
                <h4>🏆 Achievements</h4>
                <p style="font-size: 24px; font-weight: bold; color: #667eea;">{achievements_earned}</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Honest Game Results History
        if st.session_state.game_results:
            st.markdown('<div class="floating-card">', unsafe_allow_html=True)
            st.markdown("### 📊 Your Honest Game Results")
            
            for result in st.session_state.game_results[-5:]:  # Show last 5 results
                status_color = "#4facfe" if result['correct'] else "#fa709a"
                status_icon = "✅" if result['correct'] else "❌"
                
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, {status_color}20, {status_color}10); 
                            border-left: 4px solid {status_color};
                            padding: 1rem; margin: 0.5rem 0; border-radius: 10px;">
                    <strong>{status_icon} {result['game']}</strong><br>
                    <small>Question: {result['question']}</small><br>
                    <small>Your Answer: {result['answer']}</small>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown('</div>', unsafe_allow_html=True)
        
        # Real Achievements
        st.markdown('<div class="floating-card">', unsafe_allow_html=True)
        st.markdown("### 🏆 Your Real Achievements!")
        
        earned_achievements = []
        if total_games >= 1:
            earned_achievements.append("🌟 First Game Completed")
        if success_rate >= 70:
            earned_achievements.append("🎨 Super Learner")
        if correct_answers >= 5:
            earned_achievements.append("😊 Answer Champion")
        
        if earned_achievements:
            for achievement in earned_achievements:
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); 
                            padding: 1rem; margin: 0.5rem 0; border-radius: 15px; 
                            text-align: center; color: white; font-weight: bold;">
                    {achievement}
                </div>
                """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div style="background: linear-gradient(135deg, #fa709a 0%, #fee140 100%); 
                        padding: 1rem; margin: 0.5rem 0; border-radius: 15px; 
                        text-align: center; color: white; font-weight: bold;">
                🌟 Play games to earn achievements!
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.current_page == 'help':
    st.markdown('<div class="floating-card">', unsafe_allow_html=True)
    st.markdown("### 🌟 Help & Support")
    
    help_topics = [
        ("🎮 How to Play Games", "Click on games and follow the colorful instructions!"),
        ("👤 Creating Your Profile", "Tell us about yourself so we can make everything perfect for you!"),
        ("📊 Understanding Results", "See how amazing you're doing with pretty charts and colors!"),
        ("🛡️ Staying Safe", "We keep all your information safe and private!"),
        ("👨👩👧👦 For Parents", "This app helps understand your child's unique abilities!")
    ]
    
    for topic, description in help_topics:
        with st.expander(topic):
            st.markdown(f"**{description}**")
    
    st.markdown('</div>', unsafe_allow_html=True)

# Floating Action Button (simulated)
st.markdown("""
<div class="fab" onclick="window.scrollTo(0,0)">
    ↑
</div>
""", unsafe_allow_html=True)

# Perfect Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 2rem; 
            background: rgba(255, 255, 255, 0.1); 
            backdrop-filter: blur(20px); 
            border-radius: 20px; 
            margin: 2rem 0; 
            color: white;">
    <h3 style="margin: 0; color: white;">🦄 Perfect Autism Helper</h3>
    <p style="margin: 0.5rem 0; opacity: 0.8;">Made with 💖 for amazing kids everywhere</p>
    <p style="margin: 0; font-size: 14px; opacity: 0.7;">Beautiful • Safe • Perfect for You</p>
</div>
""", unsafe_allow_html=True)