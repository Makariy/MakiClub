import classes from './recipe.module.css';
import { Link } from 'react-router-dom';


const Recipe = ({title, preview_url, description, uuid}) => {

    let title_ = title.length > 25 ? title.substr(0, 25) + "..." : title;
    let description_ = description.length > 65 ? description.substr(0, 65) + "..." : title;

    return (
      <Link className={classes.recipe__item} to={"/recipes/recipe/?recipe_uuid=" + uuid} replace>
        <img className={classes.recipe__item_image} src={'/recipes/' + preview_url}/>
        <div className={classes.recipe__item_text}>
          <p className={classes.recipe__item_text_title}>
            {title_}
          </p>
          <p className={classes.recipe__item_text_description}>
            {description_}
          </p>
        </div>
      </Link>
    );
  }

export default Recipe;