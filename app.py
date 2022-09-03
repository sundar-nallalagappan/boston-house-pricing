import os
import pickle
import os
from flask import Flask, request, app, jsonify, url_for, render_template
import numpy as np
import pandas as pd

#Starting point of the flask application
app = Flask(__name__)
std_scaler = pickle.load(open('std_scaler.pkl', 'rb'))
lr_model   = pickle.load(open('lr_model.pkl', 'rb'))

#Home-page/Landing page
@app.route('/')
def home():
    return render_template('home.html')

#Get & Post are functionally same. POST is secured as the data is encrypted but GET is not 
#secured as data is attached to the url as query
@app.route('/predict_api', methods=['POST'])
def predict_api():
    #Json will bear the key value as data
    data = request.json['data']
    print('Consumed data is {}'.format(data))
    print('dictionary values:', data.values())
    print(list(data.values()))
    print('Initial shape:', np.array(list(data.values())).shape)
    print(np.array(list(data.values())).reshape(1,-1))
    transformed_data = np.array(list(data.values())).reshape(1,-1)
    print('Transformed shape:', transformed_data.shape)
    
    #Apply the scaler on reshaped data
    std_transformed_data = std_scaler.transform(transformed_data)
    print('Std data : ', std_transformed_data)
    
    #Apply the model to make predictions
    output = lr_model.predict(std_transformed_data)
    print('Raw output is {}'.format(output))
    
    print('Json:', jsonify(output[0]))
    
    return jsonify(output[0])


#Below method is to invoked when FE UI form is filled with values for input features
@app.route('/predict', methods=['POST'])
def predict():
    data = [float(x) for x in request.form.values()]
    print('Raw input:', data)
    #print('Raw input shape', data.shape)
    
    transformed_data = np.array(data).reshape(1,-1)
    print('Transformed data :', transformed_data)
    
    #Apply the scaler on reshaped data
    std_transformed_data = std_scaler.transform(transformed_data)
    print('Std data : ', std_transformed_data)
    
    #Apply the model to make predictions
    output = lr_model.predict(std_transformed_data)
    print('Raw output is {}'.format(output))
    
    return render_template('home.html', prediction_text = 'Predicted housing price is {}'.format(output[0]))
   
    
    

if __name__ == "__main__":
    app.run(debug=True)
    
    



