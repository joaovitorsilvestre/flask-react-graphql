import React from 'react'
import cookie from 'react-cookie'
import gql from 'graphql-tag';
import axiosInstance from '../../config'
import { graphql } from 'react-apollo'

import HearderLi from './HeaderLi'

class Layout extends React.Component {
    static propTypes = {
        data: React.PropTypes.shape({
            loading: React.PropTypes.bool,
            error: React.PropTypes.object,
            me: React.PropTypes.object,
        }).isRequired,
    };

    logout() {
        const browserHistory = { this };

        axiosInstance.get('/logout/' + cookie.load('secret'))
            .then((res) => {
                cookie.remove('secret')
                this.props.history.push('/')
            })
    }

    render() {
        if (this.props.data.loading) {
            return (<div>Loading</div>)
        }

        if (this.props.data.error) {
            console.log(this.props.data.error)
            return (<div>An unexpected error occurred</div>)
        }

        return (
            <div>
                <nav className="navbar navbar-default">
                    <div className="container-fluid">
                        <div className="navbar-header">
                            <a href="" className="navbar-brand">Learning</a>
                        </div>
                        <ul className="nav navbar-nav">
                            <HearderLi pathTo="/" actualPath={this.props.location.pathname}  text="Inicio" ></HearderLi>
                            {!this.props.data.me ? <HearderLi pathTo="/register" actualPath={this.props.location.pathname} text="Registrar-se" ></HearderLi> : null}
                            {!this.props.data.me ? <HearderLi pathTo="/signin" actualPath={this.props.location.pathname} text="Logar"></HearderLi> : null}
                            {this.props.data.me ? <HearderLi pathTo="/create-product" actualPath={this.props.location.pathname} text="Criar Produto"></HearderLi> : null}
                            {this.props.data.me ? <HearderLi pathTo="/products" actualPath={this.props.location.pathname} text="Produtos"></HearderLi> : null}
                            {this.props.data.me ? <li>
                                    <a onClick={this.logout.bind(this)}>Logout</a>
                                </li> : null}
                            <li><a href="">{this.props.location.pathname}</a></li>
                            {this.props.data.me ? <li><a href="">{this.props.data.me.name}</a></li> : null}
                        </ul>
                    </div>
                </nav>
                {this.props.children}
            </div>
        )
    }
}

const MeQuery = gql` query me {
    me {
        name
    }
}`

const LayoutWithData = graphql(MeQuery)(Layout)

export default LayoutWithData