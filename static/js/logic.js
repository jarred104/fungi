API_KEY = "pk.eyJ1IjoiamFycmVkMTA0IiwiYSI6ImNrMHlrdGQ1ZDAxbWQzaW45NHlzeDR1cm8ifQ.rbjD9XrfyhsMDeD_tVI2kQ"

// #mapid { height: 250px; }

var mymap = L.map('mapid').setView([51.505, -0.09], 13);

L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
	attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
	maxZoom: 18,
	id: 'mapbox.streets',
	accessToken: API_KEY
}).addTo(mymap);



