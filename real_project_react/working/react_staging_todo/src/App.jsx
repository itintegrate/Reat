import React, { Component } from 'react'
import Footer from './components/Footer'
import Header from './components/Header'
import List from './components/List'
import "./App.css"

export default class App extends Component {


    state = {
        todos:[
            {id:"001",name:"eating",done:true},
            {id:"002",name:"working",done:false}
        ]
    }

    addToDo = (todoObj)=>{
     
     const {todos} = this.state
     const newTodos = [todoObj,...todos]
     this.setState({todos:newTodos})     

    }

    updateTodo = (id,done)=>{
     const {todos} = this.state
     const newTodos = todos.map(todo=>{
         if(todo.id === id){             
             return {...todo,done}
         }
         else{
             return todo
         }
     
     })
     this.setState({todos: newTodos})
      
    }

    deleteTodo = (id) =>{
        const {todos} = this.state
        const newTodo = todos.filter(todo => {
            return todo.id !== id
        })
        this.setState({todos:newTodo})
      
    }

    checkAllTodo = (done) =>{
        const {todos} = this.state
        const newTodo = todos.map(todo=>{
            return {...todo,done}
        })
        this.setState({todos:newTodo})
     
    }

    clearAllDone = () =>{
       const {todos} = this.state
       const newTodos = todos.filter(todo => {
           return !todo.done
       })
       this.setState({todos:newTodos})
    }
    

    render() {
        const {todos} = this.state
        return (
            <div className="todo-container">
                <div className="todo-wrap">
                <Header addToDo = {this.addToDo}/>
                <List todos = {todos} updateTodo={this.updateTodo} deleteTodo={this.deleteTodo} />
                <Footer clearAllDone = {this.clearAllDone}/>
                <button onClick={()=>this.deleteTodo("002",false)}>DelTodo</button>
                <button onClick={()=>this.checkAllTodo(true)}>checkAllTodo</button>
                <button onClick={()=>this.clearAllDone()}>clearAllDone</button>
                </div>
                

            </div>
        )
    }
}
