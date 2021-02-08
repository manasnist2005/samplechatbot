# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 00:29:58 2021

@author: lalatendu
"""

from flask import Flask, request, jsonify
import numpy as np
import pandas as pd
#from keras.models import model_from_json
import json

#from tensorflow.keras.preprocessing.text import Tokenizer
#from tensorflow.keras.preprocessing.sequence import pad_sequences



#with open('/var/www/flask_predict_api/rf.pkl', 'rb') as model_file:
 #   model = pickle.load(model_file)

app = Flask(__name__)

Week_day1 = {"Sunday":0,"Monday":1,"Tuesday":2,"Wednesday":3,"Thrusday":4,"Friday":5,"Saturday":6}
Season1 = {"Spring":1,"Summer":2,"Autumn":3,"Winter":4}

def input_datafarame(lst):
    df = pd.DataFrame(lst,columns=['Country','Local','Industry Sector','Gender','Employee type','Critical Risk','Year','Month','Day','Weekday','Season','Description'])
    X_cat=df[['Country','Local','Industry Sector','Gender','Employee type','Critical Risk','Year','Month','Day','Weekday','Season']]
    X_nlp=df[['Description']]
    print(df)
    return X_nlp,X_cat

'''def read_model():
    # load json and create model
    json_file = open('model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model=loaded_model.load_weights("model.h5")
    print("Loaded model from disk")
    return loaded_model'''

def tokenizer_text(data):
    print("tokenizer_text")
    max_features=10000
    maxlen = 110
    tokenizer = Tokenizer(num_words=max_features,lower = False)
    tokenizer.fit_on_texts(data)
    data = tokenizer.texts_to_sequences(data)
    data = pad_sequences(data, maxlen = maxlen, padding='post')
    return data

def month2seasons(x):
    if x in [9, 10, 11]:
        season = 'Spring'
    elif x in [12, 1, 2]:
        season = 'Summer'
    elif x in [3, 4, 5]:
        season = 'Autumn'
    elif x in [6, 7, 8]:
        season = 'Winter'
    print("season in function:",season)
    return Season1[season]

def data_extact(x):
    print("Date Extract Started")
    date = pd.to_datetime(x)
    print("date:",date)
    print("year:",date.year)
    year = date.year
    
    month = date.month
    print("month:",month)
    day = date.day
    week_day = Week_day1[date.day_name()]
    print("week_day:",week_day)
    season = month2seasons(month)
    print("season:",season)
    print(year,month,day,week_day,season)
    return year,month,day,week_day,season




@app.route('/predict', methods=["POST"])
def predict_json():
    input= request.get_json()
    print("Lala")
    print(input)
    #input_data = json.loads(input)
    input_data=input
    print(input_data["accident_deatils"])
    #print(input_data)
    
    
    data = input_data["accident_deatils"]
    country	= data.get("Country")
    print("Country:",country)
    local   = data.get("Local")
    industry_Sector = data.get("Industry_Sector")
    gender = data.get("Gender")
    employee_type = data.get("Employee_Type")
    critical_risk = data.get("Critical_Risk")
    year,month,day,weekday,season=data_extact(data.get("Date"))	
    description = data.get("Description")
    
    print("Input data :")        
    print(country,local,industry_Sector,gender,employee_type,critical_risk,year,month,day,weekday,season)

    print(description)

    # cat_data=[country,local,industry_Sector,gender,employee_type,critical_risk,year,month,day,weekday,season]
    #nlp_data,cat_data=input_datafarame([country,local,industry_Sector,gender,employee_type,critical_risk,year,month,day,weekday,season,description])
    
    #nlp_data = tokenizer_text(nlp_data)
    #print(nlp_data)
    
    
    #model = read_model()
    #print(model.summary())
    
   # y_pred = model.predict(x=[nlp_data, cat_data], batch_size=1024, verbose=1)
    y_pred=1
    print("Lala")
    print(input)
    #print(jsonify(input))
    #input_data = pd.read_csv(request.files.get("input_file"), header=None)
    #prediction = model.predict(input_data)
    return jsonify({"pedict":y_pred})

@app.route('/test', methods=["GET"])
def Test():
	return("Test method")
	
if __name__ == '__main__':
    app.run()
    
    
