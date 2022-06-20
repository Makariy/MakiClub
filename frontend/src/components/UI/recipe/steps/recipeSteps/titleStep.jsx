import React from 'react';
import classes from '../../recipe.module.css';



const TitleStep = (props) => {

    return (
        <React.Fragment>
            <h3 className={classes.recipe_recipe__data_title}>{props.value}</h3>
        </React.Fragment>
    );
}

export default TitleStep;