import React, { Component } from 'react'
import './index.css'

export default class Item extends Component {
    handleCheck(e,id){
        console.log(e.target.checked)
        this.props.updateTodo(id,e.target.checked)
    }

    handleDel(id){
        this.props.deleteTodo(id)
        
    }

    render() {
        const {name,id,done} = this.props
        console.log(name,"........")
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
