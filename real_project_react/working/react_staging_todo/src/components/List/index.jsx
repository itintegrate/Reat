import React, { Component } from 'react'
import "./index.css"
import Item from '../Item'

export default class List extends Component {
    render() {
        const {todos,updateTodo,deleteTodo} = this.props
        console.log(todos)
        return (
            <ul className="todo-main">
                {
                    todos.map(todo => {
                        console.log(todo,"xxxxx")
                        return <Item key = {todo.id} {...todo} updateTodo={updateTodo} deleteTodo={deleteTodo}/>
                    })
                }
                 

            </ul>
        )
    }
}
