var map = L.map('mapExitPoint', { zoomControl: false }).setView([51.505, -0.09], 13);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">HalfBrainCoders</a>'
}).addTo(map);

var marker
map.on('click', function (e) {
    let lat = e.latlng.lat;
    let lng = e.latlng.lng;

  if (marker) {
    map.removeLayer(marker);
  }
  marker = new L.Marker(e.latlng).addTo(map);
  document.getElementById('id_lon').value = lng;
  document.getElementById('id_lat').value = lat;
});

