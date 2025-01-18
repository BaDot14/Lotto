import streamlit as st
import pandas as pd
from io import StringIO

# Streamlit app title
st.title("Lotto Dataset Analysis")

# File uploader
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    # Read the uploaded CSV file
    data = pd.read_csv(uploaded_file)

    # Display dataset preview
    st.subheader("Dataset Preview")
    st.write(data.head())

    # Check for missing values
    st.subheader("Missing Values")
    missing_values = data.isnull().sum()
    st.write(missing_values)

    # Convert date column to datetime if applicable
    if 'DRAW DATE' in data.columns:
        data['DRAW DATE'] = pd.to_datetime(data['DRAW DATE'], errors='coerce')
        st.write("'DRAW DATE' column converted to datetime format.")

    # Display column names
    st.subheader("Column Names")
    st.write(data.columns.tolist())

    # Feature and label selection
    st.subheader("Select Features and Target")

    # Multiselect for features
    features = st.multiselect(
        "Select feature columns",
        options=data.columns,
        default=[col for col in data.columns if "NUMBER DRAWN" in col]
    )

    # Dropdown for target
    target = st.selectbox(
        "Select target column",
        options=data.columns,
        index=data.columns.get_loc('DRAW NUMBER') if 'DRAW NUMBER' in data.columns else 0
    )

    if features and target:
        # Display selected features and target
        st.write("Selected Features:", features)
        st.write("Selected Target:", target)

        # Prepare features (X) and target (y)
        X = data[features]
        y = data[target]

        st.subheader("Feature and Target Preview")
        st.write("Features (X):", X.head())
        st.write("Target (y):", y.head())

    else:
        st.warning("Please select at least one feature and a target column.")

else:
    st.info("Awaiting file upload. Please upload a CSV file.")
