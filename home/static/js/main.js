function renderRecipe(recipe) {
	return `
		<a href="/recipes/recipe/?recipe_uuid=${recipe.uuid}" class="recipe__item">
			<img src="static/img/most_popular1.jpg" class="recipe__item-img">
			<div class="recipe__item_text">	
				<h4 class="recipe__item_text-title">
					${recipe.title}
				</h4>
				<p class="recipe__item_text-description">
					${recipe.description}
				</p>
			</div>
		</a>
	`;
}


function renderGroup(group) {
	let recipes = group.recipes;
	let renderedRecipes = '';
	for (var i = 0; i < recipes.length; i+=1) {
		renderedRecipes += renderRecipe(recipes[i].recipe);
	}
	return `
		<div class="groups__group">
			<div class="groups__group_title">
				<h3 class="groups__group_title-title">
					${group.title}
				</h3>
			</div>
			<div class="groups__group_recipes">
				${renderedRecipes}
			</div>
		</div>
	`;
}




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
			let recipe = recipes[i].recipe;
			let rendered = renderRecipe(recipe);
			$('.recommendation__best_month_list')[0].innerHTML += rendered;
		}
	});	
}


function loadFeasts() {
	$.get({
		url: '/recipes/get/best_feasts/'
	}).done(function(data) {
		let recipes = data.recipes;
		for (var i = 0; i < recipes.length; i+=1) {
			let recipe = recipes[i].recipe;
			let rendered = renderRecipe(recipe);
			$('.feasts__list')[0].innerHTML += rendered;
		}
	});	
}


function loadGroups() {
	$.get({
		url: '/recipes/get/groups'
	}).done(function(data) {
		let groups = data.groups;
		for (var i = 0; i < groups.length; i+=1) {
			$('.groups')[0].innerHTML += renderGroup(groups[i]);
		}
	});
}


function loadElements() {
	loadBestToday();
	loadBestMonth();
	loadFeasts();
	loadGroups();
}	



window.onload = loadElements;
