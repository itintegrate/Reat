function a() {
    setTimeout(() => {
        console.log("print AA")
        ite.next("I am AA")
    }, 2000)
}

function b(v) {
    setTimeout(() => {
        console.log("print BB")
        ite.next(v + "I am BB")
    }, 5000)
}

function c(v) {
    setTimeout(() => {
        console.log("print CC")
        ite.next(v + "I am CC")
    }, 1000)
}


function* gen() {
    const a_a = yield a()
    console.log(a_a)
    const b_b = yield b(a_a)
    console.log(b_b)
    const c_c = yield c(b_b)
    console.log(c_c)
}

let ite = gen()
ite.next()