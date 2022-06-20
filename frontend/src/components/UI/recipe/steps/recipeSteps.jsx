import React, { useEffect, useState } from "react"
import RecipeStep from "./recipeStep";
import { fetchRecipeSteps } from "../../../../API/fetcher";
import classes from "./recipeSteps.module.css";


const RecipeSteps = (props) => {
    const [steps, setSteps] = useState(null);


    useEffect(() => {
        fetchRecipeSteps(props.recipeUUID).then(
            data => setSteps(data)
        );
    }, []);

    return (
        <section className={classes.recipe_recipe_section}>
            <div className="container">
                <div className={classes.recipe_recipe}>
                    {
                        !steps ? "" :
                            steps.data.map((step, index) => 
                                <RecipeStep {...step} key={index}/>
                            )
                    }
                </div>  
            </div>
        </section>
    );  
}


export default RecipeSteps;