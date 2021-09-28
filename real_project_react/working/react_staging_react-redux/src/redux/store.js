import {createStore,applyMiddleware,combineReducers} from 'redux'

import countReducer from './reducer/count'
import personReducer from './reducer/person'

import {composeWithDevTools} from 'redux-devtools-extension'


import thunk from 'redux-thunk'


const allReducer = combineReducers({
    countReducer,personReducer
})

export default createStore(allReducer,composeWithDevTools(applyMiddleware(thunk)))