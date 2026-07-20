import streamlit as st

st.title("User Login Form")

uid = st.text_input("User ID :-")
pswd = st.text_input("Password :-", type="password")

# Create two columns
col1, col2 = st.columns(2) # divide the page into two equal columns || ratio :([1, 2] means col1 will take 1/3 of the page and col2 will take 2/3 of the page)

with col1:
    st.button("Login")

with col2:
    st.button("Sign Up")

st.write("User ID:", uid)