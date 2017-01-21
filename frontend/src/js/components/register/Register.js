import React from 'react'
import axios from 'axios'

const instance = axios.create({
    baseURL: 'http://localhost:5000',
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
    }
});

class Register extends React.Component {
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
        instance.post('/register', {
            name: this.state.name,
            cpf: this.state.cpf
        }).then((response) => {
            console.log(response)
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
                            <label htmlFor="cpf">CPF</label>
                            <input type="text" id="cpf" className="form-control" onChange={this.updateInputValue.bind(this)}/>
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