# Importing essential libraries
from flask import Flask, render_template, request
import pickle
import pandas as pd
import numpy as np

# Load the Random Forest Regressor model
filename = 'score_RF.pkl'
regressor = pickle.load(open(filename, 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/predict', methods=['GET','POST'])
def predict():
    temp_array = list()
    
    if request.method == 'POST':
        
        batting_team = request.form['batting-team']
        if batting_team == 'Chennai Super Kings':
            bat_team_Delhi_Daredevils = 0
            bat_team_Kings_XI_Punjab = 0
            bat_team_Kolkata_Knight_Riders = 0
            bat_team_Mumbai_Indians = 0
            bat_team_Rajasthan_Royals = 0
            bat_team_Royal_Challengers_Bangalore = 0
            bat_team_Sunrisers_Hyderabad = 0
        elif batting_team == 'Delhi Daredevils':
            bat_team_Delhi_Daredevils = 1
            bat_team_Kings_XI_Punjab = 0
            bat_team_Kolkata_Knight_Riders = 0
            bat_team_Mumbai_Indians = 0
            bat_team_Rajasthan_Royals = 0
            bat_team_Royal_Challengers_Bangalore = 0
            bat_team_Sunrisers_Hyderabad = 0
        elif batting_team == 'Kings XI Punjab':
            bat_team_Delhi_Daredevils = 0
            bat_team_Kings_XI_Punjab = 1
            bat_team_Kolkata_Knight_Riders = 0
            bat_team_Mumbai_Indians = 0
            bat_team_Rajasthan_Royals = 0
            bat_team_Royal_Challengers_Bangalore = 0
            bat_team_Sunrisers_Hyderabad = 0
        elif batting_team == 'Kolkata Knight Riders':
            bat_team_Delhi_Daredevils = 0
            bat_team_Kings_XI_Punjab = 0
            bat_team_Kolkata_Knight_Riders = 1
            bat_team_Mumbai_Indians = 0
            bat_team_Rajasthan_Royals = 0
            bat_team_Royal_Challengers_Bangalore = 0
            bat_team_Sunrisers_Hyderabad = 0
        elif batting_team == 'Mumbai Indians':
            bat_team_Delhi_Daredevils = 0
            bat_team_Kings_XI_Punjab = 0
            bat_team_Kolkata_Knight_Riders = 0
            bat_team_Mumbai_Indians = 1
            bat_team_Rajasthan_Royals = 0
            bat_team_Royal_Challengers_Bangalore = 0
            bat_team_Sunrisers_Hyderabad = 0
        elif batting_team == 'Rajasthan Royals':
            bat_team_Delhi_Daredevils = 0
            bat_team_Kings_XI_Punjab = 0
            bat_team_Kolkata_Knight_Riders = 0
            bat_team_Mumbai_Indians = 0
            bat_team_Rajasthan_Royals = 1
            bat_team_Royal_Challengers_Bangalore = 0
            bat_team_Sunrisers_Hyderabad = 0
        elif batting_team == 'Royal Challengers Bangalore':
            bat_team_Delhi_Daredevils = 0
            bat_team_Kings_XI_Punjab = 0
            bat_team_Kolkata_Knight_Riders = 0
            bat_team_Mumbai_Indians = 0
            bat_team_Rajasthan_Royals = 0
            bat_team_Royal_Challengers_Bangalore = 1
            bat_team_Sunrisers_Hyderabad = 0
        elif batting_team == 'Sunrisers Hyderabad':
            bat_team_Delhi_Daredevils = 0
            bat_team_Kings_XI_Punjab = 0
            bat_team_Kolkata_Knight_Riders = 0
            bat_team_Mumbai_Indians = 0
            bat_team_Rajasthan_Royals = 0
            bat_team_Royal_Challengers_Bangalore = 0
            bat_team_Sunrisers_Hyderabad = 1
            
            
        bowling_team = request.form['bowling-team']
        if bowling_team == 'Chennai Super Kings':
            bowl_team_Delhi_Daredevils = 0
            bowl_team_Kings_XI_Punjab = 0
            bowl_team_Kolkata_Knight_Riders = 0
            bowl_team_Mumbai_Indians = 0
            bowl_team_Rajasthan_Royals = 0
            bowl_team_Royal_Challengers_Bangalore = 0
            bowl_team_Sunrisers_Hyderabad = 0
        elif bowling_team == 'Delhi Daredevils':
            bowl_team_Delhi_Daredevils = 1
            bowl_team_Kings_XI_Punjab = 0
            bowl_team_Kolkata_Knight_Riders = 0
            bowl_team_Mumbai_Indians = 0
            bowl_team_Rajasthan_Royals = 0
            bowl_team_Royal_Challengers_Bangalore = 0
            bowl_team_Sunrisers_Hyderabad = 0
        elif bowling_team == 'Kings XI Punjab':
            bowl_team_Delhi_Daredevils = 0
            bowl_team_Kings_XI_Punjab = 1
            bowl_team_Kolkata_Knight_Riders = 0
            bowl_team_Mumbai_Indians = 0
            bowl_team_Rajasthan_Royals = 0
            bowl_team_Royal_Challengers_Bangalore = 0
            bowl_team_Sunrisers_Hyderabad = 0
        elif bowling_team == 'Kolkata Knight Riders':
            bowl_team_Delhi_Daredevils = 0
            bowl_team_Kings_XI_Punjab = 0
            bowl_team_Kolkata_Knight_Riders = 1
            bowl_team_Mumbai_Indians = 0
            bowl_team_Rajasthan_Royals = 0
            bowl_team_Royal_Challengers_Bangalore = 0
            bowl_team_Sunrisers_Hyderabad = 0
        elif bowling_team == 'Mumbai Indians':
            bowl_team_Delhi_Daredevils = 0
            bowl_team_Kings_XI_Punjab = 0
            bowl_team_Kolkata_Knight_Riders = 0
            bowl_team_Mumbai_Indians = 1
            bowl_team_Rajasthan_Royals = 0
            bowl_team_Royal_Challengers_Bangalore = 0
            bowl_team_Sunrisers_Hyderabad = 0
        elif bowling_team == 'Rajasthan Royals':
            bowl_team_Delhi_Daredevils = 0
            bowl_team_Kings_XI_Punjab = 0
            bowl_team_Kolkata_Knight_Riders = 0
            bowl_team_Mumbai_Indians = 0
            bowl_team_Rajasthan_Royals = 1
            bowl_team_Royal_Challengers_Bangalore = 0
            bowl_team_Sunrisers_Hyderabad = 0
        elif bowling_team == 'Royal Challengers Bangalore':
            bowl_team_Delhi_Daredevils = 0
            bowl_team_Kings_XI_Punjab = 0
            bowl_team_Kolkata_Knight_Riders = 0
            bowl_team_Mumbai_Indians = 0
            bowl_team_Rajasthan_Royals = 0
            bowl_team_Royal_Challengers_Bangalore = 1
            bowl_team_Sunrisers_Hyderabad = 0
        elif bowling_team == 'Sunrisers Hyderabad':
            bowl_team_Delhi_Daredevils = 0
            bowl_team_Kings_XI_Punjab = 0
            bowl_team_Kolkata_Knight_Riders = 0
            bowl_team_Mumbai_Indians = 0
            bowl_team_Rajasthan_Royals = 0
            bowl_team_Royal_Challengers_Bangalore = 0
            bowl_team_Sunrisers_Hyderabad = 1
            
        venue = request.form['Venue']    
        overs = float(request.form['overs'])
        runs = int(request.form['runs'])
        wickets = int(request.form['wickets'])
        runs_last_5 = int(request.form['runs_in_prev_5'])
        wickets_last_5 = int(request.form['wickets_in_prev_5'])
        
        lat=[venue, runs, wickets, overs, runs_last_5, wickets_last_5,
             bowl_team_Delhi_Daredevils, bowl_team_Kings_XI_Punjab,
             bowl_team_Kolkata_Knight_Riders, bowl_team_Mumbai_Indians,
             bowl_team_Rajasthan_Royals, bowl_team_Royal_Challengers_Bangalore,
             bowl_team_Sunrisers_Hyderabad, bat_team_Delhi_Daredevils,
             bat_team_Kings_XI_Punjab, bat_team_Kolkata_Knight_Riders,
             bat_team_Mumbai_Indians, bat_team_Rajasthan_Royals,
             bat_team_Royal_Challengers_Bangalore, bat_team_Sunrisers_Hyderabad]
        
        df = pd.DataFrame([lat])
        df.columns =['venue', 'runs', 'wickets', 'overs', 'runs_last_5', 'wickets_last_5',
                       'bowl_team_Delhi_Daredevils', 'bowl_team_Kings_XI_Punjab',
                       'bowl_team_Kolkata_Knight_Riders', 'bowl_team_Mumbai_Indians',
                       'bowl_team_Rajasthan_Royals', 'bowl_team_Royal_Challengers_Bangalore',
                       'bowl_team_Sunrisers_Hyderabad', 'bat_team_Delhi_Daredevils',
                       'bat_team_Kings_XI_Punjab', 'bat_team_Kolkata_Knight_Riders',
                       'bat_team_Mumbai_Indians', 'bat_team_Rajasthan_Royals',
                       'bat_team_Royal_Challengers_Bangalore', 'bat_team_Sunrisers_Hyderabad']
        my_prediction = int(regressor.predict(df)[0])
              
        return render_template('result.html', lower_limit = my_prediction-5, upper_limit = my_prediction+5)



if __name__ == '__main__':
	app.run(debug=True)
