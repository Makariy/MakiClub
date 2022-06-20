import classes from "./recipesList.module.css";
import Recipe from "../recipe/recipe";


const GroupRecipesList = ({recipes}) => {
    return (
        <section className={classes.recipes_section}>
            <div className="container">
                <div className={classes.recipes}>
                    <div className={classes.recipes__inner}>
                        {
                            recipes.map(item =>
                                    <Recipe {...item.recipe} key={item.recipe.uuid}/> 
                                )
                        }
                    </div>
                </div>
            </div>
        </section>
    );
}

export default GroupRecipesList;
