# this one is linked to streamlit app

import streamlit as st
import numpy as np
import pickle
from predict import predict_dog


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

    # load classifier
    with open('./model_rfc.pkl', 'rb') as f:
        classifier = pickle.load(f)

    # load transformer
    with open('./encode_data.pkl', 'rb') as f:
        transformer = pickle.load(f)

    # user input: enter location for search
    zipcode = st.text_input('Enter your zipcode')

    # when button is pushed: search for dogs in zipcode entered (automatically searches for dogs most recently added)
    if st.button('Search for Dogs'):
        try:
            with st.spinner('Finding Available Dogs'):
                dogs = pf.animals(
                    pages=1,
                    results_per_page=10, 
                    return_df=True, 
                    animal_type='dog', 
                    location=f'{zipcode}',
                    status='adoptable'
                )
            # st.write(type(dogs))

        # if no dogs found in zipcode entered:
        except:
            st.header('No dogs found in your area')
            
        
            
        if len(dogs) > 0:

            dogs_copy = dogs.copy()
            dogs_copy = dogs_copy[['age', 'breeds.primary', 'photos', 'name', 'size', 'gender', 'url']]
            dogs_copy['pred'] = np.nan

            for i in range(len(dogs_copy)):

                np_dog = np.array(
                    [
                        dogs_copy.iloc[i]['age'].lower(), 
                        dogs_copy.iloc[i]['breeds.primary'].lower(),
                        'normal'
                    ]
                )

                prediction = np.round(predict_dog(np_dog, classifier, transformer) * 100, 2)
                dogs_copy.loc[i, 'pred'] = prediction

            dogs_copy.sort_values(by='pred', ascending=False, inplace=True)
        
            # output: feed of available dogs determined to be 'high risk' by model
            st.header('Furry friends available in your area:')
            for i in range(len(dogs_copy)):
                
                try:

                    col1, col2, col3, col4 = st.columns([1,3,3,1])
                    
                    with col2:
                        # - photo
                        if dogs_copy.iloc[i]['photos'] != []:
                            st.image(dogs_copy.iloc[i]['photos'][0]['medium'])
                        else:
                            st.image(
                                image='https://cdn.pixabay.com/photo/2016/04/03/21/54/dog-1305702_960_720.png',
                                caption='Photo Not Available',
                                # width=300
                            )
                    with col3:
                        # - dog's name and details
                        st.subheader(dogs_copy.iloc[i]['name'])
                        st.metric('At Risk %', dogs_copy.iloc[i]['pred'])
                        st.write('Breed: ', dogs_copy.iloc[i]['breeds.primary'])
                        st.write('Size: ', dogs_copy.iloc[i]['size'])
                        st.write('Gender: ', dogs_copy.iloc[i]['gender'])
                        st.write('Age: ', dogs_copy.iloc[i]['age'])
                        
                        # - link to petfinder
                        url = dogs_copy.iloc[i]['url']
                        st.write("[Learn More on Petfinder!](%s)" % url) 
                except:
                    pass

                # space in between dogs
                st.text("")
                st.write(":heavy_minus_sign:" * 30)
                st.text("")

        
