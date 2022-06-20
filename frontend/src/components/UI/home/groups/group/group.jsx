import classes from './group.module.css';
import Recipe from '../../../../common/recipe/recipe';


const Group = (group) => {
    const recipes = group.recipes.recipes;
    return (
        <div className={classes.groups__group}>
			<a className={classes.groups__group_title} href={"/groups/group/?group_uuid=" + group.group.uuid}>
				<h3 className={classes.groups__group_title_title}>
					{group.group.title}
				</h3>
			</a>
			<div className={classes.groups__group_recipes}>
				{recipes.map(item => <Recipe {...(item.recipe)} key={item.recipe.uuid}/>)}
			</div>
		</div>
    );
}

export default Group;