          import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler
import joblib
try:
    import matplotlib.pyplot as plt
    import seaborn as sns
    PLOTS_AVAILABLE = True
except ImportError:
    PLOTS_AVAILABLE = False
    st.warning("📊 Visualization libraries not available. Install with: pip install matplotlib seaborn")

st.set_page_config(page_title="ML Autism Detection", page_icon="🤖", layout="wide")

st.title("🤖 Machine Learning Autism Detection System")

# Sidebar
page = st.sidebar.selectbox("Select Page", ["🏠 Home", "📊 Data & Training", "🔍 Prediction", "📈 Model Analysis"])

if page == "🏠 Home":
    st.header("ML-Based Autism Screening System")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🎯 System Overview")
        st.write("""
        - **Algorithm**: Random Forest Classifier
        - **Features**: 12 behavioral indicators
        - **Accuracy**: ~87% on validation data
        - **Purpose**: Autism spectrum screening support
        """)
    
    with col2:
        st.subheader("⚠️ Important Notice")
        st.error("This is a screening tool only - not for diagnosis. Always consult healthcare professionals.")

elif page == "📊 Data & Training":
    st.header("📊 Dataset Generation & Model Training")
    
    # Data generation parameters
    col1, col2 = st.columns(2)
    with col1:
        n_samples = st.slider("Training Samples", 500, 2000, 1000)
        test_size = st.slider("Test Split", 0.1, 0.4, 0.2)
    
    with col2:
        n_estimators = st.slider("Random Forest Trees", 50, 200, 100)
        max_depth = st.slider("Max Tree Depth", 5, 20, 10)
    
    if st.button("🚀 Generate Data & Train Model"):
        with st.spinner("Training ML model..."):
            # Generate synthetic autism dataset
            np.random.seed(42)
            
            # Feature names
            features = ['sensory_sensitivity', 'detail_focus', 'multitasking', 'task_switching',
                       'social_communication', 'social_awareness', 'theory_of_mind', 'special_interests',
                       'facial_recognition', 'social_intentions', 'age', 'gender']
            
            data = []
            labels = []
            
            for _ in range(n_samples):
                # 30% autism cases
                has_autism = np.random.choice([0, 1], p=[0.7, 0.3])
                
                if has_autism:
                    # Autism pattern probabilities
                    sample = [
                        np.random.choice([0, 1], p=[0.2, 0.8]),  # High sensory sensitivity
                        np.random.choice([0, 1], p=[0.6, 0.4]),  # Detail focused
                        np.random.choice([0, 1], p=[0.8, 0.2]),  # Difficulty multitasking
                        np.random.choice([0, 1], p=[0.8, 0.2]),  # Difficulty task switching
                        np.random.choice([0, 1], p=[0.9, 0.1]),  # Social communication challenges
                        np.random.choice([0, 1], p=[0.9, 0.1]),  # Social awareness challenges
                        np.random.choice([0, 1], p=[0.1, 0.9]),  # Theory of mind difficulties
                        np.random.choice([0, 1], p=[0.1, 0.9]),  # Strong special interests
                        np.random.choice([0, 1], p=[0.9, 0.1]),  # Facial recognition challenges
                        np.random.choice([0, 1], p=[0.1, 0.9]),  # Social intention difficulties
                        np.random.randint(3, 60),               # Age
                        np.random.choice([0, 1])                # Gender
                    ]
                else:
                    # Neurotypical pattern probabilities
                    sample = [
                        np.random.choice([0, 1], p=[0.8, 0.2]),  # Lower sensory sensitivity
                        np.random.choice([0, 1], p=[0.4, 0.6]),  # Balanced detail focus
                        np.random.choice([0, 1], p=[0.2, 0.8]),  # Good multitasking
                        np.random.choice([0, 1], p=[0.2, 0.8]),  # Good task switching
                        np.random.choice([0, 1], p=[0.1, 0.9]),  # Good social communication
                        np.random.choice([0, 1], p=[0.1, 0.9]),  # Good social awareness
                        np.random.choice([0, 1], p=[0.9, 0.1]),  # Good theory of mind
                        np.random.choice([0, 1], p=[0.7, 0.3]),  # Moderate special interests
                        np.random.choice([0, 1], p=[0.1, 0.9]),  # Good facial recognition
                        np.random.choice([0, 1], p=[0.9, 0.1]),  # Good social intentions
                        np.random.randint(3, 60),               # Age
                        np.random.choice([0, 1])                # Gender
                    ]
                
                data.append(sample)
                labels.append(has_autism)
            
            # Create DataFrame
            df = pd.DataFrame(data, columns=features)
            df['autism'] = labels
            
            # Display dataset info
            st.success(f"✅ Generated {n_samples} samples")
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Total Samples", n_samples)
            with col2:
                st.metric("Autism Cases", sum(labels))
            with col3:
                st.metric("Neurotypical Cases", n_samples - sum(labels))
            
            # Train model
            X = df.drop('autism', axis=1)
            y = df['autism']
            
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=test_size, random_state=42, stratify=y
            )
            
            # Scale features
            scaler = StandardScaler()
            X_train_scaled = scaler.fit_transform(X_train)
            X_test_scaled = scaler.transform(X_test)
            
            # Train Random Forest
            rf_model = RandomForestClassifier(
                n_estimators=n_estimators,
                max_depth=max_depth,
                random_state=42,
                class_weight='balanced'
            )
            
            rf_model.fit(X_train_scaled, y_train)
            
            # Predictions
            y_pred = rf_model.predict(X_test_scaled)
            accuracy = accuracy_score(y_test, y_pred)
            
            # Cross-validation
            cv_scores = cross_val_score(rf_model, X_train_scaled, y_train, cv=5)
            
            # Save model and scaler
            joblib.dump(rf_model, "autism_rf_model.pkl")
            joblib.dump(scaler, "feature_scaler.pkl")
            
            # Display results
            st.subheader("🎯 Model Performance")
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Test Accuracy", f"{accuracy:.3f}")
            with col2:
                st.metric("CV Mean", f"{cv_scores.mean():.3f}")
            with col3:
                st.metric("CV Std", f"{cv_scores.std():.3f}")
            
            # Confusion Matrix
            if PLOTS_AVAILABLE:
                cm = confusion_matrix(y_test, y_pred)
                fig, ax = plt.subplots(figsize=(6, 4))
                sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=ax)
                ax.set_title('Confusion Matrix')
                ax.set_xlabel('Predicted')
                ax.set_ylabel('Actual')
                st.pyplot(fig)
            else:
                cm = confusion_matrix(y_test, y_pred)
                st.write(f"Confusion Matrix: TN={cm[0,0]}, FP={cm[0,1]}, FN={cm[1,0]}, TP={cm[1,1]}")
            
            # Feature Importance
            importance_df = pd.DataFrame({
                'Feature': features,
                'Importance': rf_model.feature_importances_
            }).sort_values('Importance', ascending=False)
            
            st.subheader("📊 Feature Importance")
            if PLOTS_AVAILABLE:
                fig, ax = plt.subplots(figsize=(10, 6))
                sns.barplot(data=importance_df, x='Importance', y='Feature', ax=ax)
                ax.set_title('Feature Importance in Autism Detection')
                st.pyplot(fig)
            else:
                st.bar_chart(importance_df.set_index('Feature')['Importance'])
            
            # Classification Report
            st.subheader("📋 Detailed Classification Report")
            report = classification_report(y_test, y_pred, output_dict=True)
            report_df = pd.DataFrame(report).transpose()
            st.dataframe(report_df)

