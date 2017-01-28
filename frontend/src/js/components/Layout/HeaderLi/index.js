import React from 'react'
import { Link } from 'react-router'
import classNames from 'classnames'


class HeaderLi extends React.Component {
    actualPath(type) {
        return classNames({'active': this.props.pathTo == this.props.actualPath})
    }

    render() {
        return (
            <li className={this.actualPath(this.props.pathTo)}>
                <Link className="active" to={this.props.pathTo}>{this.props.text}</Link>
            </li>
        )
    }
}

export default HeaderLi