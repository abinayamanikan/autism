import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import time
import random
import json

# Perfect Game UI Configuration
st.set_page_config(
    page_title="🎮 Perfect Game Center",
    page_icon="🌟",
    layout="wide"
)

# Game-focused CSS
st.markdown("""
<style>
    .stApp {
        font-family: 'Comic Sans MS', cursive;
        background: linear-gradient(45deg, #ff9a9e 0%, #fecfef 50%, #fecfef 100%);
    }
    
    .game-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 25px;
        color: white;
        text-align: center;
        margin: 1rem 0;
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);
    }
    
    .game-card {
        background: white;
        border-radius: 20px;
        padding: 2rem;
        margin: 1rem 0;
        box-shadow: 0 8px 25px rgba(0,0,0,0.1);
        border: 3px solid #ff69b4;
        transition: transform 0.3s ease;
    }
    
    .game-card:hover {
        transform: translateY(-5px);
    }
    
    .question-box {
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        color: white;
        padding: 2rem;
        border-radius: 20px;
        text-align: center;
        margin: 1rem 0;
        font-size: 1.5rem;
        box-shadow: 0 8px 25px rgba(79, 172, 254, 0.3);
    }
    
    .option-button {
        background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%);
        border: none;
        padding: 1rem 2rem;
        border-radius: 15px;
        margin: 0.5rem;
        font-size: 1.2rem;
        font-weight: bold;
        color: #333;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(255, 154, 158, 0.3);
    }
    
    .option-button:hover {
        transform: scale(1.05);
        box-shadow: 0 6px 20px rgba(255, 154, 158, 0.5);
    }
    
    .correct-popup {
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        color: white;
        padding: 3rem;
        border-radius: 25px;
        text-align: center;
        z-index: 9999;
        box-shadow: 0 20px 60px rgba(79, 172, 254, 0.4);
        animation: popIn 0.5s ease;
    }
    
    .wrong-popup {
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        background: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
        color: white;
        padding: 3rem;
        border-radius: 25px;
        text-align: center;
        z-index: 9999;
        box-shadow: 0 20px 60px rgba(250, 112, 154, 0.4);
        animation: popIn 0.5s ease;
    }
    
    @keyframes popIn {
        0% { transform: translate(-50%, -50%) scale(0); }
        100% { transform: translate(-50%, -50%) scale(1); }
    }
    
    .score-display {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1rem;
        border-radius: 15px;
        text-align: center;
        margin: 1rem 0;
        font-size: 1.2rem;
        font-weight: bold;
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #ff69b4, #ff1493);
        color: white;
        border: none;
        padding: 1rem 2rem;
        border-radius: 25px;
        font-size: 1.2rem;
        font-weight: bold;
        box-shadow: 0 6px 20px rgba(255, 105, 180, 0.4);
    }
</style>
""", unsafe_allow_html=True)

# Initialize game state
if 'game_session' not in st.session_state:
    st.session_state.game_session = {
        'current_game': None,
        'score': 0,
        'total_questions': 0,
        'current_question': 0,
        'questions': [],
        'game_active': False,
        'show_result': False,
        'last_answer': None
    }

if 'all_scores' not in st.session_state:
    st.session_state.all_scores = []

# Game Header
st.markdown("""
<div class="game-header">
    <h1>🎮 Perfect Game Center</h1>
    <p>Play, Learn, and Have Fun!</p>
</div>
""", unsafe_allow_html=True)

# Game Selection
game_type = st.selectbox("🌟 Choose Your Game:", [
    "🌈 Color Matching Challenge",
    "😊 Emotion Recognition Game", 
    "🔢 Number Memory Game",
    "🐶 Animal Sound Quiz"
])