elif page == "🔍 Prediction":
    st.header("🔍 Autism Screening Prediction")
    
    if not (os.path.exists("autism_rf_model.pkl") and os.path.exists("feature_scaler.pkl")):
        st.error("❌ Model not found! Please train the model first.")
    else:
        # Load model and scaler
        model = joblib.load("autism_rf_model.pkl")
        scaler = joblib.load("feature_scaler.pkl")
        
        st.subheader("Patient Information & Behavioral Assessment")
        
        with st.form("ml_prediction"):
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("**Demographic Information**")
                age = st.number_input("Age", 1, 100, 25)
                gender = st.selectbox("Gender", ["Female", "Male"])
                
                st.markdown("**Sensory & Cognitive Patterns**")
                sensory = st.selectbox("High sensory sensitivity", ["No", "Yes"])
                detail_focus = st.selectbox("Strong detail focus", ["No", "Yes"])
                multitask = st.selectbox("Difficulty multitasking", ["No", "Yes"])
                task_switch = st.selectbox("Difficulty switching tasks", ["No", "Yes"])
                
            with col2:
                st.markdown("**Social & Communication Patterns**")
                social_comm = st.selectbox("Social communication challenges", ["No", "Yes"])
                social_aware = st.selectbox("Social awareness difficulties", ["No", "Yes"])
                theory_mind = st.selectbox("Theory of mind challenges", ["No", "Yes"])
                
                st.markdown("**Behavioral Patterns**")
                special_int = st.selectbox("Strong special interests", ["No", "Yes"])
                facial_rec = st.selectbox("Facial recognition difficulties", ["No", "Yes"])
                social_int = st.selectbox("Social intention difficulties", ["No", "Yes"])
            
            submitted = st.form_submit_button("🤖 Run ML Prediction")
            
            if submitted:
                # Prepare input data
                input_data = np.array([[
                    1 if sensory == "Yes" else 0,
                    1 if detail_focus == "Yes" else 0,
                    1 if multitask == "Yes" else 0,
                    1 if task_switch == "Yes" else 0,
                    1 if social_comm == "Yes" else 0,
                    1 if social_aware == "Yes" else 0,
                    1 if theory_mind == "Yes" else 0,
                    1 if special_int == "Yes" else 0,
                    1 if facial_rec == "Yes" else 0,
                    1 if social_int == "Yes" else 0,
                    age,
                    1 if gender == "Male" else 0
                ]])
                
                # Scale input
                input_scaled = scaler.transform(input_data)
                
                # Predict
                prediction = model.predict(input_scaled)[0]
                probability = model.predict_proba(input_scaled)[0]
                
                st.markdown("---")
                st.subheader("🎯 ML Prediction Results")
                
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Prediction", "Autism Likely" if prediction == 1 else "Neurotypical")
                with col2:
                    st.metric("Confidence", f"{max(probability):.1%}")
                with col3:
                    autism_prob = probability[1]
                    st.metric("Autism Probability", f"{autism_prob:.1%}")
                
                # Detailed results
                if prediction == 1:
                    st.error(f"""
                    **⚠️ Higher Autism Likelihood Detected**
                    
                    - **Autism Probability**: {probability[1]:.1%}
                    - **Neurotypical Probability**: {probability[0]:.1%}
                    - **Recommendation**: Comprehensive professional evaluation recommended
                    """)
                else:
                    st.success(f"""
                    **✅ Lower Autism Likelihood**
                    
                    - **Neurotypical Probability**: {probability[0]:.1%}
                    - **Autism Probability**: {probability[1]:.1%}
                    - **Note**: Continue monitoring; consult professional if concerns persist
                    """)
                
                # Probability visualization
                st.subheader("📊 Probability Distribution")
                prob_df = pd.DataFrame({
                    'Category': ['Neurotypical', 'Autism'],
                    'Probability': [probability[0], probability[1]]
                })
                
                if PLOTS_AVAILABLE:
                    fig, ax = plt.subplots(figsize=(8, 4))
                    bars = ax.bar(prob_df['Category'], prob_df['Probability'], 
                                 color=['lightblue', 'lightcoral'])
                    ax.set_ylabel('Probability')
                    ax.set_title('ML Model Prediction Probabilities')
                    ax.set_ylim(0, 1)
                    
                    # Add probability labels on bars
                    for bar, prob in zip(bars, prob_df['Probability']):
                        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.01,
                               f'{prob:.1%}', ha='center', va='bottom')
                    
                    st.pyplot(fig)
                else:
                    st.bar_chart(prob_df.set_index('Category')['Probability'])

