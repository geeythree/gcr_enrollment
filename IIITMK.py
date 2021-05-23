import streamlit as st
import pandas as pd
from PIL import Image
import base64
from io import BytesIO

def show_data(mail):
    ind = int(data[data["Student Email"] == mail].index.values)
    st.write("Student Email : ", data['Student Email'][ind])
    st.write("Student Name : ", data['Student Name'][ind])
    st.write("Institution : ", data['Institution'][ind])
    st.write("Enrolment Status : ",data['Enrolment Status'][ind])
    st.write("Qwiklabs Profile URL : ", data['Qwiklabs Profile URL'][ind])
    st.write("No. of Quests Completed : ", data['quests'][ind])
    st.write("No. of Skill Badges Completed : ",data['skills'][ind])
    mil = milestone(ind)
    if mil is not None:
        if mil == "milestone_1":
            st.write("Milestone achieved : Milestone 1")
            st.write("Prizes : T-shirt + Pen + Badge + Stickers + Thank-you card from Google")
        elif mil == "milestone_2":
            st.write("Milestone achieved : Milestone 2")
            st.write("Prizes : Sling Bag + T-shirt + Pen + Badge + Stickers + Thank-you card from Google")
        elif mil == "milestone_3":
            st.write("Milestone achieved : Milestone 3")
            st.write("Prizes : Laptop Bag + Sling Bag + T-shirt + Pen + Badge + Stickers + Thank-you card from Google")
        else:
            st.write("Milestone achieved : Ultimate Milestone!!")
            st.write("Prizes : Career Readiness Program seat + Laptop Bag + Sling Bag + T-shirt + Pen + Badge + Stickers + Thank-you card from Google")
    st.subheader("For any queries, kindly drop in a mail to gayathri.mi20@iiitmk.ac.in")
    st.write(" ")

def milestone(ind):
    quests = int(data['quests'][ind])
    skill = int(data['skills'][ind])
    if (quests>=8 and quests<16) and (skill>=4 and skill<8):
        return "milestone_1"
    elif (quests>=16 and quests<24) and (skill>=8 and skill<12):
        return "milestone_2"
    elif (quests>=24 and quests<30) and (skill>=12 and skill<15) :
        return "milestone_3"
    elif quests>=30 and skill>=15:
        return "milestone_4"
    else:
        return None
    

def error():
    st.subheader("No data found!")
    st.subheader("For any queries, kindly drop in a mail to gayathri.mi20@iiitmk.ac.in")
    st.write(" ")

def create_leaderboard(data):
    data.drop(data[data.quests < 8].index, inplace=True)
    data.drop(data[data.skills < 4].index, inplace=True)
    data.sort_values('skills', ascending=False, inplace=True, na_position="last")
    data.sort_values('quests', ascending=False, inplace=True, na_position="last") 
    #st.write(data)
    
    cols = st.beta_columns(6)
    cols[2].write('Position')
    cols[3].write('Name')
    pos=1
    names=data["Student Name"].tolist()
    new_names=[]
    for name in names:
        split_name=name.split(" ")
        first=split_name[0]
        if len(split_name) > 1:
            initial=split_name[1][0]
        else:
            initial = ""
        new_names.append(first+" "+initial)
    for student in new_names:
        cols[2].write(str(pos))
        cols[3].write(student)
        pos = int(pos)
        pos += 1

def generate_badge(mail):
    ind = int(data[data["Student Email"] == mail].index.values)
    mil = milestone(ind)
    if mil is not None:
        if mil == "milestone_1":
            template = Image.open("milestone_1.png")
        elif mil == "milestone_2":
            template = Image.open("milestone_2.png")
        elif mil == "milestone_3":
            template = Image.open("milestone_3.png")
        else:
            template = Image.open("milestone_4.png")
        uploaded_file = st.file_uploader("Upload your image",type="jpg")
        if uploaded_file is not None:
            student = Image.open(uploaded_file)
            create_collage(student, template)
    else:
        st.write("Sorry, you cannot regenerate badge.")
        st.write("Complete atleast one milestone to generate badge.")

def get_image_download_link(img):
	buffered = BytesIO()
	img.save(buffered, format="PNG")
	img_str = base64.b64encode(buffered.getvalue()).decode()
	href = f'<a href="data:image/png;base64,{img_str}" download="gcrf_badge.png">Download Badge</a>'
	return href

def create_collage(student, template):
    gcrf_badge = template.copy()
    resized_student = student.resize((610,610))
    gcrf_badge.paste(resized_student,(0,0))
    st.markdown(get_image_download_link(gcrf_badge), unsafe_allow_html=True)
    st.image(gcrf_badge)
        
selected_page = st.sidebar.radio("Navigate to :",['Track Progress','Leaderboard',"Generate Badge"])
st.title("GoogleCloudReady Facilitator Program Host - IIITMK")
data = pd.read_csv("GCR-IIITMK.csv")
data=data.rename(columns={'# of Quests Completed' : 'quests'})
data=data.rename(columns={'# of Skill Badges Completed' : 'skills'})

if selected_page == "Leaderboard":
    st.write(" ")
    st.markdown("""<p style='display: block; text-align: center; font-weight: 600; font-size:32px;'>Leaderboard</p>""",unsafe_allow_html=True)
    create_leaderboard(data)
elif selected_page == "Track Progress":
    st.write(" ")
    st.markdown("""<p style='display: block; text-align: center; font-weight: 600; font-size:32px;'>Track Progress</p>""",unsafe_allow_html=True)
    mail = st.text_input("Enter your mail-id : ")

    if mail in data['Student Email'].tolist():
        show_data(mail)

    if mail != "" and mail not in data['Student Email'].tolist(): 
        error()
else:
    st.write(" ")
    st.markdown("""<p style='display: block; text-align: center; font-weight: 600; font-size:32px;'>Generate Badge</p>""",unsafe_allow_html=True)
    mail = st.text_input("Enter your mail-id : ")
    if mail in data['Student Email'].tolist():
        generate_badge(mail)
    

st.markdown("""<p style='display: block; text-align: center;'>Developed & maintained by <a href="https://www.linkedin.com/in/gayathri-satheesh-8a1740151/">Geeythree</a> with ❤️</p>""",unsafe_allow_html=True)