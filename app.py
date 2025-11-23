import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import joblib
import os

# Page config
st.set_page_config(page_title="Autism Detection App", page_icon="🧠", layout="wide")

# Title
st.title("🧠 Autism Detection Using Machine Learning")
st.markdown("This app uses machine learning to assist in autism screening based on behavioral patterns.")

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Choose a page", ["Prediction", "Model Training", "About"])

if page == "Prediction":
    st.header("Autism Screening Questionnaire")
    
    # Create input form
    with st.form("screening_form"):
        st.subheader("Please answer the following questions:")
        
        # AQ-10 questions (simplified version)
        q1 = st.selectbox("1. I often notice small sounds when others do not", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
        q2 = st.selectbox("2. I usually concentrate more on the whole picture, rather than small details", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
        q3 = st.selectbox("3. I find it easy to do more than one thing at once", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
        q4 = st.selectbox("4. If there is an interruption, I can switch back to what I was doing very quickly", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
        q5 = st.selectbox("5. I find it easy to 'read between the lines' when someone is talking", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
        q6 = st.selectbox("6. I know how to tell if someone listening to me is getting bored", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
        q7 = st.selectbox("7. When I'm reading a story I find it difficult to work out the characters' intentions", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
        q8 = st.selectbox("8. I like to collect information about categories of things", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
        q9 = st.selectbox("9. I find it easy to work out what someone is thinking or feeling just by looking at their face", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
        q10 = st.selectbox("10. I find it difficult to work out people's intentions", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
        
        # Additional demographic info
        age = st.number_input("Age", min_value=1, max_value=100, value=25)
        gender = st.selectbox("Gender", ["Male", "Female"])
        
        submitted = st.form_submit_button("Get Prediction")
        
        if submitted:
            # Prepare input data
            gender_encoded = 1 if gender == "Male" else 0
            input_data = np.array([[q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, age, gender_encoded]])
            
            # Load model if exists
            if os.path.exists("autism_model.pkl"):
                model = joblib.load("autism_model.pkl")
                prediction = model.predict(input_data)[0]
                probability = model.predict_proba(input_data)[0]
                
                st.subheader("Prediction Result")
                if prediction == 1:
                    st.error(f"⚠️ High likelihood of autism traits (Confidence: {probability[1]:.2%})")
                    st.markdown("**Recommendation:** Please consult with a healthcare professional for proper diagnosis.")
                else:
                    st.success(f"✅ Low likelihood of autism traits (Confidence: {probability[0]:.2%})")
                    st.markdown("**Note:** This is a screening tool only. Consult a professional if you have concerns.")
            else:
                st.warning("Model not found. Please train the model first in the 'Model Training' section.")

elif page == "Model Training":
    st.header("Train the Machine Learning Model")
    
    if st.button("Generate Sample Data & Train Model"):
        with st.spinner("Generating data and training model..."):
            # Generate synthetic autism screening data
            np.random.seed(42)
            n_samples = 1000
            
            # Generate features (10 AQ questions + age + gender)
            data = []
            labels = []
            
            for i in range(n_samples):
                # Simulate autism traits (30% positive cases)
                has_autism = np.random.choice([0, 1], p=[0.7, 0.3])
                
                if has_autism:
                    # Higher scores on certain questions for autism
                    features = [
                        np.random.choice([0, 1], p=[0.3, 0.7]),  # q1: notice sounds
                        np.random.choice([0, 1], p=[0.7, 0.3]),  # q2: whole picture
                        np.random.choice([0, 1], p=[0.7, 0.3]),  # q3: multitask
                        np.random.choice([0, 1], p=[0.7, 0.3]),  # q4: switch tasks
                        np.random.choice([0, 1], p=[0.8, 0.2]),  # q5: read between lines
                        np.random.choice([0, 1], p=[0.8, 0.2]),  # q6: detect boredom
                        np.random.choice([0, 1], p=[0.2, 0.8]),  # q7: character intentions
                        np.random.choice([0, 1], p=[0.2, 0.8]),  # q8: collect info
                        np.random.choice([0, 1], p=[0.8, 0.2]),  # q9: read faces
                        np.random.choice([0, 1], p=[0.2, 0.8]),  # q10: people's intentions
                        np.random.randint(3, 60),  # age
                        np.random.choice([0, 1])   # gender
                    ]
                else:
                    # Lower scores for neurotypical
                    features = [
                        np.random.choice([0, 1], p=[0.7, 0.3]),  # q1
                        np.random.choice([0, 1], p=[0.3, 0.7]),  # q2
                        np.random.choice([0, 1], p=[0.3, 0.7]),  # q3
                        np.random.choice([0, 1], p=[0.3, 0.7]),  # q4
                        np.random.choice([0, 1], p=[0.2, 0.8]),  # q5
                        np.random.choice([0, 1], p=[0.2, 0.8]),  # q6
                        np.random.choice([0, 1], p=[0.8, 0.2]),  # q7
                        np.random.choice([0, 1], p=[0.7, 0.3]),  # q8
                        np.random.choice([0, 1], p=[0.2, 0.8]),  # q9
                        np.random.choice([0, 1], p=[0.8, 0.2]),  # q10
                        np.random.randint(3, 60),  # age
                        np.random.choice([0, 1])   # gender
                    ]
                
                data.append(features)
                labels.append(has_autism)
            
            # Create DataFrame
            columns = [f'Q{i+1}' for i in range(10)] + ['Age', 'Gender']
            df = pd.DataFrame(data, columns=columns)
            df['Label'] = labels
            
            # Split data
            X = df.drop('Label', axis=1)
            y = df['Label']
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
            
            # Train model
            model = RandomForestClassifier(n_estimators=100, random_state=42)
            model.fit(X_train, y_train)
            
            # Evaluate
            y_pred = model.predict(X_test)
            accuracy = accuracy_score(y_test, y_pred)
            
            # Save model
            joblib.dump(model, "autism_model.pkl")
            
            st.success(f"✅ Model trained successfully!")
            st.info(f"📊 Model Accuracy: {accuracy:.2%}")
            
            # Show feature importance
            feature_importance = pd.DataFrame({
                'Feature': columns,
                'Importance': model.feature_importances_
            }).sort_values('Importance', ascending=False)
            
            st.subheader("Feature Importance")
            st.bar_chart(feature_importance.set_index('Feature')['Importance'])

elif page == "About":
    st.header("About This App")
    
    st.markdown("""
    ### 🎯 Purpose
    This application is designed to assist in autism screening using machine learning techniques. 
    It's based on simplified AQ-10 (Autism Spectrum Quotient) questionnaire patterns.
    
    ### ⚠️ Important Disclaimer
    - This is a **screening tool only**, not a diagnostic instrument
    - Results should **never replace professional medical evaluation**
    - Always consult qualified healthcare professionals for proper diagnosis
    - The model is trained on synthetic data for demonstration purposes
    
    ### 🔬 How It Works
    1. **Data Collection**: Uses behavioral pattern questions
    2. **Machine Learning**: Random Forest classifier analyzes responses
    3. **Prediction**: Provides likelihood assessment with confidence scores
    
    ### 📊 Model Features
    - 10 behavioral questions (simplified AQ-10)
    - Age and gender demographics
    - Random Forest algorithm
    - Feature importance analysis
    
    ### 🚀 Usage
    1. Train model first (Model Training page)
    2. Complete questionnaire (Prediction page)
    3. Get instant ML-based assessment
    """) AQ-10)
    - Age and gender demographics
    - Random Forest algorithm for classification
    - Feature importance analysis
    
    ### 🛠️ Technical Stack
    - **Frontend**: Streamlit
    - **ML Library**: Scikit-learn
    - **Model**: Random Forest Classifier
    - **Data Processing**: Pandas, NumPy
    """)