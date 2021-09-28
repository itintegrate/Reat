// import * as Mod from './lesson2-14-mod'

// let test = new Mod.Test()
// console.log(test.id)
// let animal = new Mod.Animal()
// console.log(animal.name)
// let people = new Mod.default()
// console.log(people.id)
// 如果是node.js 必须在package。js 里面加上 {"type": "module"}

import People, {Animal,Test,say} from './lesson_export-mod.js'

let test = new Test()
console.log(test.id)
let people = new People()
console.log(people.id)
let animal = new Animal()
console.log(animal.name)
say()