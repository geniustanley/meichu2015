var map;
var center = {
    lat: 24.787,
    lng: 120.995
};
var markers = [];
var mc;

function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
        center: center,
        zoom: 13
    });
}

function clearMarkers() {
	mc.clearMarkers();
}

function showMarkers(m) {
        mc = new MarkerClusterer(map, m);
}

