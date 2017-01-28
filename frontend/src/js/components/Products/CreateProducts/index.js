import React from 'react'
import { graphql } from 'react-apollo'
import gql from 'graphql-tag'

class CreateProducts extends React.Component {
    constructor() {
        super()
        this.state = {
            error: null,
            success: null
        }
    }

    onClick() {
        this.props.mutate({ variables: { name: this.state.name, price: this.state.price } })
            .then(({ data }) => {
                console.log('got data', data)
            }).catch((error) => {
                console.log('theres a error in query', error)
            })
    }

    updateInputValue(evt) {
        this.setState({
            [evt.target.id]: evt.target.value
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
                                <button className="btn btn-info" onClick={this.onClick.bind(this)}>Criar</button>
                            </div>
                        </div>
                    </div>
                </form>
            </div>
        )
    }
}
CreateProducts.propTypes = {
    mutate: React.PropTypes.func.isRequired,
};

const submitProduct = gql`
    mutation createProduct($name: String!, $price: Float!) {
        createProduct(name: $name, price: $price) {
            product {
                name
                price
            }
            ok
        }
    }
`

const CreateProductsWithData = graphql(submitProduct)(CreateProducts)

export default CreateProductsWithData