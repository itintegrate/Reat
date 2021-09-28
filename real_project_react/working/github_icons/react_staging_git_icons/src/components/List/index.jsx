import React, { Component } from 'react'
import PubSub from 'pubsub-js'
import "./index.css"
export default class List extends Component {

    state = { //初始化状态
        users: [], //users初始值为数组
        isFirst: true, //是否为第一次打开页面
        isLoading: false,//标识是否处于加载中
        err: '',//存储请求相关的错误信息
    }

    componentDidMount() {
        this.token = PubSub.subscribe("Search_value", (_, stateObj) => {
            console.log("xxxxxx",_,stateObj)
            this.setState(stateObj)
            console.log(this.state)
        })
    }
    componentWillUnmount() {
        PubSub.unsubscribe(this.token)

    }


    render() {
        const { users, isFirst, isLoading, err } = this.state
        return (
            <div>
                {
                    isFirst ? <h2>Please enter keyword</h2> :
                        isLoading ? <h2>it is loading.....</h2> :
                            err ? <h2>{err}</h2> :
                                users.map(user => {
                                    return (
                                        <div key={user.id} className="card">
                                            <a rel="noreferrer" href={user.html_url} target="_blank">
                                                <img alt="head_portrait" src={user.avatar_url} style={{ width: '100px' }} />
                                            </a>
                                            <p>{user.login}</p>
                                        </div>
                                    )
                                })
                }
            </div>
        )
    }
}
