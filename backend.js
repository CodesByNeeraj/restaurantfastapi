function handleButton1Click(){
    var textbox1 = document.getElementById("textbox1"); //where the user inputs cuisine
    var span1 = document.getElementById("span1");  //display restaurant name and menu 
    
    //fetch to make HTTP requests (below is the api aka HTTP endpoint)
    //fetch is an api and replacement to xmlhttprequest
    //the response is returned by the python fastapi backend. the response is json string
    //we turn that json string into a javascript object
    fetch("http://127.0.0.1:8000/restaurant",{
        method: "POST", //post means sending data over to the server. we are sending user input over to the backend
        headers: {
            "Content-Type": "application/json" //application/json means that the data we are sending is in json format

        },
        body: JSON.stringify({cuisine: textbox1.value}) //converts the javascript object({cuisine:...)}) into a JSON string to send over the network. body of HTTP requests expects a string 

    })
    .then(response => response.json()) //fetch returns a promise. so when the server replies, convert the response body from JSON text into a JavaScript object
    .then(data=>{ //data is the javascript object that we got from the server after parsing JSON
        //backtick `
        //strong means bold
        span1.innerHTML= ` 
        <strong>Name:</strong> ${data.name}<br/>
        <strong>Menu</strong> ${data.menu_items}
        `;
    })
    .catch(error=>{
        span1.innerHTML = "Oops, an error!"
        console.error(error);
    })
    
}

function handlebutton2click(){
    var span2 = document.getElementById("span2")
    //sends a http request to backend fastapi server
    //server responds with whats stored in sqlite database in json format
    //.map: loops through each entry in the array and html string is created for each one of them
    //.join joins the html strings with line breaks in between 
    fetch("http://127.0.0.1:8000/history",{
        method:"GET"
    })
    .then(response=>response.json())
    .then(data=>{
        if (data.length === 0){
            span2.innerHTML = "No past ideas found."
            return;
        }
        //using .map() to loop through the array
        span2.innerHTML = data.map(entry=>`
            <div>
                <strong>${entry.name}</strong> (${entry.cuisine}):
                ${entry.menu_items}
            </div>
        `).join("<br>");
    })
    .catch(error=>{
        span2.innerHTML = "failed to load history"
        console.error(error)

    });        
    
}

function run(){
    var button1 = document.getElementById("button1");
    button1.addEventListener("click",handleButton1Click);
    button2.addEventListener("click",handlebutton2click);

}
document.addEventListener("DOMContentLoaded",run)