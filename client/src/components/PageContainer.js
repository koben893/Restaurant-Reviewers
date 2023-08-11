import React from 'react';
import { Switch, Route } from 'react-router-dom';
// import Home from './Home'
import Ratings from './Ratings'
import Restaurants from "./Restaurants"
import Reviews from './Reviews';
import About from "./About"

function PageContainer() {
    return (
        <>
            <Switch>
        <Route path="/ratings">
            <Ratings />
        </Route>
        <Route path="/restaurants">
            <Restaurants />
        </Route>
        <Route path="/reviews">
            <Reviews />
        </Route>
        <Route path="/about">
            <About />
        </Route>
        </Switch>
    </>
    );
}

export default PageContainer;