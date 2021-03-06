// for 循环
//
const arr = [1, 2, 3, 4, 5]

// 可以break 可以 continue
for (let i = 0; i < arr.length; i++) {
  if (arr[i] === 2) {
    continue
  }
  // console.log(arr[i])
}
// forEach

//不支持 break 和 continue
arr.forEach(function (item) {
  if (item === 2) {
    // continue
  }
  // console.log(item)
})

// every
// 可以 break 和 continue 但不同是 break：return false  continue： return true
arr.every(function (item) {
  if (item === 2) {

  } else {
    // console.log(item)
  }
  return true
})
// for in
// arr.a = 8

// 可以 continue 和break

// for in 可以拿到 index 值  for of 拿到value值

for (let index in arr) {
  if (arr[index] === 2) {
    break
  }
  // console.log(index, arr[index])
}
// for of 
//可以 break he continue
for (let item of arr) {
  // console.log(item)
  if(item === 2){
    continue
  }
  //console.log(item)
}

const Price = {
  A: [1.5, 2.3, 4.5],
  B: [3, 4, 5],
  C: [0.5, 0.8, 1.2]
}

for (let key in Price) {
  // console.log(key, Price[key])
}

// 第二小节 转换
//
// let args = [].slice.call(arguments) // collection
// let imgs = [].slice.call(document.querySelectorAll('img')) // NodeList
// console.log(args)

// let args = Array.from(arguments)
// let imgs = Array.from(document.querySelectorAll('img'))
// imgs.forEach()
// Array.from(arrayLike,mapFn,thisArg)
// let array = Array(5)
// for (let i = 0, len = array.length; i < len; i++) {
//   array[i] = 1
// }
// console.log(array)
// from 创建新数组
let array = Array.from({ length: 5 }, function () { return 1 })
// console.log(array)
// {0:'a',1:'b',length:2}

// 第三小节 生成新数组
// let array = Array(5)
// let array = []

// let array = Array.of(1)
// console.log(array)
// Array.prototype.fill
//
// let array = Array(5).fill(7)
// console.log(array)
// Array.fill(value,start,end)
let array = [1, 2, 3, 4, 5]
// console.log(array.fill(8, 2, 4))
// 满足条件所以值
// let find = array.filter(function (item) {
//   return item % 2 === 0
// })
// console.log(find)
// find 只找第一个值
// Array.prototype.find
let find = array.findIndex(function (item) {
  return item % 2 === 0
})
console.log(find)
// Array.prototype.findIndex
