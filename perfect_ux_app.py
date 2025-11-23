import streamlit as st
import random
from datetime import datetime

# Perfect UX Configuration
st.set_page_config(
    page_title="🌟 Perfect Helper",
    page_icon="🎈",
    layout="centered"
)

# Modern UX CSS
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    }
    
    .main-container {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(20px);
        border-radius: 25px;
        padding: 2rem;
        margin: 1rem 0;
        box-shadow: 0 20px 40px rgba(0,0,0,0.1);
        border: 1px solid rgba(255,255,255,0.2);
    }
    
    .nav-button {
        background: linear-gradient(135deg, #ff6b6b, #4ecdc4);
        color: white;
        padding: 1rem 2rem;
        border-radius: 50px;
        border: none;
        font-size: 1.1rem;
        font-weight: 600;
        margin: 0.5rem;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 8px 25px rgba(255, 107, 107, 0.3);
    }
    
    .nav-button:hover {
        transform: translateY(-3px);
        box-shadow: 0 12px 35px rgba(255, 107, 107, 0.4);
    }
    
    .game-card {
        background: white;
        border-radius: 20px;
        padding: 2rem;
        margin: 1rem 0;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        transition: transform 0.3s ease;
        border: 2px solid transparent;
    }
    
    .game-card:hover {
        transform: translateY(-5px);
        border-color: #667eea;
    }
    
    .success-alert {
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        color: white;
        padding: 2rem;
        border-radius: 20px;
        text-align: center;
        margin: 1rem 0;
        animation: slideIn 0.5s ease;
    }
    
    .warning-alert {
        background: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
        color: white;
        padding: 2rem;
        border-radius: 20px;
        text-align: center;
        margin: 1rem 0;
        animation: slideIn 0.5s ease;
    }
    
    @keyframes slideIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .metric-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 15px;
        text-align: center;
        margin: 0.5rem 0;
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.3);
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 0.75rem 2rem;
        border-radius: 25px;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
    }
</style>
""", unsafe_allow_html=True)

# Safe initialization
def init_app():
    defaults = {
        'current_page': 'home',
        'user_name': '',
        'games_played': 0,
        'correct_count': 0,
        'game_results': [],
        'active_game': None,
        'game_state': {}
    }
    
    for key, default_value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = default_value

init_app()

# Header
st.markdown("""
<div class="main-container">
    <div style="text-align: center;">
        <h1 style="color: #667eea; margin-bottom: 0.5rem;">🎈 Perfect Helper</h1>
        <p style="color: #666; font-size: 1.2rem;">Beautiful • Simple • Safe</p>
    </div>
