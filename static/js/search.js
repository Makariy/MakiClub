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



function loadRecipes() {
    let title = getGetParameter('title');
    if(title != null) {
        $.ajax({
            type: 'GET',
            url: `/search/get/?title=${title}`
        }).done(function(response) {
            let recipes = response.recipes;
            recipes.forEach(function(item) {
                document.getElementsByClassName('recipes__inner')[0].innerHTML += renderRecipe(item.recipe);
            })
        });
    }
}


function preparePage() {
    let title = getGetParameter('title');
    document.getElementById('search__text-query').innerHTML = title;
    loadRecipes();
}



window.onload = preparePage;
