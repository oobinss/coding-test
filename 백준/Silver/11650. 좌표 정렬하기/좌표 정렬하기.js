const input = require('fs')
  .readFileSync('/dev/stdin')
  .toString()
  .trim()
  .split('\n');
const N = input.shift();
input.sort(
  (a, b) =>
    Number(a.split(' ')[0]) - Number(b.split(' ')[0]) ||
    Number(a.split(' ')[1]) - Number(b.split(' ')[1]),
);
console.log(input.join('\n'));