import streamlit as st

st.title("Hello guys! Welcome to my website")
st.header("Muhtasim Abir")
st.subheader("Class 7 B")
st.markdown("made by Abir")
st.code("""This is a website of our class 7b group.
In future i will upload many videos of our class 7b group. So stay tuned!😊""")


name = st.text_input("Enter your name:")
fname = st.text_input("Enter your father name:")
adr = st.text_area("Write your address")
classdata = st.selectbox("Eenter your class :",(1,2,3,4,5,6,7,8,9,10))

button = st.button("Submit")
if button :
    st.markdown(f"""
     yoour name : {name}
   Father name : {fname}
    Address : {adr}
    Class : {classdata}""")