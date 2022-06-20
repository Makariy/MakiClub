
import classes from "./filters.module.css";


const Filters = (props) => {
    return (
        <section className={classes.filters_section}>
            <div className="container">
                <div className={classes.filters}>
                    <h4 className={classes.filter__title}>
                        Filtered with: 
                    </h4>
                    <ul className={classes.filter__list}>
                        {
                            props.groups.map(filter => 
                                <li className={classes.filter__list_item} key={filter.group.uuid}>
                                    <a className={classes.filter__list_item_link} href={"/groups/group/?group_uuid=" + filter.group.uuid}>
                                        {filter.group.title}
                                    </a>
                                </li>
                            )
                        }
                    </ul>
                </div>
            </div>
        </section>
    );
}

export default Filters;