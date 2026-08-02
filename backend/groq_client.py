from groq import Groq
from dotenv import load_dotenv
import os
import json


load_dotenv()


api_key = os.getenv("GROQ_API_KEY")


if not api_key:
    raise ValueError("GROQ_API_KEY is missing in .env file")



client = Groq(
    api_key=api_key
)



def get_travel_guide(city):


    response = client.chat.completions.create(

        model="llama-3.3-70b-versatile",


        messages=[


            {
                "role":"system",

                "content":"""

You are a professional travel assistant.

Return ONLY valid JSON.

No markdown.
No explanations.
No extra text.

Use this exact format:

{
 "destination":"",
 "best_time":"",
 "attractions":[
    "",
    "",
    ""
 ],
 "foods":[
    "",
    "",
    ""
 ],
 "tips":[
    "",
    "",
    ""
 ]
}

"""
            },


            {
                "role":"user",

                "content":f"Create a travel guide for {city}"

            }


        ]

    )



    content = response.choices[0].message.content.strip()



    print("\nRAW AI RESPONSE:")
    print(content)



    # Remove markdown formatting if AI adds it

    if "```" in content:


        content = content.replace("```json","")

        content = content.replace("```","")

        content = content.strip()




    try:

        guide = json.loads(content)

        return guide


    except json.JSONDecodeError:


        return {

            "destination": city,

            "best_time":"Not available",

            "attractions":[

                "Unable to generate attractions"

            ],

            "foods":[

                "Unable to generate foods"

            ],

            "tips":[

                content

            ]

        }