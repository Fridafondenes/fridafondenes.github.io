

const options = {
	method: 'GET',
	headers: {
		'X-RapidAPI-Key': 'e872ef5656msh85919413c26c930p1999b2jsn2a57ccac8e61',
		'X-RapidAPI-Host': 'spotify81.p.rapidapi.com'
	}
};

fetch("https://spotify81.p.rapidapi.com/search?q=Broiler&type=multi&offset=0&limit=10&numberOfTopResults=5", options)
	.then(response => response.json())
	.then(response => behandleSvar(response))
	.catch(err => console.error(err));


function behandleSvar(svar){

  console.log(svar)
  console.log("Tester enkeltutskrifter...");
  console.log("Navn: " + svar.artists.items[0].data.profile.name);
  console.log("Bilde: " + svar.artists.items[0].data.visuals.avatarImage.sources[0].url);
  console.log("topAlbum: " + svar.albums.items[0].data.name);
  console.log("Albumcov: " + svar.albums.items[0].data.coverArt.sources[0].url);
  console.log("Albumuri: " + svar.albums.items[0].data.uri);
  
  // for (let i = 0; i < svar.artists.items.length; ) {
     
    
  //   let navn = document.createElement("h1");
  //   navn.innerText = svar.artists.items[i].data.profile.name; 
  //   let bilde = document.createElement("img");
  //   bilde.src = svar.artists.items[i].data.visuals.avatarImage.sources[i].url;

  //   let topAlbum = document.createElement("h2");
  //   topAlbum.innerText = svar.albums.items[i].data.name;

  //   let Albumcov = document.createElement("img");
  //   Albumcov.src = svar.albums.items[i].data.coverArt.sources[i].url;

  //   let Albumuri = document.createElement("h2");
  //   Albumuri.innerText = svar.albums.items[i].data.uri;
        
  //   document.querySelector("#utskrifth1").appendChild(navn); 
  //   document.querySelector("#utskriftBilde").appendChild(bilde);
  //   document.querySelector("#utskriftALbumNavn").appendChild(topAlbum);
  //   document.querySelector("#utskriftAlbumBilde").appendChild(Albumcov);
  //   document.querySelector("#utskriftSpotify").appendChild(Albumuri);

  // }
  function displayArtistDetails() {

    let i = 0

    let navn = document.createElement("h1");
    navn.innerText = svar.artists.items[i].data.profile.name; 
    let bilde = document.createElement("img");
    bilde.src = svar.artists.items[i].data.visuals.avatarImage.sources[i].url;

    let AlbumNavn = document.createElement("h2");
    AlbumNavn.innerText = svar.albums.items[i].data.name;

    let AlbumBilde = document.createElement("img");
    AlbumBilde.src = svar.albums.items[i].data.coverArt.sources[i].url;

    let Spotify = document.createElement("h2");
    Spotify.innerText = svar.albums.items[i].data.uri;
        
    document.querySelector("#utskrifth1").appendChild(navn); 
    document.querySelector("#utskriftBilde").appendChild(bilde);
    document.querySelector("#utskriftAlbumNavn").appendChild(AlbumNavn);
    document.querySelector("#utskriftAlbumBilde").appendChild(AlbumBilde);
    document.querySelector("#utskriftSpotify").appendChild(Spotify);
  }

  displayArtistDetails();
}
