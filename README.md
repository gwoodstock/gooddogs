# Project 4: GOOD DOGS App

## Authors
Gene Woodstock, Anna Rutledge, Nate Cox & Elena Yakubchik

General Assembly DSI-1213

## Contents:
- Executive Summary
- Data Dictionary
- Limitations and next steps
- Conclusions

## Executive Summary
It came to our attention that many animal shelters are going through a tough time lately. They are experiencing capacity problems and some of them have already reached their space and resources limits, for example Austin Animal Center.
 
This shelter has a no kill policy and for years their main goal has been to find forever homes for all adoptable animals. Austin Animal Center has been accepting and taking care of thousands of animals annually regardless of age, health, species or breed. On Feb 10th Austin Animal Center announced they are nearing capacity and are unable to accept medium and large dogs, and asked the community for help. So our team decided to respond.
 
We started with datasets, provided by Austin Animal Center and The Intelligence of Dogs dataset (1994). Our idea was to identify dogs AT RISK to experience extremely long adoption wait times, and help these dogs to be adopted faster. To be able to make predictions we had to clean our data and use a variety of features to find valuable correlations.
 
The next step was modeling. Our project team explored a number of models, looking for the best fit. We ended up using Neural Net, XGBoost and Random Forest models for the best results.
 
While building a model we realized that we can make an App, which can help dogs at risk all over the country to be adopted. So we used Streamlit to create an App that is able to gather up to date data from hundreds of shelters by web scraping Petfinder.com and filter dogs at higher risk.
 
Here is a list of notebooks with our work process:


## Data Dictionary

Datasets:

1) [Austin Animal Center](https://github.com/gwoodstock/project4/blob/main/datasets/cleaned_data/austin.csv)
- Intake & Outcome data for Austin Animal Center. [Original Source](https://data.world/siyeh/austin-animal-center-live-data)

2) [Dog Inteligence](https://github.com/gwoodstock/project4/blob/main/datasets/raw_data/dog_intelligence.csv)

3) [Prtfinder](https://github.com/gwoodstock/project4/blob/main/datasets/raw_data/petfinder.csv)

## Limitations and next steps
Limitations:
1) Finding Signal
   - Intelligence not predictive
   - Limited data crossover for Shelter & PetFinder
2) Inconsistent & Missing Data
   - Intake & Outcome Shelter data misaligned
3) Historical data unavailable from PetFinder


Next steps:

1) Model Improvement
   - Voting ensemble
2) More Data
   - Daily PetFinder data
   - Data from more shelters
3) Design
   - More app features
4) Go International
   - Dogs around the world!!


## Conclusions
Our app can help Austin Animal Center and shelters all around the country increase exposure of dogs at risk of experiencing long adoption wait times.


