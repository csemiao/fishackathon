/*
Author: alek
Purpose: Init map alongside points with back-end.
GET gets list.
*/

var map;

var data = [ {
  name: 'Point Grey River',
  lat: '49.1320129',
  lng: '-123.1',
  suitable: 'major'
},
{
name: 'A Grey River',
lat: '50.11',
lng: '-119.57',
suitable: 'minor'
},
{
name: 'Some Grey River',
lat: '54.2',
lng: '-115.73',
suitable: 'invalid'

},
{
name: 'lol a Grey River',
lat: '52.71',
lng: '-113.43',
suitable: 'major'

},
{
name: 'i wont swim and hate Grey Rivers',
lat: '49.1320129',
lng: '-123.1',
suitable: 'minor'

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

function setInfoWindowMarkup () {
  var html;
  html = '<div class = "cw-flow-status"> Hi this is my flow status'
        +'<div class="cw-graph">graph goes here. scale size as necessary</div>'
        + '</div>'
  return html;
}


function setUpInfoWindow (info, i, marker) {
  var infowindow = new google.maps.InfoWindow({
    content: setInfoWindowMarkup()
  });
  marker.addListener('click',function(){
    infowindow.open(map, marker);
  });
};

function processData(info){
  var marker, markerColor, position, greenMarker, icon;
  greenMarker =  new google.maps.MarkerImage("http://maps.google.com/mapfiles/ms/icons/green-dot.png")

  if (info){
  for (var i =0; i < info.length; i++){
    position = {lat: parseInt(info[i].lat), lng: parseInt(info[i].lng)};
    marker = new google.maps.Marker({
    icon: greenMarker,
    map: map,
    position: position,
    title: info[i].name});
    // setupInfoWindow will need to be passed the suitable status in text.
    setUpInfoWindow(info, i, marker);
    }
  }
}
function handleGetMarkerDataSuccess (response) {
  alert('success');
}
function handleGetMarkerDataError(error){
  alert('error!');
}

function getMarkerData(){
  $.ajax({
    url: "/showall/",
    type: "get", //send it through get method
    success: handleGetMarkerDataSuccess(response),
    error: handleGetMarkerDataError(error)
  });
}

function initMap() {
  var info;
  setupMap();
  // GET request.
//  info = getMarkerData();
  info = data;
  processData(info);
};
