import React from 'react';
import {BrowserRouter,Route,Switch} from 'react-router-dom'
import ProductList from './pages/ProductList'

function Routes() {
  return (
    <BrowserRouter>
      <Switch>
        <Route path="/" component={ProductList}/>
      </Switch>
    </BrowserRouter>
    
  );
}

export default Routes;