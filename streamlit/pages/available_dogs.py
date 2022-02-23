# this one is linked to streamlit app

import streamlit as st
import numpy as np
import pickle
from predict import predict_dog
from clean_breeds import breed_func

from pathlib import Path


def app():
    st.sidebar.image(
        'https://images.unsplash.com/photo-1586671267731-da2cf3ceeb80?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NHx8ZG9nfGVufDB8MXwwfHw%3D&auto=format&fit=crop&w=800&q=60',
        use_column_width=True
        )

    # page header
    st.header('Finding a Way Home') 

    st.markdown('**Animal shelters around the country are struggling with overcrowding and are striving to create positive outcomes for all animals. Our mission is to provide relief and assistance to these organizations, and to help every dog find a loving home.**')
    
    st.markdown('**Enter your location and find your new forever friend! Dogs in your area available for adoption through Petfinder are displayed, with those at higher risk for longer shelter wait times highlighted first.**')

    
    # imports 
    import petpy
    import pandas as pd
    # import pyarrow.parquet as pq  # are these used?
    # import pyarrow as pa

    # import model from production_model.py

    # set up petfinder search
    pf = petpy.Petfinder(
        key=st.secrets["key"], 
        secret=st.secrets["secret"],
    )
    
    pkl_path = Path(__file__).parents[1] / 'pages/model_rfc.pkl'
    # load classifier
    with open(pkl_path, 'rb') as f:
        classifier = pickle.load(f)
    
    pkl_path = Path(__file__).parents[1] / 'pages/encode_data.pkl'
    # load transformer
    with open(pkl_path, 'rb') as f:
        transformer = pickle.load(f)

    # user input: enter location for search
    location = st.text_input('Enter Your City, State or Zipcode:')

    # initialize dogs
    dogs = []

    # when button is pushed: search for dogs in zipcode entered (automatically searches for dogs most recently added)
    if st.button('Search for Dogs'):
        with st.spinner('Finding Available Dogs'):
            try:
                # with st.spinner('Finding Available Dogs'):
                    dogs = pf.animals(
                        pages=1,
                        results_per_page=100, 
                        return_df=True, 
                        animal_type='dog', 
                        location=f'{location}',
                        status='adoptable'
                    )

            # if no dogs found in zipcode entered:
            except:
                st.header('No dogs found in your area')
                
            # if dogs were found, run this block of code
            # makes predictions and displays dogs
            if len(dogs) > 0:

                # copy dogs dataframe and selects only the columns that will be used
                dogs_copy = dogs.copy()
                dogs_copy = dogs_copy[['age', 'breeds.primary', 'photos', 'name', 'size', 'gender', 'url', 'attributes.special_needs']]

                # maps special needs to be used in the model
                dogs_copy['attributes.special_needs'] = dogs_copy['attributes.special_needs'].map({True: 0, False: 1})

                # create prediction column
                dogs_copy['pred'] = np.nan

                # prediction section
                # loops over all the dogs in the search results
                for i in range(len(dogs_copy)):
                    # clean breed names to make them usuable for the model
                    breed = dogs_copy.iloc[i]['breeds.primary'].lower()
                    cleaned_breed = breed_func(breed)

                    # creates an np.array of the features to be used in the prediction
                    np_dog = np.array(
                        [
                            dogs_copy.iloc[i]['age'].lower(), 
                            cleaned_breed,
                            dogs_copy.iloc[i]['attributes.special_needs']
                        ]
                    )

                    # makes the prediction for this dog and assigns the score to the pred column
                    prediction = predict_dog(np_dog, classifier, transformer)
                    dogs_copy.loc[i, 'pred'] = np.round(prediction * 100, 2)

                # create labels for at risk
                dogs_copy['pred_label'] = dogs_copy['pred'].map(lambda x: 'At Risk' if x >= 50 else 'Low Risk')

                # sort dataframe so the highest % are at the top
                dogs_copy.sort_values(by='pred', ascending=False, inplace=True)
                dogs_copy.reset_index(drop=True, inplace=True)
            
                # output: feed of available dogs determined to be 'high risk' by model
                st.header('Furry friends available in your area:')
                for i in range(len(dogs_copy)):
                    
                    try:
                        # creates columns for spacers and displaying the image and info
                        col1, col2, col3, col4 = st.columns([1,3,3,1])
                        
                        with col2:
                            # photo
                            if dogs_copy.iloc[i]['photos'] != []:
                                st.image(dogs_copy.iloc[i]['photos'][0]['medium'])
                            else:
                                # default image
                                st.image(
                                    image='https://cdn.pixabay.com/photo/2016/04/03/21/54/dog-1305702_960_720.png',
                                    caption='Photo Not Available',
                                    # width=300
                                )

                        with col3:
                            # dog's name and details
                            st.subheader(dogs_copy.iloc[i]['name'])
                            # st.metric('At Risk %', dogs_copy.iloc[i]['pred'])
                            # st.metric(dogs_copy.loc[i, 'pred_label'])
                            st.metric('Status:', dogs_copy.loc[i, 'pred_label'])
                            st.write('Breed: ', dogs_copy.iloc[i]['breeds.primary'])
                            st.write('Size: ', dogs_copy.iloc[i]['size'])
                            st.write('Gender: ', dogs_copy.iloc[i]['gender'])
                            st.write('Age: ', dogs_copy.iloc[i]['age'])
                            
                            # link to petfinder
                            url = dogs_copy.iloc[i]['url']
                            st.write("[Learn More on Petfinder!](%s)" % url) 
                    except:
                        pass

                    # space in between dogs
                    st.text("")
                    st.write(":heavy_minus_sign:" * 30)
                    st.text("")

    # clears dogs to be able to do another search   
    dogs = []
