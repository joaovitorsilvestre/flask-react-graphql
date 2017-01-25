import React from 'react'

class Product extends React.Component {
    render() {
        return (
            <div className="col-sm-6 col-md-2">
                <div className="thumbnail">
                    <div className="caption">
                        <h3>{this.props.name}</h3>
                        <p>Preço: R${this.props.price}</p>
                        <p>
                            <a href="#" className="btn btn-primary" role="button">Adicionar ao carrinho</a>
                        </p>
                    </div>
                </div>
            </div>
        )
    }
}

export default Product