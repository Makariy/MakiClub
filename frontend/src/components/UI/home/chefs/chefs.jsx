import classes from './chefs.module.css';

const Chefs = () => {
    return (
        <section className={classes.chefs_section}>
            <div className={classes.container}>
                <div className={classes.chefs}>
                    
                    <div className={classes.chefs__text}>
                        <img src="/static/img/venchik.png" className={classes.chefs__text_img}/>				
                        <h4 className={classes.chefs__text_title}>
                            The Simply Recipes Team
                        </h4>
                        <p className={classes.chefs__text_description}>
                            Simply Recipes is a trusted resource for home cooks with more than 3,000 tested recipes, guides, and meal plans, drawing over 15 million readers each month from around the world. We’re supported by a group of recipe developers, food writers, recipe and product testers, photographers, and other creative professionals.
                        </p>
                        <a href="#" className={classes.chefs__text_link}>Read more {'>'}</a>
                    </div>

                    <div className={classes.chefs__chefs}>
                        <div className={classes.chefs__chefs_chef}>
                            <img src="/static/img/chef.png" className={classes.chefs__chefs_chef_img}/>
                            <h5 className={classes.chefs__chefs_chef_title}>
                                Chef №1
                            </h5>
                        </div>
                    </div>

                </div>
            </div>
	    </section>
    );
}

export default Chefs;