</div>
""", unsafe_allow_html=True)

# Navigation
st.markdown('<div class="main-container">', unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("🏠 Home", key="home_btn"):
        st.session_state.current_page = 'home'

with col2:
    if st.button("👋 Hello", key="hello_btn"):
        st.session_state.current_page = 'hello'

with col3:
    if st.button("🎮 Games", key="games_btn"):
        st.session_state.current_page = 'games'

with col4:
    if st.button("📊 Progress", key="progress_btn"):
        st.session_state.current_page = 'progress'

st.markdown('</div>', unsafe_allow_html=True)

# Page Content
if st.session_state.current_page == 'home':
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    st.markdown("### 🌟 Welcome!")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="game-card">
            <div style="text-align: center;">
                <div style="font-size: 3rem;">🎨</div>
                <h4>Beautiful Design</h4>
                <p>Modern and colorful interface made just for you!</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="game-card">
            <div style="text-align: center;">
                <div style="font-size: 3rem;">🛡️</div>
                <h4>100% Safe</h4>
                <p>No errors, no crashes, just pure fun!</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("#### 🚀 Quick Start:")
    st.markdown("""
    1. **👋 Say Hello** - Tell us your name (optional)
    2. **🎮 Play Games** - Fun learning activities
    3. **📊 Check Progress** - See your amazing results!
    """)
    
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.current_page == 'hello':
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    st.markdown("### 👋 Hello There!")
    
    if not st.session_state.user_name:
        st.markdown("#### What should we call you? 😊")
        
        name = st.text_input("Your name (optional):", placeholder="Type your name here...", key="name_input")
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("✨ Save Name", key="save_name"):
                if name.strip():
                    st.session_state.user_name = name.strip()
                    st.success(f"Nice to meet you, {name}! 🎉")
                    st.balloons()
                else:
                    st.warning("Please enter your name first! 😊")
        
        with col2:
            if st.button("⏭️ Skip for Now", key="skip_name"):
                st.session_state.user_name = "Friend"
                st.info("No problem! We'll call you Friend! 👋")
    
    else:
        greeting = f"Hello {st.session_state.user_name}!" if st.session_state.user_name != "Friend" else "Hello there, Friend!"
        
        st.markdown(f"""
        <div class="success-alert">
            <div style="font-size: 3rem;">🎉</div>
            <h2>{greeting}</h2>
            <p>Ready for some fun activities?</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("🎮 Let's Play!", key="start_games"):
                st.session_state.current_page = 'games'
                st.rerun()
        
        with col2:
            if st.button("🔄 Change Name", key="change_name"):
                st.session_state.user_name = ''
                st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.current_page == 'games':
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    
    display_name = st.session_state.user_name if st.session_state.user_name else "Friend"
    st.markdown(f"### 🎮 Games for {display_name}!")
    
    if not st.session_state.active_game:
        st.markdown("#### Choose Your Game:")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div class="game-card">
                <div style="text-align: center;">
                    <div style="font-size: 4rem;">🌈</div>
                    <h4>Color Match</h4>
                    <p>Find the matching colors!</p>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button("🌈 Play Color Game", key="start_color"):
                st.session_state.active_game = 'color'
                colors = ["🔴 Red", "🔵 Blue", "🟢 Green", "🟡 Yellow"]
                target = random.choice(colors)
                options = random.sample(colors, 3)
                if target not in options:
                    options[0] = target
                random.shuffle(options)
                
                st.session_state.game_state = {
                    'target': target,
                    'options': options,
                    'completed': False
                }
                st.rerun()
        
        with col2:
            st.markdown("""
            <div class="game-card">
                <div style="text-align: center;">
                    <div style="font-size: 4rem;">😊</div>
                    <h4>Emotion Match</h4>
                    <p>Learn about feelings!</p>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button("😊 Play Emotion Game", key="start_emotion"):
                st.session_state.active_game = 'emotion'
                emotions = {"😊": "Happy", "😢": "Sad", "😠": "Angry", "😴": "Sleepy"}
                emoji, name = random.choice(list(emotions.items()))
                options = list(emotions.values())
                random.shuffle(options)
                
                st.session_state.game_state = {
                    'emoji': emoji,
                    'target': name,
                    'options': options,
                    'completed': False
                }
                st.rerun()
    
    else:
        # Show active game
        if st.session_state.active_game == 'color' and not st.session_state.game_state.get('completed'):
            target = st.session_state.game_state['target']
            options = st.session_state.game_state['options']
            
            st.markdown(f"""
            <div class="game-card">
                <div style="text-align: center;">
                    <h3>🌈 Find This Color:</h3>
                    <div style="font-size: 2rem; margin: 1rem 0;">{target}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            selected = st.radio("Choose the correct color:", options, key="color_answer")
            
            if st.button("✅ Check Answer", key="check_color"):
                correct = selected == target
                st.session_state.games_played += 1
                
                if correct:
                    st.session_state.correct_count += 1
                
                result = {
                    'game': 'Color Match',
                    'correct': correct,
                    'target': target,
                    'answer': selected,
                    'time': datetime.now().strftime('%H:%M')
                }
                st.session_state.game_results.append(result)
                st.session_state.game_state['completed'] = True
                st.session_state.game_state['result'] = result
                st.rerun()
        
        elif st.session_state.active_game == 'emotion' and not st.session_state.game_state.get('completed'):
            emoji = st.session_state.game_state['emoji']
            target = st.session_state.game_state['target']
            options = st.session_state.game_state['options']
            
            st.markdown(f"""
            <div class="game-card">
                <div style="text-align: center;">
                    <h3>😊 What Feeling Is This?</h3>
                    <div style="font-size: 5rem; margin: 1rem 0;">{emoji}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            selected = st.radio("Choose the feeling:", options, key="emotion_answer")
            
            if st.button("✅ Check Answer", key="check_emotion"):
                correct = selected == target
                st.session_state.games_played += 1
                
                if correct:
                    st.session_state.correct_count += 1
                
                result = {
                    'game': 'Emotion Match',
                    'correct': correct,
                    'target': target,
                    'answer': selected,
                    'time': datetime.now().strftime('%H:%M')
                }
                st.session_state.game_results.append(result)
                st.session_state.game_state['completed'] = True
                st.session_state.game_state['result'] = result
                st.rerun()
        
        else:
            # Show result
            result = st.session_state.game_state.get('result', {})
            
            if result.get('correct'):
                st.markdown("""
                <div class="success-alert">
                    <div style="font-size: 4rem;">🎉</div>
                    <h2>PERFECT!</h2>
                    <p>You got it right! Amazing work!</p>
                </div>
                """, unsafe_allow_html=True)
                st.balloons()
            else:
                st.markdown(f"""
                <div class="warning-alert">
                    <div style="font-size: 4rem;">🌟</div>
                    <h2>Good Try!</h2>
                    <p>The answer was: {result.get('target', 'Unknown')}</p>
                    <p>You're learning so well!</p>
                </div>
                """, unsafe_allow_html=True)
            
            col1, col2 = st.columns(2)
            
            with col1:
                if st.button("🎮 Play Again", key="play_again"):
                    st.session_state.active_game = None
                    st.session_state.game_state = {}
                    st.rerun()
            
            with col2:
                if st.button("📊 See Progress", key="view_progress"):
                    st.session_state.current_page = 'progress'
                    st.session_state.active_game = None
                    st.session_state.game_state = {}
                    st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.current_page == 'progress':
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    
    display_name = st.session_state.user_name if st.session_state.user_name else "Friend"
    st.markdown(f"### 📊 {display_name}'s Progress")
    
    if st.session_state.games_played > 0:
        success_rate = (st.session_state.correct_count / st.session_state.games_played) * 100
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown(f"""
            <div class="metric-box">
                <div style="font-size: 2rem;">🎮</div>
                <h3>{st.session_state.games_played}</h3>
                <p>Games Played</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div class="metric-box">
                <div style="font-size: 2rem;">⭐</div>
                <h3>{st.session_state.correct_count}</h3>
                <p>Correct Answers</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown(f"""
            <div class="metric-box">
                <div style="font-size: 2rem;">📈</div>
                <h3>{success_rate:.0f}%</h3>
                <p>Success Rate</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Recent games
        st.markdown("#### 🎯 Recent Games:")
        for game in st.session_state.game_results[-5:]:
            icon = "✅" if game['correct'] else "🔄"
            color = "#4facfe" if game['correct'] else "#fa709a"
            
            st.markdown(f"""
            <div style="background: {color}20; border-left: 4px solid {color}; 
                        padding: 1rem; margin: 0.5rem 0; border-radius: 10px;">
                {icon} <strong>{game['game']}</strong> at {game['time']}<br>
                <small>Answer: {game['answer']}</small>
            </div>
            """, unsafe_allow_html=True)
        
        # Encouragement
        if success_rate >= 80:
            st.markdown("""
            <div class="success-alert">
                <div style="font-size: 3rem;">🏆</div>
                <h3>You're Amazing!</h3>
                <p>Fantastic work! Keep it up!</p>
            </div>
            """, unsafe_allow_html=True)
        elif success_rate >= 50:
            st.markdown("""
            <div class="warning-alert">
                <div style="font-size: 3rem;">🌟</div>
                <h3>Great Progress!</h3>
                <p>You're doing so well!</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="warning-alert">
                <div style="font-size: 3rem;">💪</div>
                <h3>Keep Learning!</h3>
                <p>Every game makes you stronger!</p>
            </div>
            """, unsafe_allow_html=True)
        
        if st.button("🔄 Reset Progress", key="reset_progress"):
            st.session_state.games_played = 0
            st.session_state.correct_count = 0
            st.session_state.game_results = []
            st.success("Progress reset! Ready for new adventures! 🚀")
            st.rerun()
    
    else:
        st.markdown("""
        <div style="text-align: center; padding: 3rem;">
            <div style="font-size: 5rem;">📊</div>
            <h3>No Progress Yet!</h3>
            <p style="font-size: 1.2rem;">Play some games to see your amazing progress!</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("🎮 Start Playing", key="start_playing"):
            st.session_state.current_page = 'games'
            st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="main-container">
    <div style="text-align: center; color: #666;">
        <h4 style="color: #667eea; margin-bottom: 0.5rem;">🎈 Perfect Helper</h4>
        <p style="margin: 0;">Beautiful • Error-Free • Made with 💖</p>
    </div>
</div>
""", unsafe_allow_html=True)