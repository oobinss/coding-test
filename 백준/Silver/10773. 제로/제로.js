const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

const [n, ...arr] = input.map((v) => +v)
let sum = []
arr.map((pushNumber) => {
  if (pushNumber === 0) {
    sum.pop()
    return
  }
  sum.push(pushNumber)
})
let answer = sum.length ? sum.reduce((pre, cur) => pre + cur,0) : 0
console.log(answer)
