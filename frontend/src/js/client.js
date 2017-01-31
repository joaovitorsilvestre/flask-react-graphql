import React from "react";
import cookie from 'react-cookie';
import ReactDOM from "react-dom";
import { Router, Route, IndexRoute, hashHistory } from 'react-router'
import ApolloClient, { createNetworkInterface } from 'apollo-client';
import { ApolloProvider } from 'react-apollo';

import Layout from "./components/Layout"
import Home from "./components/Home"
import Register from "./components/sign/Register"
import SignIn from "./components/sign/SignIn"
import CreateProducts from "./components/Products/CreateProducts"
import Products from "./components/Products"

const app = document.getElementById('app');

const networkInterface = createNetworkInterface('http://localhost:5000/graphql', {
    uri: 'http://localhost:5000/graphql',
    headers: {
        Authorization: cookie.load('secret')
    },
    opts: {
        credentials: 'same-origin',
    },
});

const client = new ApolloClient({ networkInterface });


ReactDOM.render(
    <ApolloProvider client={client}>
        <Router history={hashHistory}>
            <Route path="/" component={Layout}>
                <IndexRoute component={Home}></IndexRoute>
                <Route path="register" component={Register}></Route>
                <Route path="signin" component={SignIn}></Route>
                <Route path="create-product" component={CreateProducts}></Route>
                <Route path="products" component={Products}></Route>
            </Route>
        </Router>
    </ApolloProvider>,
app)
