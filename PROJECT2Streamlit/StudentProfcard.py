import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Student Performance System", page_icon="🧑‍🎓", layout="wide")
st.markdown("<h1 style='text-align:center;'>🎓 Student Performance System</h1>", unsafe_allow_html=True)
st.divider()

# Only changed this line
st.markdown("<h1 style='text-align:center;'>🎓 Student Profile</h1>", unsafe_allow_html=True)

st.divider()

student_photo = st.file_uploader("Student Photo", type=["jpg", "png", "jpeg"])

Name = st.text_input("Student Name: ")
Course = st.text_input("Course: ")
College = st.text_input("College Name:")
Email = st.text_input("Email ID:")
Mobile = st.text_input("Mobile Number: ")

st.subheader("Skills")

skills = st.multiselect("Select your skills:",[ "✔️Python","✔️Data Analysis","✔️Machine Learning","✔️Web Development","✔️Database Management"])

if st.button("Submit"):
    st.balloons()

# showing the student profile details

st.divider()

# Only added these 3 lines
left, center, right = st.columns([1, 2, 1])

with center:

    st.subheader("Student Profile Details")

    # Only added these 4 lines for centered image
    if student_photo is not None:
        c1, c2, c3 = st.columns([1,2,1])
        with c2:
            st.image(student_photo, caption="Student Photo", width=180)

    st.write("**Name:**", Name)
    st.write("**Course:**", Course)
    st.write("**College:**", College)
    st.write("**Email:**", Email)
    st.write("**Mobile:**", Mobile)
    st.write("**Skills:**", ", ".join(skills))