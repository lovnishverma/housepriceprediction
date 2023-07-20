from flask import *
import pandas as pd
from sklearn.linear_model import LinearRegression

app = flask(__name__)


@app.route('/')
def index():
  return render_template('index.html')

@app.route('/predict')

def predict():
  BHK = eval(request.form.get("BHK"))
  Bathroom = eval(request.form.get("Bathroom"))
  Parking = eval(request.form.get("Parking"))
  Per_Sqft = eval(request.form.get("Per_Sqft"))
  Furnishing = eval(request.form.get("Furnishing"))
  
   return render_template('predict.html')

@app.route('/cp',methods = ['POST'])
def housepricepredict():
  
  BHK = eval(request.form.get("BHK"))
  Bathroom = eval(request.form.get("Bathroom"))
  Parking = eval(request.form.get("Parking"))
  Per_Sqft = eval(request.form.get("Per_Sqft"))
  Furnishing = eval(request.form.get("Furnishing"))
  
  url = "delhi property price for ml project1.csv"
  df = pd.read_csv(url)




if __name__ == '__main__':
  app.run(debug = "true")