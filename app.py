from flask import Flask, request, jsonify, render_template, session, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import sqlite3
import models as dbHandler
# import numpy as np
# from wtforms import TextField, SubmitField
# import tensorflow
# from tensorflow.keras.models import load_model
# import joblib'
app = Flask(__name__) 
 

@app.route("/", methods=['GET', 'POST'])
def login():
    msg=""
    if request.method== "POST":
        name = request.form["name"]   
        phone_number = request.form["phone_number"]   
        password = request.form["password"]
        age=request.form["age"]
        relationship_status=request.form["rs"]
        gender=request.form["gender"]
        result= dbHandler.insertUser(name,phone_number,password,age,gender,relationship_status)
        if result:
            msg="Account Created"
        else:
            msg="Error"
    return render_template('login.html', msg = msg)



@app.route("/search", methods=['GET', 'POST'])
def home():
    msg='message'
    if request.method == "POST":
        phone_number = request.form["phone_number"]   
        password = request.form["password"]
        result = dbHandler.retrieveUsers(phone_number,password)
        if result == True:     
            msg='successful'
            return render_template("search.html")  
        else:
            msg='Invalid Username or password'
            return render_template("login.html",msg = msg)     


# model = load_model('ANN1.h5')
# scaler = joblib.load("model1.pkl", 'r')


# @app.route('/prediction', methods=['POST'])
# def prediction():

    # t_ = float(request.form['t'])
    # TM_ = float(request.form['tM'])
    # Tm_ = float(request.form['tm'])
    # SLP_ = float(request.form['slp'])
    # H_ = float(request.form['h'])
    # VV_ = float(request.form['vv'])
    # V_ = float(request.form['v'])
    # VM_ = float(request.form['vm'])
    # content = [[t_, TM_, Tm_, SLP_, H_, VV_, V_, VM_]]

    # """content['T'] = float(request.form['t'])
    # content['TM'] = float(request.form['tM'])
    # content['Tm'] = float(request.form['tm'])
    # content['SLP'] = float(request.form['slp'])
    # content['H'] = float(request.form['h'])
    # content['VV'] = float(request.form['vv'])
    # content['V'] = float(request.form['v'])
    # content['VM'] = float(request.form['vm'])"""
    # content = scaler.transform(content)
    # result = model.predict(content)[0][0]
    # return render_template('prediction.html', results=result)


if __name__ == '__main__':
    app.run(debug=True)