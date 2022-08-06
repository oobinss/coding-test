const fs=require('fs');
let input=fs.readFileSync('/dev/stdin').toString().trim();
let result=0;
while(true){
    if(input%5===0){
        console.log(input/5 + result)
        break;
    } else if(input <= 0){
        console.log(-1)
        break;
    }
    input = input - 3
    result++
}