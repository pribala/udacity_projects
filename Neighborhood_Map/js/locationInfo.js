// View Definition

var Location = function(data) {
	this.title = ko.observable(data.title);
	this.loation = ko.observable(data.location);
	this.address = ko.observable(data.address);
	this.showLocation = ko.observable(true);
	this.marker = data.marker;
}

// View Model

var ViewModel = function(){
	var self = this;
	this.locationList = ko.observableArray([]);
	initialLocations.forEach(function(locationItem) {
		self.locationList.push(new Location(locationItem));
	});

	// Setting the current location to the selected list item.
	// On click event uses the Wiki Api to display relevant articles
	// for the selected location.
	// Set the toggleInfoWindow variable to false to indicate a list item has been clicked not a marker.
	this.currentLocation = ko.observable(this.locationList()[0]);
	this.setSelectedLocation = function(currentlocation) {
		self.currentLocation(currentlocation);
		self.currentLocation().marker.setAnimation(google.maps.Animation.BOUNCE);
		map.panTo(self.currentLocation().marker.position);
		toggleInfoWindow = false;
		loadData(self.currentLocation().marker);
	};

	// On selecting a different location from the list, set the animation of the current marker to null.
	this.changeMarker = function() {
			self.currentLocation().marker.setAnimation(null);
	};

	// Define a filter option for the location list.
	// Show and hide the location and its marker based on the filter.
	this.optionList = ko.observableArray([]);
	filters.forEach(function(filterOption) {
		self.optionList.push(filterOption);
	});
	this.selectedOption = ko.observable(self.optionList()[0]);
	this.filterLocation = ko.computed(function() {
		var placeList = self.locationList();
		for(var i=0;i<placeList.length;i++) {
			if (self.selectedOption() === 'None') {
				placeList[i].showLocation(true);
				placeList[i].marker.setVisible(true);
			} else if(self.selectedOption() !== placeList[i].address()){
				placeList[i].showLocation(false);
				placeList[i].marker.setVisible(false);
			} else {
				placeList[i].showLocation(true);
				placeList[i].marker.setVisible(true);
			}
		}
	});
}
