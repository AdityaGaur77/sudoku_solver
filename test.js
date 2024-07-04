let array = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

for(let i = 0; i < array.length; i++){
    console.log(array[i])// add + " " after arrays[i] for the output to look cleaner
}
console.log();
for (let i = 0; i < array.length; i++) { 
    for (let j = 0; j < array[i].length; j++) { 
        console.log(array[j] + " ")
    } 
    console.log(); 
    break;
}

