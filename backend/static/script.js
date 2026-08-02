async function generateTrip(){


    const city = document
    .getElementById("city")
    .value
    .trim();



    const loader =
    document.getElementById("loader");


    const result =
    document.getElementById("result");


    const gallery =
    document.getElementById("gallery");


    const weatherBox =
    document.getElementById("weather");




    if(city === ""){


        result.innerHTML = `

        <div class="card">

        ⚠️ Please enter a destination

        </div>

        `;

        return;

    }




    loader.style.display="block";


    result.innerHTML="";


    gallery.innerHTML="";


    if(weatherBox){

        weatherBox.innerHTML="";

    }







    try{


        const response = await fetch("/travel",{


            method:"POST",


            headers:{


                "Content-Type":"application/json"

            },


            body:JSON.stringify({

                city:city

            })


        });







        const data =
        await response.json();




        console.log(
            "Backend Response:",
            data
        );





        loader.style.display="none";





        if(data.error){

            throw new Error(data.error);

        }






        const trip =
        data.answer || {};



        const weather =
        data.weather || {};







        // =========================
        // IMAGE ALBUM
        // =========================


        let images = data.images || [];



        if(images.length === 0){


            images=[

            "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee"

            ];

        }






        gallery.innerHTML = images
        .slice(0,5)
        .map(img=>`

            <img

            src="${img}"

            alt="Travel Image"

            >

        `)
        .join("");









        // =========================
        // RESULT CARD
        // =========================



        result.innerHTML = `


        <div class="card">



        <h2>

        ${trip.destination || city}

        </h2>





        <button

        class="fav-btn"

        id="saveBtn">

        ❤️ Save Favourite

        </button>







        <div class="weather-card">


        <h3>

        🌦️ Weather

        </h3>



        <p>

        🌡️ Temperature:

        ${weather.temperature || "N/A"}

        °C

        </p>




        <p>

        ☁️ Condition:

        ${weather.condition || "N/A"}

        </p>




        <p>

        💧 Humidity:

        ${weather.humidity || "N/A"}

        %

        </p>




        <p>

        🌬️ Wind:

        ${weather.wind || "N/A"}

        m/s

        </p>



        </div>









        <div class="section">


        <h3>

        📅 Best Time

        </h3>


        <p>

        ${trip.best_time || "Not available"}

        </p>


        </div>









        <div class="section">


        <h3>

        📍 Attractions

        </h3>



        <ul>


        ${(trip.attractions || [])
        .map(place=>`

        <li>${place}</li>

        `)
        .join("")}


        </ul>


        </div>









        <div class="section">


        <h3>

        🍛 Foods

        </h3>



        <ul>


        ${(trip.foods || [])
        .map(food=>`

        <li>${food}</li>

        `)
        .join("")}



        </ul>


        </div>









        <div class="section">


        <h3>

        💡 Travel Tips

        </h3>



        <ul>


        ${(trip.tips || [])
        .map(tip=>`

        <li>${tip}</li>

        `)
        .join("")}



        </ul>


        </div>





        </div>



        `;








        // SAVE BUTTON


        document
        .getElementById("saveBtn")
        .onclick=function(){


            saveFavourite(
                trip.destination || city
            );


        };







    }



    catch(error){


        console.error(
            "ERROR:",
            error
        );



        loader.style.display="none";



        result.innerHTML = `


        <div class="card">


        ❌ ${error.message}


        </div>


        `;


    }


}









// =========================
// DARK MODE
// =========================


const themeButton =
document.getElementById("themeToggle");



if(themeButton){


themeButton.onclick=function(){


document.body
.classList
.toggle("dark");


};


}









// =========================
// MUSIC
// =========================


const musicButton =
document.getElementById("musicBtn");


const music =
document.getElementById("bgMusic");



if(musicButton && music){



musicButton.onclick=function(){



if(music.paused){


music.play()
.then(()=>{


this.innerHTML="🔊";


})
.catch(err=>{


console.log(
"Music error:",
err
);


});


}


else{


music.pause();


this.innerHTML="🎵";


}



};



}









// =========================
// SAVE FAVOURITES
// =========================


function saveFavourite(city){



let favourites =
JSON.parse(
localStorage.getItem("favourites")
)
|| [];





if(!favourites.includes(city)){


favourites.push(city);



localStorage.setItem(

"favourites",

JSON.stringify(favourites)

);



alert(
city+" added ❤️"
);



}

else{


alert(
"Already saved ❤️"
);


}



}









// =========================
// SHOW FAVOURITES
// =========================


const favBtn =
document.getElementById("favBtn");



if(favBtn){



favBtn.onclick=function(){



let favourites =
JSON.parse(

localStorage.getItem("favourites")

)
|| [];




if(favourites.length===0){


alert(
"No favourite destinations yet ❤️"
);


}

else{


alert(

"❤️ Favourite Destinations\n\n"
+
favourites.join("\n")

);


}



};



}