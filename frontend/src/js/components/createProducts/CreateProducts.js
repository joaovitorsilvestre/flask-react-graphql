import React from 'react'
import axiosInstance from '../../config'

class CreateProducts extends React.Component {
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
        axiosInstance.post('/create-product', {
            name: this.state.name,
            price: this.state.price
        }).then((res) => {
            this.setState({
                success: res.data.success
            })
        })
    }

    render() {
        return (
            <div>
                <form>
                    <div className="form-group">
                        <div className="col-md-4 col-md-offset-4">
                            <label htmlFor="name">Nome</label>
                            <input type="text" id="name" className="form-control" onChange={this.updateInputValue.bind(this)}/>
                            <label htmlFor="price">Preço</label>
                            <input type="number" step="0.01" min="0.01" max="99" id="price" className="form-control" onChange={this.updateInputValue.bind(this)}/>
                            <br/>
                            <div className="col-md-6 col-md-offset-3 text-center">
                                <button className="btn btn-info" onClick={this.send.bind(this)}>Criar</button>
                            </div>
                        </div>
                    </div>
                </form>
            </div>
        )
    }
}

export default CreateProducts