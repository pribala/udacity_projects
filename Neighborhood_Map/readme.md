# Neighborhood Map Project

This project is a single page application featuring a map of New York City with seven of the prominent New York
landmarks highlighted. The application utilizes the Google Maps API for displaying a fullscreen map and the 
MediaWiki API to provide unique information for the highlighted locations.  All data APIs used in the project 
load asynchronously. 
The application displays a list view of the set of highlighted locations and provides a filter option that uses 
a dropdown list to filter both the list view and the map markers displayed by default on load. 
The Knockout framework is used to handle the list and filter option and the code adheres to a MVVM pattern. 
The template uses HTML with CSS for styling.

### Installation

Clone this repository using:

git clone https://github.com/pribala/udacity_projects.git

### App Functionality

The application features a fullscreen map of New York City with seven highlighted locations. A list view displays 
the locations and a dropdown list provides the user options to filter the displayed locations. 
The user can choose to view landmarks either in Uptown, Downtown or Midtown New York. All locations and map
markers are displayed by default.
Selecting a filter option filters the locations in the list view and on the map and displays the filtered subset 
of location and map markers when a filter is applied. Clicking a location on the list displays unique information 
about the location, and animates its associated map marker causing it to bounce. The MediaWiki API is used to provide
unique data as a list of Wiki articles pertaining to the location using an Ajax call. 
Clicking a marker displays a street view panaroma for that location in an infoWindow using Google Map Api's Street
View Service. When a marker has focus it bounces.

### APIs and MVVM pattern

The application relies on Google Maps API for the map functionality and data. 
The MediaWiki API is used to provide unique data for the locations. 
All data requests are retrieved in an asynchronous manner.
Code is separated based upon Knockout Framework and follows an MVVM pattern and avoids updating the DOM manually with 
jQuery or JS with the use of observables, observable arrays, computed observables.
Knockout is used to implement dynamic UI update to create a rich and responsive display.

### What's Included

Within the repo you'll find the following directories and files:

  * Neighborhood_Map 
      * index.html - this file is the main template file that defines the structure of the page and links to the script and 
	  css files.
  * /js 
      * model.js - defines the model data for the application. 
	  * locationInfo.js - defines the view and model view for the application.
	  * map.js - handles the map functionality using Google Maps API.
	  * wiki.js - loads Wikipedia API info specific to a location. Uses JQuery.ajax() to perform an asynchronous HTTP (Ajax) request.
  * /css 
      * main.css - styles for the html template.
      * under365.css - styles for smaller screen sizes.
      * under450.css - styles for smaller screen sizes.
	  * under650.css - styles for smaller screen sizes.

### Instructions to run the application:

To start the application run the index.html from any browser.

### Reference:
  * Udacity's Intro to AJAX course
  * Udacity's JavaScript Design Patterns course
  * Udacity's Google Maps API course
  * Google Maps API Documentation
  * Knockout.js documentation
  * MediaWiki API documentation
  * Udacity Forums
  * http://www.w3schools.com/ for CSS,HTML, JavaScript reference
   