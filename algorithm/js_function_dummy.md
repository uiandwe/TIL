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
