import streamlit as st
import pandas as pd

def show_data(mail):
    ind = int(data[data["Student Email"] == mail].index.values)
    st.write("Student Email : ", data['Student Email'][ind])
    st.write("Student Name : ", data['Student Name'][ind])
    st.write("Institution : ", data['Institution'][ind])
    st.write("Enrolment Status : ",data['Enrolment Status'][ind])
    st.write("Qwiklabs Profile URL : ", data['Qwiklabs Profile URL'][ind])
    st.write("No. of Quests Completed : ", data['quests'][ind])
    st.write("No. of Skill Badges Completed : ",data['skills'][ind])
    quests = int(data['quests'][ind])
    skill = int(data['skills'][ind])
    if (quests>=8 and quests<16) or (skill>=4 and skill<8):
        st.write("Milestone achieved : Milestone 1")
        st.write("Prizes : T-shirt + Pen + Badge + Stickers + Thank-you card from Google")
    elif (quests>=16 and quests<24) or (skill>=8 and skill<12):
        st.write("Milestone achieved : Milestone 2")
        st.write("Prizes : Sling Bag + T-shirt + Pen + Badge + Stickers + Thank-you card from Google")
    elif (quests>=24 and quests<30) or (skill>=12 and skill<15) :
        st.write("Milestone achieved : Milestone 3")
        st.write("Prizes : Laptop Bag + Sling Bag + T-shirt + Pen + Badge + Stickers + Thank-you card from Google")
    elif quests>=30 or skill>=15:
        st.write("Milestone achieved : Ultimate Milestone!!")
        st.write("Prizes : Career Readiness Program seat + Laptop Bag + Sling Bag + T-shirt + Pen + Badge + Stickers + Thank-you card from Google")
    st.subheader("For any queries, kindly drop in a mail to gayathri.mi20@iiitmk.ac.in")
    st.write(" ")

def error():
    st.subheader("No data found!")
    st.subheader("For any queries, kindly drop in a mail to gayathri.mi20@iiitmk.ac.in")
    st.write(" ")

def create_leaderboard(data):
    data.sort_values('quests', ascending=False, inplace=True, na_position="last") 
    data.sort_values('skills', ascending=False, inplace=True, na_position="last")
    data.drop(data[data.quests < 9].index, inplace=True)
    data.drop(data[data.skills < 5].index, inplace=True)
    
    cols = st.beta_columns(8)
    cols[3].write('Position')
    cols[4].write('Name')
    pos=1
    names=data["Student Name"].tolist()
    new_names=[]
    for name in names:
        split_name=name.split(" ")
        first=split_name[0]
        initial=split_name[1][0]
        new_names.append(first+" "+initial)
    for student in new_names:
        cols[3].write(str(pos))
        cols[4].write(student)
        pos = int(pos)
        pos += 1
        
selected_page = st.sidebar.radio("Navigate to :",['Track Progress','Leaderboard'])
st.title("GoogleCloudReady Facilitator Program Host - IIITMK")
data = pd.read_csv("GCR-IIITMK.csv")
data=data.rename(columns={'# of Quests Completed' : 'quests'})
data=data.rename(columns={'# of Skill Badges Completed' : 'skills'})

if selected_page == "Leaderboard":
    st.write(" ")
    st.markdown("""<p style='display: block; text-align: center; font-weight: 600; font-size:32px;'>Leaderboard</p>""",unsafe_allow_html=True)
    create_leaderboard(data)
else:
    st.subheader("Track your progress")
    mail = st.text_input("Enter your mail-id : ")

    if mail in data['Student Email'].tolist():
        show_data(mail)

    if mail != "" and mail not in data['Student Email'].tolist(): 
        error()

st.markdown("""<p style='display: block; text-align: center;'>Developed & maintained by <a href="https://www.linkedin.com/in/gayathri-satheesh-8a1740151/">Geeythree</a> with ❤️</p>""",unsafe_allow_html=True)