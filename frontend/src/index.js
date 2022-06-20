import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';

import {Route, Routes, Navigate, BrowserRouter} from 'react-router-dom';
 
import HomeRoute from './routes/home';
import RecipeRoute from './routes/recipe';
import GroupRoute from './routes/group';
import SearchRoute from './routes/search';


ReactDOM.render(
  <BrowserRouter>
    <Routes>
        <Route path="/" element={<HomeRoute/>}/>
        <Route path="/recipes/recipe/" element={<RecipeRoute/>}/>
        <Route path="/groups/group/" element={<GroupRoute/>}/>
        <Route path="/search/" element={<SearchRoute/>}/>
        <Route path="*" element={<Navigate to="/" replace/>}/>
    </Routes>
  </BrowserRouter>,
  document.getElementById('root')
);

