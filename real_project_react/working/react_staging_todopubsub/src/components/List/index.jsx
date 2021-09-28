import React, { Component } from 'react'
import PubSub from 'pubsub-js'
import { connect } from 'react-redux'
import {AddToDo,UpdateToDo} from "../../redux/action/todo"


import "./index.css"
import Item from '../Item'
class List extends Component {    
    
    componentDidMount() {
        this.token = PubSub.subscribe("Search_value", (_, stateObj) => {
            // const { todos } = this.state
            // this.setState({ todos: [stateObj, ...todos] })
            this.props.AddToDo(stateObj)
        })

        this.token_handleCheck = PubSub.subscribe("handleCheck", (_, stateObj) => {
            // const { todos } = this.state
            const newTodos = this.props.todos.map(todo => {
                if (todo.id === stateObj.id) {
                    // todo.done = stateObj.done
                    // return todo
                    return { ...todo, done: stateObj.done }
                }
                else {
                    return todo
                }
            })
            // this.setState({ todos: newTodos })
            this.props.UpdateToDo(newTodos)
        })

        this.token_handleDel = PubSub.subscribe("handleDel", (_, id) => {
            // const { todos } = this.state
            const newTodos = this.props.todos.filter(todo => {
                return todo.id !== id
            })
            // this.setState({ todos: newTodos })
            this.props.UpdateToDo(newTodos)
        })

        this.token_handleClear = PubSub.subscribe("handleClear", (_, _2) => {          
            // const { todos } = this.state

            const newTodos = this.props.todos.filter(todo => {
                return !todo.done
            })
            // this.setState({ todos: newTodos })
            this.props.UpdateToDo(newTodos)
        })

    }

    componentWillUnmount() {
        PubSub.unsubscribe(this.token)
        PubSub.unsubscribe(this.token_handleCheck)
        PubSub.unsubscribe(this.token_handleDel)
        PubSub.unsubscribe(this.token_handleClear)

    }


    render() {
        return (
            <ul className="todo-main">
                {
                    this.props.todos.map(todo => {
                        return <Item key={todo.id} {...todo} />
                    })
                }
            </ul>
        )
    }
}

export default connect(
    state =>({
        todos:state.todoReducer
    }),{AddToDo,UpdateToDo}
)(List)
