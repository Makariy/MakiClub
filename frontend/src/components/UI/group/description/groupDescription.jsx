import React from "react";
import classes from "./groupDescription.module.css";


const GroupDescription = (props) => {


    return (
        <section className={classes.group_section}>
            <div className="container">
                <div className={classes.group}>
                    <div className={classes.group__text}>
                        <h2 className={classes.group__text_title}>
                            {props.group.title}
                        </h2>
                        <p className={classes.group__text_description}>
                            {props.group.description}
                        </p>
                    </div>
                </div>
            </div>
        </section>
    );
};

export default GroupDescription;

