var fs = require('fs');
var input = fs.readFileSync('/dev/stdin').toString().split(' ');
var n = parseInt(input[0]);
var k = parseInt(input[1]);
var arr = [];
var answer = '';
var deleted = [];
for(var i=0; i<n; i++){
    arr[i] = i+1;
}
for(j=0; j<n; j++){
    for(var m=1; m<=k; m++){
        if(m === k){
            deleted.push(arr.shift());
        }else{
            arr.push(arr.shift());
        }
    }
}
answer = '<' +deleted.join(', ') + '>';
console.log(answer);