from flask import Flask, request, render_template, url_for
import numpy as np
import pandas as pd
import pickle
import umap.umap_ as umap
app=Flask(__name__)
model=pickle.load(open('clf77.pkl','rb'))
umap1=pickle.load(open('umap77.pkl','rb'))
@app.route('/')
def preprehome():
    return render_template('preprehome.html')
@app.route('/data')
def data():
    return render_template('data.html')

@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/contactus')
def contactus():
    return render_template('contactus.html')

@app.route('/prehome',methods=['POST'])
def prehome():
    return render_template('prehome.html')

@app.route('/bmipedigree',methods=['POST'])
def home():
    if request.method == 'POST':
        x1=request.form.get("parent-sibling")
        x1=float(x1)
        x2=request.form.get("grandparent-aunt-uncle")
        x2=float(x2)
        x3=request.form.get("first-cousin")
        x3=float(x3)
        x4=request.form.get("gender")
        x5=request.form.get("weight")
        x5=float(x5)
        x6=request.form.get("height")
        x6=float(x6)
        dpf = (0.5 * x1) + (0.25 * x2) + (0.125 * x3)
        if x1>0 and x2>0 and x3>0:
            dpf=dpf/(x1+x2+x3)
        else:
            dpf=0
        dpf = '{:.3f}'.format(dpf)
        bmi1 = x5 / (x6 * x6);
        bmi1=bmi1*10000
        bmi1 = '{:.1f}'.format(bmi1)
    return render_template('home.html',pedigree=dpf,bmi=bmi1,gender=x4)
@app.route('/predict',methods=['POST'])
def predict():
    feat=[]
    if request.method == 'POST':
        x=request.form.get("Pregnancies")
        feat.append(float(x))
        x=request.form.get("glucose")
        feat.append(float(x))
        x=request.form.get("Diabetes_Pedigree")
        feat.append(float(x))
        x=request.form.get("BMI")
        feat.append(float(x))
    k=np.array(feat).reshape(1,-1)
    pred=model.predict(umap1.transform(k))
    return render_template('res.html',prediction=pred)
if __name__=="__main__":
    app.run(debug=True)
    