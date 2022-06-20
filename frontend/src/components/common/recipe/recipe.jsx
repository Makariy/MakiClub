import classes from './recipe.module.css';



const Recipe = ({title, preview_url, description, uuid}) => {

    let title_ = title.length > 25 ? title.substr(0, 25) + "..." : title;
    let description_ = description.length > 65 ? description.substr(0, 65) + "..." : title;

    return (
      <a className={classes.recipe__item} href={"/recipes/recipe/?recipe_uuid=" + uuid}>
        <img className={classes.recipe__item_image} src={'/recipes/' + preview_url}/>
        <div className={classes.recipe__item_text}>
          <p className={classes.recipe__item_text_title}>
            {title_}
          </p>
          <p className={classes.recipe__item_text_description}>
            {description_}
          </p>
        </div>
      </a>
    );
  }

export default Recipe;