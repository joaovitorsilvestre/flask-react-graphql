import React from 'react'
import { Link } from 'react-router'
import classNames from 'classnames'

class Layout extends React.Component {
    actualPath(type) {
        return classNames({'active': this.props.location.pathname == type})
    }

    render() {
        return (
            <div>
                <nav className="navbar navbar-default">
                    <div className="container-fluid">
                        <div className="navbar-header">
                            <a href="" className="navbar-brand">Learning</a>
                        </div>
                        <ul className="nav navbar-nav">
                            <li className={this.actualPath('/')}>
                                <Link className="active" to="/">Inicio</Link>
                            </li>
                            <li className={this.actualPath('/register')}>
                                <Link to="register">Registrar-se</Link>
                            </li>
                            <li className={this.actualPath('/signIn')}>
                                <Link to="signIn">Logar</Link>
                            </li>
                            <li className={this.actualPath('/create-products')}>
                                <Link to="create-products">Criar Produto</Link>
                            </li>
                            <li className={this.actualPath('/products')}>
                                <Link to="products">Produtos</Link>
                            </li>
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