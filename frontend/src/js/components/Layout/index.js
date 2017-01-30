import React from 'react'
import HearderLi from './HeaderLi'

class Layout extends React.Component {
    render() {
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
                            <HearderLi pathTo="/create-product" actualPath={this.props.location.pathname} text="Criar Produto"></HearderLi>
                            <HearderLi pathTo="/products" actualPath={this.props.location.pathname} text="Produtos"></HearderLi>
                            <li><a href="">{this.props.location.pathname}</a></li>
                        </ul>
                    </div>
                </nav>
                {this.props.children}
            </div>
        )
    }
}

export default Layout