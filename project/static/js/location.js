
function roundToSix(num) {    
    return +(Math.round(num + "e+6")  + "e-6");
}

function enableButton(){
    $('#submit_button').prop("disabled", false);
    const button_name = $('#submit_button').attr("name");
    $('#submit_button').val(button_name);
    $('#id_address').keyup(disableButton);
}

function disableButton(){
  $('#submit_button').prop("disabled", true);
  $('#submit_button').val('Please Enter a Valid Location');
  $('#address_status').text('');
}

function addTimeChangeListeners(id){
  $("#id_" + id + "_time_hour").change(removeError);
  $("#id_" + id + "_time_minute").change(removeError);
  $("#id_" + id + "_time_meridiem").change(removeError);
}

function removeError(){
  $('.timeError').hide();
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
      enableButton();
    }
  
    function error() {
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
    address_el = $('#id_address');
    address = address_el.val();
    if (address != ''){
      $.ajax({
        url: '/ajax/check_address/',
        data: {
          'address': address
        },
        dataType: 'json',
        success: function (data) {
          console.log('got ajax response')
          if (data.lat) {
            $('#id_lat_coord').val(roundToSix(data.lat));
            $('#id_long_coord').val(roundToSix(data.long));
            enableButton();
          }
          $("#address_status").text(data.msg);
        }
      });
    }
}

function updateCategories(){
  var url = $("#search_form").attr("data-categories-url");  // get the url of the `load_categories` view
  var loc_type = $('#id_loc_type').val(); // get the selected location type from the HTML input
  var spin_loader = '<div id="spin_loader" class="d-flex justify-content-center">\
                      <div class="spinner-border" role="status">\
                        <span class="sr-only">Loading...</span>\
                      </div>\
                    </div>';
  $('#id_loc_category').prop("disabled", true);
  $('#id_loc_category').hide()
  $("#id_loc_category").before(spin_loader);
  disableButton();
  $.ajax({                       // initialize an AJAX request
    url: url,                    // set the url of the request
    data: {
      'loc_type': loc_type       // add the location type to the GET parameters
    },
    success: function (data) {   // `data` is the return of the `load_categories` view function
      $("#id_loc_category").html(data);  // replace the contents of the category input with the data that came from discovery
      $("#id_loc_category").prop("disabled", false);
      $("#id_loc_category").show();
      $("#spin_loader").remove();
      if($('#load_category').length){
        const category = $('#load_category').attr('data');
        $('#id_loc_category').val(category);
        $('#load_category').remove()
      }
      enableButton();
    }
  });
}

$('#currentLocationButton').click(currentLocation);
$('#id_address').change(checkAddress);
$('#id_address').keyup(function(event){
    if(event.keyCode === 13) {
        checkAddress();
    }
});
if($('#id_loc_type').length){
  $('#id_loc_type').change(updateCategories);
  if($('#id_loc_type').val().length > 0){
    updateCategories();
  } else {
    if ($('#id_address').val().length > 0){
        enableButton();
    }
  }
} else{
    if ($('#id_address').val().length > 0){
        enableButton();
    }
}
if($('.timeError').length){
  addTimeChangeListeners("start");
  addTimeChangeListeners("end");
}
