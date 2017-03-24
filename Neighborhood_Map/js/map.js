// Load  Map with 5 markers and infowindow when markers are clicked. 

var markers = [];
var map;
var marker;

function initMap() {
	map = new google.maps.Map(document.getElementById('map'), {
		center: {lat: 40.7413549, lng: -73.9980244},
		zoom: 13,
	});

	// Style the markers a bit. This will be our POI marker icon.
	// Creating a vector based image (Symbol) to be displayed on the marker.
	// Path defines the shape of the symbol
	var defaultIcon = {
			path: google.maps.SymbolPath.BACKWARD_CLOSED_ARROW,
			scale: 6,
			strokeColor: 'red',
			strokeWeight: 2,
		};

	var largeInfowindow = new google.maps.InfoWindow();
	var placeList = initialLocations;

	// The following group uses the location array to create an array of markers on initialize.
	for (var i = 0; i < placeList.length; i++) {
		// Get the position from the location array.
		var position = placeList[i].location;
		var title = placeList[i].title;
		// Create a marker per location, and put into markers array.
		var marker = new google.maps.Marker({
			map: map,
			position: position,
			title: title,
			animation: google.maps.Animation.DROP,
			icon: defaultIcon,
			id: i
		});

		// Create an onclick event to open an infowindow at each marker.
		marker.addListener('click', function() {
			populateInfoWindow(this, largeInfowindow);
		});

		// Two event listeners - one for mouseover, one for mouseout,
		// to toggle the bounce back and forth.
		marker.addListener('mouseover', function() {
			this.setAnimation(google.maps.Animation.BOUNCE);
		});

		marker.addListener('mouseout', function() {
			this.setAnimation(null);
		});


		// Push the marker to our array of markers.
		markers.push(marker);
		placeList[i].marker = marker;
	}

	ko.applyBindings(new ViewModel());
}

// This function populates the infowindow when the marker is clicked. We'll only allow
// one infowindow which will open at the marker that is clicked, and populate based
// on that markers position.
function populateInfoWindow(marker, infowindow) {
	// Check to make sure the infowindow is not already opened on this marker.
	if (infowindow.marker != marker) {
		// Clear the infowindow content to give the streetview time to load.
		infowindow.setContent('');
		infowindow.marker = marker;
		// Make sure the marker property is cleared if the infowindow is closed.
		infowindow.addListener('closeclick',function(){
			infowindow.setMarker = null;
		});
		var streetViewService = new google.maps.StreetViewService();
		var radius = 50;
		// In case the status is OK, which means the pano was found, compute the
		// position of the streetview image, then calculate the heading, then get a
		// panorama from that and set the options
		function getStreetView(data, status) {
			if (status == google.maps.StreetViewStatus.OK) {
				var nearStreetViewLocation = data.location.latLng;
				var heading = google.maps.geometry.spherical.computeHeading(
					nearStreetViewLocation, marker.position);
				infowindow.setContent('<div><strong>' + marker.title + '</strong></div><div id="pano"></div>');
				var panoramaOptions = {
					position: nearStreetViewLocation,
					pov: {
						heading: heading,
						pitch: 30
					}
				};
				var panWindow = document.getElementById('pano');
				panWindow.className = "pan-window";
				var panorama = new google.maps.StreetViewPanorama(
					document.getElementById('pano'), panoramaOptions);
			} else {
				infowindow.setContent('<div>' + marker.title + '</div>' +
					'<div>No Street View Found</div>');
			}
		}
		// Use streetview service to get the closest streetview image within
		// 50 meters of the markers position
		streetViewService.getPanoramaByLocation(marker.position, radius, getStreetView);
		// Open the infowindow on the correct marker.
		infowindow.open(map, marker);
	}
};

function displayWikiWindow(marker, articleStr) {
	var wikiInfoWindow = new google.maps.InfoWindow();
	if (wikiInfoWindow.marker != marker) {
		// Clear the infowindow content to give the streetview time to load.
		wikiInfoWindow.setContent('');
		wikiInfoWindow.marker = marker;
		// Make sure the marker property is cleared if the infowindow is closed.
		wikiInfoWindow.addListener('closeclick',function(){
			wikiInfoWindow.setMarker = null;
		});
		wikiInfoWindow.setContent('<div><strong>' + marker.title + '</strong>'+articleStr+'</div>');
		wikiInfoWindow.open(map, marker);
	}
};

// Display user friendly error message
function errorHandling() {
	alert('Google Maps failed to load.');
};