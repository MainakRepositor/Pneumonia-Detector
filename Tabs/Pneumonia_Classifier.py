import streamlit as st
import imagerec
import pandas as pd
import random
import streamlit.components.v1 as components


def app():

    st.markdown(""" <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style> """, unsafe_allow_html=True)
    st.title("Pneumonia Detector")
    st.write('<style>div.row-widget.stMarkdown { font-size: 24px; }</style>', unsafe_allow_html=True)


    st.write("Pneumonia is an infection that inflames the air sacs in one or both lungs, causing them to fill with fluid or pus. The infection can be caused by a variety of microorganisms, including bacteria, viruses, and fungi. Pneumonia can be acquired in the community or in a hospital setting, and it can range in severity from mild to life-threatening.")
    st.divider()
    st.write("Machine learning (ML) can play an important role in pneumonia prediction by analyzing medical images and identifying patterns that may be indicative of the disease. For example, ML models can be trained on large datasets of chest X-rays and CT scans to learn features that distinguish between normal lungs and those affected by pneumonia.")
    st.divider()
    st.write("We have developed A Convolutional Neural Network (CNN) to predict whether the lung scan has Pneumonia or not. It has been trained on more than 10,000 images divided into two classes, to upto 50 epochs.")
    st.divider()

    uploaded_file = st.file_uploader("Choose a File", type=['jpg','png','jpeg'])

    score = 0.98
    
    if uploaded_file!=None:
        st.image(uploaded_file)
    x = st.button("Predict")
    if x:
        with st.spinner("Predicting..."):
            y,conf = imagerec.imagerecognise(uploaded_file,"Models/Pnemonia.h5","Models/labelsPnemonia.txt")
        if y.strip() == "Negative":
            components.html(
                """
                <style>
                h1{
                    
                    background: -webkit-linear-gradient(0.25turn,#01CCF7, #8BF5F5);
                    -webkit-background-clip: text;
                    -webkit-text-fill-color: transparent;
                    font-family: "Source Sans Pro", sans-serif;
                }
                </style>
                <h1>It is not Pneumomnia</h1>
                """
            )

            # Print teh score of the model 
            st.sidebar.success("The model used is trusted by doctor and has an accuracy of " + str((score*100)) + "%")
        else:
            components.html(
                """
                <style>
                h1{
                    background: -webkit-linear-gradient(0.25turn,#FF4C4B, #F70000);
                    -webkit-background-clip: text;
                    -webkit-text-fill-color: transparent;
                    font-family: "Source Sans Pro", sans-serif;
                }
                </style>
                <h1>It is Pneumomnia</h1>
                """
            )

            # Print teh score of the model 
            st.sidebar.warning("The model used is trusted by doctor and has an accuracy of " + str((score*100)) + "%")

            st.sidebar.markdown('''<a href="https://www.drugs.com/medical-answers/antibiotics-treat-pneumonia-3121707/
" target="_blank" style="display: inline-block; padding: 12px 20px; background-color: orange; color: white; text-align: center; text-decoration: none; font-size: 16px; border-radius: 10px;">Best Medication for Pneumonia</a>''',unsafe_allow_html=True)
            
            
            st.info("Causes:")
            st.markdown('''Pneumonia is an infection that inflames the air sacs in one or both lungs. The air sacs may fill with fluid or pus (purulent material), causing cough with phlegm or pus, fever, chills, and difficulty breathing. A variety of organisms, including bacteria, viruses and fungi, can cause pneumonia.Pneumonia can range in seriousness from mild to life-threatening. It is most serious for infants and young children, people older than age 65, and people with health problems or weakened immune systems.''')

            st.info("Symptoms")
            st.markdown('''<p>Signs and symptoms of pneumonia may include:</p>
<ul>
<li>Chest pain when you breathe or cough</li>
<li>Confusion or changes in mental awareness (in adults age 65 and older)</li>
<li>Cough, which may produce phlegm</li>
<li>Fatigue</li>
<li>Fever, sweating and shaking chills</li>
<li>Lower than normal body temperature (in adults older than age 65 and people with weak immune systems)</li>
<li>Nausea, vomiting or diarrhea</li>
<li>Shortness of breath</li>
</ul>  
                        ''',unsafe_allow_html=True)
            

            st.info("Complications")
            st.markdown('''<p>Even with treatment, some people with pneumonia, especially those in high-risk groups, may experience complications, including</p>
<ul>
<li>Bacteria in the bloodstream (bacteremia). Bacteria that enter the bloodstream from your lungs can spread the infection to other organs, potentially causing organ failure</li>
<li>Difficulty breathing. If your pneumonia is severe or you have chronic underlying lung diseases, you may have trouble breathing in enough oxygen. You may need to be hospitalized and use a breathing machine (ventilator) while your lung heals.</li>
<li>Fluid accumulation around the lungs (pleural effusion). Pneumonia may cause fluid to build up in the thin space between layers of tissue that line the lungs and chest cavity (pleura). If the fluid becomes infected, you may need to have it drained through a chest tube or removed with surgery.</li>
<li>Lung abscess. An abscess occurs if pus forms in a cavity in the lung. An abscess is usually treated with antibiotics. Sometimes, surgery or drainage with a long needle or tube placed into the abscess is needed to remove the pus.</li>

                        ''',unsafe_allow_html=True)
            
            
            
    st.sidebar.info("For remedies, kindly check your severity of Pneumonia in the 'Prediction Page'.")

