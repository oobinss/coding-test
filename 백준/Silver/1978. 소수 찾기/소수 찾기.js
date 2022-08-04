const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split(/\s+/)
const [n, ...arr] = input.map((v) => +v)

let answer = 0

for (let i = 0; i < n; i++) {
  if (arr[i] === 1) {
    continue
  } else {
    let count = 0
    for (let j = 2; j < arr[i]; j++) {
      if (arr[i] % j === 0) {
        count++
      }
    }
    if (count === 0) {
      answer++
    }
  }
}
console.log(answer)
