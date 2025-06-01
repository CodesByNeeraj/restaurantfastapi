function handleButton1Click(){
    var textbox1 = document.getElementById("textbox1"); //where the user inputs cuisine
    var span1 = document.getElementById("span1");  //display restaurant name and menu 
    
    //fetch to make HTTP requests (below is the api aka HTTP endpoint)
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

function run(){
    var button1 = document.getElementById("button1");
    button1.addEventListener("click",handleButton1Click);

}
document.addEventListener("DOMContentLoaded",run)