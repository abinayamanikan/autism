# Autism Detection App using Machine Learning

A web-based application that uses machine learning to assist in autism screening based on behavioral patterns from the AQ-10 questionnaire.

## ⚠️ Important Disclaimer

This is a **screening tool only** and should never replace professional medical evaluation. Always consult qualified healthcare professionals for proper autism diagnosis.

## Features

- **Interactive Web Interface**: Easy-to-use Streamlit web app
- **ML-Based Screening**: Random Forest classifier for pattern recognition
- **Real-time Predictions**: Instant results with confidence scores
- **Model Training**: Built-in synthetic data generation and model training
- **Feature Analysis**: Visualization of important behavioral indicators

## Quick Start

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the App**:
   ```bash
   streamlit run app.py
   ```

3. **Train the Model** (first time):
   - Navigate to "Model Training" page
   - Click "Generate Sample Data & Train Model"

4. **Use for Screening**:
   - Go to "Prediction" page
   - Answer the questionnaire
   - Get instant results

## How It Works

### Data Input
- 10 behavioral questions (simplified AQ-10)
- Age and gender demographics
- Binary responses (Yes/No)

### Machine Learning
- **Algorithm**: Random Forest Classifier
- **Features**: 12 input variables
- **Training**: Synthetic data with realistic patterns
- **Validation**: Cross-validation and test accuracy

### Output
- Risk assessment (High/Low likelihood)
- Confidence percentage
- Recommendations for next steps

## File Structure

```
Autism/
├── app.py              # Main Streamlit application
├── model_trainer.py    # Standalone model training
├── requirements.txt    # Python dependencies
├── README.md          # This file
└── autism_model.pkl   # Trained model (generated)
```

## Technical Details

### Model Performance
- Accuracy: ~85-90% on synthetic data
- Cross-validation: 5-fold validation
- Feature importance analysis included

### Key Features Analyzed
1. Sensory sensitivity (sounds, details)
2. Social communication patterns
3. Cognitive flexibility
4. Theory of mind abilities
5. Repetitive behaviors/interests

## Usage Guidelines

### For Healthcare Professionals
- Use as a preliminary screening tool
- Combine with clinical observation
- Follow up with comprehensive assessment

### For Individuals/Families
- Self-screening for awareness
- Educational purposes
- Starting point for professional consultation

## Limitations

- Based on synthetic training data
- Simplified questionnaire (AQ-10 subset)
- Not validated on clinical populations
- Cultural and linguistic factors not considered
- Age-specific variations not fully modeled

## Future Enhancements

- [ ] Real clinical data integration
- [ ] Multi-language support
- [ ] Age-specific models
- [ ] Additional screening instruments
- [ ] Professional dashboard
- [ ] Data export capabilities

## Contributing

This is an educational/demonstration project. For production use:
1. Validate with clinical data
2. Obtain proper medical approvals
3. Implement security measures
4. Add comprehensive testing

## License

Educational use only. Not for commercial or clinical deployment without proper validation and approvals.