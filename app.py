from flask import *
import pandas as pd
from sklearn.linear_model import LinearRegression

app = flask(__name__)


@app.route('/')
def index():
  return render_template()







if __name__ == '__main__':
  app.run(debug = "true")