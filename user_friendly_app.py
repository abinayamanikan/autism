import streamlit as st
import random
from datetime import datetime

# Ultra user-friendly configuration
st.set_page_config(
    page_title="🌈 Friendly Helper",
    page_icon="😊",
    layout="wide"
)

# Super simple and friendly CSS
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(45deg, #ff9a9e 0%, #fecfef 50%, #fecfef 100%);
        font-family: 'Comic Sans MS', cursive;
    }
    
    .friendly-card {
        background: white;
        padding: 2rem;
        border-radius: 20px;
        margin: 1rem 0;
        box-shadow: 0 8px 25px rgba(0,0,0,0.1);
        border: 3px solid #ff69b4;
    }
    
    .big-button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1.5rem 3rem;
        border-radius: 25px;
        border: none;
        font-size: 1.3rem;
        font-weight: bold;
        margin: 1rem;
        cursor: pointer;
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.4);
    }
    
    .happy-message {
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        color: white;
        padding: 2rem;
        border-radius: 20px;
        text-align: center;
        margin: 1rem 0;
        font-size: 1.2rem;
    }
    
    .try-again-message {
        background: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
        color: white;
        padding: 2rem;
        border-radius: 20px;
        text-align: center;
        margin: 1rem 0;
        font-size: 1.2rem;
    }
    
    .score-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 15px;
        text-align: center;
        margin: 1rem 0;
        font-size: 1.3rem;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# Safe session state initialization
def safe_init():
    defaults = {
        'page': 'home',
        'user_name': '',
        'total_games': 0,
        'correct_answers': 0,
        'game_history': [],
        'current_game': None,
        'show_result': False,
        'last_result': None
    }
    
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

safe_init()

# Friendly header
st.markdown("""
<div class="friendly-card">
    <h1 style="text-align: center; color: #667eea;">😊 Super Friendly Helper</h1>
    <p style="text-align: center; font-size: 1.3rem; color: #666;">
        Safe • Simple • Fun for Everyone! 🌈
    </p>
</div>
""", unsafe_allow_html=True)

# Simple navigation
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("🏠 Home", key="nav_home", help="Go to main page"):
        st.session_state.page = 'home'
        st.session_state.show_result = False

with col2:
    if st.button("👋 Say Hello", key="nav_hello", help="Tell us your name"):
        st.session_state.page = 'hello'
        st.session_state.show_result = False

with col3:
    if st.button("🎮 Play Games", key="nav_games", help="Fun learning games"):
        st.session_state.page = 'games'
        st.session_state.show_result = False

with col4:
    if st.button("⭐ My Stars", key="nav_stars", help="See your progress"):
        st.session_state.page = 'stars'
        st.session_state.show_result = False

