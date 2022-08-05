let result = [];

function selfNumber(N){
    let total_sum = N;
    while(true){
        if(N===0){
            break;
        };
        total_sum += N%10;
        N = Math.floor(N/10);      
    }
    result[total_sum] = N;
    return total_sum;
   
}
for(let i=1; i<10001; i++){
    selfNumber(i);
    if(result[i]===undefined){
        console.log(i);
    }
};
