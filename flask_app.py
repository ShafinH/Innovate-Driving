from flask import Flask, request, jsonify, render_template
from severity_predictor import model
import pandas as pd


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

# for more pages


@app.route('/pred/')
def rec():
    return render_template('severity.html')


@app.route('/recommend', methods=['POST'])
def recommend():

    data = request.form['sev']

    output = model.predict(data)
    # call function

    return render_template('index.html', prediction_text='. {}'.format(output[0]), prediction_text2='. {}'.format(output[1]),
                           prediction_text3='. {}'.format(output[2]), prediction_text4='. {}'.format(output[3]), prediction_text5='. {}'.format(output[4]),
                           message='Your accident has been predicited to be a stage', pred=output, one=1, two=2, three=3, four=4, five=5)


if __name__ == "__main__":
    app.run(debug=True)
