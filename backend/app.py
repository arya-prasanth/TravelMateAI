from flask import Flask, render_template, request, jsonify

from groq_client import get_travel_guide
from image_api import get_destination_images
from weather_api import get_weather


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")



@app.route("/travel", methods=["POST"])
def travel():

    try:

        data = request.get_json()

        if not data:
            return jsonify({
                "error":"Invalid request"
            }),400


        city = data.get("city","").strip()


        if city == "":
            return jsonify({
                "error":"Please enter a destination"
            }),400



        guide = get_travel_guide(city)


        images = get_destination_images(city)


        weather = get_weather(city)



        return jsonify({

            "answer":guide,

            "images":images,

            "weather":weather

        })



    except Exception as e:

        print("ERROR:",e)

        return jsonify({

            "error":str(e)

        }),500




if __name__=="__main__":

    app.run(debug=True)