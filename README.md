## Student Performance Prediction

This project aims to predict students’ average academic performance using machine learning techniques. It follows a modular, production-ready ML pipeline including data ingestion, data transformation, model training, evaluation, and model persistence.

The dataset contains student demographic and academic information such as:
- Gender
- Race / Ethnicity
- Parental Level of Education
- Lunch Type
- Test Preparation Course
- Math Score
- Reading Score
- Writing Score

### Target Variable
The target variable is calculated as:
average_score = (math_score + reading_score + writing_score) / 3


<br>

### Machine Learning Pipeline
#### Data Ingestion
- Reads raw CSV data
- Splits the dataset into training and testing sets

#### Data Transformation
- Handles missing values using SimpleImputer
- Encodes categorical features using OneHotEncoder
- Scales features using StandardScaler
- Saves preprocessing pipeline as preprocessor.pkl

#### Model Training
- Trains multiple regression models
- Performs hyperparameter tuning using GridSearchCV
- Selects the best model based on R² score
- Saves the trained model as model.pkl

#### Model Evaluation
- Evaluates model performance on test data
- Uses R² score as the evaluation metric

<img src = "https://github.com/bishal-pandey/StudentPerformanceSystem/blob/main/image/image.png">
