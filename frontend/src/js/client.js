import React from "react";
import ReactDOM from "react-dom";
import { Router, Route, IndexRoute, hashHistory } from 'react-router'
import ApolloClient, { createNetworkInterface } from 'apollo-client';
import { ApolloProvider } from 'react-apollo';

import Layout from "./components/Layout"
import Home from "./components/Home"
import Register from "./components/sign/Register"
import SignIn from "./components/sign/SignIn"
import CreateProducts from "./components/CreateProducts"
import Products from "./components/Products"

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
