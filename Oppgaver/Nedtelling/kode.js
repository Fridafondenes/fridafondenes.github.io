let nedtelling = setInterval(tikk, 1000);

let antallSekunder = prompt("Hvor mange sekunder?");

let musikkFerdig = new Audio("jazz-happy-110855.mp3");

let musikkBakgrunn = new Audio("happy-day-113985 (1).mp3");



function tikk() {
    antallSekunder = antallSekunder - 1; //trekk fra en på antall sekunder
    console.log(antallSekunder); //skriv ut anntall gjennværende sekund
    document. getElementById("utskrift").innerText = antallSekunder;


    if (antallSekunder <=3) {
        document.getElementById("utskrift").style.color = "red";
    
    }
    
    
    if (antallSekunder <= 0) {
        document.getElementById("utskrift").innerText = "Gratulerer!";
        document.getElementById("utskrift").style.color = "green";
        musikkFerdig.play();
        musikkBakgrunn.pause();
        clearInterval(nedtelling);
    }

}   

document.body.addEventListener("click",spillMusikk);

function spillMusikk(){
    musikkBakgrunn.play();
}