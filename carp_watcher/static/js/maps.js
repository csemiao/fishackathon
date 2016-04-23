/*
Author: alek
Purpose: Init map alongside points with back-end.
GET gets list.
*/
var map;
/*var blueMarker = new google.maps.MarkerImage("http://maps.google.com/mapfiles/ms/icons/blue-dot.png")
var yellowMarker = new google.maps.MarkerImage("http://maps.google.com/mapfiles/ms/icons/yellow-dot.png")
var redMarker = new google.maps.MarkerImage("http://maps.google.com/mapfiles/ms/icons/red-dot.png")
var orangeMarker = new google.maps.MarkerImage("http://maps.google.com/mapfiles/ms/icons/orange-dot.png")
var greenMarker = new google.maps.MarkerImage("http://maps.google.com/mapfiles/ms/icons/green-dot.png")
*/

var data = [ {
  name: 'Point Grey River',
  lat: '49.1320129',
  lng: '-123.1',
},
{
name: 'A Grey River',
lat: '50.11',
lng: '-119.57',
},
{
name: 'Some Grey River',
lat: '54.2',
lng: '-115.73',
},
{
name: 'lol a Grey River',
lat: '52.71',
lng: '-113.43',
},
{
name: 'i wont swim and hate Grey Rivers',
lat: '49.1320129',
lng: '-123.1',
},
]

function setupMap() {
  var americaCenter, infoWindow;

  americaCenter = {lat: 39.5 , lng: -98.35};

  map = new google.maps.Map(document.getElementById('map'), {
    center: americaCenter,
    zoom: 3
  });

}

function processData(info){
  var marker, markerColor, blueMarker, yellowMarker, redMArker, orangeMarker, greenMarker, position;

  if (info){ // if we have info to parse
  for (var i =0; i < info.length; i++){
    // lat lng,
    position = {lat: parseInt(info[i].lat), lng: parseInt(info[i].lng)};
    marker = new google.maps.Marker({
    icon:  markerColor,
    map: map,
    position: position,
    title: info[i].name});
    var infowindow = new google.maps.InfoWindow({
      content: info[i].name
    });
    marker.addListener('click',function(){
      infowindow.open(map, marker);
    })
    }
  }
}

function initMap() {
  setupMap();
  var info = data;
  processData(info);
    // init Map needs to make a GET request.
    // init Map needs to setup the map.
    // init Map then needs to process the information.
    // init Map then needs to plot the points.
};
