"""This modules contains data about prediction page"""

# Import necessary modules
import streamlit as st

# Import necessary functions from web_functions
from web_functions import predict


def app(df, X, y):
    """This function create the prediction page"""

    # Add title to the page
    st.title("Prediction Page")

    # Add a brief description
    st.markdown(
        """
            <p style="font-size:25px">
                This app uses <b style="color:green">Random Forest Classifier</b> for the Prediction of Pneumonia Type and Intensity.
            </p>
        """, unsafe_allow_html=True)
    
    # Take feature input from the user
    # Add a subheader
    st.subheader("Select Values:")
    
    col1,col2, col3 = st.columns(3)
    with col1:
        # Take input of features from the user.
        Resp_pm = st.slider("Respiration Per Minute", int(df["Resp_pm"].min()), int(df["Resp_pm"].max()))
        AGE = st.slider("Age", int(df["AGE"].min()), int(df["AGE"].max()))
        PackHistory = st.slider("PackHistory", int(df["PackHistory"].min()), int(df["PackHistory"].max()))
        MWT1 = st.slider("MWT1", float(df["MWT1"].min()), float(df["MWT1"].max()))
        MWT2 = st.slider("MWT2", float(df["MWT2"].min()), float(df["MWT2"].max()))
        MWT1Best = st.slider("MWT1Best", float(df["MWT1Best"].min()), float(df["MWT1Best"].max()))
        FEV1 = st.slider("FEV1", float(df["FEV1"].min()), float(df["FEV1"].max()))
        FEV1PRED = st.slider("FEV1PRED", float(df["FEV1PRED"].min()), float(df["FEV1PRED"].max()))

    with col2:
        FVC = st.slider("FVC", int(df["FVC"].min()), int(df["FVC"].max()))
        FVCPRED = st.slider("FVCPRED", int(df["FVCPRED"].min()), int(df["FVCPRED"].max()))
        CAT = st.slider("CAT", float(df["CAT"].min()), float(df["CAT"].max()))
        HAD = st.slider("HAD", float(df["HAD"].min()), float(df["HAD"].max()))
        SGRQ = st.slider("SGRQ", float(df["SGRQ"].min()), float(df["SGRQ"].max()))
        AGEquartiles = st.slider("AGEquartiles", float(df["AGEquartiles"].min()), float(df["AGEquartiles"].max()))
        copd = st.slider("copd", float(df["copd"].min()), float(df["copd"].max()))

    with col3:
        gender = st.slider("gender", int(df["gender"].min()), int(df["gender"].max()))
        smoking = st.slider("smoking", int(df["smoking"].min()), int(df["smoking"].max()))
        Diabetes = st.slider("Diabetes", int(df["Diabetes"].min()), int(df["Diabetes"].max()))
        muscular = st.slider("muscular", float(df["muscular"].min()), float(df["muscular"].max()))
        hypertension = st.slider("hypertension", float(df["hypertension"].min()), float(df["hypertension"].max()))
        AtrialFib = st.slider("AtrialFib", float(df["AtrialFib"].min()), float(df["AtrialFib"].max()))
        IHD = st.slider("IHD", float(df["IHD"].min()), float(df["IHD"].max()))
        

    # Create a list to store all the features
    features = [Resp_pm,AGE,PackHistory,MWT1,MWT2,MWT1Best,FEV1,FEV1PRED,FVC,FVCPRED,CAT,HAD,SGRQ,AGEquartiles,copd,gender,smoking,Diabetes,muscular,hypertension,AtrialFib,IHD]

    # Create a button to predict
    if st.button("Predict"):
        # Get prediction and model score
        prediction, score = predict(X, y, features)
        
     

        if (AGE< 60):
            st.info("Follow clinical procedures and recommendations with 600 mg of paracetamol to keep away fever")

        if (AGE >60):
            st.info("Immediate attention needed!")

        # Print the output according to the prediction
        if (prediction == 1):
            st.warning("The person has risk of Aspiration Pneumonia")
            st.info("Severity Level 1: This is a nominal pneumonia and gets cured easily.")
            st.success("Smell some Eucalyptus oil and inhale medicated vapour especially with clove oil")

        elif (prediction == 2):
            st.warning("The person has risk of Bacterial Pneumonia")
            st.info("Severity Level 2: This is a common pneumonia and requires some mild doses of medication.")
            st.success("Requires medical attention and nebulizaton and medication courses like antibiotics and antihismatics. Consult a Physician for more details.")

        elif (prediction == 3):
            st.error("The person has high risk of Viral Pneumonia")
            st.info("Severity Level 3: This is a severe pneumonia and needs good medical attention and proper course of medication")
            st.success("Required ventilation / air purifier and stronger doses of antibiotics. However it gets cured faster than bacterial pneumonia.")

        elif (prediction == 4):
            st.error("The person has Fungal Pneumonia")
            st.info("Severity Level :4 This is a chronic pneumonia and is hard to cure if medications and clinical care are not provided in time.")
            st.success("Require Amycline or similar antibiotics and possible chances of being admitted to ICU with ventilation. Requires hospital level treatment.")
       
        # Print teh score of the model 
        st.sidebar.info("The model used is trusted by doctor and has an accuracy of " + str((score*100)) + "%")

        st.sidebar.markdown('''<a href="https://www.drugs.com/medical-answers/antibiotics-treat-pneumonia-3121707/
" target="_blank" style="display: inline-block; padding: 12px 20px; background-color: orange; color: white; text-align: center; text-decoration: none; font-size: 16px; border-radius: 10px;">Best Medication for Pneumonia</a>''',unsafe_allow_html=True)