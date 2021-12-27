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


function renderFilter(filter) {
    return `
        <li class="filter__list_item">
            ${filter}
        </li>
    `;
}    


function renderRecipeDataElement(recipe_data) {
    if (recipe_data.type == 'title') {
        return `<h3 class="recipe_recipe__data-title">${recipe_data.title}</h3>`;
    }
    else if (recipe_data.type == 'text') {
        return `<p class="recipe_recipe__data-text">${recipe_data.text}</p>`;
    }
    else if (recipe_data.type == 'image') {
        return `<img src="${recipe_data.image_link}" class="recipe_recipe__data-img">`;
    }
}

function renderRecipeData(recipe_data) {
    for (var i = 0; i < recipe_data.length; i+=1) {
       let rendered_recipe_data_element = renderRecipeDataElement(recipe_data[i]);
       $('.recipe_recipe')[0].innerHTML += rendered_recipe_data_element;
    }
}

function renderRecipe(recipe) {
    // Add filters to filter list 
    for (var i = 0; i < recipe.groups.length; i+=1)
        document.getElementById('filter__list').innerHTML += renderFilter(recipe.groups[i]);

    // Add recipe title 
    document.getElementById('recipe__title').innerHTML += recipe.title;

    // Add recipe description 
    document.getElementById('recipe__description').innerHTML += recipe.description;

    // Add recipe author 
    document.getElementById('recipe__author').innerHTML += recipe.author;

    // Add recipe date 
    document.getElementById('recipe__date').innerHTML += recipe.date;

    // Add recipe image
    document.getElementById('recipe__image').src = recipe.image_link;
}

function loadRecipe() {
    let recipe_uuid = getGetParameter('recipe_uuid');
    $.get({
        url: '/recipes/get/recipe/?recipe_uuid=' + recipe_uuid,
    }).done(function (data) {
        let recipe = data.recipe; 
        renderRecipe(recipe);
    });

    $.get({
        url: '/recipes/get/recipe_data/?recipe_uuid=' + recipe_uuid
    }).done(function (data) {
        let recipe_data = data.data;
        renderRecipeData(recipe_data);
    });
}



window.onload = loadRecipe;
