// Model Definition

// Defining an array of objects with location info.
var initialLocations = [
		{title: 'Statue Of Liberty', location: {lat: 40.6885884, lng: -74.0445316}, address: 'Downtown'},
		{title: 'Empire State Building', location: {lat: 40.748566, lng: -73.985785}, address: 'Midtown'},
		{title: 'World Trade Center', location: {lat: 40.7121288, lng: -74.01330639999999}, address: 'Downtown'},
		{title: 'Times Square, New York', location: {lat: 40.758895, lng: -73.985131}, address: 'Midtown'},
		{title: 'Brooklyn Bridge', location: {lat: 40.7060855, lng: -73.9968643}, address: 'Downtown'},
		{title: 'Metropolitan Museum of Art', location: {lat: 40.7791655, lng: -73.9629278}, address: 'Uptown'},
		{title: 'American Museum of Natural History', location:{lat: 40.7810311, lng: -73.9731034}, address: 'Uptown'}
	];

// Filter the location by the defined criteria
var filters = ['None', 'Downtown', 'Midtown', 'Uptown'];
