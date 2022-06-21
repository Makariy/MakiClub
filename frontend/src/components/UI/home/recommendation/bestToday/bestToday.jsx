import {useEffect, useState} from 'react';
import { Link } from 'react-router-dom';
import classes from './bestToday.module.css';
import { fetchBestToday } from '../../../../../API/fetcher';



const BestToday = (props) => {

    const [recipe, setRecipe] = useState(null);

    useEffect(() => {
        fetchBestToday().then(
            data => setRecipe(data.recipe)
        )
    }, []);    

    return (
        <div className={classes.recommendation__best_today} id="recommendation__best_today">
            <div>
                {!recipe ? "" : 
                    <div className={classes.recommendation__best_today_image}>
                        <img src={'/recipes/' + recipe.image_url} alt="" className={classes.recommendation__best_today_image_img}/>
                        <div className={classes.recommendation__best_today_image_text}>
                            <div className={classes.recommendation__best_today_image_text_inner}>
                                <h3 className={classes.recommendation__best_today_image_text_title}>
                                    {recipe.title}
                                </h3>
                                <p className={classes.recommendation__best_today_image_text_description}>
                                    {recipe.description}
                                </p>
                                <Link to={"/recipes/recipe/?recipe_uuid=" + recipe.uuid} replace 
                                    className={classes.recommendation__best_today_image_text_link}>
                                    Get the recipe {'>'} 
                                </Link>
                            </div>
                        </div>
                    </div>
                }
            </div>
        </div>
    );
}


export default BestToday;
