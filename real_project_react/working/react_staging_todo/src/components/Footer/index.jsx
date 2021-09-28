import React, { Component } from 'react'
import './index.css'

export default class Footer extends Component {

    handleClear = () =>{
        this.props.clearAllDone()
    }

    render() {
        return (
            <div className="todo-footer">
                <label>
                    <input type="checkbox"  />
                </label>
                <span><span>finished </span> / Total </span>
                <button onClick={this.handleClear} className="btn btn-danger">Clear finished tasks</button>
            </div>
        )
    }
}
