import streamlit as st
from backend import create_model, identify_mail

def create_and_launch_ui():
    st.title("Email Spam Detection")
    
    #first create model
    create_model()

    #Wait for user input
    user_input = st.text_input("Mail Subject", "")
    if not user_input:
        st.warning("Please fill out mail subject...")
    else:
        print(user_input)
        retMsg = identify_mail(user_input)
        st.warning(retMsg)

