# importing the libraries
from flask import Flask,render_template,request
from Scraping import stockdata
from TableData import stock_table_data
import pandas as pd
import numpy as np


#Global variables

app=Flask(__name__)

# temp = stockdata(['AAPL','META'])
# print(temp)
#user defined routes


@app.route("/", methods=["GET" ,"POST" ])
def home1():   
    
    context,tablehead =  stock_table_data()
    return render_template('base.html',context=context,tablehead = tablehead)



@app.route("/index",methods=['GET','POST'])
def home():
    global code 
    if request.method == "POST":
        code =request.form['code']
     
        if code is None or code == "":
            code = ['AAPL']

    temp =[code]
    # temp = ['AAPL','META']
    context,tablehead = stockdata(temp)

    return render_template('index1.html',context=context,tablehead = tablehead)
   
   
# @app.route("/prediction",methods=['GET','POST'])
# def predict():
#     output = pre(list(df['text']))
#     df['ouput'] = output
#     context = df
#     return render_template('prediction.html',tables=context)



if __name__ =='__main__':
    app.run(debug=True)       


