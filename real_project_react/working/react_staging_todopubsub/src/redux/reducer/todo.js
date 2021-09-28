import {ADD,UPDATE} from "../../until/constant"


const initSate =  [
    { id: "001", name: "eating2", done: true },
    { id: "002", name: "working2", done: false }
]
export default function personReducer(perSta = initSate ,action){
    const {type,data} = action
    switch(type){
        case ADD:
            return [data,...perSta]
        case UPDATE:
            return perSta = data
        default:
            return perSta
    }

}