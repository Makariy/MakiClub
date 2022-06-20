
import React, { useEffect, useState } from "react";
import { fetchRecipeDescription } from "../../../../API/fetcher";

import Filters from "./filters/filters";
import RecipeDescription from "./description/description";



const Description = (props) => {

    const [recipe, setRecipe] = useState(null);

    useEffect(() => {
        fetchRecipeDescription(props.recipeUUID).then(
            data => setRecipe(data.recipe)
        )
    }, []);

    return (
        <React.Fragment>
        {
            !recipe ? "" : 
                <React.Fragment>
                    <Filters {...recipe}/>
                    <RecipeDescription {...recipe}/>
                </React.Fragment>
        }
        </React.Fragment>
    );
}
export default Description;