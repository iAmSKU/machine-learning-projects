import streamlit as st
from backend import load_create_model, identify_mail_type

def create_and_launch_ui():
    st.title("Email Spam Detection")
    
    #first load or create model
    load_create_model()

    #Wait for user input
    user_input = st.text_input("Mail Subject", "")
    if not user_input:
        st.warning("Please fill out mail subject...")
    else:
        print(user_input)
        retMsg = identify_mail_type(user_input)
        st.warning(retMsg)

