import streamlit as st

st.title("New App")
st.write("Hello, this is a simple application using Streamlit.")

user_input = st.text_input("Please enter your favorite words.")

if user_input:
    st.write(f"Your favorite word is {user_input}.")