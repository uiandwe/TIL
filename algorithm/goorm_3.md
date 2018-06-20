```



function palindrome(num, index){
    if(num >= 100000 || index > 3){
        return -1;
    }
    
    var wjd = num.toString();
    var dur = num.toString().split("").reverse().join("");
    if(wjd == dur){
        return dur;
    }
    else {
        return palindrome(parseInt(wjd) + parseInt(dur), index+1);
    }
}

console.log(palindrome(57, 1))
console.log(palindrome(78, 1))
console.log(palindrome(85, 1))
console.log(palindrome(196, 1))

```