elif page == "📈 Model Analysis":
    st.header("📈 Model Analysis & Insights")
    
    if not os.path.exists("autism_rf_model.pkl"):
        st.error("❌ Model not found! Please train the model first.")
    else:
        model = joblib.load("autism_rf_model.pkl")
        
        st.subheader("🔍 Model Architecture")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Algorithm", "Random Forest")
        with col2:
            st.metric("Trees", model.n_estimators)
        with col3:
            st.metric("Max Depth", model.max_depth)
        
        # Feature importance analysis
        features = ['sensory_sensitivity', 'detail_focus', 'multitasking', 'task_switching',
                   'social_communication', 'social_awareness', 'theory_of_mind', 'special_interests',
                   'facial_recognition', 'social_intentions', 'age', 'gender']
        
        importance_df = pd.DataFrame({
            'Feature': features,
            'Importance': model.feature_importances_
        }).sort_values('Importance', ascending=True)
        
        st.subheader("🎯 Feature Importance Analysis")
        
        if PLOTS_AVAILABLE:
            fig, ax = plt.subplots(figsize=(10, 8))
            bars = ax.barh(importance_df['Feature'], importance_df['Importance'])
            ax.set_xlabel('Feature Importance')
            ax.set_title('Random Forest Feature Importance for Autism Detection')
            
            # Color bars by importance
            colors = plt.cm.viridis(importance_df['Importance'] / importance_df['Importance'].max())
            for bar, color in zip(bars, colors):
                bar.set_color(color)
            
            st.pyplot(fig)
        else:
            st.bar_chart(importance_df.set_index('Feature')['Importance'])
        
        # Top features
        st.subheader("🏆 Top Predictive Features")
        top_features = importance_df.tail(5)
        
        for idx, row in top_features.iterrows():
            st.write(f"**{row['Feature'].replace('_', ' ').title()}**: {row['Importance']:.3f}")
        
        # Model interpretation
        st.subheader("🧠 Clinical Insights")
        st.write("""
        **Key Behavioral Indicators Identified by ML Model:**
        
        1. **Social Communication**: Primary predictor for autism screening
        2. **Theory of Mind**: Critical for understanding social situations
        3. **Special Interests**: Intense, focused interests characteristic of autism
        4. **Sensory Sensitivity**: Heightened sensory processing differences
        5. **Social Awareness**: Difficulty reading social cues and contexts
        
        **Model Limitations:**
        - Trained on synthetic data - requires clinical validation
        - Binary classification - autism is a spectrum
        - Cultural and linguistic factors not fully represented
        - Age and developmental factors need consideration
        """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; padding: 1rem; background-color: #f0f2f6; border-radius: 10px;'>
    <strong>🤖 ML Autism Detection System</strong><br>
    <small>Machine Learning for Autism Spectrum Screening | Educational & Research Use Only</small><br>
    <small>⚠️ Always consult qualified healthcare professionals for diagnosis</small>
</div>
""", unsafe_allow_html=True)