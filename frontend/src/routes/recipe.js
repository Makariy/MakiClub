import React from "react"
import { useLocation } from "react-router-dom";

import Menu from "../components/UI/menu/menu";
import Footer from "../components/UI/footer/footer";

import Description from "../components/UI/recipe/description/description";
import RecipeSteps from '../components/UI/recipe/steps/recipeSteps';


import '../components/UI/recipe/recipe.module.css';



const RecipeRoute = () => {
    const location = useLocation();
    const recipeUUID = new URLSearchParams(location.search).get('recipe_uuid');

    return (
        <React.Fragment>
            <Menu/>

            <Description recipeUUID={recipeUUID}/>
            <RecipeSteps recipeUUID={recipeUUID}/>


            <Footer/>
        </React.Fragment>
    )
};

export default RecipeRoute;
