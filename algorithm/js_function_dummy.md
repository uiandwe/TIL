### 범위 array 구하기 
```

function range(start, end){

    if(!Number.isInteger(start) || !Number.isInteger(end)){
        return -1;
    }

    var returnArray = [];

    if(start > end){
        var temp = start;
        start = end;
        end = start;
    }

    for(var i=start; i<=end; i++){
        returnArray.push(i);
    }

    return returnArray;
}




ex ) console.log(range(1, 10));
     [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
     
     console.log(range("a", 10)); //int형이 아닐때 -1 리턴 
     -1
     
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

### 모든 경우의 수 
```
function numberCases(array){
    if(array.length <= 1){
        return array;
    }
    else{
        var hash = {};
        var returnArray = [];
        var copyArray = array;
        var copyArray = JSON.parse(JSON.stringify(array))
        for(var i=0; i<array.length; i++){
            var array = JSON.parse(JSON.stringify(copyArray))
            
            var temp = array[0];
            array[0] = array[i];
            array[i] = temp;         
            for(var j=1; j<array.length; j++){
                for(var k=j; k<array.length; k++){
                    var temp = array[k];
                    array[k] = array[j];
                    array[j] = temp;
                
                    if(!hash[array.join(",")]){
                        hash[array.join(",")] = array.join(",");
                    }
                }
            }
        }

        var keysArray = Object.keys(hash);
        for (var i = 0; i < keysArray.length; i++) {
            returnArray.push(keysArray[i])
        }
            
        return returnArray;
    }
}

console.log(numberCases([1, 2, 3]));
console.log(numberCases([1, 2, 3, 4]));
console.log(numberCases(['a', 'b', 'c']));


[ '1,2,3', '1,3,2', '2,1,3', '2,3,1', '3,2,1', '3,1,2' ]
[ '1,2,3,4',
  '1,3,2,4',
  '1,4,2,3',
  '1,4,3,2',
  '2,1,3,4',
  '2,3,1,4',
  '2,4,1,3',
  '2,4,3,1',
  '3,2,1,4',
  '3,1,2,4',
  '3,4,2,1',
  '3,4,1,2',
  '4,2,3,1',
  '4,3,2,1',
  '4,1,2,3',
  '4,1,3,2' ]
[ 'a,b,c', 'a,c,b', 'b,a,c', 'b,c,a', 'c,b,a', 'c,a,b' ]



```
