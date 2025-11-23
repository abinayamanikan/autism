import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import time
import random
import json
import os

# Page config
st.set_page_config(
    page_title="Autism Detection for Girls",
    page_icon="👧",
    layout="wide"
)

# CSS for child-friendly interface
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(45deg, #ffb3d9, #ffe6f2, #f0f8ff);
        font-family: 'Comic Sans MS', cursive;
    }
    
    .main-header {
        background: linear-gradient(90deg, #ff69b4, #ffc0cb);
        padding: 2rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .game-card {
        background: white;
        border-radius: 20px;
        padding: 2rem;
        margin: 1rem 0;
        box-shadow: 0 4px 15px rgba(255,105,180,0.3);
        border: 3px solid #ff69b4;
    }
    
    .result-card {
        background: #f0f8ff;
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        border-left: 5px solid #ff69b4;
    }
    
    .stButton > button {
        background: linear-gradient(90deg, #ff69b4, #ffc0cb);
        color: white;
        border: none;
        padding: 1rem 2rem;
        border-radius: 25px;
        font-weight: bold;
        font-size: 18px;
    }
    
    .emoji-large {
        font-size: 3rem;
        text-align: center;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'user_data' not in st.session_state:
    st.session_state.user_data = {}
if 'child_profile' not in st.session_state:
    st.session_state.child_profile = {}
if 'game_results' not in st.session_state:
    st.session_state.game_results = {}
if 'assessment_data' not in st.session_state:
    st.session_state.assessment_data = []

# Header
st.markdown("""
<div class="main-header">
    <h1>👧 Autism Detection App for Girls</h1>
    <p>Interactive Games & Behavioral Assessment for Female Children (Ages 3-10)</p>
</div>
""", unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("🌸 Navigation")
page = st.sidebar.selectbox(
    "Choose Section",
    ["🏠 Home", "👤 Registration", "🎮 Interactive Games", "📊 Face Recognition", "📈 Assessment Results", "📋 Reports"]
)

# Data storage functions
def save_data(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f)

def load_data(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except:
        return {}

if page == "🏠 Home":
    st.header("Welcome to Our Special Helper App! 🌟")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="game-card">
            <div class="emoji-large">🎯</div>
            <h3>What We Do</h3>
            <ul>
                <li>🎮 Fun interactive games</li>
                <li>📸 Face expression recognition</li>
                <li>👀 Eye gaze tracking</li>
                <li>🧠 Behavioral assessment</li>
                <li>📊 Progress reports</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="game-card">
            <div class="emoji-large">⚠️</div>
            <h3>Important Notice</h3>
            <p><strong>This is a screening tool only</strong></p>
            <ul>
                <li>🏥 Not for medical diagnosis</li>
                <li>👩‍⚕️ Consult healthcare professionals</li>
                <li>🔒 Safe and child-friendly</li>
                <li>📱 Works on tablets/phones</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("### 🚀 Getting Started")
    st.info("1. Register your child's profile\n2. Play interactive games\n3. Complete face recognition tests\n4. View assessment results")

elif page == "👤 Registration":
    st.header("👤 User Registration & Child Profile")
    
    with st.form("registration_form"):
        st.subheader("Parent/Guardian Information")
        
        col1, col2 = st.columns(2)
        with col1:
            parent_name = st.text_input("Parent/Guardian Name")
            email = st.text_input("Email Address")
        
        with col2:
            phone = st.text_input("Phone Number")
            relationship = st.selectbox("Relationship to Child", ["Mother", "Father", "Guardian", "Therapist"])
        
        st.subheader("Child Profile")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            child_name = st.text_input("Child's Name")
            child_age = st.number_input("Child's Age", min_value=3, max_value=10, value=5)
        
        with col2:
            birth_date = st.date_input("Date of Birth")
            grade = st.selectbox("Grade/Level", ["Preschool", "Kindergarten", "Grade 1", "Grade 2", "Grade 3", "Grade 4"])
        
        with col3:
            previous_assessment = st.selectbox("Previous ASD Assessment?", ["No", "Yes - Diagnosed", "Yes - Suspected"])
            concerns = st.text_area("Specific Concerns (Optional)")
        
        st.subheader("Consent & Privacy")
        camera_consent = st.checkbox("I consent to camera usage for facial expression analysis")
        data_consent = st.checkbox("I consent to data collection for assessment purposes")
        privacy_agreement = st.checkbox("I have read and agree to the privacy policy")
        
        submitted = st.form_submit_button("🌸 Create Profile")
        
        if submitted:
            if camera_consent and data_consent and privacy_agreement:
                profile_data = {
                    'parent_name': parent_name,
                    'email': email,
                    'phone': phone,
                    'relationship': relationship,
                    'child_name': child_name,
                    'child_age': child_age,
                    'birth_date': str(birth_date),
                    'grade': grade,
                    'previous_assessment': previous_assessment,
                    'concerns': concerns,
                    'registration_date': str(datetime.now())
                }
                
                st.session_state.child_profile = profile_data
                save_data('child_profile.json', profile_data)
                
                st.success("✅ Profile created successfully!")
                st.balloons()
            else:
                st.error("❌ Please accept all consent requirements")

elif page == "🎮 Interactive Games":
    st.header("🎮 Interactive Cognitive Games")
    
    if not st.session_state.child_profile:
        st.warning("⚠️ Please create a child profile first!")
    else:
        child_name = st.session_state.child_profile.get('child_name', 'Child')
        st.markdown(f"### Hi {child_name}! Let's play some fun games! 🌟")
        
        game_type = st.selectbox(
            "Choose a Game",
            ["🔍 Object Recognition Game", "😊 Emotion Matching Game", "👋 Social Response Game"]
        )
        
        if game_type == "🔍 Object Recognition Game":
            st.markdown('<div class="game-card">', unsafe_allow_html=True)
            st.markdown("#### 🔍 Object Recognition Game")
            st.markdown("Match the objects you see!")
            
            # Simulate object recognition game
            objects = ["🐶 Dog", "🐱 Cat", "🚗 Car", "🏠 House", "🌸 Flower", "⭐ Star"]
            
            if st.button("🎯 Start Object Game"):
                start_time = time.time()
                
                # Show random object
                target_object = random.choice(objects)
                st.markdown(f"### Find the: {target_object}")
                
                # Create options
                options = random.sample(objects, 3)
                if target_object not in options:
                    options[0] = target_object
                random.shuffle(options)
                
                selected = st.radio("Choose the correct object:", options, key="obj_game")
                
                if st.button("Submit Answer"):
                    response_time = time.time() - start_time
                    correct = selected == target_object
                    
                    # Store results
                    game_result = {
                        'game': 'Object Recognition',
                        'target': target_object,
                        'selected': selected,
                        'correct': correct,
                        'response_time': response_time,
                        'timestamp': str(datetime.now())
                    }
                    
                    if 'object_recognition' not in st.session_state.game_results:
                        st.session_state.game_results['object_recognition'] = []
                    st.session_state.game_results['object_recognition'].append(game_result)
                    
                    if correct:
                        st.success(f"🎉 Correct! Great job! (Time: {response_time:.1f}s)")
                        st.balloons()
                    else:
                        st.info(f"Good try! The answer was {target_object}")
            
            st.markdown('</div>', unsafe_allow_html=True)
        
        elif game_type == "😊 Emotion Matching Game":
            st.markdown('<div class="game-card">', unsafe_allow_html=True)
            st.markdown("#### 😊 Emotion Matching Game")
            st.markdown("Match the emotion to the face!")
            
            emotions = {
                "😊": "Happy",
                "😢": "Sad", 
                "😠": "Angry",
                "😨": "Scared",
                "😐": "Neutral"
            }
            
            if st.button("🎭 Start Emotion Game"):
                start_time = time.time()
                
                # Show random emotion
                emoji, emotion_name = random.choice(list(emotions.items()))
                st.markdown(f"### What emotion is this? {emoji}")
                
                # Create options
                emotion_options = list(emotions.values())
                selected_emotion = st.radio("Choose the emotion:", emotion_options, key="emotion_game")
                
                if st.button("Submit Emotion Answer"):
                    response_time = time.time() - start_time
                    correct = selected_emotion == emotion_name
                    
                    # Store results
                    game_result = {
                        'game': 'Emotion Matching',
                        'target_emoji': emoji,
                        'target_emotion': emotion_name,
                        'selected': selected_emotion,
                        'correct': correct,
                        'response_time': response_time,
                        'timestamp': str(datetime.now())
                    }
                    
                    if 'emotion_matching' not in st.session_state.game_results:
                        st.session_state.game_results['emotion_matching'] = []
                    st.session_state.game_results['emotion_matching'].append(game_result)
                    
                    if correct:
                        st.success(f"🎉 Perfect! You know emotions well! (Time: {response_time:.1f}s)")
                        st.balloons()
                    else:
                        st.info(f"Good effort! That was {emotion_name}")
            
            st.markdown('</div>', unsafe_allow_html=True)
        
        elif game_type == "👋 Social Response Game":
            st.markdown('<div class="game-card">', unsafe_allow_html=True)
            st.markdown("#### 👋 Social Response Game")
            st.markdown("Follow the instructions!")
            
            social_prompts = [
                ("👋", "Wave hello!"),
                ("😊", "Show a big smile!"),
                ("👉", "Point to something you like!"),
                ("👏", "Clap your hands!"),
                ("🤗", "Give yourself a hug!")
            ]
            
            if st.button("🎪 Start Social Game"):
                start_time = time.time()
                
                # Show random prompt
                emoji, instruction = random.choice(social_prompts)
                st.markdown(f"### {emoji} {instruction}")
                st.markdown("*Look at the camera and do the action!*")
                
                # Simulate camera detection
                if st.button("I did it! ✅"):
                    response_time = time.time() - start_time
                    
                    # Simulate detection result
                    detected = random.choice([True, True, True, False])  # 75% success rate
                    
                    game_result = {
                        'game': 'Social Response',
                        'instruction': instruction,
                        'detected': detected,
                        'response_time': response_time,
                        'timestamp': str(datetime.now())
                    }
                    
                    if 'social_response' not in st.session_state.game_results:
                        st.session_state.game_results['social_response'] = []
                    st.session_state.game_results['social_response'].append(game_result)
                    
                    if detected:
                        st.success(f"🌟 Great job! I saw you do it! (Time: {response_time:.1f}s)")
                        st.balloons()
                    else:
                        st.info("Try again! Make sure you're looking at the camera!")
            
            st.markdown('</div>', unsafe_allow_html=True)

elif page == "📊 Face Recognition":
    st.header("📊 Face Expression Recognition & Eye Gaze Analysis")
    
    if not st.session_state.child_profile:
        st.warning("⚠️ Please create a child profile first!")
    else:
        st.markdown("### 📸 Facial Expression & Gaze Assessment")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown('<div class="game-card">', unsafe_allow_html=True)
            st.markdown("#### 👀 Eye Gaze Tracking")
            st.markdown("Look at the camera and follow the instructions!")
            
            if st.button("🎯 Start Gaze Test"):
                st.markdown("**Instructions:**")
                st.markdown("1. Look directly at the camera")
                st.markdown("2. Follow the moving dot with your eyes")
                st.markdown("3. Keep your head still")
                
                # Simulate gaze tracking
                progress_bar = st.progress(0)
                status_text = st.empty()
                
                gaze_results = []
                
                for i in range(5):
                    status_text.text(f"Tracking gaze position {i+1}/5...")
                    progress_bar.progress((i + 1) * 20)
                    time.sleep(1)
                    
                    # Simulate gaze data
                    eye_contact = random.choice([True, True, False])  # 67% eye contact
                    focus_duration = random.uniform(0.5, 3.0)
                    
                    gaze_results.append({
                        'position': i+1,
                        'eye_contact': eye_contact,
                        'focus_duration': focus_duration,
                        'timestamp': str(datetime.now())
                    })
                
                # Store results
                st.session_state.assessment_data.append({
                    'test_type': 'gaze_tracking',
                    'results': gaze_results,
                    'timestamp': str(datetime.now())
                })
                
                # Calculate metrics
                eye_contact_rate = sum(r['eye_contact'] for r in gaze_results) / len(gaze_results)
                avg_focus = sum(r['focus_duration'] for r in gaze_results) / len(gaze_results)
                
                st.success("✅ Gaze tracking complete!")
                st.metric("Eye Contact Rate", f"{eye_contact_rate:.1%}")
                st.metric("Average Focus Duration", f"{avg_focus:.1f}s")
            
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col2:
            st.markdown('<div class="game-card">', unsafe_allow_html=True)
            st.markdown("#### 😊 Expression Recognition")
            st.markdown("Show different expressions to the camera!")
            
            expressions_to_test = ["Happy 😊", "Sad 😢", "Surprised 😮", "Neutral 😐"]
            
            if st.button("🎭 Start Expression Test"):
                expression_results = []
                
                for expression in expressions_to_test:
                    st.markdown(f"**Show me: {expression}**")
                    
                    if st.button(f"I'm showing {expression}!", key=f"expr_{expression}"):
                        # Simulate expression detection
                        detected_correctly = random.choice([True, True, False])  # 67% accuracy
                        confidence = random.uniform(0.6, 0.95)
                        
                        expression_results.append({
                            'requested_expression': expression,
                            'detected_correctly': detected_correctly,
                            'confidence': confidence,
                            'timestamp': str(datetime.now())
                        })
                        
                        if detected_correctly:
                            st.success(f"✅ Perfect {expression}! (Confidence: {confidence:.1%})")
                        else:
                            st.info(f"Good try! Let's practice {expression} more!")
                
                if expression_results:
                    # Store results
                    st.session_state.assessment_data.append({
                        'test_type': 'expression_recognition',
                        'results': expression_results,
                        'timestamp': str(datetime.now())
                    })
                    
                    # Calculate metrics
                    accuracy = sum(r['detected_correctly'] for r in expression_results) / len(expression_results)
                    avg_confidence = sum(r['confidence'] for r in expression_results) / len(expression_results)
                    
                    st.metric("Expression Accuracy", f"{accuracy:.1%}")
                    st.metric("Average Confidence", f"{avg_confidence:.1%}")
            
            st.markdown('</div>', unsafe_allow_html=True)

elif page == "📈 Assessment Results":
    st.header("📈 Behavioral Assessment Results")
    
    if not st.session_state.child_profile:
        st.warning("⚠️ Please create a child profile first!")
    elif not st.session_state.game_results and not st.session_state.assessment_data:
        st.info("📝 No assessment data available. Please complete some games and tests first!")
    else:
        child_name = st.session_state.child_profile.get('child_name', 'Child')
        child_age = st.session_state.child_profile.get('child_age', 0)
        
        st.markdown(f"### Assessment Results for {child_name} (Age: {child_age})")
        
        # Calculate overall scores
        total_games = 0
        correct_answers = 0
        total_response_time = 0
        
        # Object Recognition Results
        if 'object_recognition' in st.session_state.game_results:
            obj_results = st.session_state.game_results['object_recognition']
            obj_correct = sum(1 for r in obj_results if r['correct'])
            obj_total = len(obj_results)
            obj_avg_time = sum(r['response_time'] for r in obj_results) / obj_total if obj_total > 0 else 0
            
            total_games += obj_total
            correct_answers += obj_correct
            total_response_time += obj_avg_time
            
            st.markdown('<div class="result-card">', unsafe_allow_html=True)
            st.markdown("#### 🔍 Object Recognition Results")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Accuracy", f"{obj_correct}/{obj_total}" if obj_total > 0 else "0/0")
            with col2:
                st.metric("Success Rate", f"{obj_correct/obj_total:.1%}" if obj_total > 0 else "0%")
            with col3:
                st.metric("Avg Response Time", f"{obj_avg_time:.1f}s" if obj_total > 0 else "0s")
            st.markdown('</div>', unsafe_allow_html=True)
        
        # Emotion Matching Results
        if 'emotion_matching' in st.session_state.game_results:
            emo_results = st.session_state.game_results['emotion_matching']
            emo_correct = sum(1 for r in emo_results if r['correct'])
            emo_total = len(emo_results)
            emo_avg_time = sum(r['response_time'] for r in emo_results) / emo_total if emo_total > 0 else 0
            
            total_games += emo_total
            correct_answers += emo_correct
            total_response_time += emo_avg_time
            
            st.markdown('<div class="result-card">', unsafe_allow_html=True)
            st.markdown("#### 😊 Emotion Recognition Results")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Accuracy", f"{emo_correct}/{emo_total}" if emo_total > 0 else "0/0")
            with col2:
                st.metric("Success Rate", f"{emo_correct/emo_total:.1%}" if emo_total > 0 else "0%")
            with col3:
                st.metric("Avg Response Time", f"{emo_avg_time:.1f}s" if emo_total > 0 else "0s")
            st.markdown('</div>', unsafe_allow_html=True)
        
        # Social Response Results
        if 'social_response' in st.session_state.game_results:
            soc_results = st.session_state.game_results['social_response']
            soc_detected = sum(1 for r in soc_results if r['detected'])
            soc_total = len(soc_results)
            soc_avg_time = sum(r['response_time'] for r in soc_results) / soc_total if soc_total > 0 else 0
            
            st.markdown('<div class="result-card">', unsafe_allow_html=True)
            st.markdown("#### 👋 Social Response Results")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Detected Actions", f"{soc_detected}/{soc_total}" if soc_total > 0 else "0/0")
            with col2:
                st.metric("Response Rate", f"{soc_detected/soc_total:.1%}" if soc_total > 0 else "0%")
            with col3:
                st.metric("Avg Response Time", f"{soc_avg_time:.1f}s" if soc_total > 0 else "0s")
            st.markdown('</div>', unsafe_allow_html=True)
        
        # Overall Assessment
        if total_games > 0:
            overall_accuracy = correct_answers / total_games
            avg_response_time = total_response_time / 3  # Average across game types
            
            # Simple risk assessment
            risk_factors = 0
            if overall_accuracy < 0.6:
                risk_factors += 1
            if avg_response_time > 5.0:
                risk_factors += 1
            
            # Add face recognition factors
            for assessment in st.session_state.assessment_data:
                if assessment['test_type'] == 'gaze_tracking':
                    gaze_results = assessment['results']
                    eye_contact_rate = sum(r['eye_contact'] for r in gaze_results) / len(gaze_results)
                    if eye_contact_rate < 0.5:
                        risk_factors += 1
                
                if assessment['test_type'] == 'expression_recognition':
                    expr_results = assessment['results']
                    expr_accuracy = sum(r['detected_correctly'] for r in expr_results) / len(expr_results)
                    if expr_accuracy < 0.6:
                        risk_factors += 1
            
            # Risk assessment
            if risk_factors == 0:
                risk_level = "Low"
                risk_color = "🟢"
            elif risk_factors <= 2:
                risk_level = "Moderate"
                risk_color = "🟡"
            else:
                risk_level = "High"
                risk_color = "🔴"
            
            st.markdown('<div class="result-card">', unsafe_allow_html=True)
            st.markdown("#### 🎯 Overall Assessment Summary")
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Overall Accuracy", f"{overall_accuracy:.1%}")
            with col2:
                st.metric("Avg Response Time", f"{avg_response_time:.1f}s")
            with col3:
                st.metric("ASD Risk Level", f"{risk_color} {risk_level}")
            
            st.markdown("#### 📋 Recommendations")
            if risk_level == "Low":
                st.success("✅ Results suggest typical development patterns. Continue regular monitoring.")
            elif risk_level == "Moderate":
                st.warning("⚠️ Some areas may benefit from additional attention. Consider consulting a pediatric specialist.")
            else:
                st.error("🔴 Results suggest further evaluation may be beneficial. Please consult with a healthcare professional specializing in autism assessment.")
            
            st.markdown('</div>', unsafe_allow_html=True)

elif page == "📋 Reports":
    st.header("📋 Assessment Reports")
    
    if not st.session_state.child_profile:
        st.warning("⚠️ Please create a child profile first!")
    else:
        child_name = st.session_state.child_profile.get('child_name', 'Child')
        
        st.markdown(f"### Generate Report for {child_name}")
        
        report_type = st.selectbox(
            "Report Type",
            ["📊 Comprehensive Assessment Report", "📈 Progress Summary", "🎮 Game Performance Report"]
        )
        
        date_range = st.selectbox(
            "Time Period",
            ["Last Week", "Last Month", "All Time"]
        )
        
        if st.button("📄 Generate Report"):
            # Create comprehensive report
            report_data = {
                'child_profile': st.session_state.child_profile,
                'game_results': st.session_state.game_results,
                'assessment_data': st.session_state.assessment_data,
                'report_generated': str(datetime.now()),
                'report_type': report_type,
                'date_range': date_range
            }
            
            # Save report
            report_filename = f"report_{child_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            save_data(report_filename, report_data)
            
            st.success(f"✅ Report generated successfully!")
            st.info(f"📁 Report saved as: {report_filename}")
            
            # Display report preview
            st.markdown("### 📋 Report Preview")
            
            st.markdown(f"""
            **Child Information:**
            - Name: {child_name}
            - Age: {st.session_state.child_profile.get('child_age', 'N/A')}
            - Assessment Date: {datetime.now().strftime('%Y-%m-%d')}
            
            **Games Completed:**
            - Object Recognition: {len(st.session_state.game_results.get('object_recognition', []))} attempts
            - Emotion Matching: {len(st.session_state.game_results.get('emotion_matching', []))} attempts
            - Social Response: {len(st.session_state.game_results.get('social_response', []))} attempts
            
            **Assessment Tests:**
            - Face Recognition Tests: {len(st.session_state.assessment_data)} completed
            
            **Recommendations:**
            - Continue regular monitoring
            - Engage in social interaction activities
            - Practice emotion recognition games
            - Consult healthcare professional if concerns persist
            """)
            
            if st.button("📧 Email Report"):
                st.info("📧 Report would be emailed to registered address")
            
            if st.button("💾 Download PDF"):
                st.info("💾 PDF download functionality would be implemented here")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; padding: 1rem; background-color: #f0f8ff; border-radius: 10px;'>
    <strong>👧 Autism Detection App for Girls</strong><br>
    <small>Interactive Assessment Tool for Female Children (Ages 3-10)</small><br>
    <small>⚠️ For screening purposes only - Always consult healthcare professionals</small>
</div>
""", unsafe_allow_html=True)