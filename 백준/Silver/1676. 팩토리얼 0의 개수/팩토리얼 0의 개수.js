const fs = require('fs');
const N = +(fs.readFileSync("./dev/stdin").toString().trim());

let arr = [0, 0];

for (let i = 2; i <= N; i++) {
  let temp = i;

  while (temp % 2 == 0) {
    if (temp % 2 == 0) {
      arr[0]++;
      temp /= 2;
    }
  }

  temp = i;
  while (temp % 5 == 0) {
    if (temp % 5 == 0) {
      arr[1]++;
      temp /= 5;
    }
  }
}

console.log(Math.min(...arr))