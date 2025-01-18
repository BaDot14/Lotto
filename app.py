import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# Streamlit app title
st.title("Lotto Dataset Prediction")

# File uploader
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    # Read the uploaded CSV file
    data = pd.read_csv(uploaded_file)

    # Display dataset preview
    st.subheader("Dataset Preview")
    st.write(data.head())

    # Check for necessary columns
    required_columns = ['NUMBER DRAWN 1', 'NUMBER DRAWN 2', 'NUMBER DRAWN 3', 
                        'NUMBER DRAWN 4', 'NUMBER DRAWN 5', 'NUMBER DRAWN 6', 'DRAW NUMBER']
    if all(col in data.columns for col in required_columns):
        # Select features and target
        X = data[['NUMBER DRAWN 1', 'NUMBER DRAWN 2', 'NUMBER DRAWN 3', 
                  'NUMBER DRAWN 4', 'NUMBER DRAWN 5', 'NUMBER DRAWN 6']]
        y = data['DRAW NUMBER']

        # Split the data
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train the model
        model = LinearRegression()
        model.fit(X_train, y_train)

        # Make predictions
        predictions = model.predict(X_test)

        # Calculate accuracy
        accuracy = 100 - mean_absolute_error(y_test, predictions)

        # Display results
        st.subheader("Prediction Results")
        st.write(f"Accuracy: {accuracy:.2f}%")
        st.write("Predicted Numbers:")
        st.write(predictions[:10])  # Show the first 10 predictions
    else:
        st.error(f"The dataset must contain the following columns: {', '.join(required_columns)}")
else:
    st.info("Awaiting file upload. Please upload a CSV file.")
