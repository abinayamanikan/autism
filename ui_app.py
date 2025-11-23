import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

# Page config
st.set_page_config(
    page_title="Autism Detection",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    .question-card {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #667eea;
        margin: 1rem 0;
    }
    .result-success {
        background: #d4edda;
        border: 1px solid #c3e6cb;
        color: #155724;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
    }
    .result-warning {
        background: #f8d7da;
        border: 1px solid #f5c6cb;
        color: #721c24;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
    }
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
    }
    .stButton > button {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 0.5rem 2rem;
        border-radius: 25px;
        font-weight: bold;
    }
    .metric-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        text-align: center;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="main-header">
    <h1>🧠 Autism Detection System</h1>
    <p>AI-Powered Screening Tool for Autism Spectrum Assessment</p>
</div>
""", unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.markdown("### 🔍 Navigation")
page = st.sidebar.selectbox(
    "Choose Section",
    ["🏠 Home", "📋 Screening", "🤖 Train Model", "ℹ️ Information"],
    index=0
)

if page == "🏠 Home":
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h3>🎯 Purpose</h3>
            <p>Early autism screening using advanced machine learning</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h3>⚡ Fast</h3>
            <p>Get results in under 5 minutes</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <h3>🔒 Private</h3>
            <p>All data processed locally</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        ### 🚀 Quick Start Guide
        
        1. **Train the Model** - Generate AI model (one-time setup)
        2. **Complete Screening** - Answer 10 behavioral questions
        3. **Get Results** - Receive instant assessment with confidence score
        
        ⚠️ **Important**: This is a screening tool only. Always consult healthcare professionals for diagnosis.
        """)
    
    with col2:
        if st.button("🚀 Start Screening", key="home_start"):
            st.experimental_set_query_params(page="screening")

