import classes from './recommendation.module.css';

import BestToday from './bestToday/bestToday';
import BestMonth from './bestMonth/bestMonth';


const Recommendation = () => {
    return (
        <div className={classes.recommendation}>
           <BestToday/>
           <BestMonth/>
        </div>
    );
}

export default Recommendation;
