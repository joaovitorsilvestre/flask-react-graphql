import React from 'react'
import { graphql } from 'react-apollo'
import gql from 'graphql-tag'

import Product from './Product'

class Products extends React.Component {

    static propTypes = {
        data: React.PropTypes.shape({
            loading: React.PropTypes.bool,
            error: React.PropTypes.object,
            products: React.PropTypes.array,
        }).isRequired,
    }

    render () {
        if (this.props.data.loading) {
            return (<div>Loading</div>)
        }

        if (this.props.data.error) {
            console.log(this.props.data.error)
            return (<div>An unexpected error occurred</div>)
        }

        return (
            <div className="row">
                {this.props.data.products.map((product, index) => {
                    return <Product name={product.name} price={product.price} key={index} ></Product>
                })}
            </div>
        )
    }
}

const ProductQuery = gql`query ProductQuery {
  products {
    name
    price
  }
}`

const ProductsWithData = graphql(ProductQuery)(Products)

export default ProductsWithData
