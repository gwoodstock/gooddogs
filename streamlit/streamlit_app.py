import streamlit as st

# Custom imports 
from multipage import MultiPage
from pages import tableau, available_dogs, available_dogs_nate # import your pages here

# Create an instance of the app 
app = MultiPage()

# Title of the main page
# col1, col2, col3 = st.columns([1,6,1])
# with col2:
st.title("Good Dogs")

# Add all your applications (pages) here
<<<<<<< HEAD
app.add_page("Explore Shelter Dog Data", tableau.main)
=======
>>>>>>> main
app.add_page("Find Your New Friend!", available_dogs_nate.app)
app.add_page("Explore Shelter Dog Data", tableau.main)

# The main app
app.run()