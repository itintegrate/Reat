import React, { Component } from 'react'
import PubSub from 'pubsub-js'
import './index.css'

export default class Item extends Component {
    handleCheck(e,id){
        console.log(e.target.checked)
        PubSub.publish("handleCheck",{id,done:e.target.checked})
    }

    handleDel(id){
        PubSub.publish("handleDel",id)
        
    }

    render() {
        const {name,id,done} = this.props    
        return (
            <li>
                <label>
                <input type="checkbox" checked={done} onChange={event => this.handleCheck(event,id)}/>
                    <span>{name}</span>
                </label>
                <button onClick={()=>this.handleDel(id)} className="btn btn-danger" >DEL</button>
            </li>
        )
    }
}
