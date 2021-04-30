# Project-3 - Machine Learning Oscar Nominations
This project focused on predicting whether a movie will be oscar nominated based on multiple features from IMDB data. We ended up adding more features to fine-tune our model and see if these held any more weight than the original features chosen. Finally, we developed an flask app to connect our most successful model to a front-facing, user-friendly html page for others to predict whether a newly released film might be Oscar Nominated.   

![Screen Shot 2021-03-30 at 5 29 45 PM](https://github.com/eenabow/oscar_nominations/blob/b5f18564e824b8558795b13f25b057d74796e60b/ML_tests/xgbmodel2_importantfeatures.png)

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
* Narrowed down visualization inspiration to enhance our data findings 
* [Cleaned 3 csv's](data/Clean_Data.ipynb)  
* Located the top 20 Countries with the highest CO2 Emissions and [parsed through each cleaned csv to filter the top 20 countries](data/climate_change.ipynb)
* Loaded our new tables into [Postgres](SQL_DATA/Table_script.sql)
* Created [sqlalchemy routes](app.py) and [javascript d3 visualizations](static/js/climate.js) to append the graphs to the browser 
* Developed an [html page](templates/welcome.html)  and [css](static/css/style.css) to enhance the user's experience. 

# Visuals 
We created a dashboard of visuals using [d3, plotly] to showcase our findings. 
* Pie chart 
* Bar Chart 

# Data Sources 
* IMDB - https://www.kaggle.com/vipulgote4/oscars-nominated-movies-from-2000-to-2017


Team members: Anna Bowers, Mario Lozano, LaTisha Habersham, Jack Griffin, Jean-Pierre Gilbert
