import React from 'react'
import axiosInstance from '../../../config'
import { withApollo } from 'react-apollo'
import ApolloClient from 'apollo-client';
import gql from 'graphql-tag'

class SignIn extends React.Component{
    constructor() {
        super()
        this.state = {}
    }

    updateInputValue(evt) {
        this.setState({
            [evt.target.id]: evt.target.value
        })
    }

    send() {
        axiosInstance.post('/signin', {
            name: this.state.name,
            password: this.state.password
        }).then((response) => {
            this.props.client.query({
                query: gql` query me {
                    me {
                        name
                    }
                }`
            });
        })
    }

    render() {
        return (
            <div className="row">
                <form>
                    <div className="form-group">
                        <div className="col-md-4 col-md-offset-4">
                            <label htmlFor="name">Nome</label>
                            <input type="text" id="name" className="form-control" onChange={this.updateInputValue.bind(this)}/>
                            <label htmlFor="password">Senha</label>
                            <input type="password" id="password" className="form-control" onChange={this.updateInputValue.bind(this)}/>
                            <br/>
                            <div className="col-md-6 col-md-offset-3 text-center">
                                <button className="btn btn-info" onClick={this.send.bind(this)}>Logar</button>
                            </div>
                        </div>
                    </div>
                </form>
            </div>
        )
    }
}
SignIn.propTypes = {
    client: React.PropTypes.instanceOf(ApolloClient).isRequired,
}

const MyComponentWithApollo = withApollo(SignIn);

export default MyComponentWithApollo
