function renderRecipe(recipe) {
    let title = recipe.title;
    let description = recipe.description;

    let max_title_length = 25;
    let max_description_length = 55;
    if (title.length > max_title_length) {
        title = title.substr(0, max_title_length) + '...';
    }
    if (description.length > max_description_length) {
        description = description.substr(0, max_description_length) + '...';
    }
	return `
		<a href="/recipes/recipe/?recipe_uuid=${recipe.uuid}" class="recipe__item">
			<img src="/recipes/img/${recipe.image_link}" class="recipe__item-img">
			<div class="recipe__item_text">	
				<h4 class="recipe__item_text-title">
					${title}
				</h4>
				<p class="recipe__item_text-description">
					${description}
				</p>
			</div>
		</a>
	`;
}


function renderGroup(group) {
	let recipes = group.recipes.recipes;
	let renderedRecipes = '';
	for (var i = 0; i < recipes.length; i+=1) {
		renderedRecipes += renderRecipe(recipes[i].recipe);
	}
	return `
		<div class="groups__group">
			<a class="groups__group_title" href="/groups/group/?group_uuid=${group.group.uuid}">
				<h3 class="groups__group_title-title">
					${group.group.title}
				</h3>
			</a>
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
		bestToday.getElementsByClassName('recommendation__best_today_image_text-link')[0].href = `/recipes/recipe/?recipe_uuid=${recipe.uuid}`;

	});
}

a = null;
function loadBestMonth() {
	$.get({
		url: '/recipes/get/best_month'
	}).done(function(data) {
		data.recipes.forEach(function(elem) {
		    $('.recommendation__best_month_list')[0].innerHTML += renderRecipe(elem.recipe);
		});
	});
}


function loadFeasts() {
	$.get({
		url: '/recipes/get/best_feasts/'
	}).done(function(data) {
		data.recipes.forEach(function(elem) {
			$('.feasts__list')[0].innerHTML += renderRecipe(elem.recipe);
		});
	});
}

function loadGroups() {
	$.get({
		url: '/recipes/get/groups/'
	}).done(function(data) {
        data.groups.forEach(function(elem) {
            $('.groups')[0].innerHTML += renderGroup(elem);
        });
	});
}


function loadElements() {
	loadBestToday();
	loadBestMonth();
	loadFeasts();
	loadGroups();
}	


function goSearch() {
    let title = document.getElementById('menu__search_input').value;
    if (title != null && title != "")
        document.location.href = document.location.origin + `/search/?title=${encodeURI(title)}`;
}



window.onload = loadElements;
