import streamlit as st
import tensorflow as tf

# Load the saved model
model = tf.keras.models.load_model('customer_churn_model.h5')

# Create the user interface
st.title("SunbaseData - Machine Learning Internship Assignment")
st.header('Customer Churn Prediction')
st.write('Enter the following information:')

age = st.number_input('Age')
gender = st.selectbox('Gender', ['Male', 'Female'])
if gender == 'Male':
    gender_val = 1
else:
    gender_val = 0

location_mapping = {'Miami': 1, 'New York': 2, 'Chicago': 3, 'Houston': 4, 'Los Angeles': 5}
location = st.selectbox('Location', list(location_mapping.keys()))
location_val = location_mapping[location]

subscription_length = st.number_input('Subscription Length (months)')
monthly_bill = st.number_input('Monthly Bill')
total_usage = st.number_input('Total Usage (GB)')

if st.button('Submit'):
    # Make predictions using the loaded model
    prediction = model.predict([[age, gender_val, location_val, subscription_length, monthly_bill, total_usage]])

    st.text(f"Confidence - {prediction[0]}")
    # Display the prediction
    if prediction[0] > 0.5:
        st.write('Churn: Yes')
    else:
        st.write('Churn: No')