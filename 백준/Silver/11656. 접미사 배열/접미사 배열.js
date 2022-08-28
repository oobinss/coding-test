var fs = require('fs');
var input = fs.readFileSync('/dev/stdin').toString().split('');
var stack = [...input];
var answer = [];
var tmp = [];
for(var i=0; i<input.length; i++){
    tmp.unshift(stack.pop());
    answer.push(tmp.join('').trim());
}
console.log(answer.sort().join('\n').trim());