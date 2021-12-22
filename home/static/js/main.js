$('.presentation__recipes_slider').slick({
	dots: true,
	arrows: false,

});

$('.presentation__popular_list').slick({
	dots: true,
	arrows: false,

	slidesToShow: 5,
	slidesToScroll: 2,
});


var result = 1;

function loadPresentation() {
	$.get({url: 'get/presentation'}).done(function(response) {
		var recipes = response.recipes;
		for (var i = 0; i < recipes.length; i+=1) {
			var element = document.createElement('div');
			element.innerHTML = `
			<div class="presentation__recipes_slider_item">
				<img src="static/img/presentation-food.jpg" class="presentation__recipes_slider_item-image">
				<div class="presentation__recipes_slider_item_text">
					<h4 class="presentation__recipes_slider_item_text-title">${recipes[i].title}</h4>
					<p class="presentation__recipes_slider_item_text-description">${recipes[i].description}</p>
					<a href="${recipes[i].id}" class="presentation__recipes_slider_item_text-link">Checkout</a>
				</div>
			</div>
			`;
			result = $('.presentation__recipes_slider').slick('slickAdd', element);
		}
	});
}

function loadPopular() {
	$.get({url: 'get/popular'}).done(function(response){
		var popular = response.popular;

		console.log(popular)
	});
}


function loadElements() {
	loadPresentation();
	loadPopular();
}	



window.onload = loadElements;
