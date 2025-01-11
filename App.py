import streamlit as st
import joblib
import numpy as np

# Set custom CSS for a modern, sleek design
st.markdown(
    """
    <style>
    /* App background with a soft pink gradient */
    .stApp {
        background: linear-gradient(135deg, #FFC0CB, #FFB6C1);
        color: black;
        font-family: 'Arial', sans-serif;
    }

    /* Center-align all elements */
    .stApp .block-container {
        max-width: 800px;
        margin: auto;
        padding-top: 2rem;
    }

    /* Styling headers */
    h1, h2, h3, h4, h5, h6 {
        text-align: center;
        font-weight: bold;
        color: #8B0000; /* Dark red for emphasis */
    }

    /* Customize input fields */
    input[type="number"] {
        border: 2px solid #FF69B4; /* Hot pink */
        border-radius: 10px;
        padding: 10px;
        width: 100%;
        font-size: 16px;
    }

    /* Styling buttons */
    button {
        background: #FF69B4; /* Hot pink */
        color: white;
        border: none;
        border-radius: 20px;
        padding: 10px 20px;
        font-size: 16px;
        transition: all 0.3s ease;
        cursor: pointer;
    }

    button:hover {
        background: #FF1493; /* Deep pink */
        transform: scale(1.05);
    }

    /* Success and error message boxes */
    .st-success, .st-error {
        border-radius: 10px;
        font-weight: bold;
        text-align: center;
    }

    /* Image customization */
    img {
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        margin-bottom: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Load the pre-trained model (replace with your model's path)
model = joblib.load('Breast-Cancer-Model')

# Splash page
def splash_page():
    st.title('✨ Breast Cancer Tumor Classification ✨')
    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/4/4e/Medical_icons_for_website_use.png",
        use_column_width=True,
    )
    st.markdown(
        """
        ### Welcome to the Tumor Classification App!
        Predict whether a tumor is **Malignant (M)** or **Benign (B)** using advanced machine learning.

        Simply enter the required tumor features, and let the app do the rest!

        #### How it works:
        - Enter features like **Radius Mean**, **Concavity Mean**, etc.
        - Click "Predict" to see the result.
        - Consult a healthcare professional for accurate diagnosis.
        """
    )
    if st.button('🚀 Get Started'):
        st.session_state.page = 'main'

# Main page
def main_page():
    st.title("🎀 Tumor Feature Input 🎀")

    st.markdown("#### Enter the following tumor features for prediction:")

    # Input fields for user
    radius_mean = st.number_input(
        "Radius Mean", min_value=0.0, format="%.4f", help="Average radius of the tumor cells"
    )
    concavity_mean = st.number_input(
        "Concavity Mean", min_value=0.0, format="%.4f", help="Average concavity of the tumor cells"
    )
    radius_worst = st.number_input(
        "Radius Worst", min_value=0.0, format="%.4f", help="Worst-case radius of the tumor cells"
    )
    concave_points_worst = st.number_input(
        "Concave Points Worst", min_value=0.0, format="%.4f", help="Worst-case concave points"
    )

    # Button to get prediction
    if st.button('🔮 Predict'):
        features = np.array([[radius_mean, concavity_mean, radius_worst, concave_points_worst]])
        prediction = model.predict(features)
        result = 'Malignant (M)' if prediction == 1 else 'Benign (B)'
        
        st.subheader(f'🎉 Prediction: {result}')
        
        if result == 'Malignant (M)':
            st.error("This tumor is **malignant**.They may need to consult a healthcare professional")
        else:
            st.success("This tumor is **benign**. Regular monitoring is advised.")

# App configuration
if 'page' not in st.session_state:
    st.session_state.page = 'splash'

# Page navigation
if st.session_state.page == 'splash':
    splash_page()
else:
    main_page()

# NOTE TO SELF: MAKE THE BACKGROUND OF THE APP PINK AND YOUR DONE. DEPLOY IT TO THE CLOUD.