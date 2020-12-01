# Core Pkg
import streamlit as st 

# TEXT
# title
st.title("Streamlit Demo")

# header/subheader
st.header("ICFOSS")

st.subheader("icfoss")

# text
st.text("Welcome to ICFOSS")

# MARKDOWN
st.markdown("# ICFOSS")

# Links
st.markdown("[Icfoss](https://icfoss.in/)")

url_link = "https://icfoss.in/"

st.markdown(url_link)

st.success("Succcess!")

st.info("Information")
st.warning("This is a warning")
st.error("This is an error")

st.exception('NameError()') 

# MEDIA
# Images
from PIL import Image
img = Image.open("index.jpeg")
st.image(img,width=300,caption="Icfoss")

# Audio
audio_file = open('new.mp3',"rb")
audio_bytes = audio_file.read()
st.audio(audio_bytes,format="audio/mp3")

# Video
video_file = open("ml.mp4","rb")
video_bytes = video_file.read()
st.video(video_bytes)


# Video URL/YTB
# st.video("https://www.youtube.com/watch?v=_9WiB2PDO7k")


# WIDGET
st.button("Submit")

if st.button("Play"):
	st.text("Hello world")

# Checkbox
if st.checkbox("Show/hide"):
	st.success("Hiding or Showing")

# Radio
gender = st.radio("Your Gender",["Male","Female"])

if gender == 'Male':
	st.info("Is a male")

# Select
location = st.selectbox("Your Location",["UK","USA","India","Accra"])


# Multiselect
occupation = st.multiselect("Your Occupation",["Developer","Doctor","BusinessMan","Banker"])


# TEXT INPUT
name = st.text_input("Your Name","Type Here")
st.text(name)

# NUMBER INPUT
age = st.number_input("Age")

# TEXT_AREA
message = st.text_area("Your Message","Type here")

# SLider
level = st.slider("Your Level",2,6)

# Balloons
# st.balloons()



# DATA SCIENCE
st.write(range(10))

#DATAFRAME

import pandas as pd 
df = pd.read_csv("iris.csv")

 #M1
st.dataframe(df.head())
# #M2
# st.write(df.head())


# TABLES

st.table(df.head())
# PLOT

# Plot Pkgs
import matplotlib.pyplot as plt 
import seaborn as sns 

# Area_chart
st.area_chart(df.head(20))
# Bar_chart

st.bar_chart(df.head(20))
# Line Chart

st.line_chart(df)

# Heatmap
c_plot = sns.heatmap(df.corr(),annot=True)
st.write(c_plot)
st.pyplot()

# Altair
# Vega
# D

# Date/Time
import datetime 
today = st.date_input("Today is",datetime.datetime.now())


import time
the_time = st.time_input("The time is",datetime.time(10,0))


