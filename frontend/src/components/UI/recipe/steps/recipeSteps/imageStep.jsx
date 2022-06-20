import React from "react";
import classes from '../../recipe.module.css';


const ImageStep = (props) => {

    return (
        <React.Fragment>
            <img src={props.value} className={classes.recipe_recipe__data_img}/>
        </React.Fragment>
    );
};

export default ImageStep;
