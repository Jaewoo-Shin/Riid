from flask import Flask, jsonify, request
import pandas as pd
from xgboost import XGBClassifier
import pickle
app = Flask(__name__)

@app.route("/predict", methods=['POST']) 
def predict():
  if request.method == 'POST':
      file = request.files['csv'] #csv 파일 받기
      data = pd.read_csv(file)
      Gender = data.Gender.map({'Boy':1, 'Girl':0})
      Age = data.Age.map({'1-5':0, '6-10':1, '11-15':2, '16-20':3, '21-25':4, '26-30':5})
      Education_Level = data['Education Level'].map({'School':0,'College':1,'University':2})
      Institution_Type = data['Institution Type'].map({'Non Government':0,'Government':1})
      IT_Student = data['IT Student'].map({'Yes':1, 'No':0})
      Location = data.Location.map({'Yes':1, 'No':0})
      Load_shedding = data['Load-shedding'].map({'High':1, 'Low':0})
      Financial_Condition = data['Financial Condition'].map({'Poor':0,'Mid':1,'Rich':2})
      Internet_Type = data['Internet Type'].map({'Mobile Data':1, 'Wifi':0})
      Network_Type = data['Network Type'].map({'2G':0,'3G':1,'4G':2})
      Class_Duration = data['Class Duration'].map({'0':0,'1-3':1,'3-6':2})
      Self_Lms = data['Self Lms'].map({'Yes':1,'No':0})
      Device = data.Device.map({'Mobile':0, 'Tab':1, 'Computer':2})

      X_data = pd.concat([Gender,Age,Education_Level,Institution_Type,IT_Student,Location,Load_shedding,
                Financial_Condition,Internet_Type,Network_Type,Class_Duration,Self_Lms,Device], axis=1)
      model = pickle.load(open('model','rb'))
      prediction = model.predict(X_data)
      predict_dict = {0:'Low',1:'Moderate',2:'High'}
      result = [predict_dict[i] for i in prediction]
  return jsonify(list(result)), 200

