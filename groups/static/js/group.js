function getGetParameter(parameterName) {
    var result = null;
    location.search
        .substr(1)
        .split("&")
        .forEach(function (item) {
          var tmp = item.split("=");
          if (tmp[0] === parameterName) result = decodeURIComponent(tmp[1]);
        });
    return result;
}


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

var recipes = null;


function orderByTitle() {
    $('.filters__filters_item').removeClass('active');
    $('#filter-title').addClass('active');
    let sorted = [...recipes].sort(function(first, second) {
        if (first.recipe.title < second.recipe.title) return -1;
        if (first.recipe.title > second.recipe.title) return 1;
        else return 0;
    });
    $('.recipes__inner')[0].innerHTML = '';
    sorted.forEach(function(item) {
        let rendered = renderRecipe(item.recipe);
        $('.recipes__inner')[0].innerHTML += rendered;
    });
}

// Just for some time
function orderByPopularity() {
    $('.filters__filters_item').removeClass('active');
    $('#filter-popularity').addClass('active');
    let sorted = [...recipes].sort(function(first, second) {
        if (first.recipe.uuid < second.recipe.uuid) return -1;
        if (first.recipe.uuid > second.recipe.uuid) return 1;
        else return 0;
    });
    $('.recipes__inner')[0].innerHTML = '';
    sorted.forEach(function(item) {
        let rendered = renderRecipe(item.recipe);
        $('.recipes__inner')[0].innerHTML += rendered;
    });
}

// Just for some time
function orderByDate() {
    $('.filters__filters_item').removeClass('active');
    $('#filter-recent').addClass('active');
    let sorted = [...recipes].sort(function(first, second) {
        if (first.recipe.uuid < second.recipe.uuid) return -1;
        if (first.recipe.uuid > second.recipe.uuid) return 1;
        else return 0;
    });
    $('.recipes__inner')[0].innerHTML = '';
    sorted.forEach(function(item) {
        let rendered = renderRecipe(item.recipe);
        $('.recipes__inner')[0].innerHTML += rendered;
    });
}


function orderByAll() {
    $('.filters__filters_item').removeClass('active');
    $('#filter-all').addClass('active');

    $('.recipes__inner')[0].innerHTML = '';

    recipes.forEach(function(item) {
        let rendered = renderRecipe(item.recipe);
        $('.recipes__inner')[0].innerHTML += rendered;
    });
}


function loadRecipes() {
    var group_uuid = getGetParameter('group_uuid');
    if (group_uuid == null) {
        document.location.href = document.location.origin;
    }
    $.ajax({
        type: 'GET',
        url: '/groups/get/group/?group_uuid=' + group_uuid,
    }).done(function(data) {
        recipes = data.recipes;
        $('.group__text-title')[0].innerHTML = data.group.title;
        orderByAll();
    });
}


window.onload = loadRecipes;

