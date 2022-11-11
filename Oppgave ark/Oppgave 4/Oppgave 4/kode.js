const utskrift = document.getElementById("utskrift")
// utskfrift.innerTexst = "test";
// console.log(utskrift;

const språk = navigator.language;
console.log("Nettlleser: " + språk);
if (språk === "NO" || språk === "nb-NO") {
    console.log("Du har norsk språk i nettleseren.")
} else if (språk === "en-GB") {
    console.log("Brittisk")
}
else {
    console.log("Du har et annet språk..")
}

const plattform = navigator.platform;
console.log("Plattform: " + plattform); 

const nettleser = navigator.userAgent;
console.log("Nettleser: " + nettleser);
if (nettleser.includes ("x64")) {
    console.log("Du sitter på et 64-bits oprativsystem.");
} else {
    console.log("Du har 32-bit");
}

let hoyde = window.innerHeight;
console.log("Høyde: " + hoyde);
let hoydeScreen = screen.height;
console.log("Høyde (screen): " + bredde);
let bredde = window.innerWidth;
console.log("Bredde: " + bredde);
let breddeScreen = screen.width;
console.log("Bredde (screen): " + breddeScreen);

// Hent ut geolokasjon, kjelde: https://www.w3schools.com/html/html5_geolocation.asp
function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);
    } else { 
        utskrift.innerHTML = "Geolocation is not supported by this browser.";
    }
}

function showPosition(position) {
    utskrift.innerHTML = "Latitude: " + position.coords.latitude + "<br>Longitude: " + position.coords.longitude;
}

getLocation();

// Temp, test
// let listeParagrafer = document.querySelectorAll(".test, h1");
// console.log(listeParagrafer);
// for(let element of listeParagrafer) {
//     element.style.backgroundColor = "red";
// }