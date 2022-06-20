import { useEffect, useState } from "react";
import { fetchFeasts } from '../../../../API/fetcher';
import Recipe from "../../../common/recipe/recipe";

import classes from './feasts.module.css';


const Feasts = () => {

    const [recipes, setRecipes] = useState(null);

    useEffect(() => {
        fetchFeasts().then(data => setRecipes(data.recipes));
    }, []);

    return (
        <section className="feasts_section">
            <div className={classes.container}>
                <div className={classes.feasts}>
                    
                    <div className={classes.feasts__title}>
                        <h3 className={classes.feasts__title_title}>
                            Christmas Feasts >
                        </h3>
                    </div>

                    <div className={classes.feasts__list}>
                        {
                            !recipes ? "" : 
                                recipes.map(item => <Recipe {...(item.recipe)} key={item.recipe.uuid}/>) 
                        }
                    </div>

                </div>
            </div>
        </section>	
    );
}

export default Feasts;
