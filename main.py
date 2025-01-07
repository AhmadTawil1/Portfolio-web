import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo100.png", width=300)

with col2:
    st.title("Ahmad Tawil")
    content = """
        Hi! I’m a passionate software engineering student specializing in Python programming.
        I love crafting efficient, user-friendly solutions and am dedicated to continuous learning and innovation.
        With a strong drive to excel,
        I’m focused on building impactful projects and advancing my career in software development.
    """

    st.info(content)

content2 = """
    Below you can find some of the apps i have built in Python, Feel free to contact me!
"""
st.write(content2)

col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])