# Color Matching Game
if game_type == "🌈 Color Matching Challenge":
    st.markdown('<div class="game-card">', unsafe_allow_html=True)
    st.markdown("### 🌈 Color Matching Challenge")
    
    col1, col2 = st.columns([2, 1])
    
    with col2:
        if st.session_state.game_session['game_active'] and st.session_state.game_session['current_game'] == 'color':
            st.markdown(f"""
            <div class="score-display">
                🎯 Score: {st.session_state.game_session['score']}/{st.session_state.game_session['total_questions']}<br>
                📊 Question: {st.session_state.game_session['current_question']}/{len(st.session_state.game_session['questions'])}
            </div>
            """, unsafe_allow_html=True)
    
    with col1:
        if not st.session_state.game_session['game_active']:
            num_questions = st.slider("Number of Questions:", 3, 10, 5)
            
            if st.button("🚀 Start Color Game!"):
                # Generate color questions
                colors = ["🔴 Red", "🔵 Blue", "🟢 Green", "🟡 Yellow", "🟣 Purple", "🟠 Orange"]
                questions = []
                
                for i in range(num_questions):
                    target = random.choice(colors)
                    options = random.sample(colors, 3)
                    if target not in options:
                        options[0] = target
                    random.shuffle(options)
                    
                    questions.append({
                        'target': target,
                        'options': options,
                        'answered': False
                    })
                
                st.session_state.game_session = {
                    'current_game': 'color',
                    'score': 0,
                    'total_questions': num_questions,
                    'current_question': 1,
                    'questions': questions,
                    'game_active': True,
                    'show_result': False,
                    'last_answer': None
                }
                st.rerun()
        
        else:
            # Show current question
            current_q = st.session_state.game_session['questions'][st.session_state.game_session['current_question'] - 1]
            
            if not current_q['answered']:
                st.markdown(f"""
                <div class="question-box">
                    Find the color: {current_q['target']}
                </div>
                """, unsafe_allow_html=True)
                
                # Answer options
                selected_answer = st.radio("Choose the correct color:", current_q['options'], key=f"color_q_{st.session_state.game_session['current_question']}")
                
                if st.button("✨ Submit Answer", key=f"submit_{st.session_state.game_session['current_question']}"):
                    correct = selected_answer == current_q['target']
                    
                    # Update score
                    if correct:
                        st.session_state.game_session['score'] += 1
                    
                    # Mark question as answered
                    current_q['answered'] = True
                    st.session_state.game_session['last_answer'] = {
                        'correct': correct,
                        'target': current_q['target'],
                        'selected': selected_answer
                    }
                    
                    st.rerun()
            
            else:
                # Show result popup
                if st.session_state.game_session['last_answer']:
                    result = st.session_state.game_session['last_answer']
                    
                    if result['correct']:
                        st.markdown("""
                        <div class="correct-popup">
                            <div style="font-size: 4rem;">🎉</div>
                            <h2>CORRECT!</h2>
                            <p>Amazing job!</p>
                        </div>
                        """, unsafe_allow_html=True)
                    else:
                        st.markdown(f"""
                        <div class="wrong-popup">
                            <div style="font-size: 4rem;">🤔</div>
                            <h2>TRY AGAIN!</h2>
                            <p>The answer was {result['target']}</p>
                            <p>You're learning great!</p>
                        </div>
                        """, unsafe_allow_html=True)
                
                # Next question or finish
                if st.session_state.game_session['current_question'] < len(st.session_state.game_session['questions']):
                    if st.button("➡️ Next Question"):
                        st.session_state.game_session['current_question'] += 1
                        st.session_state.game_session['last_answer'] = None
                        st.rerun()
                else:
                    if st.button("🏁 Finish Game"):
                        # Save final score
                        final_score = {
                            'game': 'Color Matching',
                            'score': st.session_state.game_session['score'],
                            'total': st.session_state.game_session['total_questions'],
                            'percentage': (st.session_state.game_session['score'] / st.session_state.game_session['total_questions']) * 100,
                            'timestamp': str(datetime.now())
                        }
                        st.session_state.all_scores.append(final_score)
                        
                        # Reset game
                        st.session_state.game_session = {
                            'current_game': None,
                            'score': 0,
                            'total_questions': 0,
                            'current_question': 0,
                            'questions': [],
                            'game_active': False,
                            'show_result': True,
                            'last_answer': None
                        }
                        st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

