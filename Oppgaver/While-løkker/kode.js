// Whilde-løkke
console.log("While-løkke:");

//let teller = 10; 
//while (teller > 0) { 
    //console.log(teller); 
    //teller = teller - 1; }

///let start = prompt

//Fore-løkke 
//console.log("For-løkke:")

//   Start     slutt   hopp
//for (let i =0; i < 10; i + 1){};

let arrayNavn = ["Frida Fondenes", "Frida Fonnes", "Fridus"];
console.log("Lengde på arryen: " + arrayNavn.length)
console.log(arrayNavn.length);
console.table(arrayNavn);
console.log(arrayNavn[1]);
arrayNavn[1] = "Fridusfridusfridus";
console.table(arrayNavn);

or (let i = 0; i < arrayNavn.length; i++ ) {
    console.log ("Element nr. " + i + " er: " + arrayNavn[i]);
}

//let navn = "Frida Marie Hannesdatter Fondenes";
//arrayNavn.puch(navn);


for (let navn of arrayNavn) {
    console.log(navn);
}
    
