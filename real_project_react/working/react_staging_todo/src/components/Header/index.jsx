import React, { Component } from 'react'
import {nanoid} from "nanoid"
import './index.css'


export default class Header extends Component {

    handleOnkeyup = (event) =>{
       
        if(event.key === 'Enter'){
         const value = {id:nanoid(),name:event.target.value.trim(),done:"false"}
         console.log(value)
         this.props.addToDo(value)
         event.target.value = ""
            
        }

    }
    render() {

        return (
            <div className="todo-header">
                <input type="text" onKeyPress={this.handleOnkeyup} placeholder="put your task" />
            </div>
        )
    }
}
