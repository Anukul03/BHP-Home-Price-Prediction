from flask import Flask,Request,jsonify
import util

app = Flask(__name__)

@app.route('/get_location_names',methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations' : util.get_location_names()
    })

    response.headers.add('Access-Control-Allow-Origin','*')
    return response


@app.route('/predict_home_prices',methods=['GET','POST'])
def predict_home_prices():
    location = (Request.form['location'])
    total_sqft = float(Request.form['total_sqft'])
    bhk = int(Request.form['bhk'])
    bath = int(Request.form['bath'])

    response = jsonify({
        'estimated_price':util.get_estimated_price(location,total_sqft,bhk,bath)
    })

    response.headers.add('Access-Control-Allow-Origin','*')
    return response

if __name__=="__main__":
    print("starting python flask server for home price prediction")
    util.load_saved_artifacts()
app.run()