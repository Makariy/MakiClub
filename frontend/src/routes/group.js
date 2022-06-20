import React, { useEffect, useState } from "react";

import Menu from "../components/UI/menu/menu";
import Footer from "../components/UI/footer/footer";
import { fetchGroupInfo } from "../API/fetcher";
import { useLocation } from "react-router-dom";
import GroupDescription from "../components/UI/group/description/groupDescription";
import Filters from "../components/UI/group/filters/filters";
import RecipesList from "../components/common/recipesList/recipesList";


const GroupRoute = () => {
    const [group, setGroup] = useState(null);
    const [recipes, setRecipes] = useState(null);

    const group_uuid = new URLSearchParams(useLocation().search).get('group_uuid')

    useEffect(() => {
        fetchGroupInfo(group_uuid).then(data => {
            setGroup(data)
            setRecipes(data.recipes);
        }); 
    }, []);

    return (
        <React.Fragment>
            
            <Menu/>
            {
                !group ? "" : 
                        <GroupDescription {...group}/>
            }
            {
                !recipes ? "" : 
                        <React.Fragment>
                            <Filters setRecipes={setRecipes} recipes={recipes}/>
                            <RecipesList recipes={recipes}/>
                        </React.Fragment>
            }
            <Footer/>

        </React.Fragment>
    );
};

export default GroupRoute;
