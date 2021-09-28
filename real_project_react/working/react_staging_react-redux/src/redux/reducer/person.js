import {ADDPERSON} from "../../until/constant"


const initSate = [{id:"001",name:"Jin",age:"20"}]
export default function personReducer(perSta = initSate ,action){
    const {type,data} = action

    switch(type){
        case ADDPERSON:
            return [data,...perSta]
        default:
            return perSta
    }

}