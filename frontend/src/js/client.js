import React from "react";
import ReactDOM from "react-dom";
import { Router, Route, IndexRoute, hashHistory } from 'react-router'
import ApolloClient, { createNetworkInterface } from 'apollo-client';
import { ApolloProvider } from 'react-apollo';

import Layout from "./components/layout/Layout"
import Home from "./components/home/Home"
import Register from "./components/register/Register"
import SignIn from "./components/signIn/SignIn"
import CreateProducts from "./components/createProducts/CreateProducts"
import Products from "./components/products/Products"

const app = document.getElementById('app');

const client = new ApolloClient({
  networkInterface: createNetworkInterface({ uri: 'http://localhost:5000/graphql' }),
});

ReactDOM.render(
    <ApolloProvider client={client}>
        <Router history={hashHistory}>
            <Route path="/" component={Layout}>
                <IndexRoute component={Home}></IndexRoute>
                <Route path="register" component={Register}></Route>
                <Route path="signin" component={SignIn}></Route>
                <Route path="create-products" component={CreateProducts}></Route>
                <Route path="products" component={Products}></Route>
            </Route>
        </Router>
    </ApolloProvider>,
app)
