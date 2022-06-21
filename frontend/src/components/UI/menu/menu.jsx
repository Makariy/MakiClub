import React, { useEffect, useRef } from 'react';
import classes from './menu.module.css';
import { Link, Navigate, useNavigate } from 'react-router-dom';
import { useState } from 'react';



const Menu = (props) => {

    const [isMenuActive, setIsMenuActive] = useState(false);
    const [search_query, setSearchQuery] = useState("");


    const goSearch = () => {
        if (search_query.length > 0)
            document.location.to = document.location.origin + `/search/?title=${encodeURI(search_query)}`;
    }

    const onSearchInput = e => { 
        setSearchQuery(e.target.value)
    }
    const onKeyDown = e => {
        if (e.keyCode == 13) 
            goSearch();
    }

    return (
        <React.Fragment>
        <section className={[classes.menu_section, isMenuActive ? classes.active : ''].join(' ')}>
            <div className={classes.container}>
                <div className={classes.menu}>
                    
                    <div className={classes.menu__logo}>
                        <Link to="/" className={classes.menu__logo_logo}>
                            Maki<span>Club</span>
                        </Link>
                    </div>
                    <div className={classes.menu__categories}>
                        <ul className={classes.menu__categories_list}>
                            <li className={classes.menu__categories_list_item}>
                                <Link to="/groups/group/?group_uuid=6d5cda17-a9c2-410d-baaf-34586ee50652" replace>Recent</Link>
                            </li>
                            <li className={classes.menu__categories_list_item}>
                                <Link to="#" replace>Popular</Link>
                            </li>
                            <li className={classes.menu__categories_list_item}>
                                <Link to="#" replace>Offers</Link>
                            </li>
                            <li className={classes.menu__categories_list_item}>
                                <Link to="#" replace>Best</Link>
                            </li>
                        </ul>
                    </div>
                    <div className={classes.menu__search}>
                        <input  type="text" 
                                className={classes.menu__search_input} 
                                onKeyDown={onKeyDown}
                                onChange={onSearchInput} 
                                placeholder="Search..."/>
                        <button className={classes.menu__search_input_button} onClick={goSearch}>
                            <img className={classes.menu__search_input_button_img} src="/static/img/search.svg" alt=""/>
                        </button>
                    </div>

                    <div className={classes.menu__hide}>
                        <button onClick={() => setIsMenuActive(isMenuActive ? false : true)} className={classes.menu__hide_button}>
                            <div className={classes.menu__hide_button_stick}></div>
                            <div className={classes.menu__hide_button_stick}></div>
                            <div className={classes.menu__hide_button_stick}></div>
                        </button>
                    </div>
                    
                </div>
            </div>
	    </section>

        <section className={classes.mobile_top_section}>
            <div className={classes.container}>
                <div className={classes.mobile_top}>

                    <div className={classes.menu__hide}>
                        <button onClick={() => setIsMenuActive(isMenuActive ? false : true)} className={classes.menu__hide_button}>
                            <div className={classes.menu__hide_button_stick}></div>
                            <div className={classes.menu__hide_button_stick}></div>
                            <div className={classes.menu__hide_button_stick}></div>
                        </button>
                    </div>

                    <div className={classes.menu__logo}>
                        <Link to="/" replace className={classes.menu__logo_logo}>
                            Maki<span>Club</span>
                        </Link>
                    </div>

                </div>
            </div>
        </section>
        </React.Fragment>
    );
}

export default Menu;