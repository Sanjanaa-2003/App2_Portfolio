import streamlit as st
import pandas
st.set_page_config(layout="wide")

col1,col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Sanjanaa Jayachandran")
    content="""
    Hi, this is Sanjanaa Jayachandran! WELCOME to my website! I am pursuing B.Tech in ECE from
    VIT, Vellore. I love learning python and would like to create more
    apps, websites and projects to diversify my learning. Thid is my portfolio
    website where you get to see the apps I've created in the journey of learning
    the Python Programming Language!
    """
    st.info(content)
content2="""
Below you can find some of the apps I have built in Python.
Feel free to contact me!
"""
st.write(content2)
col3, empty_col, col4=st.columns([1.5,0.5,1.5]) #The 1st and 3rd column are spaced from each other

df=pandas.read_csv("data.csv",sep=";")  #by default the seperator is comma, here we explicitly use ; as it is used to seperate items in data.txt

with col3:
    for index,row in  df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])    #the description content has been obtained from data.csv file
        st.image('images/' + row["image"])
        st.write(f"[Source Code]({row['url']})")    #the url links for each app
with col4:
    for index,row in  df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image('images/'+row["image"])    #images/1.png - in this format path all images are extracted
        st.write(f"[Source Code]({row['url']})")

# Run on terminal "  streamlit run E:\app2-portfolio\main.py  "
