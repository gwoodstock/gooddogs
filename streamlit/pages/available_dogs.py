import streamlit as st

def app():
    st.header('Insert header for page here')  

    st.text('Feed of adoptable dogs here')

    ##import model from production_model.py##


    ##load data from petfinder API scraper##
    # imports
    import petpy
    import pandas as pd
    import pyarrow.parquet as pq
    import pyarrow as pa

    # data
    pf = petpy.Petfinder(
    key='Ww9PL1UlVo7Wdj0DeGkkRo6PXKCXdsStCMKQ2Jc9CYvX5OTNPX', 
    secret='7RNX05UlYJdUIbhy90BfgGwG0ZuwWkQTMNeIYAGk'
    )
    dogs = pf.animals(pages=1, results_per_page=100, return_df=True, animal_type='dog')


    ##put data through model##

    ##outputs: feed of available dogs determined to be 'high risk' by model##
    col1, col2, col3 = st.columns([1,6,1])
    with col2:
        st.title("Insert project title here")
        st.title("Insert project title here")
        # - dog's name
        st.subheader(dogs.iloc[0]['name'])

        # - photo
        st.image(dogs.iloc[0]['photos'][0]['medium'])

        # - 'Animal Profile' description from petfinder
        # - link to petfinder
        url = dogs.iloc[0]['url']
        st.write("[Learn More on Petfinder!](%s)" % url)