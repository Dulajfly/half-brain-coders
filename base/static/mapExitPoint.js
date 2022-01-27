

x = '/pl/api/exitpoint/'
fetch(x)
  .then(response => response.json())
  .then(data => showMarkers(data))

const showMarkers =(data)=>{
    for(var i=0; i<data.length; i++){
        marker = new L.marker([data[i][1]])
    }
}







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




const id_name = document.getElementById('id_name');
const id_tracking_difficulty_level = document.getElementById('id_tracking_difficulty_level');
const id_wingsuit_difficulty_level = document.getElementById('id_wingsuit_difficulty_level');
const id_rock_drop_second = document.getElementById('id_rock_drop_second');
const id_rock_drop_altitude = document.getElementById('id_rock_drop_altitude');
const id_landing_altitude = document.getElementById('id_landing_altitude');
const id_lon = document.getElementById('id_lon');
const id_lat = document.getElementById('id_lat');
console.log(id_name)
id_name.classList.add('form-control')
id_tracking_difficulty_level.classList.add('form-control')
id_wingsuit_difficulty_level.classList.add('form-control')
id_rock_drop_second.classList.add('form-control')
id_rock_drop_altitude.classList.add('form-control')
id_lon.classList.add('form-control')
id_landing_altitude.classList.add('form-control')
id_lat.classList.add('form-control')