# Emotion Recognition Game
elif game_type == "😊 Emotion Recognition Game":
    st.markdown('<div class="game-card">', unsafe_allow_html=True)
    st.markdown("### 😊 Emotion Recognition Game")
    
    col1, col2 = st.columns([2, 1])
    
    with col2:
        if st.session_state.game_session['game_active'] and st.session_state.game_session['current_game'] == 'emotion':
            st.markdown(f"""
            <div class="score-display">
                🎯 Score: {st.session_state.game_session['score']}/{st.session_state.game_session['total_questions']}<br>
                📊 Question: {st.session_state.game_session['current_question']}/{len(st.session_state.game_session['questions'])}
            </div>
            """, unsafe_allow_html=True)
    
    with col1:
        if not st.session_state.game_session['game_active']:
            num_questions = st.slider("Number of Questions:", 3, 10, 5, key="emotion_slider")
            
            if st.button("🚀 Start Emotion Game!"):
                emotions = {
                    "😊": "Happy",
                    "😢": "Sad", 
                    "😠": "Angry",
                    "😨": "Scared",
                    "😴": "Sleepy",
                    "😮": "Surprised"
                }
                
                questions = []
                emotion_list = list(emotions.items())
                
                for i in range(num_questions):
                    target_emoji, target_emotion = random.choice(emotion_list)
                    options = random.sample(list(emotions.values()), 3)
                    if target_emotion not in options:
                        options[0] = target_emotion
                    random.shuffle(options)
                    
                    questions.append({
                        'emoji': target_emoji,
                        'target': target_emotion,
                        'options': options,
                        'answered': False
                    })
                
                st.session_state.game_session = {
                    'current_game': 'emotion',
                    'score': 0,
                    'total_questions': num_questions,
                    'current_question': 1,
                    'questions': questions,
                    'game_active': True,
                    'show_result': False,
                    'last_answer': None
                }
                st.rerun()
        
        else:
            # Show current question
            current_q = st.session_state.game_session['questions'][st.session_state.game_session['current_question'] - 1]
            
            if not current_q['answered']:
                emoji_display = current_q.get('emoji', '😊')
                st.markdown(f"""
                <div class="question-box">
                    <div style="font-size: 4rem; margin-bottom: 1rem;">{emoji_display}</div>
                    What emotion is this?
                </div>
                """, unsafe_allow_html=True)
                
                selected_answer = st.radio("Choose the emotion:", current_q['options'], key=f"emotion_q_{st.session_state.game_session['current_question']}")
                
                if st.button("✨ Submit Answer", key=f"emotion_submit_{st.session_state.game_session['current_question']}"):
                    correct = selected_answer == current_q['target']
                    
                    if correct:
                        st.session_state.game_session['score'] += 1
                    
                    current_q['answered'] = True
                    st.session_state.game_session['last_answer'] = {
                        'correct': correct,
                        'target': current_q['target'],
                        'selected': selected_answer,
                        'emoji': current_q['emoji']
                    }
                    
                    st.rerun()
            
            else:
                # Show result popup
                if st.session_state.game_session['last_answer']:
                    result = st.session_state.game_session['last_answer']
                    
                    if result['correct']:
                        st.markdown("""
                        <div class="correct-popup">
                            <div style="font-size: 4rem;">🎉</div>
                            <h2>PERFECT!</h2>
                            <p>You know emotions well!</p>
                        </div>
                        """, unsafe_allow_html=True)
                    else:
                        st.markdown(f"""
                        <div class="wrong-popup">
                            <div style="font-size: 4rem;">🤗</div>
                            <h2>GOOD TRY!</h2>
                            <p>{result['emoji']} was {result['target']}</p>
                            <p>Keep learning!</p>
                        </div>
                        """, unsafe_allow_html=True)
                
                # Navigation
                if st.session_state.game_session['current_question'] < len(st.session_state.game_session['questions']):
                    if st.button("➡️ Next Question", key="emotion_next"):
                        st.session_state.game_session['current_question'] += 1
                        st.session_state.game_session['last_answer'] = None
                        st.rerun()
                else:
                    if st.button("🏁 Finish Game", key="emotion_finish"):
                        final_score = {
                            'game': 'Emotion Recognition',
                            'score': st.session_state.game_session['score'],
                            'total': st.session_state.game_session['total_questions'],
                            'percentage': (st.session_state.game_session['score'] / st.session_state.game_session['total_questions']) * 100,
                            'timestamp': str(datetime.now())
                        }
                        st.session_state.all_scores.append(final_score)
                        
                        st.session_state.game_session = {
                            'current_game': None,
                            'score': 0,
                            'total_questions': 0,
                            'current_question': 0,
                            'questions': [],
                            'game_active': False,
                            'show_result': True,
                            'last_answer': None
                        }
                        st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

# Show Game Results
if st.session_state.game_session['show_result'] or st.session_state.all_scores:
    st.markdown('<div class="game-card">', unsafe_allow_html=True)
    st.markdown("### 🏆 Your Perfect Scores!")
    
    if st.session_state.all_scores:
        for i, score in enumerate(st.session_state.all_scores[-5:]):  # Show last 5 games
            percentage = score['percentage']
            
            if percentage >= 80:
                color = "#4facfe"
                emoji = "🌟"
                message = "Excellent!"
            elif percentage >= 60:
                color = "#fee140" 
                emoji = "👍"
                message = "Good job!"
            else:
                color = "#fa709a"
                emoji = "💪"
                message = "Keep practicing!"
            
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, {color}20, {color}10); 
                        border-left: 4px solid {color};
                        padding: 1rem; margin: 0.5rem 0; border-radius: 10px;">
                <strong>{emoji} {score['game']}</strong><br>
                Score: {score['score']}/{score['total']} ({percentage:.0f}%) - {message}<br>
                <small>Played: {score['timestamp'][:19]}</small>
            </div>
            """, unsafe_allow_html=True)
        
        # Overall statistics
        if len(st.session_state.all_scores) > 0:
            total_games = len(st.session_state.all_scores)
            avg_percentage = sum(s['percentage'] for s in st.session_state.all_scores) / total_games
            
            st.markdown(f"""
            <div class="score-display">
                📊 Total Games: {total_games}<br>
                🎯 Average Score: {avg_percentage:.1f}%<br>
                🏆 Best Game: {max(s['percentage'] for s in st.session_state.all_scores):.0f}%
            </div>
            """, unsafe_allow_html=True)
    else:
        st.info("🎮 Play some games to see your scores here!")
    
    st.markdown('</div>', unsafe_allow_html=True)

# Reset scores button
if st.session_state.all_scores:
    if st.button("🔄 Reset All Scores"):
        st.session_state.all_scores = []
        st.session_state.game_session = {
            'current_game': None,
            'score': 0,
            'total_questions': 0,
            'current_question': 0,
            'questions': [],
            'game_active': False,
            'show_result': False,
            'last_answer': None
        }
        st.rerun()