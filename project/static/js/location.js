
function roundToSix(num) {    
    return +(Math.round(num + "e+6")  + "e-6");
}

function disableButton(){
  $('#submit_button').prop("disabled", true);
  $('#submit_button').val('Please Enter a Valid Location');
  $('#address_status').text('');
}

function currentLocation() {

    address = $('#id_address');

    function success(position) {
      const latitude  = roundToSix(position.coords.latitude);
      const longitude = roundToSix(position.coords.longitude);
  
      address.val(`Latitude: ${latitude}°, Longitude: ${longitude}°`);
      $("#address_status").text("Valid Location!");
      $('#id_lat_coord').val(latitude);
      $('#id_long_coord').val(longitude);
      $('#submit_button').prop("disabled", false);
      const button_name = $('#submit_button').attr("name");
      $('#submit_button').val(button_name);
      address.keyup(disableButton)
    }
  
    function error() {
      //status.textContent = 'Unable to retrieve your location';
      $("#address_status").text('Unable to retrieve your location, try again or enter an address');
    }
  
    if (!navigator.geolocation) {
      $("#address_status").text('Geolocation is not supported by your browser. Try typing a location.');
    } else {
      $("#address_status").text('Locating…');
      navigator.geolocation.getCurrentPosition(success, error);
    }
  
}

function checkAddress(){
    address = $('#id_address');
    $.ajax({
      url: '/ajax/check_address/',
      data: {
        'address': address.val()
      },
      dataType: 'json',
      success: function (data) {
        if (data.lat) {
          // alert(`Latitude: ${data.lat}°, Longitude: ${data.long}°`);
          $('#id_lat_coord').val(roundToSix(data.lat));
          $('#id_long_coord').val(roundToSix(data.long));
          $('#submit_button').prop("disabled", false);
          const button_name = $('#submit_button').attr("name");
          $('#submit_button').val(button_name);
          address.keyup(disableButton)
        }
        $("#address_status").text(data.msg);
      }
    });
}

$('#currentLocationButton').click(currentLocation)
$('#checkAddressButton').click(checkAddress)
