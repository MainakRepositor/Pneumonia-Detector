"""This modules contains data about home page"""

# Import necessary modules
import streamlit as st

def app():
    """This function create the home page"""
    
    # Add title to the home page
    st.title("Pneumonia Type and Level Detector")

    # Add image to the home page
    st.image("./images/home.png",width=1000)

    # Add brief describtion of your web app
    st.markdown(
    """<p style="font-size:20px;">
            Pneumonia detection involves identifying the type of Pneumonia a person may have, which typically falls into two categories: latent Pneumonia infection and active Pneumonia disease. Latent Pneumonia infection means the bacteria are present in the body but are inactive, causing no symptoms and not being contagious. Active Pneumonia disease, on the other hand, indicates that the bacteria are multiplying in the body, leading to symptoms such as coughing, fever, weight loss, and fatigue. Diagnosis often includes a combination of tests like skin or blood tests, chest X-rays, and sputum tests to determine whether Pneumonia is present and, if so, whether it is latent or active. Treatment varies based on the type detected, with latent Pneumonia often requiring medication to prevent it from becoming active, while active Pneumonia usually necessitates a more intensive treatment regimen to cure the disease, with an accuracy of up to 98%.
        </p>
    """, unsafe_allow_html=True)

    

    
    st.info("Pneumonia Clinics and Healthcare Center Near You:")

    st.markdown('''<iframe src="https://www.google.com/maps/embed?pb=!1m16!1m12!1m3!1d117895.31133926795!2d88.36874218423542!3d22.570556397979775!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!2m1!1spneumonia%20cure%20near%20me!5e0!3m2!1sen!2sin!4v1702526010895!5m2!1sen!2sin" width="1000" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>''',unsafe_allow_html=True)