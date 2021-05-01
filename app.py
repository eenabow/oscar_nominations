from flask import Flask, render_template
# from data import origin_dict, dest_dict, miles_dict
from joblib import load
import pandas as pd

app = Flask(__name__)
trained_machine_learning_model = load('assets/xgb_oscars.joblib')

# @app.route('/')
# def home():
#     return render_template('index.html')


# flask forms examples - https://flask-wtf.readthedocs.io/en/stable/quickstart.html
# flask query string parameters
# 4/2/40/1/16
@app.route('/generatepredictions')
# @app.route('/generatepredictions/<Quarter>/<Origin>/<Dest>/<NumTicketsOrdered>/<AirlineCompany>')
def predict(Quarter, Origin, Dest, NumTicketsOrdered, AirlineCompany):
    try:
        df = pd.DataFrame({
            'Quarter': [int(Quarter)],
            'Origin': [int(Origin)],
            'Dest': [int(Dest)],
            'Miles': [miles_dict[f"{origin_dict[int(Origin)]}>{dest_dict[int(Dest)]}"]],
            'NumTicketsOrdered': [int(NumTicketsOrdered)],
            'AirlineCompany': [int(AirlineCompany)]
        })

        PricePerTicket = str(trained_machine_learning_model.predict(df)[0])[0:6]
        PricePerTicket = f"${PricePerTicket}"

        return render_template('predictions.html', pricePerTicket=PricePerTicket)

    except:
        return render_template('predictions.html', pricePerTicket='RETRY')
    

if __name__ == '__main__':
    app.run()