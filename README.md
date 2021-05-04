# Project-3 - Machine Learning Oscar Nominations
This project focused on predicting whether a movie will be oscar nominated based on multiple features from IMDB data. We ended up adding more features to fine-tune our model and see if these held any more weight than the original features chosen. Finally, we developed an flask app to connect our most successful model to a front-facing, user-friendly html page for others to predict whether a newly released film might be Oscar Nominated.   

# Accuracy Ratings
XGBoost Model 3: 86.62%  
Logistic Classification with Gridsearch CV: 86.76%  
Random Forest - Randomizedsearch CV (60 fits) best fit: 87.16%  
XGBoost Model 1 - 87.26%  
XGBoost Model 4: 88.22%  
XGBoost Model 2: 88.85%   


# Feature Importances in order (Most Accurate Model) : 
* Total non-oscars awards nominations       
* Golden Globes nominations   
* Non-oscars awards won           
* IMDB popularity              
* Gross profits                     
* Metascore                
* Duration (min)                 
* Critic Reviews          


# Process 
* Identify data source (csv file) to clean and use for learning models. 
* Cleaned our csv and identified features we believed would add significant weight towards our models. We created a dedicated [CSV](data/oscars_df.csv) to use for our models.
* Created supervised learning models using [logistic classification](ML_tests), [random forest](ML_tests) and [XGBoost](ML_tests) (decision trees) to produce the highest accuracy rating.
* Developed an [html page](templates/predictions.html) for users to interact with our best trained model. The page has links to our project repository, the IMDB website and a carousel of bar graphs highlighting the relationship between features and likelihood of an oscar nomination.
* Created a [Flask API](app1.py) to communicate with our html page. The app returns a prediction using the XGBoost Model (2) based on user inputs.

![Screenshot](https://github.com/eenabow/oscar_nominations/blob/main/templates/Predictions.PNG)

# Visuals 
We created a carousel of bar graphs using [Tableau] to showcase some of our findings. We also used matplotlib to create horizontal bar graphs which display feature importance per model.

# Data Sources 
* IMDB - https://www.kaggle.com/vipulgote4/oscars-nominated-movies-from-2000-to-2017


Team members: Anna Bowers, Mario Lozano, LaTisha Habersham, Jack Griffin, Jean-Pierre Gilbert
