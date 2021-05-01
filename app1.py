# from flask import Flask, render_template, request
# import pickle
# import numpy as np
# from joblib import load
# import pandas as pd
# import sklearn
# from sklearn.preprocessing import StandardScaler

# app = Flask(__name__)
# trained_machine_learning_model = load('ML_test/logistic_classification_oscars.joblib')

# @app.route('/',methods=['GET'])
# def Home():
#     return render_template('pre1.html')


# standard_to = StandardScaler()
# @app.route("/predict", methods=['POST'])
# def predict():
#     if request.method == 'POST':
#         Duration = int(request.form['duration'])
#         Metascore = float(request.form['Present_Price'])
#         Gross = int(request.form['Kms_Driven'])
#         Critic_Reviews = int(request.form['Year'])
#         Awards_Wins = float(request.form['Present_Price'])
#         Popularity = int(request.form['Kms_Driven'])
#         Awards_Nominations = int(request.form['Year'])
#         Golden_Globe_Nominations =float(request.form['Present_Price'])
#         Gross =int(request.form['Kms_Driven'])
#         Kms_Driven2=np.log(Kms_Driven)
#         Owner=int(request.form['Owner'])
#         Fuel_Type_Petrol=request.form['Fuel_Type_Petrol']
#         if(Fuel_Type_Petrol=='Petrol'):
#                 Fuel_Type_Petrol=1
#                 Fuel_Type_Diesel=0
#         else:
#             Fuel_Type_Petrol=0
#             Fuel_Type_Diesel=1
#         Year=2020-Year
#         Seller_Type_Individual=request.form['Seller_Type_Individual']
#         if(Seller_Type_Individual=='Individual'):
#             Seller_Type_Individual=1
#         else:
#             Seller_Type_Individual=0	
#         Transmission_Mannual=request.form['Transmission_Mannual']
#         if(Transmission_Mannual=='Mannual'):
#             Transmission_Mannual=1
#         else:
#             Transmission_Mannual=0
#         prediction=model.predict([[Present_Price,Kms_Driven2,Owner,Year,Fuel_Type_Diesel,Fuel_Type_Petrol,Seller_Type_Individual,Transmission_Mannual]])
#         output=round(prediction[0],2)
#         if output<0:
#             return render_template('pre1.html',prediction_texts="Sorry you will not be nominated for an Oscar.")
#         else:
#             return render_template('pre1.html',prediction_text="Congratulations, you will be nominated for an Oscar {}".format(output))
#     else:
#         return render_template('pre1.html')

# if __name__=="__main__":
#     app.run(debug=True)

# YOUR FLASK APP:
from flask import Flask, request
import joblib
from joblib import load

filename = 'assets/xgb_oscars.joblib'
loaded_model = joblib.load(filename)

app = Flask(__name__)
@app.route('/generatepredictions', methods=['GET'])
def return_prediction():
    # ex url might be:
    # localhost:8000/generatepredictions?duration=30&metascore=50&test=hello
    query_string = request.args.url
    # do some stuff to parse the query string
    duration = query_string['duration']
    metascore = query_string['metascore']
    gross = query_string['gross']
    critic_reviews = query_string['critic_reviews']
    awards_wins = query_string['awards_wins']
    popularity = query_string['popularity']
    awards_nominations = query_string['awards_nominations']
    golden_globe_nominations = query_string['golden_globe_nominations']

    new_datapoint = [duration, metascore, gross, critic_reviews, awards_wins, popularity, awards_nominations, golden_globe_nominations]
    prediction = loaded_model.predict(new_datapoint)
    return { 'prediction': prediction }
    # return { 'prediction': query_string }
if __name__ == '__main__':
    app.run(debug=True)