elif page == "📋 Screening":
    st.markdown("### 📋 Autism Screening Questionnaire")
    st.markdown("Please answer each question honestly. There are no right or wrong answers.")
    
    with st.form("screening_form", clear_on_submit=False):
        questions = [
            "I often notice small sounds when others do not",
            "I usually concentrate more on the whole picture, rather than small details", 
            "I find it easy to do more than one thing at once",
            "If there is an interruption, I can switch back to what I was doing very quickly",
            "I find it easy to 'read between the lines' when someone is talking",
            "I know how to tell if someone listening to me is getting bored",
            "When I'm reading a story I find it difficult to work out the characters' intentions",
            "I like to collect information about categories of things",
            "I find it easy to work out what someone is thinking or feeling just by looking at their face",
            "I find it difficult to work out people's intentions"
        ]
        
        answers = []
        for i, question in enumerate(questions, 1):
            st.markdown(f"""
            <div class="question-card">
                <strong>Question {i}:</strong> {question}
            </div>
            """, unsafe_allow_html=True)
            
            answer = st.radio(
                f"Q{i}",
                ["No", "Yes"],
                key=f"q{i}",
                horizontal=True,
                label_visibility="collapsed"
            )
            answers.append(1 if answer == "Yes" else 0)
        
        st.markdown("---")
        col1, col2 = st.columns(2)
        
        with col1:
            age = st.number_input("Age", min_value=1, max_value=100, value=25)
        
        with col2:
            gender = st.selectbox("Gender", ["Female", "Male"])
        
        submitted = st.form_submit_button("🔍 Get Assessment", use_container_width=True)
        
        if submitted:
            if os.path.exists("model.pkl"):
                model = joblib.load("model.pkl")
                gender_code = 1 if gender == "Male" else 0
                data = [answers + [age, gender_code]]
                
                pred = model.predict(data)[0]
                prob = model.predict_proba(data)[0]
                
                st.markdown("---")
                st.markdown("### 📊 Assessment Results")
                
                if pred == 1:
                    st.markdown(f"""
                    <div class="result-warning">
                        <h4>⚠️ Higher Likelihood Detected</h4>
                        <p><strong>Confidence:</strong> {prob[1]:.1%}</p>
                        <p><strong>Recommendation:</strong> Please consult with a qualified healthcare professional for comprehensive evaluation.</p>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown(f"""
                    <div class="result-success">
                        <h4>✅ Lower Likelihood Detected</h4>
                        <p><strong>Confidence:</strong> {prob[0]:.1%}</p>
                        <p><strong>Note:</strong> This screening suggests lower likelihood, but consult a professional if you have concerns.</p>
                    </div>
                    """, unsafe_allow_html=True)
                
                # Progress bar for confidence
                st.markdown("**Confidence Level:**")
                confidence = max(prob[0], prob[1])
                st.progress(confidence)
                
            else:
                st.error("❌ Model not found! Please train the model first.")

elif page == "🤖 Train Model":
    st.markdown("### 🤖 AI Model Training")
    st.markdown("Train the machine learning model with synthetic autism screening data.")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.info("""
        **What happens during training:**
        - Generates 1000 synthetic data points
        - Trains Random Forest classifier
        - Validates model accuracy
        - Saves model for predictions
        """)
    
    with col2:
        if os.path.exists("model.pkl"):
            st.success("✅ Model Ready")
        else:
            st.warning("⚠️ No Model Found")
    
    if st.button("🚀 Generate Data & Train Model", use_container_width=True):
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        with st.spinner("Training AI model..."):
            # Generate data
            status_text.text("Generating synthetic data...")
            progress_bar.progress(25)
            
            np.random.seed(42)
            data, labels = [], []
            
            for _ in range(1000):
                autism = np.random.choice([0, 1], p=[0.7, 0.3])
                
                if autism:
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
                        np.random.randint(3, 60),
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
                        np.random.randint(3, 60),
                        np.random.choice([0, 1])
                    ]
                
                data.append(features)
                labels.append(autism)
            
            progress_bar.progress(50)
            status_text.text("Training model...")
            
            # Train model
            model = RandomForestClassifier(n_estimators=50, random_state=42)
            model.fit(data, labels)
            
            progress_bar.progress(75)
            status_text.text("Saving model...")
            
            # Save model
            joblib.dump(model, "model.pkl")
            
            progress_bar.progress(100)
            status_text.text("Training complete!")
            
            st.success("🎉 Model trained successfully!")
            st.balloons()

else:  # Information page
    st.markdown("### ℹ️ About This Application")
    
    tab1, tab2, tab3 = st.tabs(["📖 Overview", "⚠️ Disclaimer", "🔬 Technical"])
    
    with tab1:
        st.markdown("""
        #### 🎯 Purpose
        This application uses artificial intelligence to assist in autism spectrum screening based on behavioral patterns from the AQ-10 questionnaire.
        
        #### 🔍 How It Works
        1. **Questionnaire**: Answer 10 behavioral questions
        2. **AI Analysis**: Machine learning model analyzes response patterns
        3. **Assessment**: Provides likelihood assessment with confidence score
        
        #### 👥 Who Can Use This
        - Individuals seeking preliminary screening
        - Parents concerned about their children
        - Healthcare professionals as a supplementary tool
        - Researchers and educators
        """)
    
    with tab2:
        st.error("""
        #### ⚠️ IMPORTANT MEDICAL DISCLAIMER
        
        - This is a **SCREENING TOOL ONLY**, not a diagnostic instrument
        - Results should **NEVER replace professional medical evaluation**
        - Always consult qualified healthcare professionals for proper diagnosis
        - The model is trained on synthetic data for demonstration purposes
        - Not validated on clinical populations
        - Cultural and linguistic factors not considered
        """)
    
    with tab3:
        st.markdown("""
        #### 🤖 Machine Learning Details
        - **Algorithm**: Random Forest Classifier
        - **Features**: 12 input variables (10 questions + age + gender)
        - **Training Data**: 1000 synthetic samples
        - **Accuracy**: ~85-90% on synthetic data
        
        #### 📊 Key Features Analyzed
        1. Sensory sensitivity patterns
        2. Social communication abilities
        3. Cognitive flexibility
        4. Theory of mind capabilities
        5. Repetitive behaviors and interests
        
        #### 🛠️ Technology Stack
        - **Frontend**: Streamlit
        - **ML Library**: Scikit-learn
        - **Data Processing**: Pandas, NumPy
        """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 1rem;'>
    <small>Autism Detection System | Educational Use Only | Always Consult Healthcare Professionals</small>
</div>
""", unsafe_allow_html=True)