import streamlit as st
from PIL import Image

st.set_page_config(
     page_title="Ex-stream-ly Cool App",
     page_icon="🧊",
     layout="wide",)
st.title('***WELCOME TO MY PORTFOLIO***')
####################### metadata###############################


if st.sidebar.button('ABOUT ME'):
   
   profile_image = Image.open('image_n.jpg')
   st.image(profile_image,width = 500)
   st.title("NEETHI PRIYA")
   #st.subheader("Data Analyst intern")  
   


   st.info("My goal is to join a leading company in the IT field. I want to develop myself more and gain experience to become one of the top developers of the future.I am willing to learn new things,especially in the field of data analytics")

   #st.sidebar.warning('CONTENT')
######################contact details ##############################

if st.sidebar.button('PERSONAL INFORMATION'):
    st.success("**Reach Me:sunglasses:**")
    st.write('-------------------------------------------------------')
    st._transparent_write(":email: neethipriya37@gmail.com")
    st.write('-------------------------------------------------------')
    st._transparent_write('linkedn: https://www.linkedin.com/in/neethi-priya-b37b6b1b8')
    st.write('-------------------------------------------------------')
    st.write(':iphone: +91 9113008868')
    st.write('-------------------------------------------------------')
    st.write('Ho.No 14-7-23,Eden colony zharna road Mangalpet')
    st.write('Bidar-585401')


#########################   Education ##########################

if st.sidebar.button('EDUCATION'):
    st.success("EDUCATION")

    st.write('-------------------------------------------------------')
    st.subheader('M.Tech in Computer Science')
    st.write('Visveswaraya technological university')
    st.write('Guru Nanak Dev Engineering College,Bidar')
    st.write('-------------------------------------------------------')
    st.subheader('Bachelor of Engineering(CSE)')
    st.write('Visveswaraya technological university')
    st.write('Guru Nanak Dev Engineering College,Bidar')

    

#########################   Projects ##########################

if st.sidebar.button('PROJECTS'):
    st.success("PROJECTS")
    st.write('-------------------------------------------------------')
    st.subheader('1.Web scraping using python')
    st.write('Performed web scraping on the website named makaan.com a real estate website using python libraries')
    st.write('-------------------------------------------------------')

    st.subheader('2.URL Shortener using python and flask')
    st.write('Built an real time application for shortening the url using python for frontend and flask for backend')
    st.write('-------------------------------------------------------')

    st.subheader('3.Notepad application using python and flask')
    st.write('Built an real time Notepad application using python for frontend and flask for backend')
    st.write('-------------------------------------------------------')

    st.subheader('4.Thyroid disease pridiction using machine learning classifiers')
    st.write('the goal of this project is detect early stage thyroid disease with high accuracy using machine learning classifiers')
    st.write('-------------------------------------------------------') 

######################## Internships ##################################
if st.sidebar.button('EXPERIENCE'):
    
    st.header("TRAINING")

    st.write('Company: Innomatics Research Labs,Hyd')
    st.write('Role : Data Analyst trainee')
    st.write('Duration: 08/09/2021 -Present')
    st.write('Job Description: Learning Python,Flask and Data Analysis')

    st.header('INTERNSHIP')
    st.write('Company: High ideals Pvt Ltd., mailoor cross Bidar')
    st.write('Role : Front End Web Developer Intern')
    st.write('Duration: 15/07/2019 -26/08/2019')
    st.write('Job Description: Developed webpage using HTML, CSS, and groovy grails skills for project “matrimonial site”')
    st.write('-------------------------------------------------------')
    
  

   
##################################skills#########################################
if st.sidebar.button('SKILLS'):
    st.success("SKILLS")
    st.markdown("* Python")
    st.markdown("* Data Analysis")  
    st.markdown("* SQL")
    st.markdown("* Flask")
    st.markdown("* Microsoft Office Excel")
    st.markdown("* Email Ethiquette")
    st.markdown("* Business Communication")


################################## CERTIFICATES #########################################

if st.sidebar.button('CERTIFICATES'):
    st.success("CERTIFICATES")

    st.write('-------------------------------------------------------')
    st.subheader('Hackathon')
    st.write('3-days of Hackathon of data analysis and Data mining on FIFA dataset conducted by Innomatics Research Labs')
    st.write('-------------------------------------------------------')
    
    st.subheader('IJAEMA')
    st.write('Published research paper named Thyroid disease prediction using feature selection and machine learning classifiers')
    st.write('-------------------------------------------------------')
    
    st.subheader('Start-up-training program')
    st.write('participated and successfully completed workshop program of start up training')
    st.write('-------------------------------------------------------')
    

################################## LANGUAGES #########################################


if st.sidebar.button('LANGUAGES'):
    st.success("LANGUAGES")

    st.write('-------------------------------------------------------')
    st.subheader('English')
    st.write('Professional Working Proficiency')
    st.write('-------------------------------------------------------')

    st.subheader('Kannada')
    st.write('Full Professional Proficiency')
    st.write('-------------------------------------------------------')

    st.subheader('Hindi')
    st.write('Full Professional Proficiency')
    st.write('-------------------------------------------------------')

################################## INTERESTS #########################################

if st.sidebar.button('INTERESTS'):
    st.success("INTERESTs")
    st.write('-------------------------------------------------------')
    st.markdown("* Athletics")
    st.markdown("* Cooking")
    st.markdown("* Singing")
    st.markdown("* Travel")
    st.markdown("* Music")
    st.write('-------------------------------------------------------')