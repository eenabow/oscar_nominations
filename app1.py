from flask import Flask, request, render_template
import joblib
from joblib import load
import pandas as pd

filename = 'assets/xgb_oscars.joblib'
loaded_model = joblib.load(filename)

app = Flask(__name__)
@app.route('/generatepredictions', methods=['GET'])

def return_prediction():
    try:
        
        query_string = request.url
        print(query_string)

        # Parse the query string
        duration = request.args.get('duration')
        metascore = request.args.get('metascore')
        gross = request.args.get('gross')
        critic_reviews = request.args.get('critic_reviews')
        awards_wins = request.args.get('awards_wins')
        popularity = request.args.get('popularity')
        awards_nominations = request.args.get('awards_nominations')
        golden_globe_nominations = request.args.get('golden_globe_nominations')

        # Create a df to feed model
        df = pd.DataFrame({
            'duration': [int(duration)],
            'metascore': [int(metascore)],
            'gross': [int(gross)],
            'critic_reviews': [int(critic_reviews)],
            'awards_wins': [int(awards_wins)],
            'popularity': [int(popularity)], 
            'awards_nominations': [int(awards_nominations)],
            'golden_globe_nominations': [int(golden_globe_nominations)]
        })
        
        print(df)
        prediction = loaded_model.predict(df)[0]
   

        print(prediction)

        if prediction ==1:
            prediction = "YES"
        else: 
            prediction = "NO"
        return render_template('predictions.html', yes_no=prediction)

    except:
        return render_template('predictions.html', yes_no='RETRY')

if __name__ == '__main__':
    app.run(debug=True)