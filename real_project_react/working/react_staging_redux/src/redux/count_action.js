import {INCREMENT,DECREMENT} from "../until/constant"

export const createIncrement =  data => ({type:INCREMENT,data})
export const createDecrement =  data => ({type:DECREMENT,data})
export const createIncrementAsync = (data,time) => {
    return (dispatch) => {
        setTimeout(()=>{
            dispatch(createIncrement(data))
        },time)
    }
}