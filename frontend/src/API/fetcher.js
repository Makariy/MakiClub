import axios from 'axios';


export const fetchBestToday = () => {
    return axios.get('/recipes/get/best_today/')
      .then(response => response.data);
  };

export const fetchBestMonth = () => {
    return axios.get('/recipes/get/best_month/')
      .then(response => response.data);
  };


export const fetchFeasts = () => {
    return axios.get('/recipes/get/best_feasts/')
      .then(response => response.data);
  };

export const fetchGroups = () => {
    return axios.get('/recipes/get/groups/')
      .then(response => response.data);
  }; 

export const fetchRecipeSteps = (recipe_uuid) => {
    return axios.get('/recipes/get/recipe_data/?recipe_uuid=' + recipe_uuid)
      .then(response => response.data);
}; 

export const fetchRecipeDescription = (recipe_uuid) => {
    return axios.get('/recipes/get/recipe/?recipe_uuid=' + recipe_uuid)
      .then(response => response.data);
};

export const fetchGroupInfo = (group_uuid) => {
    return axios.get('/groups/get/group/?group_uuid=' + group_uuid)
      .then(response => response.data);
};

export const fetchSearchResults = (title) => {
    return axios.get('/search/get/?title=' + title)
      .then(response => response.data);
}

