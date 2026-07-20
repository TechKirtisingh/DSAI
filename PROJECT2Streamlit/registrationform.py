import streamlit as st

# wide means page will be displayed in full width of the screen
st.set_page_config(page_title="Student Registration Form" , page_icon="🎓" , layout="wide")

st.title("🎓Student Registration Form")

name = st.text_input("Student Name")
father = st.text_input("Father's Name")
email = st.text_input("Email ID")
mobile = st.text_input("Mobile Number")
gender = st.radio("Gender" , ["Male" , "Female" , "Other"])
age = st.number_input("Age" , min_value = 15 , max_value =50 , step=1)
course = st.selectbox(
    "Course" , 
    ["B.tech" , "BCA" , "MCA" ,"B.Sc" , "M.Tech" , "MBA"]
)

branch = st.selectbox(
    "Branch" ,
    ["Computer Science" , "Data Science" , "AI & ML" , "Information Technology" , "Electronics"]
)

semester = st.selectbox(
    "Semester",
    [1,2,3,4,5,6,7,8]
)

address = st.text_area("Address")
agree = st.checkbox("I confirm that the above information is correct.")

if st.button("Register"):
    if name == "" or email == "" or mobile == "" :
        st.error("Please fill all the required fields.")
    elif not agree:
        st.warning("Please accept the declaration.")
    else :
        st.success("Student Registered Successfully! 🎉")
        
        st.subheader("Registration Details")
        
        st.write("**Name:**" , name) # sigle * : heading , double ** : bold and heading , triple *** : heading and italic and bold
        st.write("**Father's Name:**" , father)
        st.write("**Email:**" , email)
        st.write("**Mobile:**" , mobile)
        st.write("**Gender:**" , gender)
        st.write("**Age:**" , age)
        st.write("**Course:**" , course)
        st.write("**Branch:**" , branch)
        st.write("**Semester:**" , semester)
        st.write("**Address:**" , address)
        
        st.balloons() # animation of balloons on successful registration , balloons means  