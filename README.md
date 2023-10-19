# SunbaseData ML Assignment

## Overview
Customer churn prediction is a crucial task for businesses aiming to enhance customer satisfaction and retention. This machine learning project, developed as part of the SunbaseData Machine Learning Internship Assignment, focuses on predicting customer churn based on historical customer data. The project follows a comprehensive machine learning pipeline, encompassing data preprocessing, exploration, and the development of predictive models.

The primary objectives of the project are to:
- Understand and analyze historical customer data.
- Develop and train machine learning models to predict customer churn.
- Implement a user-friendly interface using Streamlit for real-time predictions.
- Experiment with different algorithms, including RandomForest, CatBoost, XGBoost, and an Artificial Neural Network, to determine the most effective model.

## Demo Image
Image 1
![image](https://github.com/Sarthak-1408/Semantic-Similarity/assets/72247049/75c0b368-d805-410d-961d-29848c008bd9)

Image 2
![image](https://github.com/Sarthak-1408/Semantic-Similarity/assets/72247049/03ec45f6-5f49-4c39-a695-989c81bab280)

This repository provides the code, resources, and a Streamlit app for users to interact with the developed models and gain insights into customer churn predictions.
## Files and Directory Structure
- `SunbaseData ML Assignment.ipynb`: Jupyter Notebook containing the main code for data exploration, preprocessing, and modeling.
- `app.py`: Streamlit code for the user interface allowing users to interact with the customer churn prediction model.
- `customer_churn_model.h5`: Saved weights and architecture of the trained neural network model.
- `setup.sh`: Setup or configuration script for environment setup (if applicable).
- `requirements.txt`: File listing Python packages and versions required for the project.

## How to Use
1. **Explore the Notebook:**
   - Open and run the Jupyter Notebook (`SunbaseData ML Assignment.ipynb`) to understand the data exploration, preprocessing, and model development process.

2. **Run the Streamlit App:**
   - Execute `streamlit run app.py` in the terminal to launch the Streamlit app. This provides a user-friendly interface for customer churn prediction.

3. **Model Deployment:**
   - Ensure all required dependencies are installed using `pip install -r requirements.txt`.
   - Use the saved model weights (`customer_churn_model.h5`) for deployment.

## Dependencies
- Python 3.x
- Jupyter Notebook
- Streamlit
- TensorFlow
- Scikit-learn
- Pandas
- NumPy
- Matplotlib
- Seaborn

## Model training
If you need to retrain the model, refer to the training script and data in your Jupyter notebook or Python script. Update the model file and tokenizer accordingly.
