from turtle import color
import streamlit as st


def app():

    # page header
    st.header('Insert header for page here') 

    st.sidebar.image(
        'https://images.unsplash.com/photo-1586671267731-da2cf3ceeb80?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NHx8ZG9nfGVufDB8MXwwfHw%3D&auto=format&fit=crop&w=800&q=60',
        use_column_width=True
        )

    # imports 
    import petpy
    import pandas as pd
    import pyarrow.parquet as pq
    import pyarrow as pa

    # import model from production_model.py

    # set up petfinder search
    pf = petpy.Petfinder(
    key='Ww9PL1UlVo7Wdj0DeGkkRo6PXKCXdsStCMKQ2Jc9CYvX5OTNPX', 
    secret='7RNX05UlYJdUIbhy90BfgGwG0ZuwWkQTMNeIYAGk',)

    # user input: enter location for search
    zipcode = st.text_input('Enter your zipcode')
    location_input = zipcode
    location_input

    # user input: click button to search in location entered
    result = st.button('Search for Dogs')
    # when button is pushed: search for dogs in zipcode entered (automatically searches for dogs most recently added)
    if result == True:
        try:
            with st.spinner('Finding Available Dogs'):
                dogs = pf.animals(
                    pages=1, results_per_page=10, return_df=True, 
                    animal_type='dog', location=f'{zipcode}',
                    status='adoptable'
                    )


        # run dogs found in search through model

        # output: feed of available dogs determined to be 'high risk' by model
            st.header('Furry friends available in your area:')
            for i in range(len(dogs)):
                try:
                    col1, col2, col3 = st.columns([1,6,1])
                    with col2:
                        # - dog's name
                        st.subheader(dogs.iloc[i]['name'])

                        # - photo
                        if dogs.iloc[i]['photos'] != []:
                            st.image(dogs.iloc[i]['photos'][0]['medium'])
                        else:
                            st.image(
                                image='https://cdn.pixabay.com/photo/2016/04/03/21/54/dog-1305702_960_720.png',
                                width=300,
                                caption='Photo Not Available'
                            )

                        # - 'Animal Profile' description from petfinder
                        # - link to petfinder
                        url = dogs.iloc[i]['url']
                        st.write("[Learn More on Petfinder!](%s)" % url, color='white') 
                except:
                    pass

        # if no dogs found in zipcode entered:
        except:
            st.header('No dogs found in your area')