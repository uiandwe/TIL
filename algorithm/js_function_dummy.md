### 범위 array 구하기 
```

function range(start, end){

    if(!Number.isInteger(start) || !Number.isInteger(end)){
        return -1;
    }

    var returnArray = [];

    for (var i = Math.min(start, end); i <= Math.max(start, end); i++) {
        returnArray.push(i);
    }
    
    return returnArray;
}




ex ) console.log(range(1, 10));
     [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
     
     console.log(range("a", 10)); //int형이 아닐때 -1 리턴 
     -1
     
```

### 두 수 사이의 합
```
function adder(a, b, s = 0){
  for (var i = Math.min(a, b); i <= Math.max(a, b); i++) s += i;
  return s;
}


function adder(a, b){
    return (a+b)*(Math.abs(b-a)+1)/2;
}

```


### 문자열 뒤집기
```
function reverseString(str){
    return str.split("").reverse().join("");
}
```

### 배열 딥카피 
```
var clonedArray = JSON.parse(JSON.stringify(nodesArray))
```

### 모든 경우의 수 ( 순열 )
```
// var array = [1,2,3,4];
// var array = [1,2,3];
var array = ['a','b','c'];

var returnArray = [];

function perm(arr, depth) { 
    if (depth == arr.length) { 
        returnArray.push(arr);
        return; 
    } 
    
    for (var i = depth; i < arr.length; i++) { 
        swap(arr, i, depth); 
        perm(arr, depth + 1); 
        swap(arr, i, depth); 
    } 
}

function swap(arr, i, j) { 
    var temp = arr[i]; 
    arr[i] = arr[j]; 
    arr[j] = temp; 
}


perm(array, 0);
console.log(returnArray);


[ [ 1, 2, 3 ],
  [ 1, 3, 2 ],
  [ 2, 1, 3 ],
  [ 2, 3, 1 ],
  [ 3, 2, 1 ],
  [ 3, 1, 2 ] ]
  
[ [ 1, 2, 3, 4 ],
  [ 1, 2, 4, 3 ],
  [ 1, 3, 2, 4 ],
  [ 1, 3, 4, 2 ],
  [ 1, 4, 3, 2 ],
  [ 1, 4, 2, 3 ],
  [ 2, 1, 3, 4 ],
  [ 2, 1, 4, 3 ],
  [ 2, 3, 1, 4 ],
  [ 2, 3, 4, 1 ],
  [ 2, 4, 3, 1 ],
  [ 2, 4, 1, 3 ],
  [ 3, 2, 1, 4 ],
  [ 3, 2, 4, 1 ],
  [ 3, 1, 2, 4 ],
  [ 3, 1, 4, 2 ],
  [ 3, 4, 1, 2 ],
  [ 3, 4, 2, 1 ],
  [ 4, 2, 3, 1 ],
  [ 4, 2, 1, 3 ],
  [ 4, 3, 2, 1 ],
  [ 4, 3, 1, 2 ],
  [ 4, 1, 3, 2 ],
  [ 4, 1, 2, 3 ] ]


[ [ 'a', 'b', 'c' ],
  [ 'a', 'c', 'b' ],
  [ 'b', 'a', 'c' ],
  [ 'b', 'c', 'a' ],
  [ 'c', 'b', 'a' ],
  [ 'c', 'a', 'b' ] ]



```


### 문자열에서 index 의 문자 수정 

```

String.prototype.replaceAt=function(index, character) {
    return this.substr(0, index) + character + this.substr(index+character.length);
}
var str = "test";

console.log(str.replaceAt(1, 'Z'));
console.log(str);

tZst
test

```

### string replaceAll

```

String.prototype.replaceAll = function(target, replacement) {
    return this.split(target).join(replacement);
};

```




