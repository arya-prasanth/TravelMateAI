import requests
import os
from dotenv import load_dotenv


# Load .env file
load_dotenv()


# Get API key
WEATHER_KEY = os.getenv("WEATHER_API_KEY")



def get_weather(city):


    # Check API key

    if not WEATHER_KEY:

        print("❌ WEATHER_API_KEY missing")

        return {

            "temperature": "N/A",

            "condition": "API Key Missing",

            "humidity": "N/A",

            "wind": "N/A"

        }





    url = "https://api.openweathermap.org/data/2.5/weather"



    params = {

        "q": city,

        "appid": WEATHER_KEY,

        "units": "metric"

    }




    try:


        response = requests.get(

            url,

            params=params,

            timeout=10

        )



        data = response.json()



        print("\nWEATHER RESPONSE:")
        print(data)




        # Successful response

        if response.status_code == 200:



            return {


                "temperature":

                round(data["main"]["temp"],1),



                "condition":

                data["weather"][0]["description"].title(),



                "humidity":

                data["main"]["humidity"],



                "wind":

                data["wind"]["speed"]


            }





        # Invalid API key

        elif response.status_code == 401:


            return {


                "temperature":"N/A",

                "condition":

                "Invalid API Key",

                "humidity":"N/A",

                "wind":"N/A"


            }





        # City not found

        elif response.status_code == 404:


            return {


                "temperature":"N/A",

                "condition":

                "City not found",

                "humidity":"N/A",

                "wind":"N/A"


            }





        else:


            return {


                "temperature":"N/A",

                "condition":

                data.get(
                    "message",
                    "Weather unavailable"
                ),

                "humidity":"N/A",

                "wind":"N/A"


            }





    except requests.exceptions.Timeout:


        return {


            "temperature":"N/A",

            "condition":"Weather server timeout",

            "humidity":"N/A",

            "wind":"N/A"


        }





    except Exception as e:


        print("WEATHER ERROR:",e)



        return {


            "temperature":"N/A",

            "condition":"Weather error",

            "humidity":"N/A",

            "wind":"N/A"


        }