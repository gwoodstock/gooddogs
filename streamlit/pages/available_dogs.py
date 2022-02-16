import streamlit as st


def app():

    # page header
    st.header('Insert header for page here') 

    # imports 
    import petpy
    import pandas as pd
    import pyarrow.parquet as pq
    import pyarrow as pa

    # import model from production_model.py

    # set up petfinder search
    pf = petpy.Petfinder(
        key='Ww9PL1UlVo7Wdj0DeGkkRo6PXKCXdsStCMKQ2Jc9CYvX5OTNPX', 
        secret='7RNX05UlYJdUIbhy90BfgGwG0ZuwWkQTMNeIYAGk',
    )

    # user input: enter location for search
    zipcode = st.text_input('Enter your zipcode')
    # location_input = zipcode
    # location_input

    # user input: click button to search in location entered
    # result = st.button('Search for Dogs')

    

    # when button is pushed: search for dogs in zipcode entered (automatically searches for dogs most recently added)
    if st.button('Search for Dogs'):
        try:
            with st.spinner('Finding Available Dogs'):
                dogs = pf.animals(
                    pages=1,
                    results_per_page=100, 
                    return_df=True, 
                    animal_type='dog', 
                    location=f'{zipcode}',
                    status='adoptable'
                )


        # run dogs found in search through model

        # output: feed of available dogs determined to be 'high risk' by model
            st.header('Furry friends available in your area:')
            for i in range(len(dogs)):
                
                try:
                    col1, col2, col3, col4 = st.columns([1,3,3,1])
                    
                    with col2:
                        # - photo
                        if dogs.iloc[i]['photos'] != []:
                            st.image(dogs.iloc[i]['photos'][0]['medium'])
                        else:
                            st.image(
                                image='https://cdn.pixabay.com/photo/2016/04/03/21/54/dog-1305702_960_720.png',
                                caption='Photo Not Available',
                                # width=300
                            )
                    with col3:
                        # - dog's name and details
                        st.subheader(dogs.iloc[i]['name'])
                        st.write('Breed: ', dogs.iloc[i]['breeds.primary'])
                        st.write('Size: ', dogs.iloc[i]['size'])
                        st.write('Gender: ', dogs.iloc[i]['gender'])
                        st.write('Age: ', dogs.iloc[i]['age'])

                        # st.error('At Risk')
                        
                        # - link to petfinder
                        url = dogs.iloc[i]['url']
                        st.write("[Learn More on Petfinder!](%s)" % url) 
                except:
                    pass

                # space in between dogs
                st.text("")
                st.write(":heavy_minus_sign:" * 30)
                st.text("")

        # if no dogs found in zipcode entered:
        except:
            st.header('No dogs found in your area')
