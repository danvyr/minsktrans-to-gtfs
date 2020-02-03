var map = L.map( 'map', {
  center: [53.9006, 27.5585], 
  minZoom: 6,
  zoom: 14
})

//var map = L.map('map').setView([53.9006, 27.5585], 14);

L.tileLayer( 'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>',
  subdomains: ['a', 'b', 'c']
}).addTo( map )

map.on('zoomend', onResize);
map.on('moveend', onResize);
map.on('load', onResize);




var myURL = jQuery( 'script[src$="stops.js"]' ).attr( 'src' ).replace( 'stops.js', '' )

var myIcon = L.icon({
  iconUrl: myURL + 'images/pin24.png',
  iconRetinaUrl: myURL + 'images/pin48.png',
  iconSize: [29, 24],
  iconAnchor: [9, 21],
  popupAnchor: [0, -14]
})


//stops
var markerGroup = L.layerGroup().addTo(map);

function onResize(){
	var bounds = map.getBounds();	
	markerGroup.clearLayers();
  
	for ( var i=0; i < stops.length; ++i ){
	
    var item1 =stops[i];
	
		var ltln = L.latLng(item1.lat, item1.lon);
		if (bounds.contains(ltln)){
		  L.marker( [item1.lat, item1.lon], {icon: myIcon} )
       .bindPopup( item1.name + '<br> <a href="http://www.minsktrans.by/city/#minsk/search;' 
                              + item1.id 
                              + '" target="_blank">' 
                              + item1.id + '</a> <br> MinskTransRef =' 
                              + item1.id )
			 .addTo( markerGroup );
		}
	}
}

onResize();
