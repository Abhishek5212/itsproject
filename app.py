import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model_DT = pickle.load(open('major_DT.pkl','rb'))
model_KNN = pickle.load(open('major_KNN.pkl','rb'))
model_log = pickle.load(open('major_log.pkl','rb'))
model_NB = pickle.load(open('major_NB.pkl','rb'))
model_Kmean = pickle.load(open('kmeanscluster.pkl','rb'))


@app.route('/')
def home():
  
    return render_template("index.html")

@app.route('/Mini')
def mini():
  
    return render_template("Mini.html")

@app.route('/About')
def about():
  
    return render_template("About.html")

@app.route('/Description')
def desc():
  
    return render_template("Description.html")

@app.route('/Feedback')
def feed():
  
    return render_template("Feedback.html")


@app.route('/Models')
def model():
  
    return render_template("Models.html")

@app.route('/predict',methods=['GET'])
def predict():
    
    ex1 = float(request.args.get('Annual_Income'))
    ex2 = float(request.args.get('Monthly_Inhand_Salary'))
    ex3 = float(request.args.get('Num_Bank_Accounts'))
    ex4 = float(request.args.get('Interest_Rate'))
    ex5 = float(request.args.get('Num_of_Loan'))
    ex6 = float(request.args.get('Num_of_Delayed_Payment'))
    ex7 = float(request.args.get('Outstanding_Debt'))
    ex8 = (request.args.get('Payment_of_Min_Amount'))

    if ex8=="Yes":
      ex8 = 1
    else:
      ex8 = 0
    
    ex9 = float(request.args.get('Total_EMI_per_month'))
    ex10 = float(request.args.get('Amount_invested_monthly'))
    ex11 = float(request.args.get('Monthly_Balance'))

    Model = (request.args.get('Model'))

    if Model=="Random Forest Classifier":
      prediction = model_DT.predict([[ex1,ex2,ex3,ex4,ex5,ex6,ex7,ex8,ex9,ex10,ex11]])

    elif Model=="Decision Tree Classifier":
      prediction = model_DT.predict([[ex1,ex2,ex3,ex4,ex5,ex6,ex7,ex8,ex9,ex10,ex11]])

    elif Model=="KNN Classifier":
      prediction = model_KNN.predict([[ex1,ex2,ex3,ex4,ex5,ex6,ex7,ex8,ex9,ex10,ex11]])

    elif Model=="Logistic Regression Classifier":
      prediction = model_log.predict([[ex1,ex2,ex3,ex4,ex5,ex6,ex7,ex8,ex9,ex10,ex11]])

    elif Model=="SVM":
      prediction = model_log.predict([[ex1,ex2,ex3,ex4,ex5,ex6,ex7,ex8,ex9,ex10,ex11]])

    elif Model=="K Means Cluster":
      prediction = model_log.predict([[ex1,ex2,ex3,ex4,ex5,ex6,ex7,ex8,ex9,ex10,ex11]])

    else:
      prediction = model_NB.predict([[ex1,ex2,ex3,ex4,ex5,ex6,ex7,ex8,ex9,ex10,ex11]])



    if prediction==[0]:
     result="Good 🙂"

    elif prediction==[1]:
     result="Standard 😉"
    elif prediction==[2]:
     result="Poor 😞"

    return render_template('Models.html', prediction_text='Model  has predicted Credit Score : {}'.format(result))

if __name__ == "__main__":
    app.run(debug=True)