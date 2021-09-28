import {INCREMENT,DECREMENT} from "../../until/constant"


const initSate = 0
export default function countReducer(perSta = initSate ,action){
    const {type,data} = action

    switch(type){
        case INCREMENT:
            return perSta + data
        case DECREMENT:
            return perSta - data
        default:
            return perSta
    }

}