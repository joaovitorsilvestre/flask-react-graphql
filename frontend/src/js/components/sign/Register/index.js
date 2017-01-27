import React from 'react'
import axiosInstance from '../../../config'
import classNames from 'classnames'

class Register extends React.Component {
    constructor() {
        super()
        this.state = {
            error: null,
            success: null
        }
    }

    updateInputValue(evt) {
        this.setState({
            [evt.target.id]: evt.target.value
        })
    }

    send() {
        axiosInstance.post('/register', {
            name: this.state.name,
            password: this.state.password
        }).then((res) => {
            this.setState({
                success: res.data.success
            })
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
                                <button className="btn btn-info" onClick={this.send.bind(this)}>Registrar</button>
                            </div>
                        </div>
                    </div>
                </form>
            </div>
        )
    }
}

export default Register