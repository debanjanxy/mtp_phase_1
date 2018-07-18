//Main function
function initAutocomplete() {
  var map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: 19.397, lng: 76.644},
    zoom: 19,
    mapTypeId: google.maps.MapTypeId.SATELLITE
  });

  // Create the search box and link it to the UI element.
  var input = document.getElementById('pac-input');
  var searchBox = new google.maps.places.SearchBox(input);
  //   map.controls[google.maps.ControlPosition.TOP_LEFT].push(input);

  // Bias the SearchBox results towards current map's viewport.
  map.addListener('bounds_changed', function() {
    searchBox.setBounds(map.getBounds());
  });

  var geocoder = new google.maps.Geocoder();

  document.getElementById('submit').addEventListener('click', function() {
    geocodeAddress(geocoder, map);
  });

  document.getElementById('screenshot').addEventListener('click',function(){
    takeScreenshot(map);
    //processImage();
  });
}

//Utility functions

      function geocodeAddress(geocoder, resultsMap) {
        var address = document.getElementById('pac-input').value;
        geocoder.geocode({'address': address}, function(results, status) {
          if (status === 'OK') {
            resultsMap.setCenter(results[0].geometry.location);
            var marker = new google.maps.Marker({
              map: resultsMap,
              position: results[0].geometry.location
            });
          } else {
            alert("Please type the name of the place!");
          }
        });
      }

      function takeScreenshot(map){
         html2canvas(document.getElementById('map'),{
            dpi: 192,
            useCORS: true,
            allowTaint: false,
         }).then(function(canvas){
            var img = canvas.toDataURL("image/png");
            // console.log(img.length);
            var a = document.createElement('a');

            a.href = canvas.toDataURL("image/png");
            // console.log("Hello = "+a)
            a.download = 'map_image.png';

            // get this image and process it with the loaded model
            a.click();
         });
      }
