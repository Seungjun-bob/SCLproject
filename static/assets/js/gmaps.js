var map;

function initMap() {
      var location = { lat: 37.501256, lng: 127.039581 };
      var map = new google.maps.Map(
        document.getElementById('map'), {
          zoom: 17,
          center: location
        });

      new google.maps.Marker({
        position: location,
        map: map,
        label: "멀티캠퍼스"
    });
}