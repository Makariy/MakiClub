import React, { useEffect, useState } from "react";
import { useLocation } from "react-router-dom";
import { fetchSearchResults } from "../API/fetcher";
import Menu from "../components/UI/menu/menu";
import Footer from "../components/UI/footer/footer";
import RecipesList from "../components/common/recipesList/recipesList";



const SearchRoute = () => {
    const [recipes, setRecipes] = useState(null);
    const search_query = new URLSearchParams(useLocation().search).get('title');

    useEffect(() => {
        fetchSearchResults(search_query).then(
            data => setRecipes(data.recipes)
        )
    }, []);

    return (
        <React.Fragment>
            <Menu/>
            {
                !recipes ? "" : 
                    <RecipesList recipes={recipes}/>
            }
            <Footer/>
        </React.Fragment>

    );

}


export default SearchRoute;