# Page content
if st.session_state.page == 'home':
    st.markdown('<div class="friendly-card">', unsafe_allow_html=True)
    st.markdown("### 🌟 Welcome to Your Friendly Helper!")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style="text-align: center; padding: 2rem;">
            <div style="font-size: 4rem;">🎨</div>
            <h3>Colorful & Fun</h3>
            <p>Everything is bright and happy!</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="text-align: center; padding: 2rem;">
            <div style="font-size: 4rem;">🛡️</div>
            <h3>Super Safe</h3>
            <p>We keep you safe and happy!</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("#### 🚀 How to Start:")
    st.markdown("""
    1. 👋 Click "Say Hello" to tell us your name
    2. 🎮 Click "Play Games" for fun activities  
    3. ⭐ Click "My Stars" to see how awesome you are!
    """)
    
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == 'hello':
    st.markdown('<div class="friendly-card">', unsafe_allow_html=True)
    st.markdown("### 👋 Hello There!")
    
    if not st.session_state.user_name:
        st.markdown("#### What's your name? 😊")
        
        name_input = st.text_input("Type your name here:", placeholder="Your awesome name...", key="name_input")
        
        if st.button("✨ That's My Name!", key="save_name"):
            if name_input.strip():
                st.session_state.user_name = name_input.strip()
                st.balloons()
                st.rerun()
            else:
                st.warning("Please type your name first! 😊")
    else:
        st.markdown(f"""
        <div class="happy-message">
            <div style="font-size: 3rem;">🎉</div>
            <h2>Hello {st.session_state.user_name}!</h2>
            <p>What a beautiful name! Ready to have some fun?</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("🎮 Let's Play Games!", key="go_to_games"):
            st.session_state.page = 'games'
            st.rerun()
        
        if st.button("🔄 Change My Name", key="change_name"):
            st.session_state.user_name = ''
            st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == 'games':
    st.markdown('<div class="friendly-card">', unsafe_allow_html=True)
    
    if st.session_state.user_name:
        st.markdown(f"### 🎮 Fun Games for {st.session_state.user_name}!")
    else:
        st.markdown("### 🎮 Fun Games for You!")
    
    if not st.session_state.show_result:
        # Game selection
        st.markdown("#### Choose Your Favorite Game:")
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("🌈 Color Fun", key="color_game", help="Match beautiful colors!"):
                st.session_state.current_game = 'color'
                st.session_state.show_result = True
                
                # Generate color game
                colors = ["🔴 Red", "🔵 Blue", "🟢 Green", "🟡 Yellow", "🟣 Purple"]
                target = random.choice(colors)
                options = random.sample(colors, 3)
                if target not in options:
                    options[0] = target
                random.shuffle(options)
                
                st.session_state.game_data = {
                    'target': target,
                    'options': options,
                    'answered': False
                }
                st.rerun()
        
        with col2:
            if st.button("😊 Happy Faces", key="emotion_game", help="Learn about feelings!"):
                st.session_state.current_game = 'emotion'
                st.session_state.show_result = True
                
                # Generate emotion game
                emotions = {"😊": "Happy", "😢": "Sad", "😠": "Mad", "😴": "Sleepy"}
                emoji, name = random.choice(list(emotions.items()))
                options = list(emotions.values())
                random.shuffle(options)
                
                st.session_state.game_data = {
                    'emoji': emoji,
                    'target': name,
                    'options': options,
                    'answered': False
                }
                st.rerun()
    
    else:
        # Show current game
        if st.session_state.current_game == 'color':
            st.markdown("#### 🌈 Color Matching Game")
            
            if not st.session_state.game_data.get('answered', True):
                target = st.session_state.game_data['target']
                options = st.session_state.game_data['options']
                
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); 
                           color: white; padding: 2rem; border-radius: 20px; 
                           text-align: center; font-size: 1.5rem; margin: 1rem 0;">
                    Find this color: <strong>{target}</strong>
                </div>
                """, unsafe_allow_html=True)
                
                selected = st.radio("Pick the right color:", options, key="color_choice")
                
                if st.button("✨ Check My Answer!", key="check_color"):
                    correct = selected == target
                    st.session_state.total_games += 1
                    
                    if correct:
                        st.session_state.correct_answers += 1
                    
                    # Save to history
                    result = {
                        'game': 'Color Game',
                        'correct': correct,
                        'target': target,
                        'answer': selected,
                        'time': datetime.now().strftime('%H:%M')
                    }
                    st.session_state.game_history.append(result)
                    st.session_state.last_result = result
                    st.session_state.game_data['answered'] = True
                    st.rerun()
            
            else:
                # Show result
                result = st.session_state.last_result
                if result and result['correct']:
                    st.markdown("""
                    <div class="happy-message">
                        <div style="font-size: 4rem;">🎉</div>
                        <h2>AMAZING!</h2>
                        <p>You got it right! You're so smart!</p>
                    </div>
                    """, unsafe_allow_html=True)
                    st.balloons()
                else:
                    st.markdown(f"""
                    <div class="try-again-message">
                        <div style="font-size: 4rem;">🤗</div>
                        <h2>Good Try!</h2>
                        <p>The answer was {result['target'] if result else 'something else'}</p>
                        <p>You're learning so well!</p>
                    </div>
                    """, unsafe_allow_html=True)
                
                if st.button("🎮 Play Again!", key="play_again_color"):
                    st.session_state.show_result = False
                    st.session_state.current_game = None
                    st.rerun()
        
        elif st.session_state.current_game == 'emotion':
            st.markdown("#### 😊 Happy Faces Game")
            
            if not st.session_state.game_data.get('answered', True):
                emoji = st.session_state.game_data['emoji']
                target = st.session_state.game_data['target']
                options = st.session_state.game_data['options']
                
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, #fa709a 0%, #fee140 100%); 
                           color: white; padding: 2rem; border-radius: 20px; 
                           text-align: center; margin: 1rem 0;">
                    <div style="font-size: 5rem;">{emoji}</div>
                    <h3>What feeling is this?</h3>
                </div>
                """, unsafe_allow_html=True)
                
                selected = st.radio("Choose the feeling:", options, key="emotion_choice")
                
                if st.button("✨ Check My Answer!", key="check_emotion"):
                    correct = selected == target
                    st.session_state.total_games += 1
                    
                    if correct:
                        st.session_state.correct_answers += 1
                    
                    # Save to history
                    result = {
                        'game': 'Emotion Game',
                        'correct': correct,
                        'target': target,
                        'answer': selected,
                        'time': datetime.now().strftime('%H:%M')
                    }
                    st.session_state.game_history.append(result)
                    st.session_state.last_result = result
                    st.session_state.game_data['answered'] = True
                    st.rerun()
            
            else:
                # Show result
                result = st.session_state.last_result
                if result and result['correct']:
                    st.markdown("""
                    <div class="happy-message">
                        <div style="font-size: 4rem;">🌟</div>
                        <h2>PERFECT!</h2>
                        <p>You know feelings so well!</p>
                    </div>
                    """, unsafe_allow_html=True)
                    st.balloons()
                else:
                    st.markdown(f"""
                    <div class="try-again-message">
                        <div style="font-size: 4rem;">💝</div>
                        <h2>Great Guess!</h2>
                        <p>That feeling was {result['target'] if result else 'something else'}</p>
                        <p>Keep learning - you're awesome!</p>
                    </div>
                    """, unsafe_allow_html=True)
                
                if st.button("🎮 Play Again!", key="play_again_emotion"):
                    st.session_state.show_result = False
                    st.session_state.current_game = None
                    st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == 'stars':
    st.markdown('<div class="friendly-card">', unsafe_allow_html=True)
    
    if st.session_state.user_name:
        st.markdown(f"### ⭐ {st.session_state.user_name}'s Amazing Stars!")
    else:
        st.markdown("### ⭐ Your Amazing Stars!")
    
    if st.session_state.total_games > 0:
        # Calculate stats
        success_rate = (st.session_state.correct_answers / st.session_state.total_games) * 100
        
        # Show stats
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown(f"""
            <div class="score-box">
                <div style="font-size: 2rem;">🎮</div>
                <h3>{st.session_state.total_games}</h3>
                <p>Games Played</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div class="score-box">
                <div style="font-size: 2rem;">⭐</div>
                <h3>{st.session_state.correct_answers}</h3>
                <p>Stars Earned</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown(f"""
            <div class="score-box">
                <div style="font-size: 2rem;">📈</div>
                <h3>{success_rate:.0f}%</h3>
                <p>Success Rate</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Recent games
        st.markdown("#### 🎯 Your Recent Games:")
        for game in st.session_state.game_history[-5:]:  # Last 5 games
            icon = "⭐" if game['correct'] else "💫"
            color = "#4facfe" if game['correct'] else "#fa709a"
            
            st.markdown(f"""
            <div style="background: {color}20; border-left: 4px solid {color}; 
                        padding: 1rem; margin: 0.5rem 0; border-radius: 10px;">
                {icon} <strong>{game['game']}</strong> at {game['time']}<br>
                <small>Your answer: {game['answer']}</small>
            </div>
            """, unsafe_allow_html=True)
        
        # Encouragement message
        if success_rate >= 80:
            st.markdown("""
            <div class="happy-message">
                <div style="font-size: 3rem;">🏆</div>
                <h3>You're a SUPERSTAR!</h3>
                <p>Amazing work! Keep being awesome!</p>
            </div>
            """, unsafe_allow_html=True)
        elif success_rate >= 50:
            st.markdown("""
            <div class="try-again-message">
                <div style="font-size: 3rem;">🌟</div>
                <h3>You're Doing Great!</h3>
                <p>Keep playing and learning!</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="try-again-message">
                <div style="font-size: 3rem;">💪</div>
                <h3>You're Learning!</h3>
                <p>Every try makes you stronger!</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Reset option
        if st.button("🔄 Start Fresh", key="reset_stars"):
            st.session_state.total_games = 0
            st.session_state.correct_answers = 0
            st.session_state.game_history = []
            st.success("Ready for new adventures! 🚀")
            st.rerun()
    
    else:
        st.markdown("""
        <div style="text-align: center; padding: 3rem;">
            <div style="font-size: 5rem;">🌟</div>
            <h3>No stars yet!</h3>
            <p style="font-size: 1.2rem;">Play some games to earn your first stars!</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("🎮 Let's Play!", key="go_play"):
            st.session_state.page = 'games'
            st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 1.5rem; background: rgba(255,255,255,0.2); border-radius: 15px;">
    <h3 style="color: #667eea; margin: 0;">😊 Super Friendly Helper</h3>
    <p style="margin: 0.5rem 0; color: #666;">Made with 💖 for amazing kids everywhere</p>
    <small style="color: #888;">Safe • Simple • Always Fun</small>
</div>
""", unsafe_allow_html=True)