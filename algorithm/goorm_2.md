```


function checkLarge(a, b){
    return `${a}${b}` < `${b}${a}`;
};

function maxNumber(arr){
    return +arr.sort(checkLarge).join('');
};



function checkSmall(a, b){
    return `${a}${b}` > `${b}${a}`;
};

function minNumber(arr){
    return +arr.sort(checkSmall).join('');
};

var max = maxNumber([3, 30, 34, 5, 9]);
var min = minNumber([3, 30, 34, 5, 9]);

console.log(max+min);

var max = maxNumber([1, 2, 3]);
var min = minNumber([1, 2, 3]);

console.log(max+min);


var max = maxNumber([2,9,10,21,24]);
var min = minNumber([2,9,10,21,24]);

console.log(max+min);

```
