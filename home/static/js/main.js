

function loadBestToday() {
	$.get({
		url: '/recipes/get/best_today/'
	}).done(function(data) {
		let recipe = data.recipe;
		let bestToday = document.getElementById('recommendation__best_today'); 
		bestToday.getElementsByClassName('recommendation__best_today_image_text-title')[0].innerText = recipe.title;
		bestToday.getElementsByClassName('recommendation__best_today_image_text-description')[0].innerText = recipe.description;
		bestToday.getElementsByClassName('recommendation__best_today_image_text-link')[0].href = 'recipes/?id=' + recipe.id;

	});
}

function loadBestMonth() {
	$.get({
		url: '/recipes/get/best_month'
	}).done(function(data) {
		
		let recipes = data.recipes;
		for (var i = 0; i < recipes.length; i+=1) {
			let recipe = recipes[i];
			console.log(recipe);
			let itemHtml = `
				<div class="recommendation__best_month_list_item">
					<img src="static/img/most_popular1.jpg" class="recommendation__best_month_list_item-img">
					<div class="recommendation__best_month_list_item_text">	
						<h4 class="recommendation__best_month_list_item_text-title">
							${recipe.title}
						</h4>
						<p class="recommendation__best_month_list_item_text-description">
							${recipe.description}
						</p>
					</div>
				</div>
			`;
			$('.recommendation__best_month_list')[0].innerHTML += itemHtml;
		}
	});	
}


function loadElements() {
	loadBestToday();
	loadBestMonth();
}	



window.onload = loadElements;
