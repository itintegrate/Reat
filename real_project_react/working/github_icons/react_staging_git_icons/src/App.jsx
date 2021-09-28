import React, { Component } from 'react'
import "./App.css"
import List from './components/List'
import Search from './components/Search'

export default class App extends Component {
    render() {
        return (
            <div>
                <Search />
                <List />
            </div>
        )
    }
}
