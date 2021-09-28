import React, { Component } from 'react'
import { connect } from 'react-redux'
import {createAddPerson} from "../../redux/action/person"
import {nanoid} from 'nanoid'

class Person extends Component {
    addPerson = () =>{
        const newperson = {id:nanoid(),name:this.settingName.value,age:this.settingAge.value}
        this.props.addPerson(newperson)    
    }

    render() {
        return (
            <div>
                <input ref = {v => this.settingName = v}/>: Name
                <input ref = {v => this.settingAge = v}/>: Age 
                <button onClick={this.addPerson}>add Person</button>
                <div>
                    <ul>
                        {
                           this.props.person.map(v => {
                              return <li key={v.id}>Name:{v.name}---Age: {v.age}</li>
                           }) 

                        }
                        
                    </ul>
                </div>
            </div>
        )
    }
}
export default connect(
    state =>({
        person:state.personReducer
    }),
    {
        addPerson:createAddPerson
    }

)(Person)
