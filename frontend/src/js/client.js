import React from "react";
import ReactDOM from "react-dom";
import { Router, Route, IndexRoute, hashHistory } from 'react-router'

import Layout from "./components/layout/Layout"
import Home from "./components/home/Home"
import Register from "./components/register/Register"

const app = document.getElementById('app');

ReactDOM.render(
    <Router history={hashHistory}>
        <Route path="/" component={Layout}>
            <IndexRoute component={Home}></IndexRoute>
            <Route path="register" component={Register}></Route>
        </Route>
    </Router>,
app)
