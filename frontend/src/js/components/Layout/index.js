import React from 'react'
import { graphql } from 'react-apollo'
import gql from 'graphql-tag'
import HearderLi from './HeaderLi'

class Layout extends React.Component {
    static propTypes = {
        data: React.PropTypes.shape({
            loading: React.PropTypes.bool,
            error: React.PropTypes.object,
            products: React.PropTypes.array,
        }).isRequired,
    };

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
                            <HearderLi pathTo="/register" actualPath={this.props.location.pathname} text="Registrar-se" ></HearderLi>
                            <HearderLi pathTo="/signin" actualPath={this.props.location.pathname} text="Logar"></HearderLi>
                            { this.props.data.me != null ? <HearderLi pathTo="/create-product" actualPath={this.props.location.pathname} text="Criar Produto"></HearderLi> : null}
                            { this.props.data.me != null ? <HearderLi pathTo="/products" actualPath={this.props.location.pathname} text="Produtos"></HearderLi> : null}
                            <li><a href="">{this.props.location.pathname}</a></li>
                        </ul>
                    </div>
                </nav>
                {this.props.children}
            </div>
        )
    }
}

const MeQuery = gql`
    query MeQuery {
        me {
            name
        }
    }
`

const LayoutWithData = graphql(MeQuery)(Layout)

export default LayoutWithData