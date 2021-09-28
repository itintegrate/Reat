import React, { Component } from 'react'
import { connect } from 'react-redux'
import PubSub from 'pubsub-js'
import './index.css'


class Footer extends Component {

    handleClear = () =>{
        PubSub.publish("handleClear","click")
    }
    render() {
        
        const doneCount = this.props.todos.reduce((pre,todo)=>
        {
            return pre+ (todo.done ? 1: 0)
            // let new_v = 0
            // if(todo.done){
            // new_v = pre + 1
            // }else{
            // new_v = pre + 0
            // }            
            // return new_v

        } ,0)
      
        return (
            <div className="todo-footer">
                {/* <label>
                    <input type="checkbox"  />
                </label> */}
                <span><span>finished  {doneCount}</span> / Total {this.props.todos.length} </span>
                <button onClick={this.handleClear} className="btn btn-danger">Clear finished tasks</button>
            </div>
        )
    }
}
export default connect(
    state =>({
        todos:state.todoReducer
    }) 
)(Footer)

