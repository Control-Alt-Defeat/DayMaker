
function roundToSix(num) {    
    return +(Math.round(num + "e+6")  + "e-6");
}


function geoFindMe() {

    const lat_coord_input = document.querySelector('#id_lat_coord');
    const long_coord_input = document.querySelector('#id_long_coord');
  
    // mapLink.href = '';
    // mapLink.textContent = '';
  
    function success(position) {
      const latitude  = roundToSix(position.coords.latitude);
      const longitude = roundToSix(position.coords.longitude);
  
    //   status.textContent = '';
    //   mapLink.href = `https://www.openstreetmap.org/#map=18/${latitude}/${longitude}`;
    //   mapLink.textContent = `Latitude: ${latitude} °, Longitude: ${longitude} °`;
      alert(`Latitude: ${latitude} °, Longitude: ${longitude} °`);
      lat_coord_input.value = latitude
      long_coord_input.value = longitude
    }
  
    function error() {
      //status.textContent = 'Unable to retrieve your location';
      alert('Unable to retrieve your location');
    }
  
    if (!navigator.geolocation) {
      status.textContent = 'Geolocation is not supported by your browser';
    } else {
      status.textContent = 'Locating…';
      navigator.geolocation.getCurrentPosition(success, error);
    }
  
}

// function attachLocationButtonListener(){
//     document.querySelector('#currentLocationButton').addEventListener('click', geoFindMe);
// }

// attachLocationButtonListener()
document.querySelector('#currentLocationButton').addEventListener('click', geoFindMe);
