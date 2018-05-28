```


var str = "hello?!";
var str1 = "";
function rec(index){

    if(str1.length == str.length ){
        return;
    }
    else{
        str1 += str.substr(str.length-1-index, 1);
        rec(index+1);
    }
    return ;
}


console.log(str);
rec(0);
console.log(str1);


```
