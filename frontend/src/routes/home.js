import Menu from '../components/UI/menu/menu';
import Footer from '../components/UI/footer/footer';

import Recommendation from '../components/UI/home/recommendation/recommendation';
import Feasts from '../components/UI/home/feasts/feasts';
import Chefs from '../components/UI/home/chefs/chefs';
import Groups from '../components/UI/home/groups/groups';
import React from 'react';



const HomeRoute = () => {
  return (
    <React.Fragment>
      <Menu/>

      <Recommendation/>
      <Feasts/>
      <Chefs/>
      <Groups/>

      <Footer/>
    </React.Fragment>
  );
}

export default HomeRoute;

