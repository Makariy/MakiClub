import React from 'react';
import classes from '../../recipe.module.css';


const TextStep = (props) => {
    return (
        <React.Fragment>
            <p className={classes.recipe_recipe__data_text}>{props.value}</p>
        </React.Fragment>
    );
}
export default TextStep;