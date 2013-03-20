function initialize() {
	console.log("Loading map for latitiude"+latitude+" and longitude "+longitude);
	var myLatlng = new google.maps.LatLng(latitude, longitude);
  var mapOptions = {
    zoom: 18,
    center: myLatlng,
    mapTypeId: google.maps.MapTypeId.ROADMAP
  };
  var map = new google.maps.Map(document.getElementById("map-canvas"), mapOptions);
   var marker = new google.maps.Marker({
            position: myLatlng,
            map: map,
            title: 'Destination'
        });
}

function loadScript() {
  var script = document.createElement("script");
  script.type = "text/javascript";
  script.src = "http://maps.googleapis.com/maps/api/js?key=AIzaSyCOJ5S_k0sX15MpJXf4ZJSdYT3uwG1QUrg&sensor=true&callback=initialize";
  document.body.appendChild(script);
}

