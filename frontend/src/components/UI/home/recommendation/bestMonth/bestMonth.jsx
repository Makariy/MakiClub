import { useEffect, useState } from 'react';
import classes from './bestMonth.module.css';
import { fetchBestMonth } from '../../../../../API/fetcher';
import Recipe from '../../../../common/recipe/recipe'


const BestMonth = () => {

    const [recipes, setRecipes] = useState(null);

    useEffect(() => {
        fetchBestMonth().then(data => setRecipes(data.recipes))
    }, []);

    return (
        <div className={classes.recommendation__best_month}>
            <div className={classes.recommendation__best_month_logo}>
                Maki<span>Club</span>
            </div>

            <div className={classes.recommendation__best_month_title}>
                The best recipes of this month {'>'}
            </div>

            <div className={classes.recommendation__best_month_list}>
                {
                    !recipes ? "" :
                        recipes.map(item => <Recipe {...(item.recipe)} key={item.recipe.uuid}/>)
                }
            </div>
        </div>
    );
}

export default BestMonth;
