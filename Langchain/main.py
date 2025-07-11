import langchain_helper as lang
import streamlit as st

st.title('Pets name generator')

user_animal_type = st.sidebar.selectbox("What is your pet animal ?", ('Cat', 'Dog', 'Hamster', 'Snake'))

if user_animal_type == "Cat":
    pet_color = st.sidebar.text_area("What is the color of your cat?", max_chars = 15)

if user_animal_type == "Dog":
    pet_color = st.sidebar.text_area("What is the color of your Dog?", max_chars = 15)

if user_animal_type == "Hamster":
    pet_color = st.sidebar.text_area("What is the color of your Hamster?", max_chars = 15)

if user_animal_type == "Snake":
    pet_color = st.sidebar.text_area("What is the color of your Snake?", max_chars = 15)

if pet_color:
    response = lang.generate_pet_name(user_animal_type, pet_color )
    st.text(response['pet_name'])