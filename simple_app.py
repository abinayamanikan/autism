import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

st.set_page_config(page_title="Autism Detection", page_icon="🧠")

st.title("🧠 Autism Detection App")
st.write("Machine learning tool for autism screening")

# Sidebar
page = st.sidebar.selectbox("Select Page", ["Screening", "Train Model", "Info"])

if page == "Screening":
    st.header("Autism Screening Questionnaire")
    
    with st.form("questions"):
        st.write("Answer each question with Yes (1) or No (0):")
        
        q1 = st.radio("1. I notice small sounds others don't", [0, 1])
        q2 = st.radio("2. I focus on whole picture vs details", [0, 1]) 
        q3 = st.radio("3. I easily multitask", [0, 1])
        q4 = st.radio("4. I quickly return to tasks after interruption", [0, 1])
        q5 = st.radio("5. I read between the lines easily", [0, 1])
        q6 = st.radio("6. I know when someone is bored", [0, 1])
        q7 = st.radio("7. I struggle with character intentions in stories", [0, 1])
        q8 = st.radio("8. I like collecting information", [0, 1])
        q9 = st.radio("9. I read facial expressions easily", [0, 1])
        q10 = st.radio("10. I struggle understanding people's intentions", [0, 1])
        
        age = st.number_input("Age", 1, 100, 25)
        gender = st.selectbox("Gender", ["Female", "Male"])
        
        submit = st.form_submit_button("Get Prediction")
        
        if submit:
            if os.path.exists("model.pkl"):
                model = joblib.load("model.pkl")
                gender_code = 1 if gender == "Male" else 0
                data = [[q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, age, gender_code]]
                
                pred = model.predict(data)[0]
                prob = model.predict_proba(data)[0]
                
                if pred == 1:
                    st.error(f"⚠️ High autism likelihood ({prob[1]:.1%} confidence)")
                    st.write("**Consult a healthcare professional**")
                else:
                    st.success(f"✅ Low autism likelihood ({prob[0]:.1%} confidence)")
                    st.write("**This is screening only - consult professional if concerned**")
            else:
                st.warning("Train model first!")

elif page == "Train Model":
    st.header("Train ML Model")
    
    if st.button("Generate Data & Train"):
        with st.spinner("Training..."):
            # Generate synthetic data
            np.random.seed(42)
            data, labels = [], []
            
            for _ in range(1000):
                autism = np.random.choice([0, 1], p=[0.7, 0.3])
                
                if autism:
                    features = [
                        np.random.choice([0, 1], p=[0.3, 0.7]),  # sounds
                        np.random.choice([0, 1], p=[0.7, 0.3]),  # details
                        np.random.choice([0, 1], p=[0.7, 0.3]),  # multitask
                        np.random.choice([0, 1], p=[0.7, 0.3]),  # switching
                        np.random.choice([0, 1], p=[0.8, 0.2]),  # reading lines
                        np.random.choice([0, 1], p=[0.8, 0.2]),  # boredom
                        np.random.choice([0, 1], p=[0.2, 0.8]),  # intentions
                        np.random.choice([0, 1], p=[0.2, 0.8]),  # collecting
                        np.random.choice([0, 1], p=[0.8, 0.2]),  # faces
                        np.random.choice([0, 1], p=[0.2, 0.8]),  # people
                        np.random.randint(3, 60),  # age
                        np.random.choice([0, 1])   # gender
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
            
            # Train model
            model = RandomForestClassifier(n_estimators=50, random_state=42)
            model.fit(data, labels)
            
            # Save model
            joblib.dump(model, "model.pkl")
            
            st.success("✅ Model trained successfully!")
            st.info("📊 Ready for predictions")

else:  # Info page
    st.header("About This App")
    st.write("""
    **Purpose:** Autism screening using machine learning
    
    **⚠️ IMPORTANT:** This is a screening tool only, NOT for diagnosis
    
    **How to use:**
    1. Train the model first
    2. Complete the questionnaire
    3. Get screening results
    
    **Always consult healthcare professionals for proper diagnosis**
    """)