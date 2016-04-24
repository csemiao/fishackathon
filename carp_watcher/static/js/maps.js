/*
Author: alek
Purpose: Init map alongside points with back-end.
GET gets list.
*/

var map;


function setupMap() {
  var americaCenter, infoWindow;

  americaCenter = {lat: 39.5 , lng: -98.35};

  map = new google.maps.Map(document.getElementById('map'), {
    center: americaCenter,
    zoom: 4
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
  var marker, markerColor, position, greenMarker;
  greenMarker =  new google.maps.MarkerImage("http://maps.google.com/mapfiles/ms/icons/green-dot.png")

  if (info){
  for (var i =0; i < info.length; i++){
    position = {lat: parseInt(info[i].lat), lng: parseInt(info[i].lng)};
    marker = new google.maps.Marker({
    icon: greenMarker,
    map: map,
    position: position,
    title: info[i].name});
    setUpInfoWindow(info, i, marker);
    }
  }
}

function getMarkerData(){
  $.ajax({
    url:"/showall/",
    success: function( data ) {
      processData(data);  },
  error: function (data) {
    console.log(data);
    }
  });

}

function initMap() {
  var info;
  setupMap();
  getMarkerData();
};
