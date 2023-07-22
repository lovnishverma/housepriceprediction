from flask import Flask, render_template, request
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")
  
@app.route('/form')
def form():
    return render_template("predict.html")


@app.route("/predict", methods=["POST"])
def predict():
  
  BHK = eval(request.form.get("BHK"))
  Bathroom = eval(request.form.get("Bathroom"))
  Parking = eval(request.form.get("Parking"))
  Per_Sqft = eval(request.form.get("Per_Sqft"))
  Furnishing = eval(request.form.get("Furnishing"))
  
  url = "delhi_house_price_ML.csv"
  data = pd.read_csv(url)
  X = data.drop(['id', 'Price'], axis='columns')
  y = data["Price"]
  
  model = RandomForestRegressor()
  model.fit(X,y)
  
  newdata = model.predict([[BHK, Bathroom, Parking, Per_Sqft, Furnishing]])
  
  return render_template("predict.html", data1 = newdata[0])


if __name__ == '__main__':
    app.run(debug=True)
