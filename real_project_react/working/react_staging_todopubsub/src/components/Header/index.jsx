import React, { Component } from 'react'
import {nanoid} from "nanoid"
import PubSub from 'pubsub-js'
import './index.css'


export default class Header extends Component {

    handleOnkeyup = (event) =>{
       
        if(event.key === 'Enter'){
         const value = {id:nanoid(),name:event.target.value.trim(),done:false}
         console.log(value)
         PubSub.publish("Search_value",value)
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
