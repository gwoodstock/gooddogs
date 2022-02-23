import streamlit as st
import pickle

# Custom imports 
from multipage import MultiPage
from pages import tableau, available_dogs

# Create an instance of the app 
app = MultiPage()

# Title of the main page
# col1, col2, col3 = st.columns([1,6,1])
# with col2:
st.title("Good Dogs")

# Add all your applications (pages) here
app.add_page("Find Your New Friend!", available_dogs.app)
app.add_page("Explore Shelter Dog Data", tableau.main)

# The main app
app.run()
