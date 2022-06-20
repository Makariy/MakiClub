
import React from 'react';
import classes from './description.module.css';


const RecipeDescription = (props) => {
    return (
        <React.Fragment>
            <section className={classes.recipe_header_section}>
                <div className="container">
                    <div className={classes.recipe_header}>
                        <h3 className={classes.recipe_header__title}>
                            {props.title}
                        </h3>
                        <p className={classes.recipe_header__description}>
                            {props.description}
                        </p>
                        <div className={classes.recipe__header__author}>
                            <img src="/static/img/chef.png" className={classes.recipe__header__author_image}/>
                            <div className={classes.recipe__header__author_text}>
                                <p className={classes.recipe__header__author_text_username}>
                                    By: <span>
                                        {props.author}
                                    </span>
                                </p>
                                <p className={classes.recipe__header__author_text_date}>
                                    Published: <span>
                                        {props.date}
                                    </span>
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
        </React.Fragment>
    );
}

export default RecipeDescription;
