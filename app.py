import streamlit as st
import pandas as pd

def show_data(mail):
    ind = int(data[data["Student Email"] == mail].index.values)
    st.write("Student Email : ", data['Student Email'][ind])
    st.write("Student Name : ", data['Student Name'][ind])
    st.write("Institution : ", data['Institution'][ind])
    st.write("Enrolment Status : ",data['Enrolment Status'][ind])
    st.write("Qwiklabs Profile URL : ", data['Qwiklabs Profile URL'][ind])
    st.write("No. of Quests Completed : ", data['# of Quests Completed'][ind])
    st.write("No. of Skill Badges Completed : ",data['# of Skill Badges Completed'][ind])
    st.subheader("For any queries, kindly drop in a mail to gayathri.mi20@iiitmk.ac.in")
    st.write(" ")

def error():
    st.subheader("No data found!")
    st.subheader("For any queries, kindly drop in a mail to gayathri.mi20@iiitmk.ac.in")
    st.write(" ")

st.title("GoogleCloudReady Facilitator Program Host - IIITMK")
st.subheader("Track your progress")
data = pd.read_csv("GCR-IIITMK.csv")
mail = st.text_input("Enter your mail-id : ")

if mail in data['Student Email'].tolist():
    show_data(mail)

if mail != "" and mail not in data['Student Email'].tolist(): 
    error()

st.markdown("""<p style='display: block; text-align: center;'>Developed & maintained by <a href="https://www.linkedin.com/in/gayathri-satheesh-8a1740151/">Geeythree</a> with ❤️</p>""",unsafe_allow_html=True)