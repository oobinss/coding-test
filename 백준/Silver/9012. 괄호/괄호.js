const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const len = input.shift();
const result = [];

for (let i = 0; i < len; i++) {
    let cnt = 0;
    
    for (let idx of input[i]) {
        cnt += idx === "(" ? 1 : -1;
        
        if (cnt < 0) break;
    }
    
    result.push(cnt === 0 ? 'YES' : "NO");
}

console.log(result.join('\n'));