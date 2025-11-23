import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

# Kid-friendly page config
st.set_page_config(
    page_title="Kids Autism Helper 🌈",
    page_icon="🧸",
    layout="wide"
)

# Colorful kid-friendly CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Comic+Neue:wght@300;400;700&display=swap');
    
    .stApp {
        font-family: 'Comic Neue', cursive;
        background: linear-gradient(45deg, #ff9a9e 0%, #fecfef 50%, #fecfef 100%);
    }
    
    .rainbow-header {
        background: linear-gradient(90deg, #ff6b6b, #4ecdc4, #45b7d1, #96ceb4, #feca57, #ff9ff3);
        padding: 2rem;
        border-radius: 20px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 8px 32px rgba(0,0,0,0.1);
        animation: rainbow 3s ease-in-out infinite alternate;
    }
    
    @keyframes rainbow {
        0% { transform: translateY(0px); }
        100% { transform: translateY(-5px); }
    }
    
    .fun-card {
        background: white;
        border-radius: 20px;
        padding: 2rem;
        margin: 1rem 0;
        box-shadow: 0 8px 25px rgba(0,0,0,0.1);
        border: 3px solid #ff6b6b;
    }
    
    .question-bubble {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 25px;
        margin: 1rem 0;
        box-shadow: 0 4px 15px rgba(102,126,234,0.3);
    }
    
    .happy-result {
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        color: white;
        padding: 2rem;
        border-radius: 20px;
        text-align: center;
        margin: 1rem 0;
        box-shadow: 0 8px 25px rgba(79,172,254,0.3);
    }
    
    .careful-result {
        background: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
        color: white;
        padding: 2rem;
        border-radius: 20px;
        text-align: center;
        margin: 1rem 0;
        box-shadow: 0 8px 25px rgba(250,112,154,0.3);
    }
    
    .stButton > button {
        background: linear-gradient(90deg, #ff6b6b, #4ecdc4);
        color: white;
        border: none;
        padding: 1rem 2rem;
        border-radius: 25px;
        font-weight: bold;
        font-size: 18px;
        font-family: 'Comic Neue', cursive;
        box-shadow: 0 4px 15px rgba(255,107,107,0.3);
        transition: all 0.3s;
    }
    
    .stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(255,107,107,0.4);
    }
    
    .emoji-big {
        font-size: 3rem;
        text-align: center;
        margin: 1rem 0;
    }
    
    .kid-metric {
        background: white;
        border-radius: 20px;
        padding: 1.5rem;
        text-align: center;
        margin: 1rem 0;
        border: 3px solid #4ecdc4;
        box-shadow: 0 4px 15px rgba(78,205,196,0.2);
    }
    
    .progress-fun {
        background: white;
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        border: 2px solid #feca57;
    }
    
    h1, h2, h3 {
        color: #ff6b6b;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

# Fun header
st.markdown("""
<div class="rainbow-header">
    <h1>🌈 Kids Autism Helper 🧸</h1>
    <p style="font-size: 24px; margin: 0;">Fun & Friendly Assessment for Children</p>
    <p style="font-size: 18px; margin: 0.5rem 0 0 0;">Helping families understand their amazing kids! ✨</p>
</div>
""", unsafe_allow_html=True)

# Fun navigation
page = st.selectbox(
    "🎈 Choose Your Adventure!",
    ["🏠 Welcome Home", "🎯 Fun Assessment", "🤖 Magic Training", "📚 Learn More"],
    index=0
)

if page == "🏠 Welcome Home":
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="kid-metric">
            <div class="emoji-big">🎨</div>
            <h3>Creative & Fun</h3>
            <p>Colorful questions made just for kids!</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="kid-metric">
            <div class="emoji-big">⚡</div>
            <h3>Super Quick</h3>
            <p>Only takes 5 minutes - faster than brushing teeth!</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="kid-metric">
            <div class="emoji-big">🛡️</div>
            <h3>Safe & Private</h3>
            <p>All your answers stay on your computer!</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('<div class="fun-card">', unsafe_allow_html=True)
    st.markdown("""
    ### 🌟 Welcome to Our Special Helper!
    
    Hi there! This is a special tool to help parents and teachers understand how amazing and unique every child is! 
    
    **🎯 What We Do:**
    - Ask fun questions about how kids like to play and learn
    - Use smart computer magic to give helpful information
    - Help families know if they should talk to a doctor
    
    **🌈 Remember:**
    - Every child is special and wonderful! 
    - This is just a helper tool - not a doctor
    - Always talk to real doctors about important things
    - You are amazing just the way you are! ✨
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    if st.button("🚀 Start Fun Assessment!", key="home_start"):
        st.balloons()

elif page == "🎯 Fun Assessment":
    st.markdown("### 🎯 Let's Play the Question Game!")
    st.markdown("*Answer these fun questions about your child's favorite ways to play and learn!*")
    
    with st.form("kids_assessment"):
        # Child info
        st.markdown('<div class="fun-card">', unsafe_allow_html=True)
        st.markdown("#### 👶 Tell Us About Your Child")
        
        col1, col2 = st.columns(2)
        with col1:
            child_age = st.number_input("🎂 How old is your child?", min_value=2, max_value=18, value=6)
        with col2:
            child_gender = st.selectbox("👦👧 Gender", ["Girl", "Boy", "Other"])
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Fun questions
        kid_questions = [
            "🔊 Your child notices tiny sounds that others might miss (like a clock ticking far away)",
            "🖼️ Your child likes to see the whole picture instead of tiny details",
            "🎪 Your child can easily do many things at the same time (like coloring while listening)",
            "🔄 If someone interrupts your child, they can quickly go back to what they were doing",
            "💭 Your child understands when people say things without saying them directly",
            "😴 Your child knows when someone is getting bored while talking to them",
            "📖 When reading stories, your child finds it hard to guess what characters are thinking",
            "📚 Your child loves collecting facts about things they're interested in",
            "😊 Your child can tell how someone feels just by looking at their face",
            "🤔 Your child finds it tricky to understand what people really want"
        ]
        
        answers = []
        for i, question in enumerate(kid_questions, 1):
            st.markdown(f"""
            <div class="question-bubble">
                <strong>Question {i}:</strong><br>
                {question}
            </div>
            """, unsafe_allow_html=True)
            
            answer = st.radio(
                f"Q{i}",
                ["❌ Not Really", "✅ Yes, Often!"],
                key=f"kid_q{i}",
                horizontal=True,
                label_visibility="collapsed"
            )
            answers.append(1 if answer == "✅ Yes, Often!" else 0)
        
        st.markdown("---")
        
        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown("### 🎉 Ready to See the Magic Results?")
            st.markdown("Click the button to get your special report!")
        
        with col2:
            submitted = st.form_submit_button("✨ Show Me Magic Results!", use_container_width=True)
        
        if submitted:
            if os.path.exists("model.pkl"):
                model = joblib.load("model.pkl")
                gender_code = 1 if child_gender == "Boy" else 0
                data = [answers + [child_age, gender_code]]
                
                prediction = model.predict(data)[0]
                probability = model.predict_proba(data)[0]
                
                st.markdown("---")
                st.markdown("### 🎊 Your Special Results Are Here!")
                
                if prediction == 1:
                    st.markdown(f"""
                    <div class="careful-result">
                        <div class="emoji-big">🌟</div>
                        <h3>Your Child is Extra Special!</h3>
                        <p><strong>Magic Score:</strong> {probability[1]:.0%} confidence</p>
                        <p><strong>What This Means:</strong> Your child might learn and play in wonderfully unique ways!</p>
                        <p><strong>Next Adventure:</strong> Talk to a friendly doctor who knows about special kids</p>
                        <p><strong>Remember:</strong> Different is beautiful and amazing! 🌈</p>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown(f"""
                    <div class="happy-result">
                        <div class="emoji-big">🎈</div>
                        <h3>Your Child is Wonderfully Typical!</h3>
                        <p><strong>Magic Score:</strong> {probability[0]:.0%} confidence</p>
                        <p><strong>What This Means:</strong> Your child shows typical learning and play patterns</p>
                        <p><strong>Keep Doing:</strong> Continue having fun and learning together!</p>
                        <p><strong>Remember:</strong> Every child is special in their own way! ✨</p>
                    </div>
                    """, unsafe_allow_html=True)
                
                # Fun progress bar
                st.markdown("**🌈 Confidence Rainbow:**")
                confidence = max(probability[0], probability[1])
                st.progress(confidence)
                
                # Score display
                total_score = sum(answers)
                st.markdown(f"**🎯 Fun Score: {total_score}/10 stars!**")
                
                st.balloons()
                
            else:
                st.error("🤖 Oops! The magic computer needs to learn first! Go to Magic Training!")

elif page == "🤖 Magic Training":
    st.markdown("### 🤖 Teaching Our Magic Computer!")
    
    st.markdown('<div class="fun-card">', unsafe_allow_html=True)
    st.markdown("#### 🎓 Computer Learning Status")
    
    col1, col2 = st.columns(2)
    with col1:
        if os.path.exists("model.pkl"):
            st.success("✅ **Magic Computer:** Ready to help!")
            st.info("🧠 **Brain Status:** Super smart and trained!")
        else:
            st.warning("⚠️ **Magic Computer:** Still learning...")
            st.error("🎯 **Need To Do:** Teach the computer!")
    
    with col2:
        st.markdown("""
        **🎪 How Our Magic Works:**
        - 🧠 Smart computer brain (AI)
        - 📚 Learns from 1000 practice examples
        - 🎯 Gets really good at helping
        - ⚡ Gives answers super fast!
        """)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    if st.button("🎪 Teach the Magic Computer!", use_container_width=True):
        st.markdown('<div class="progress-fun">', unsafe_allow_html=True)
        
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        # Fun training messages
        status_text.text("🎨 Creating colorful practice examples...")
        progress_bar.progress(25)
        
        np.random.seed(42)
        training_data, labels = [], []
        
        for _ in range(1000):
            special_kid = np.random.choice([0, 1], p=[0.7, 0.3])
            
            if special_kid:
                features = [
                    np.random.choice([0, 1], p=[0.3, 0.7]),  # sounds
                    np.random.choice([0, 1], p=[0.7, 0.3]),  # details
                    np.random.choice([0, 1], p=[0.7, 0.3]),  # multitask
                    np.random.choice([0, 1], p=[0.7, 0.3]),  # switching
                    np.random.choice([0, 1], p=[0.8, 0.2]),  # communication
                    np.random.choice([0, 1], p=[0.8, 0.2]),  # boredom
                    np.random.choice([0, 1], p=[0.2, 0.8]),  # intentions
                    np.random.choice([0, 1], p=[0.2, 0.8]),  # collecting
                    np.random.choice([0, 1], p=[0.8, 0.2]),  # faces
                    np.random.choice([0, 1], p=[0.2, 0.8]),  # people
                    np.random.randint(2, 18),  # age
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
                    np.random.randint(2, 18),
                    np.random.choice([0, 1])
                ]
            
            training_data.append(features)
            labels.append(special_kid)
        
        progress_bar.progress(60)
        status_text.text("🧠 Teaching the computer to be super smart...")
        
        model = RandomForestClassifier(n_estimators=50, random_state=42)
        model.fit(training_data, labels)
        
        progress_bar.progress(90)
        status_text.text("💾 Saving the computer's new brain...")
        
        joblib.dump(model, "model.pkl")
        
        progress_bar.progress(100)
        status_text.text("🎉 Magic computer is ready to help kids!")
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.success("🎊 **Hooray!** The magic computer learned everything!")
        st.balloons()

else:  # Learn More page
    st.markdown("### 📚 Learn More About Our Helper!")
    
    tab1, tab2, tab3 = st.tabs(["🌈 For Kids", "👨‍👩‍👧‍👦 For Parents", "⚠️ Important Stuff"])
    
    with tab1:
        st.markdown('<div class="fun-card">', unsafe_allow_html=True)
        st.markdown("""
        #### 🌟 Hey Kids! This is For You!
        
        **🎯 What is this cool tool?**
        - It's like a fun game that asks questions about how you like to play!
        - A smart computer helps figure out what makes you special
        - It helps grown-ups understand how awesome you are!
        
        **🎨 Why are some kids different?**
        - Every kid's brain works in amazing ways!
        - Some kids are super good at noticing details
        - Some kids have special interests they love A LOT
        - Some kids need quiet time to feel happy
        - ALL kids are wonderful and important! 🌈
        
        **🤗 Remember:**
        - You are perfect just the way you are!
        - Being different makes the world more colorful
        - Ask questions if you're curious about anything
        - Grown-ups are here to help and love you! ✨
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with tab2:
        st.markdown('<div class="fun-card">', unsafe_allow_html=True)
        st.markdown("""
        #### 👨‍👩‍👧‍👦 Information for Parents & Caregivers
        
        **🎯 Purpose of This Tool:**
        - Early screening support for autism spectrum traits in children
        - Child-friendly interface to reduce assessment anxiety
        - Educational tool to promote autism awareness
        - Starting point for professional consultation
        
        **🌈 Child-Centered Approach:**
        - Colorful, engaging design reduces stress
        - Simple language appropriate for family discussions
        - Positive framing emphasizes uniqueness and strengths
        - Non-threatening assessment environment
        
        **📋 What the Assessment Covers:**
        - Sensory processing differences
        - Social communication patterns
        - Cognitive flexibility and attention
        - Special interests and repetitive behaviors
        - Theory of mind development
        
        **🔍 Next Steps After Assessment:**
        - Discuss results with your child's pediatrician
        - Consider comprehensive evaluation if indicated
        - Explore support resources in your community
        - Celebrate your child's unique strengths and abilities
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with tab3:
        st.markdown("""
        <div style="background: #fff3cd; border: 3px solid #ffc107; color: #856404; padding: 2rem; border-radius: 20px; margin: 1rem 0;">
            <h4>⚠️ SUPER IMPORTANT GROWN-UP STUFF</h4>
            
            <p><strong>🏥 This is NOT a doctor tool!</strong></p>
            <ul>
                <li><strong>Screening Only:</strong> This tool helps identify children who might benefit from professional evaluation</li>
                <li><strong>Not Diagnostic:</strong> Only qualified professionals can diagnose autism spectrum conditions</li>
                <li><strong>Professional Consultation:</strong> Always discuss results with your child's healthcare provider</li>
                <li><strong>Synthetic Data:</strong> Our computer learned from practice examples, not real medical data</li>
                <li><strong>Individual Differences:</strong> Every child develops at their own pace and in their own way</li>
            </ul>
            
            <p><strong>🌟 Remember: Every child is valuable, loved, and has unique gifts to share with the world!</strong></p>
        </div>
        """, unsafe_allow_html=True)

# Fun footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; background: linear-gradient(90deg, #ff6b6b, #4ecdc4, #45b7d1); color: white; padding: 2rem; border-radius: 20px; margin: 2rem 0;">
    <h3>🌈 Kids Autism Helper 🧸</h3>
    <p style="font-size: 16px; margin: 0;">Making assessments fun and friendly for amazing kids everywhere!</p>
    <p style="font-size: 14px; margin: 0.5rem 0 0 0;">Always remember: You are special, loved, and wonderful! ✨</p>
</div>
""", unsafe_allow_html=True)