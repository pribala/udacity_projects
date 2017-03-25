// Function toggles the menu for smaller screens

$('.menu').on('click', function(){
	$('.optionBox').toggleClass('expand');
});

$('#location-list').on('click', function(){
	$('.optionBox').toggleClass('expand');
});

/*$('.filter-container').on('click', function(){
	setTimeout(toggleSize, 5000);
});

function toggleSize() {
	$('.optionBox').toggleClass('expand');
};*/