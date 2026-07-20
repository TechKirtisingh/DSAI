import streamlit as st
import sklearn.linear_model as lm
import streamlit as st

st.set_page_config(
    page_title="Employee Salary Prediction", 
    page_icon="💵", 
    layout="wide")

st.tiltle("Employee Salary Prediction💸")
st.divider()

df = pd.DataFrame({})

df= pd.read_csv("experience_salary_40_records.csv")

X = df[["Experience"]] # independent variable
Y = df["Salary"] # dependent variable

model = lm.LinearRegression()
model.fit(X,Y)

exp = st.slider("Experience in years", 0, 90, 20)

if st.button("Predict Salary"): # NOw this work only when the button is clicked
    salary = model.predict([[exp]])
    st.write(f"**Prediction:** {salary[0]:.2f} ")