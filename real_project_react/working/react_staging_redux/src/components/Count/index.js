import React, { Component } from 'react'
import store from '../../redux/store'

import {createIncrement,createDecrement,createIncrementAsync} from'../../redux/count_action'

export default class Count extends Component {
    add = () =>{
        const {value} = this.selectValue
        store.dispatch(createIncrement(value*1))
    }
    jian = () =>{
        const {value} = this.selectValue
        store.dispatch(createDecrement(value*1))
        
    }
    oddAdd = () =>{        
        const {value} = this.selectValue
        const count = store.getState()
        if(count % 2 !== 0){
            store.dispatch(createIncrement(value*1))
        }        
    }
    asyncAdd = () =>{        
        const {value} = this.selectValue
        store.dispatch(createIncrementAsync(value*1,1000))
    }



    render() {
        return (
            <div>
                <h1>Total number: {store.getState()} </h1>
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
