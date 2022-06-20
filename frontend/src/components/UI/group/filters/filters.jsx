import classes from "./filters.module.css";
import { useState } from "react";


const Filters = (props) => {
    const recipes = props.recipes;
    const setRecipes = props.setRecipes; 

    const [default_recipes, setDefaultRecipes] = useState([...recipes]);

    
    const activateFilters = (title) => {
        let filters_ = default_filters.map(filter => {
            if (filter.title == title)
                filter.isActive = true
            else
                filter.isActive = false
            return filter 
        });
        return [...filters_]
    }

    const orderByAll = (e) => {
        setFilters(activateFilters(e.target.dataset.title))
        setRecipes([...default_recipes])
    }
    const orderByDate = (e) => {
        setFilters(activateFilters(e.target.dataset.title))
        setRecipes([...default_recipes])
    }
    const orderByPopularity = (e) => {
        setFilters(activateFilters(e.target.dataset.title))
        setRecipes([...default_recipes]);
    
    }
    const orderByTitle = (e) => {
        setFilters(activateFilters(e.target.dataset.title))
        setRecipes([...default_recipes].sort((a, b) => {
            if (a.recipe.title == b.recipe.title) return 0;
            if (a.recipe.title < b.recipe.title) return -1;
            else return 1;
        }))
    }


    const default_filters = [
        {
            title: "All",
            onClick: orderByAll,
            isActive: false,
        },
        {
            title: "Title",
            onClick: orderByTitle,
            isActive: false,
        },
        {
            title: "Popularity",
            onClick: orderByPopularity,
            isActive: false,
        },
        {
            title: "Recent",
            onClick: orderByDate,
            isActive: false
        }
    ]

    const [filters, setFilters] = useState(activateFilters("All"));


    return (
        <section className={classes.filters_section}>
            <div className="container" id="nice">
                <div className={classes.filters}>

                    <div className={classes.filters__title}>
                        <h4 className={classes.filters__title_title}>
                            Filters:
                        </h4>
                    </div>
                    <ul className={classes.filters__filters}>
                        {filters.map(filter => 
                            <button data-title={filter.title} className={[classes.filters__filters_item, filter.isActive ? classes.active : ""].join(" ")} onClick={filter.onClick} key={filter.title}>
                                <li data-title={filter.title} className={classes.filters__filters_item_text}>
                                    {filter.title}
                                </li>
                            </button>)
                        }
                    </ul>

                </div>
            </div>
        </section>
    );
}

export default Filters;