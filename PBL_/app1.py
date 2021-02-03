# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 02:20:31 2020

@author: Krish Naik
"""

# -*- coding: utf-8 -*-
"""
Created on Fri May 15 12:50:04 2020

@author: krish.naik
"""

import pandas as pd
from flask import Flask, request
import flasgger
from flasgger import Swagger
#import streamlit as st 
import joblib

app=Flask(__name__)
Swagger(app)

classifier=joblib.load('salary.pk1')

@app.route('/')
def welcome():
    return "Welcome All"

@app.route('/predict',methods=["Get"])
def predict_note_authentication():
    
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: variance
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
    variance = request.args.get("variance")
    prediction=classifier.predict([[int(variance)]])
    print(prediction)
    return "the output is " +str(prediction)

@app.route('/predict_file',methods=["POST"])    
def predict_note_file():
    """let's Predict salary
    This is using docstring for specification.
    ---
    parameters:
        - name: file
          in: formData
          type: file
          required: true
          
    responses:
        200:
            description: The output values
    
    
    """
    df_test = pd.read_csv(request.files.get('file'))
    print(df_test.head())
    prediction = classifier.predict(df_test)
    return str(list(prediction))



if __name__=='__main__':
    app.run()
    
    
    