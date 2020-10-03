from flask import Flask, request, jsonify, render_template
from severity_predictor import model
import pandas as pd


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

# for more pages


@app.route('/pred/')
def sever():
    return render_template('severity.html')


@app.route('/predict', methods=['POST'])
def predict():

    data = request.form['sev']

    output = model.predict(data)
    # call function

    return render_template('index.html', prediction_text='. {}'.format(output[0]), prediction_text2='. {}'.format(output[1]),
                           prediction_text3='. {}'.format(output[2]), prediction_text4='. {}'.format(output[3]), prediction_text5='. {}'.format(output[4]),
                           message='Your accident has been predicited to be a stage', pred=output, one=1, two=2, three=3, four=4, five=5)


# distracted driver

@app.route('/distracted/')
def distr():
    return render_template('distracted.html')


@app.route('/classify', methods=['POST'])
def classify():

    data = request.form['distracted']

    output = model.predict(data)
    # call function

    return render_template('index.html', prediction_text='. {}'.format(output[0]), prediction_text2='. {}'.format(output[1]),
                           prediction_text3='. {}'.format(output[2]), prediction_text4='. {}'.format(output[3]), prediction_text5='. {}'.format(output[4]),
                           message='The driver is ', pred=output, one=1, two=2, three=3, four=4, five=5)


if __name__ == "__main__":
    app.run(debug=True)
