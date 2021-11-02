function doSomething(value){
   return new Promise((resolve,reject)=>{
        setTimeout(()=>{
            console.log(1111)
            resolve(value)
        },5000)
    })
}

function doSomethingElse(value){
    return new Promise((resolve,reject)=>{
         setTimeout(()=>{
             console.log(22222)
             resolve(value)
         },4000)
     })
 }


 function doThirdThing(value){
    return new Promise((resolve,reject)=>{
         setTimeout(()=>{
             console.log(3333)
             resolve(value)
         },2000)
     })
 }




doSomething(1).then(function(result) {
    const s1 =  result+1
    console.log(s1)
    return doSomethingElse(s1)
  })
  .then(function(newResult) {
     const s2 =  newResult+1
     console.log(s2)
    return doThirdThing(s2)
  })
  .then(function(finalResult) {
    finalResult = finalResult +1
    console.log('Got the final result: '+finalResult)
  })
  .catch()