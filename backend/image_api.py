import requests
from dotenv import load_dotenv
import os


load_dotenv()


UNSPLASH_KEY = os.getenv("UNSPLASH_ACCESS_KEY")



def get_destination_images(city):


    url = "https://api.unsplash.com/search/photos"



    params = {

        "query": city + " travel",

        "client_id": UNSPLASH_KEY,

        "per_page": 5

    }




    response = requests.get(
        url,
        params=params
    )



    data = response.json()



    images = []



    if data.get("results"):


        for photo in data["results"]:


            images.append(
                photo["urls"]["regular"]
            )



    return images