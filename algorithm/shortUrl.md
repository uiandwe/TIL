// 최대한 짧은 문자로 최대 갯수 표현하기
// 62진수 0~Z 까지를 사용함 (md5암호화는 복수개가 생길수 있음 / sha 암호화는 너무 김)
// 진수 계산으로 처음부터 생성

```
var startNumber = 1000;
var numberFormat62String = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";


function numberFormat62(){
    var quotient = 0;
    var author = 0;
    var returnStrArray = [];
    var urlParameter = startNumber;
    for(var i=0;; i++){
        author = urlParameter%numberFormat62String.length;
        urlParameter = Math.floor(urlParameter / numberFormat62String.length);
        quotient = urlParameter;
        returnStrArray.push(numberFormat62String[author]);
        if(quotient <= 0){
            break;
        }
    }
    startNumber += 1;

    return returnStrArray.reverse().join("")
}

console.log(numberFormat62());
console.log(numberFormat62());
console.log(numberFormat62());
console.log(numberFormat62());
```
