
let Artister = [
    {Navn: "SZA",
     Alder: 30,
     ALbum:"SOS"
    },
    
    {Navn: "UNDERGRUNN",
     Alder: 18,
     Album: "EGOLAND"
    },
] 

for (let i = 0; i < Artister.length; i++ ){
    console.log(Artister[i].Navn)

    

    document.querySelector("#utskrift").innerHTML += Artister[i].Navn; 
} 