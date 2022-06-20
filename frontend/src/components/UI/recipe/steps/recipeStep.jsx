
import ImageStep from "./recipeSteps/imageStep";
import TextStep from "./recipeSteps/textStep";
import TitleStep from "./recipeSteps/titleStep";


const RecipeStep = (props) => {
    const type = props.type;
    
    let step = null;

    switch(type) {
        case "text":
            step = <TextStep {...props}/>;
            break;
        case "title":
            step = <TitleStep {...props}/>;
            break;
        case "image":
            step = <ImageStep {...props}/>;
            break;
    }

    return step;

};

export default RecipeStep;
