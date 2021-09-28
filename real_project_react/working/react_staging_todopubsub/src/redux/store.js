import {createStore,applyMiddleware,combineReducers} from 'redux'

import todoReducer from './reducer/todo'

import {composeWithDevTools} from 'redux-devtools-extension'


import thunk from 'redux-thunk'


const allReducer = combineReducers({todoReducer})

export default createStore(allReducer,composeWithDevTools(applyMiddleware(thunk)))