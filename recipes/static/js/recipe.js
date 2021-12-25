

function renderRecipeData(recipe_data) {
    if (recipe_data.type == 'title') {
        return `<h3 class="recipe_recipe__data-text">${recipe_data.text}</h3>`;
    }
    else if (recipe_data.type == 'text') {
        return `<p class="recipe_recipe__data-text">${recipe_data.text}</p>`;
    }
    else if (recipe_data.type == 'image') {
        return `<img src="${recipe_data.image_link}" class="recipe_recipe__data-img">`;
    }
}

function loadRecipe() {
    $.get({
        url: '/recipes/get/recipe_data/?recipe_id=' + document.recipe_id,
    }).done(function (data) {
        let recipe_data = data.data.recipe; 
        for (var i = 0; i < recipe_data.length; i+=1){
           let rendered_recipe_data = renderRecipeData(recipe_data[i]);
           $('.recipe_recipe')[0].innerHTML += rendered_recipe_data;
        }

    });
}

document.onload = loadRecipe;
