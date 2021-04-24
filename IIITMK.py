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
    quests = int(data['# of Quests Completed'][ind])
    skill = int(data['# of Skill Badges Completed'][ind])
    if (quests>=8 or quests<16) and skill>=4 or skill<8:
         st.write("Milestone achieved : Milestone 1")
        st.write("Prizes : T-shirt + Pen + Badge + Stickers + Thank-you card from Google")
    if (quests>=16 or quests<24) and (skill>=8 or skill<12):
        st.write("Milestone achieved : Milestone 2")
        st.write("Prizes : Sling Bag + T-shirt + Pen + Badge + Stickers + Thank-you card from Google")
    if (quests>=24 or quests<30) and (skill>=12 or skill<15) :
        st.write("Milestone achieved : Milestone 3")
        st.write("Prizes : Laptop Bag + Sling Bag + T-shirt + Pen + Badge + Stickers + Thank-you card from Google")
    if quests>=30 and skill>=15:
        st.write("Milestone achieved : Ultimate Milestone!!")
        st.write("Prizes : Career Readiness Program seat + Laptop Bag + Sling Bag + T-shirt + Pen + Badge + Stickers + Thank-you card from Google")
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