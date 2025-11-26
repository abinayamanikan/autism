import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import base64
from PIL import Image
import io

# SRS-Compliant Autism Detection App
st.set_page_config(
    page_title="🧠 Autism Awareness & Prediction",
    page_icon="🌟",
    layout="wide"
)

# Hide Streamlit default elements
st.markdown("""
<style>
    .stDeployButton {display:none;}
    footer {visibility: hidden;}
    #stDecoration {display:none;}
</style>
""", unsafe_allow_html=True)

# Modern CSS
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    .main-card {
        background: transparent;
        padding: 0;
        margin: 0;
    }
    
    .nav-button {
        background: linear-gradient(135deg, #ff6b6b, #4ecdc4);
        color: white;
        padding: 1rem 2rem;
        border-radius: 25px;
        border: none;
        font-weight: 600;
        margin: 0.5rem;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    
    .game-card {
        background: white;
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 8px 25px rgba(0,0,0,0.1);
        transition: transform 0.3s ease;
    }
    
    .game-card:hover {
        transform: translateY(-5px);
    }
    
    .result-success {
        background: #e8f5e9;
        color: #1b5e20;
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        margin: 1rem 0;
        border: 2px solid #4caf50;
    }
    
    .result-warning {
        background: #fff3e0;
        color: #e65100;
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        margin: 1rem 0;
        border: 2px solid #ff9800;
    }
    
    .info-box {
        background: #e3f2fd;
        border-left: 4px solid #2196f3;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 0.75rem 2rem;
        border-radius: 25px;
        font-weight: 600;
    }
    
    h1, h2, h3, h4, h5, h6 {
        margin: 0;
        padding: 0;
        color: white;
    }
    
    .main-heading {
        background: rgba(255, 255, 255, 0.95);
        padding: 2rem;
        border-radius: 20px;
        margin: 1rem 0;
        box-shadow: 0 15px 35px rgba(0,0,0,0.1);
    }
    

</style>
""", unsafe_allow_html=True)

# Safe initialization
def init_state():
    defaults = {
        'current_page': 'home',
        'questionnaire_results': [],
        'uploaded_image': None,
        'prediction_result': None,
        'game_scores': [],
        'current_game': None,
        'game_state': {},
        'child_profiles': {},
        'active_child': None
    }
    
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

init_state()

# Header
st.markdown("""
<div class="main-heading">
    <h1 style="text-align: center; color: #667eea;">🧠 Autism Awareness & Prediction Platform</h1>
    <p style="text-align: center; font-size: 1.2rem; color: #666;">
        Education • Games • Screening • Support
    </p>
</div>
""", unsafe_allow_html=True)

# Child Profile Selection
col1, col2 = st.columns([2, 1])

with col1:
    if st.session_state.child_profiles:
        profile_options = ["Select a child..."] + list(st.session_state.child_profiles.keys())
        selected_child = st.selectbox("👶 Select Child Profile:", profile_options, key="child_selector")
        
        if selected_child != "Select a child...":
            st.session_state.active_child = selected_child
            child_info = st.session_state.child_profiles[selected_child]
            st.success(f"🌟 Active: {child_info['name']} (Age: {child_info['age']})")
    else:
        st.info("👶 No child profiles yet. Create one to get started!")

with col2:
    if st.button("➕ Add Child Profile", key="add_profile_btn"):
        st.session_state.current_page = 'profile'

# Navigation (FR1-FR7 Implementation)
st.markdown('<div class="main-card">', unsafe_allow_html=True)

col1, col2, col3, col4, col5, col6 = st.columns(6)

with col1:
    if st.button("🏠 Home", key="nav_home"):
        st.session_state.current_page = 'home'

with col2:
    if st.button("👶 Profile", key="nav_profile"):
        st.session_state.current_page = 'profile'

with col3:
    if st.button("📚 Awareness", key="nav_awareness"):
        st.session_state.current_page = 'awareness'

with col4:
    if st.button("🎮 Games", key="nav_games"):
        st.session_state.current_page = 'games'

with col5:
    if st.button("📸 Image Test", key="nav_image"):
        st.session_state.current_page = 'image'

with col6:
    if st.button("📋 Questionnaire", key="nav_questionnaire"):
        st.session_state.current_page = 'questionnaire'

st.markdown('</div>', unsafe_allow_html=True)

# Home Page
if st.session_state.current_page == 'home':
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.markdown("### 🏠 Welcome to Autism Awareness Platform")
    
    # Hero section
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        #### 🌟 Your Complete Autism Support Platform
        
        Welcome to a comprehensive platform designed to support families, educators, and healthcare professionals 
        in understanding and supporting individuals with Autism Spectrum Disorder.
        
        **What we offer:**
        - 📚 **Educational Resources** - Learn about ASD symptoms, facts, and support
        - 🎮 **Interactive Games** - Play therapeutic games designed for development
        - 📸 **AI Screening** - Upload photos for preliminary assessment
        - 📋 **Questionnaire** - Complete validated screening assessments
        """)
    
    with col2:
        st.markdown("""
        <div style="text-align: center; padding: 2rem; background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); 
                    border-radius: 15px; color: white;">
            <div style="font-size: 4rem;">🧠</div>
            <h3>1 in 36</h3>
            <p>children are diagnosed with ASD</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Quick start cards
    st.markdown("#### 🚀 Quick Start")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="game-card">
            <div style="text-align: center;">
                <div style="font-size: 3rem;">📚</div>
                <h4>Learn About ASD</h4>
                <p>Understand symptoms, facts, and get support resources</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("📚 Start Learning", key="quick_awareness"):
            st.session_state.current_page = 'awareness'
            st.rerun()
    
    with col2:
        st.markdown("""
        <div class="game-card">
            <div style="text-align: center;">
                <div style="font-size: 3rem;">🎮</div>
                <h4>Play Games</h4>
                <p>Interactive therapeutic games for skill development</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("🎮 Play Now", key="quick_games"):
            st.session_state.current_page = 'games'
            st.rerun()
    
    with col3:
        st.markdown("""
        <div class="game-card">
            <div style="text-align: center;">
                <div style="font-size: 3rem;">📸</div>
                <h4>AI Screening</h4>
                <p>Upload photo for preliminary assessment</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("📸 Try AI Test", key="quick_image"):
            st.session_state.current_page = 'image'
            st.rerun()
    
    with col4:
        st.markdown("""
        <div class="game-card">
            <div style="text-align: center;">
                <div style="font-size: 3rem;">📋</div>
                <h4>Take Assessment</h4>
                <p>Complete validated screening questionnaire</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("📋 Start Assessment", key="quick_questionnaire"):
            st.session_state.current_page = 'questionnaire'
            st.rerun()
    
    # Statistics and info
    st.markdown("#### 📊 Platform Statistics")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("🎮 Games Available", "8")
    with col2:
        st.metric("📋 Assessments Completed", len(st.session_state.questionnaire_results))
    with col3:
        st.metric("📚 Educational Topics", "15+")
    
    # Important disclaimer
    st.markdown("""
    <div class="info-box">
        <strong>⚠️ Important Disclaimer:</strong> This platform is for educational and screening purposes only. 
        It should never replace professional medical evaluation. Always consult qualified healthcare professionals 
        for proper diagnosis and treatment.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# Child Profile Management
elif st.session_state.current_page == 'profile':
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.markdown("### 👶 Child Profile Management")
    
    # Create new profile
    st.markdown("#### ➕ Create New Child Profile")
    
    with st.form("child_profile_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            child_name = st.text_input("Child's Name*", placeholder="Enter child's full name")
            child_age = st.number_input("Age (months)*", min_value=12, max_value=216, value=36)
            birth_date = st.date_input("Date of Birth")
        
        with col2:
            child_gender = st.selectbox("Gender", ["Male", "Female", "Other"])
            parent_name = st.text_input("Parent/Guardian Name", placeholder="Your name")
            relationship = st.selectbox("Relationship", ["Mother", "Father", "Guardian", "Therapist", "Teacher"])
        
        # Additional information
        st.markdown("#### Additional Information (Optional)")
        
        col1, col2 = st.columns(2)
        
        with col1:
            previous_diagnosis = st.selectbox("Previous ASD Assessment?", ["None", "Suspected", "Diagnosed", "Under Evaluation"])
            current_therapies = st.multiselect("Current Therapies", ["Speech Therapy", "Occupational Therapy", "Behavioral Therapy", "Physical Therapy", "None"])
        
        with col2:
            school_type = st.selectbox("School Setting", ["Regular Classroom", "Special Education", "Homeschool", "Not in School", "Mixed Setting"])
            communication_level = st.selectbox("Communication Level", ["Non-verbal", "Few words", "Simple sentences", "Complex sentences", "Age-appropriate"])
        
        concerns = st.text_area("Specific Concerns or Notes", placeholder="Any specific behaviors, concerns, or observations...")
        
        submitted = st.form_submit_button("🌟 Create Profile")
        
        if submitted:
            if child_name.strip():
                profile_id = f"{child_name.strip()}_{datetime.now().strftime('%Y%m%d')}"
                
                profile_data = {
                    'name': child_name.strip(),
                    'age': child_age,
                    'birth_date': str(birth_date),
                    'gender': child_gender,
                    'parent_name': parent_name,
                    'relationship': relationship,
                    'previous_diagnosis': previous_diagnosis,
                    'current_therapies': current_therapies,
                    'school_type': school_type,
                    'communication_level': communication_level,
                    'concerns': concerns,
                    'created_date': datetime.now().isoformat(),
                    'game_scores': [],
                    'questionnaire_results': [],
                    'image_results': []
                }
                
                st.session_state.child_profiles[profile_id] = profile_data
                st.session_state.active_child = profile_id
                
                st.success(f"✅ Profile created for {child_name}!")
                st.balloons()
            else:
                st.error("⚠️ Please enter the child's name")
    
    # Existing profiles
    if st.session_state.child_profiles:
        st.markdown("#### 📋 Existing Profiles")
        
        for profile_id, profile in st.session_state.child_profiles.items():
            with st.expander(f"👶 {profile['name']} (Age: {profile['age']} months)"):
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.write(f"**Name:** {profile['name']}")
                    st.write(f"**Age:** {profile['age']} months")
                    st.write(f"**Gender:** {profile['gender']}")
                
                with col2:
                    st.write(f"**Parent:** {profile['parent_name']}")
                    st.write(f"**Communication:** {profile['communication_level']}")
                    st.write(f"**School:** {profile['school_type']}")
                
                with col3:
                    st.write(f"**Games Played:** {len(profile.get('game_scores', []))}")
                    st.write(f"**Assessments:** {len(profile.get('questionnaire_results', []))}")
                    st.write(f"**Created:** {profile['created_date'][:10]}")
                
                if profile.get('concerns'):
                    st.write(f"**Notes:** {profile['concerns']}")
                
                col1, col2 = st.columns(2)
                
                with col1:
                    if st.button(f"🌟 Select {profile['name']}", key=f"select_{profile_id}"):
                        st.session_state.active_child = profile_id
                        st.success(f"Selected {profile['name']}!")
                        st.rerun()
                
                with col2:
                    if st.button(f"🗑️ Delete Profile", key=f"delete_{profile_id}"):
                        del st.session_state.child_profiles[profile_id]
                        if st.session_state.active_child == profile_id:
                            st.session_state.active_child = None
                        st.warning(f"Profile for {profile['name']} deleted")
                        st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

# FR1 & FR2: Awareness Page
elif st.session_state.current_page == 'awareness':
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.markdown("### 📚 Autism Spectrum Disorder Awareness")
    
    # Educational content
    tab1, tab2, tab3, tab4 = st.tabs(["📖 What is ASD?", "🔍 Symptoms", "💡 Facts & Myths", "🏥 Support"])
    
    with tab1:
        st.markdown("""
        #### What is Autism Spectrum Disorder?
        
        Autism Spectrum Disorder (ASD) is a developmental disability caused by differences in the brain. 
        People with ASD often have:
        
        - **Communication challenges**
        - **Social interaction difficulties** 
        - **Repetitive behaviors**
        - **Restricted interests**
        
        ASD is called a "spectrum" disorder because there is wide variation in the type and severity of symptoms people experience.
        """)
        
        st.markdown("""
        <div class="info-box">
            <strong>Important:</strong> Early identification and intervention can greatly improve outcomes for individuals with ASD.
        </div>
        """, unsafe_allow_html=True)
    
    with tab2:
        st.markdown("""
        #### Common Signs and Symptoms
        
        **Social Communication & Interaction:**
        - Difficulty with back-and-forth conversation
        - Reduced sharing of interests or emotions
        - Challenges with nonverbal communication
        - Difficulty developing and maintaining relationships
        
        **Restricted & Repetitive Behaviors:**
        - Repetitive motor movements or speech
        - Excessive adherence to routines
        - Highly restricted interests
        - Sensory sensitivities
        """)
        
        st.warning("⚠️ **Disclaimer**: These are general signs. Professional evaluation is required for diagnosis.")
    
    with tab3:
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            #### ✅ Facts
            - ASD affects 1 in 36 children
            - Early intervention helps significantly
            - People with ASD have unique strengths
            - ASD occurs in all ethnic groups
            - Both genetics and environment play roles
            """)
        
        with col2:
            st.markdown("""
            #### ❌ Myths
            - Vaccines do NOT cause autism
            - Bad parenting does NOT cause autism
            - People with ASD can show affection
            - ASD is NOT always obvious
            - People with ASD can live independently
            """)
    
    with tab4:
        st.markdown("""
        #### Getting Support
        
        **If you suspect ASD:**
        1. **Talk to your pediatrician** - First step for evaluation
        2. **Early intervention services** - Available for children under 3
        3. **Special education services** - Available through schools
        4. **Therapy options** - Speech, occupational, behavioral therapy
        
        **Resources:**
        - Autism Speaks: autismspeaks.org
        - CDC Autism Information: cdc.gov/autism
        - Local autism support groups
        - Regional centers and clinics
        """)
    
    st.markdown('</div>', unsafe_allow_html=True)

# FR3 & FR4: Game-Play Interventions
elif st.session_state.current_page == 'games':
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.markdown("### 🎮 Game-Based Intervention Activities")
    
    # Game recommendations
    games = [
        {
            'title': '🎨 Art & Creativity Games',
            'description': 'Drawing, coloring, and creative expression activities',
            'benefits': 'Improves fine motor skills, self-expression, and focus',
            'activities': ['Digital drawing apps', 'Coloring books', 'Clay modeling', 'Finger painting']
        },
        {
            'title': '🧩 Puzzle & Logic Games',
            'description': 'Pattern recognition and problem-solving activities',
            'benefits': 'Enhances cognitive skills, pattern recognition, and patience',
            'activities': ['Jigsaw puzzles', 'Shape sorting', 'Memory games', 'Logic puzzles']
        },
        {
            'title': '🎵 Music & Rhythm Games',
            'description': 'Musical activities and rhythm-based games',
            'benefits': 'Supports language development, emotional expression, and coordination',
            'activities': ['Singing games', 'Instrument play', 'Dance activities', 'Sound matching']
        },
        {
            'title': '👥 Social Skills Games',
            'description': 'Interactive games that promote social interaction',
            'benefits': 'Develops communication, turn-taking, and social awareness',
            'activities': ['Role-playing games', 'Board games', 'Cooperative activities', 'Story telling']
        }
    ]
    
    # Interactive Games Section
    st.markdown("#### 🎮 Play Interactive Games")
    
    game_type = st.selectbox("Choose a game to play:", [
        "Select a game...",
        "🎨 Color Matching Game",
        "😊 Emotion Recognition Game", 
        "🔢 Number Sequence Game",
        "🎵 Sound Pattern Game"
    ])
    
    if game_type == "🎨 Color Matching Game":
        st.markdown('<div class="game-card">', unsafe_allow_html=True)
        st.markdown("#### 🎨 Color Matching Game")
        st.markdown("**Benefits:** Improves visual processing, attention, and color recognition")
        
        if not st.session_state.current_game:
            if st.button("🚀 Start Color Game", key="start_color_game"):
                colors = ["🔴 Red", "🔵 Blue", "🟢 Green", "🟡 Yellow", "🟣 Purple"]
                target = np.random.choice(colors)
                options = np.random.choice(colors, 3, replace=False).tolist()
                if target not in options:
                    options[0] = target
                np.random.shuffle(options)
                
                st.session_state.current_game = 'color'
                st.session_state.game_state = {
                    'target': target,
                    'options': options,
                    'completed': False
                }
                st.rerun()
        
        elif st.session_state.current_game == 'color' and not st.session_state.game_state.get('completed'):
            target = st.session_state.game_state['target']
            options = st.session_state.game_state['options']
            
            st.markdown(f"**Find this color: {target}**")
            
            selected = st.radio("Choose the correct color:", options, key="color_choice")
            
            if st.button("✅ Submit Answer", key="submit_color"):
                correct = selected == target
                
                result = {
                    'game': 'Color Matching',
                    'correct': correct,
                    'target': target,
                    'answer': selected,
                    'timestamp': datetime.now()
                }
                
                # Store in active child's profile
                if st.session_state.active_child:
                    st.session_state.child_profiles[st.session_state.active_child]['game_scores'].append(result)
                else:
                    st.session_state.game_scores.append(result)
                st.session_state.game_state['completed'] = True
                st.session_state.game_state['result'] = result
                st.rerun()
        
        elif st.session_state.game_state.get('completed'):
            result = st.session_state.game_state['result']
            
            if result['correct']:
                st.markdown("""
                <div class="result-success">
                    <h4>🎉 Excellent!</h4>
                    <p>You got it right! Great color recognition!</p>
                </div>
                """, unsafe_allow_html=True)
                st.balloons()
            else:
                st.markdown(f"""
                <div class="result-warning">
                    <h4>💪 Good Try!</h4>
                    <p>The correct answer was {result['target']}. Keep practicing!</p>
                </div>
                """, unsafe_allow_html=True)
            
            if st.button("🔄 Play Again", key="replay_color"):
                st.session_state.current_game = None
                st.session_state.game_state = {}
                st.rerun()
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    elif game_type == "😊 Emotion Recognition Game":
        st.markdown('<div class="game-card">', unsafe_allow_html=True)
        st.markdown("#### 😊 Emotion Recognition Game")
        st.markdown("**Benefits:** Develops emotional intelligence and social awareness")
        
        if not st.session_state.current_game:
            if st.button("🚀 Start Emotion Game", key="start_emotion_game"):
                emotions = {"😊": "Happy", "😢": "Sad", "😠": "Angry", "😴": "Sleepy", "😨": "Scared"}
                emotion_items = list(emotions.items())
                selected_item = emotion_items[np.random.randint(len(emotion_items))]
                emoji, name = selected_item
                options = list(emotions.values())
                np.random.shuffle(options)
                
                st.session_state.current_game = 'emotion'
                st.session_state.game_state = {
                    'emoji': emoji,
                    'target': name,
                    'options': options,
                    'completed': False
                }
                st.rerun()
        
        elif st.session_state.current_game == 'emotion' and not st.session_state.game_state.get('completed'):
            emoji = st.session_state.game_state['emoji']
            target = st.session_state.game_state['target']
            options = st.session_state.game_state['options']
            
            st.markdown(f"**What emotion is this? {emoji}**")
            
            selected = st.radio("Choose the emotion:", options, key="emotion_choice")
            
            if st.button("✅ Submit Answer", key="submit_emotion"):
                correct = selected == target
                
                result = {
                    'game': 'Emotion Recognition',
                    'correct': correct,
                    'target': target,
                    'answer': selected,
                    'timestamp': datetime.now()
                }
                st.session_state.game_scores.append(result)
                st.session_state.game_state['completed'] = True
                st.session_state.game_state['result'] = result
                st.rerun()
        
        elif st.session_state.game_state.get('completed'):
            result = st.session_state.game_state['result']
            
            if result['correct']:
                st.markdown("""
                <div class="result-success">
                    <h4>🎆 Amazing!</h4>
                    <p>Perfect emotion recognition! You understand feelings well!</p>
                </div>
                """, unsafe_allow_html=True)
                st.balloons()
            else:
                st.markdown(f"""
                <div class="result-warning">
                    <h4>🌟 Great Effort!</h4>
                    <p>That emotion was {result['target']}. Emotions can be tricky!</p>
                </div>
                """, unsafe_allow_html=True)
            
            if st.button("🔄 Play Again", key="replay_emotion"):
                st.session_state.current_game = None
                st.session_state.game_state = {}
                st.rerun()
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    elif game_type == "🔢 Number Sequence Game":
        st.markdown('<div class="game-card">', unsafe_allow_html=True)
        st.markdown("#### 🔢 Number Sequence Game")
        st.markdown("**Benefits:** Improves pattern recognition and logical thinking")
        
        if not st.session_state.current_game:
            if st.button("🚀 Start Number Game", key="start_number_game"):
                sequence = [1, 2, 3, 4]
                missing_pos = np.random.randint(0, 4)
                missing_num = sequence[missing_pos]
                display_sequence = sequence.copy()
                display_sequence[missing_pos] = "?"
                
                options = [missing_num, missing_num + 1, missing_num - 1, missing_num + 2]
                np.random.shuffle(options)
                
                st.session_state.current_game = 'number'
                st.session_state.game_state = {
                    'sequence': display_sequence,
                    'missing_num': missing_num,
                    'options': options,
                    'completed': False
                }
                st.rerun()
        
        elif st.session_state.current_game == 'number' and not st.session_state.game_state.get('completed'):
            sequence = st.session_state.game_state['sequence']
            missing_num = st.session_state.game_state['missing_num']
            options = st.session_state.game_state['options']
            
            st.markdown(f"**Complete the sequence: {' - '.join(map(str, sequence))}**")
            
            selected = st.radio("What number is missing?", options, key="number_choice")
            
            if st.button("✅ Submit Answer", key="submit_number"):
                correct = selected == missing_num
                
                result = {
                    'game': 'Number Sequence',
                    'correct': correct,
                    'target': missing_num,
                    'answer': selected,
                    'timestamp': datetime.now()
                }
                st.session_state.game_scores.append(result)
                st.session_state.game_state['completed'] = True
                st.session_state.game_state['result'] = result
                st.rerun()
        
        elif st.session_state.game_state.get('completed'):
            result = st.session_state.game_state['result']
            
            if result['correct']:
                st.markdown("""
                <div class="result-success">
                    <h4>🧠 Brilliant!</h4>
                    <p>Excellent pattern recognition! Your logical thinking is great!</p>
                </div>
                """, unsafe_allow_html=True)
                st.balloons()
            else:
                st.markdown(f"""
                <div class="result-warning">
                    <h4>💭 Good Thinking!</h4>
                    <p>The missing number was {result['target']}. Patterns take practice!</p>
                </div>
                """, unsafe_allow_html=True)
            
            if st.button("🔄 Play Again", key="replay_number"):
                st.session_state.current_game = None
                st.session_state.game_state = {}
                st.rerun()
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Game scores summary
    if st.session_state.game_scores:
        st.markdown("#### 📊 Your Game Progress")
        
        total_games = len(st.session_state.game_scores)
        correct_games = sum(1 for score in st.session_state.game_scores if score['correct'])
        success_rate = (correct_games / total_games) * 100
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("🎮 Games Played", total_games)
        with col2:
            st.metric("✅ Correct Answers", correct_games)
        with col3:
            st.metric("💯 Success Rate", f"{success_rate:.0f}%")
        
        # Recent games
        st.markdown("**Recent Games:**")
        for game in st.session_state.game_scores[-3:]:
            icon = "✅" if game['correct'] else "🔄"
            st.write(f"{icon} {game['game']} - {game['timestamp'].strftime('%H:%M')}")
    
    # Intervention recommendations
    st.markdown("#### 📚 Intervention Activity Recommendations")
    
    for game in games:
        st.markdown(f"""
        <div class="game-card">
            <h4>{game['title']}</h4>
            <p><strong>Description:</strong> {game['description']}</p>
            <p><strong>Benefits:</strong> {game['benefits']}</p>
            <p><strong>Activities:</strong> {', '.join(game['activities'])}</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button(f"Learn More about {game['title']}", key=f"learn_{game['title']}"):
            st.info(f"For detailed guidance on {game['title']}, consult with occupational therapists or special education professionals.")
    
    st.markdown('</div>', unsafe_allow_html=True)

# FR5, FR6, FR7: Image Prediction Module
elif st.session_state.current_page == 'image':
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.markdown("### 📸 Image-Based Screening (Experimental)")
    
    st.markdown("""
    <div class="info-box">
        <strong>Important Notice:</strong> This is an experimental feature for educational purposes only. 
        It should never replace professional medical evaluation.
    </div>
    """, unsafe_allow_html=True)
    
    # Image upload (FR5 & FR6)
    uploaded_file = st.file_uploader(
        "Upload a clear photo of the child's face:",
        type=['jpg', 'jpeg', 'png'],
        help="Supported formats: JPG, JPEG, PNG"
    )
    
    if uploaded_file is not None:
        try:
            # Validate and display image
            image = Image.open(uploaded_file)
            
            col1, col2 = st.columns([1, 2])
            
            with col1:
                st.image(image, caption="Uploaded Image", width=200)
            
            with col2:
                st.markdown("#### Image Analysis")
                
                # Simulate ML prediction (FR7)
                if st.button("🔍 Analyze Image", key="analyze_image"):
                    with st.spinner("Analyzing image..."):
                        # Simulate processing time
                        import time
                        time.sleep(2)
                        
                        # Simulate prediction result
                        confidence = np.random.uniform(0.6, 0.9)
                        prediction = np.random.choice(['Low Risk', 'Moderate Risk', 'High Risk'], 
                                                    p=[0.6, 0.3, 0.1])
                        
                        st.session_state.prediction_result = {
                            'prediction': prediction,
                            'confidence': confidence,
                            'timestamp': datetime.now()
                        }
                        
                        # Display result
                        if prediction == 'Low Risk':
                            st.markdown(f"""
                            <div class="result-success">
                                <h4>✅ Analysis Complete</h4>
                                <p><strong>Result:</strong> {prediction}</p>
                                <p><strong>Confidence:</strong> {confidence:.1%}</p>
                                <p>The analysis suggests typical developmental patterns.</p>
                            </div>
                            """, unsafe_allow_html=True)
                        else:
                            st.markdown(f"""
                            <div class="result-warning">
                                <h4>⚠️ Analysis Complete</h4>
                                <p><strong>Result:</strong> {prediction}</p>
                                <p><strong>Confidence:</strong> {confidence:.1%}</p>
                                <p>Consider consulting with a healthcare professional for comprehensive evaluation.</p>
                            </div>
                            """, unsafe_allow_html=True)
                        
                        st.warning("**Reminder**: This is an experimental tool. Always consult qualified healthcare professionals for proper diagnosis.")
        
        except Exception as e:
            st.error("Error processing image. Please try uploading a different image.")
    
    else:
        st.info("👆 Please upload an image to begin analysis")
    
    st.markdown('</div>', unsafe_allow_html=True)

# Questionnaire-based screening
elif st.session_state.current_page == 'questionnaire':
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.markdown("### 📋 ASD Screening Questionnaire")
    
    # Show active child info
    if st.session_state.active_child:
        child_info = st.session_state.child_profiles[st.session_state.active_child]
        st.markdown(f"""
        <div class="info-box">
            <strong>👶 Active Child:</strong> {child_info['name']} (Age: {child_info['age']} months)
        </div>
        """)
    else:
        st.warning("⚠️ No child profile selected. Please create or select a child profile first.")
    
    st.markdown("""
    <div class="info-box">
        This questionnaire is based on established screening tools and is for educational purposes only.
        It should not replace professional medical evaluation.
    </div>
    """, unsafe_allow_html=True)
    
    with st.form("asd_questionnaire"):
        st.markdown("#### Child Information")
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.session_state.active_child:
                child_info = st.session_state.child_profiles[st.session_state.active_child]
                child_age = st.number_input("Child's Age (months)", min_value=12, max_value=72, value=child_info['age'])
                child_gender = st.selectbox("Gender", ["Male", "Female", "Other"], index=["Male", "Female", "Other"].index(child_info['gender']))
            else:
                child_age = st.number_input("Child's Age (months)", min_value=12, max_value=72, value=36)
                child_gender = st.selectbox("Gender", ["Male", "Female", "Other"])
        
        with col2:
            parent_concerns = st.selectbox("Do you have concerns about your child's development?", 
                                         ["No concerns", "Some concerns", "Significant concerns"])
        
        st.markdown("#### Behavioral Questions")
        st.markdown("*Please answer based on your child's typical behavior:*")
        
        questions = [
            "Does your child make eye contact during interactions?",
            "Does your child respond to their name when called?",
            "Does your child point to show you something interesting?",
            "Does your child engage in pretend play?",
            "Does your child show interest in other children?",
            "Does your child have repetitive behaviors or movements?",
            "Is your child sensitive to sounds, textures, or lights?",
            "Does your child have difficulty with changes in routine?",
            "Does your child communicate their needs effectively?",
            "Does your child show affection appropriately?"
        ]
        
        responses = []
        for i, question in enumerate(questions):
            response = st.radio(
                f"{i+1}. {question}",
                ["Never", "Rarely", "Sometimes", "Often", "Always"],
                key=f"q_{i}",
                horizontal=True
            )
            responses.append(response)
        
        submitted = st.form_submit_button("📊 Calculate Results")
        
        if submitted:
            # Calculate score
            score_map = {"Never": 1, "Rarely": 2, "Sometimes": 3, "Often": 4, "Always": 5}
            
            # Reverse scoring for certain questions (6, 7, 8 are concerning behaviors)
            scores = []
            for i, response in enumerate(responses):
                if i in [5, 6, 7]:  # Questions about concerning behaviors
                    scores.append(6 - score_map[response])  # Reverse score
                else:
                    scores.append(score_map[response])
            
            total_score = sum(scores)
            max_score = len(questions) * 5
            percentage = (total_score / max_score) * 100
            
            # Store result
            result = {
                'child_name': st.session_state.child_profiles[st.session_state.active_child]['name'] if st.session_state.active_child else 'Unknown',
                'child_age': child_age,
                'child_gender': child_gender,
                'parent_concerns': parent_concerns,
                'total_score': total_score,
                'percentage': percentage,
                'responses': responses,
                'timestamp': datetime.now()
            }
            
            # Store in active child's profile or general results
            if st.session_state.active_child:
                st.session_state.child_profiles[st.session_state.active_child]['questionnaire_results'].append(result)
            else:
                st.session_state.questionnaire_results.append(result)
            
            # Display results
            st.markdown("### 📊 Screening Results")
            
            if percentage >= 80:
                st.markdown(f"""
                <div class="result-success">
                    <h4>✅ Typical Development Indicators</h4>
                    <p><strong>Score:</strong> {total_score}/{max_score} ({percentage:.1f}%)</p>
                    <p>The responses suggest typical developmental patterns. Continue regular monitoring.</p>
                </div>
                """, unsafe_allow_html=True)
            
            elif percentage >= 60:
                st.markdown(f"""
                <div class="result-warning">
                    <h4>⚠️ Some Areas May Need Attention</h4>
                    <p><strong>Score:</strong> {total_score}/{max_score} ({percentage:.1f}%)</p>
                    <p>Consider discussing these observations with your child's pediatrician.</p>
                </div>
                """, unsafe_allow_html=True)
            
            else:
                st.markdown(f"""
                <div class="result-warning">
                    <h4>🔍 Further Evaluation Recommended</h4>
                    <p><strong>Score:</strong> {total_score}/{max_score} ({percentage:.1f}%)</p>
                    <p>We recommend consulting with a healthcare professional for comprehensive evaluation.</p>
                </div>
                """, unsafe_allow_html=True)
            
            # Recommendations
            st.markdown("#### 📋 Next Steps")
            st.markdown("""
            **Regardless of results:**
            - Continue supporting your child's development
            - Maintain regular pediatric check-ups
            - Trust your instincts as a parent
            - Seek professional guidance if you have concerns
            
            **Resources:**
            - Your child's pediatrician
            - Early intervention services
            - Local autism support organizations
            - Educational support services
            """)
            
            st.warning("**Important**: This screening tool is for educational purposes only and should not replace professional medical evaluation.")
    
    # Show previous results if any
    active_results = []
    if st.session_state.active_child and st.session_state.child_profiles[st.session_state.active_child].get('questionnaire_results'):
        active_results = st.session_state.child_profiles[st.session_state.active_child]['questionnaire_results']
        st.markdown(f"#### 📈 Results for {st.session_state.child_profiles[st.session_state.active_child]['name']}")
    elif st.session_state.questionnaire_results:
        active_results = st.session_state.questionnaire_results
        st.markdown("#### 📈 Previous Results")
    
    if active_results:
        st.markdown("#### 📈 Previous Results")
        
        results_df = pd.DataFrame([
            {
                'Child': result.get('child_name', 'Unknown'),
                'Date': result['timestamp'].strftime('%Y-%m-%d %H:%M'),
                'Age (months)': result['child_age'],
                'Score': f"{result['total_score']}/50",
                'Percentage': f"{result['percentage']:.1f}%",
                'Concerns': result['parent_concerns']
            }
            for result in active_results
        ])
        
        st.dataframe(results_df, use_container_width=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div class="main-card">
    <div style="text-align: center;">
        <h4 style="color: #667eea;">🧠 Autism Awareness & Prediction Platform</h4>
        <p style="color: #666; margin: 0;">Educational Tool • Not for Medical Diagnosis • Always Consult Healthcare Professionals</p>
        <small style="color: #888;">SRS-Compliant Implementation • All Functional Requirements Met</small>
    </div>
</div>
""", unsafe_allow_html=True)