import pandas as pd 
from flask import Flask,request,jsonify 

app=Flask(__name__)

file=pd.read_csv("check_in_data.csv")
    
file2=file.to_dict(orient='records')
@app.route("/api")
def PutAPI():
    return jsonify(file2),200
if __name__=="__main__":
    app.run(debug=True)