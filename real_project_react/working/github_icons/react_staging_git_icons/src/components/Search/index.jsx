import React, { Component } from 'react'
import PubSub from 'pubsub-js'
import axios from "axios"
import "./index.css"
export default class Search extends Component {


    handleValue = () => {
        const { inputvalue: { value: keyWord } } = this
        console.log(keyWord)
        PubSub.publish("Search_value", { isFirst: false, isLoading: true })
        axios.get(`/api1/search/users?q=${keyWord}`).then(
            res => {
                PubSub.publish("Search_value",{isLoading:false,users:res.data.items})
            }
        ).catch(
            error => {
                PubSub.publish("Search_value",{isLoading:false,err:error.message})
            }
        )


        



    }

    render() {
        return (
            <div>
                <section className="jumbotron">
                    <h3 className="jumbotron-heading">Search git User</h3>
                    <div>
                        <input ref={r => this.inputvalue = r} type="text" placeholder="输入关键词点击搜索" />&nbsp;
                        <button onClick={this.handleValue}>Search</button>
                    </div>
                </section>
            </div>
        )
    }
}
