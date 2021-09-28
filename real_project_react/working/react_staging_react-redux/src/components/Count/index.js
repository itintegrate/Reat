import React, { Component } from 'react'

import { connect } from 'react-redux'

import {createIncrement,createDecrement,createIncrementAsync} from'../../redux/action/count'

class Count extends Component {
    add = () =>{
        const {value} = this.selectValue
        this.props.jia(value*1)
    }
    jian = () =>{
        const {value} = this.selectValue
        this.props.jian(value*1)
        
        
    }
    oddAdd = () =>{        
        const {value} = this.selectValue
        if(this.props.count % 2 !== 0){
            this.props.jia(value*1)
        }        
    }
    asyncAdd = () =>{        
        const {value} = this.selectValue
        this.props.jiaAsync(value*1)
    }



    render() {
        return (
            <div>
                <h1>Total number: {this.props.count} </h1>
                <select ref = {v=> this.selectValue = v}>
                    <option>1</option>
                    <option>2</option>
                    <option>3</option>
                </select>

                <button onClick={this.add}>+</button>
                <button onClick={this.jian}>-</button>
                <button onClick={this.oddAdd}>odd +</button>
                <button onClick={this.asyncAdd}>sync +</button>
            </div>
        )
    }
}

export default connect(
    state => ({count:state.countReducer}),
    {
        jia:createIncrement,
        jian:createDecrement,
        jiaAsync:createIncrementAsync
    }

)(Count)