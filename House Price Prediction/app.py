import flask
import pickle
import numpy as np
from flask import Flask, request, jsonify, url_for, render_template, app
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load the Model
pickle_reg_model = pickle.load(open('regmodel.pkl', 'rb'))
scalar = pickle.load(open('scaling.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('home.html')


# Route for making request on postman for prediction of JSON data
@app.route('/reg_predict_api', methods=['POST'])
def reg_predict_api():
    data = request.json['data']
    # print(data)
    print(np.array(list(data.values())).reshape(1, -1))
    new_data = scalar.transform(np.array(list(data.values())).reshape(1, -1))
    output = pickle_reg_model.predict(new_data)
    print(output[0])
    return jsonify(output[0])


# Route to create web app request to get data from the html page:
@app.route('/predict', methods=['POST'])
def predict():
    data=[float(x) for x in request.form.values()]
    final_input=scalar.transform(np.array(data).reshape(1,-1))
    print(final_input)
    output=pickle_reg_model.predict(final_input)[0]
    return render_template("home.html", prediction_text="The House price prediction is ${} K".format(output))


if __name__ == "__main__":
    app.run(debug=True, port=5000)
