const input = require('fs')
  .readFileSync('/dev/stdin')
  .toString()
  .trim()
  .split('\n')
const [n, ...inputs] = input
const arrayA = inputs[0]
  .split(' ')
  .map((num) => +num)
  .sort((a, b) => a - b)
const arrayB = inputs[1]
  .split(' ')
  .map((num) => +num)
  .sort((a, b) => b - a)

function solution(n, A, B) {
  let result = 0
  for (let i = 0; i < n; i++) {
    result += A[i] * B[i]
  }
  console.log(result)
}
solution(n, arrayA, arrayB)