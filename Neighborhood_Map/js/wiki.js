// Load wikipedia API info specific to the location when,
// a location is selected from the location list.
function loadData(marker) {
	var  wikiUrl = 'http://en.wikipedia.org/w/api.php?action=opensearch&search=' + marker.title +'&limit=5' +'&format=json&callback=wikiCallback';

	var wikiRequestTimeout = setTimeout(function(){
		var errorMessage = "Failed to get Wikipedia Resources";
		displayWikiWindow(marker, errorMessage);
		}, 8000);

	$.ajax( {
    url: wikiUrl,
    dataType: 'jsonp',

	success: function(response) {
       // loop through the returned data and display it in an infowindow.
	   var articleList = response[1];
	   var content = '';
	   if(articleList.length >0){
			for (var i=0; i< articleList.length; i++) {
				articleStr = articleList[i];
				var url = 'http://en.wikipedia.org/wiki/' + articleStr;
				content += '<li><a href="'+url+'">'+articleStr+'</a></li>';
			};
	   } else {
		   content = "<li>No wikipedia articles found for this location.</li>"
	   }
	   displayWikiWindow(marker, content);
	   clearTimeout(wikiRequestTimeout);
    }
} );
};

