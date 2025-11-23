import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib

class AutismModelTrainer:
    def __init__(self):
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        self.feature_names = [f'Q{i+1}' for i in range(10)] + ['Age', 'Gender']
    
    def generate_synthetic_data(self, n_samples=1000):
        """Generate synthetic autism screening data"""
        np.random.seed(42)
        data = []
        labels = []
        
        for i in range(n_samples):
            has_autism = np.random.choice([0, 1], p=[0.7, 0.3])
            
            if has_autism:
                # Autism-like response patterns
                features = [
                    np.random.choice([0, 1], p=[0.3, 0.7]),  # Notice sounds
                    np.random.choice([0, 1], p=[0.7, 0.3]),  # Whole picture focus
                    np.random.choice([0, 1], p=[0.7, 0.3]),  # Multitasking difficulty
                    np.random.choice([0, 1], p=[0.7, 0.3]),  # Task switching
                    np.random.choice([0, 1], p=[0.8, 0.2]),  # Reading between lines
                    np.random.choice([0, 1], p=[0.8, 0.2]),  # Detecting boredom
                    np.random.choice([0, 1], p=[0.2, 0.8]),  # Character intentions
                    np.random.choice([0, 1], p=[0.2, 0.8]),  # Collecting information
                    np.random.choice([0, 1], p=[0.8, 0.2]),  # Reading faces
                    np.random.choice([0, 1], p=[0.2, 0.8]),  # People's intentions
                    np.random.randint(3, 60),               # Age
                    np.random.choice([0, 1])                # Gender
                ]
            else:
                # Neurotypical response patterns
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
            labels.append(has_autism)
        
        df = pd.DataFrame(data, columns=self.feature_names)
        df['Label'] = labels
        return df
    
    def train_model(self, df):
        """Train the autism detection model"""
        X = df.drop('Label', axis=1)
        y = df['Label']
        
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42, stratify=y
        )
        
        # Train model
        self.model.fit(X_train, y_train)
        
        # Evaluate
        y_pred = self.model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        
        # Cross-validation
        cv_scores = cross_val_score(self.model, X, y, cv=5)
        
        print(f"Test Accuracy: {accuracy:.3f}")
        print(f"CV Accuracy: {cv_scores.mean():.3f} (+/- {cv_scores.std() * 2:.3f})")
        print("\nClassification Report:")
        print(classification_report(y_test, y_pred))
        
        return accuracy, cv_scores
    
    def save_model(self, filename="autism_model.pkl"):
        """Save the trained model"""
        joblib.dump(self.model, filename)
        print(f"Model saved as {filename}")
    
    def get_feature_importance(self):
        """Get feature importance from the trained model"""
        importance_df = pd.DataFrame({
            'Feature': self.feature_names,
            'Importance': self.model.feature_importances_
        }).sort_values('Importance', ascending=False)
        return importance_df

if __name__ == "__main__":
    # Train the model
    trainer = AutismModelTrainer()
    
    print("Generating synthetic data...")
    data = trainer.generate_synthetic_data(1000)
    
    print("Training model...")
    accuracy, cv_scores = trainer.train_model(data)
    
    print("\nFeature Importance:")
    importance = trainer.get_feature_importance()
    print(importance)
    
    trainer.save_model()
    print("\nModel training completed!")