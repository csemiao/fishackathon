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

function parseStatus(status){
    if (status == 0) {
        return "Not suitable for spawning";
    } else if (status == 1) {
        return "Minimally suitable for spawning";
    } else if (status == 2) {
        return "Suitable for spawning";
    } else if (status == 3) {
        return "Very suitable for spawning";
    } else if (status == 4) {
        return "Highly suitable for spawning";
    }
}

function setInfoWindowMarkup (streamName, statusText) {
  var html;
  html = '<div class = "cw-flow-status"><b>'
          + streamName + '</b><br>'
          + statusText + '<br>'
        + '</div>'
    + '<div class="link-container">'
      + '<a target="_blank" href="/static/graph.html">Show Graph</a>'
    + '</div>';
    
  return html;
}


function setUpInfoWindow (info, i, marker) {
    var streamData = info[i];
    console.log(streamData);
  var infowindow = new google.maps.InfoWindow({
    content: setInfoWindowMarkup(streamData.name, parseStatus(streamData.status))
  });
  marker.addListener('click',function(){
    infowindow.open(map, marker);
    //getStreamData(streamData.name);
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
