# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 19:14:44 2022

@author: siddhardhan
"""


import json
import requests


url = 'https://35d2-35-184-201-144.ngrok.io/diabetes_prediction'

input_data_for_model = {
    
    'Pregnancies' : 5,
    'Glucose' : 166,
    'BloodPressure' : 72,
    'SkinThickness' : 19,
    'Insulin' : 175,
    'BMI' : 25.8,
    'DiabetesPedigreeFunction' : 0.587,
    'Age' : 51
    
    }

input_json = json.dumps(input_data_for_model)

response = requests.post(url, data=input_json)

print(response.text)


