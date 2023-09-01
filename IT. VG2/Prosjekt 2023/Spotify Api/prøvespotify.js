
//artist = prompt("Hva er din favorittartist?")

const options = {
	method: 'GET',
	headers: {
		'X-RapidAPI-Key': 'e872ef5656msh85919413c26c930p1999b2jsn2a57ccac8e61',
		'X-RapidAPI-Host': 'spotify81.p.rapidapi.com'
	}
};

fetch("https://spotify81.p.rapidapi.com/search?q=unnergrunn&type=multi&offset=0&limit=10&numberOfTopResults=5", options)
	.then(response => response.json())
	.then(response => behandleSvar(response))
	.catch(err => console.error(err));

	function behandleSvar(svar){

		console.log(svar)
	}