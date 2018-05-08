만족하는 경우의 수를 구하시오
AA + BC = 100

위 식이 만족하도록 A,B,C를 대체할 수 있는 수를 찾으시오. 단,A,B,C는 서로 다른 한자리 수이다. 
여기서는 {11+89,22+78,33+67,44+56,66+34,77+23,88+12} 와 같이 총 7가지의 경우의 수가 발생한다.

입력으로는 p, q, r 3개의 문자열이 주어지는데, 각각 숫자와 알파벳의 조합으로 이루어져 있다. 
이때,p+q=r의 식이 만족되는 경우의 수를 출력하시오.

예) AB + CD = EEE
 ```
var p = 'AB';
var q = 'CD';
var r = 'EEE';

68 + 43 = 111
69 + 42 = 111
72 + 39 = 111
75 + 36 = 111
76 + 35 = 111
79 + 32 = 111
84 + 27 = 111
85 + 26 = 111
86 + 25 = 111
87 + 24 = 111

24가지
```

```

String.prototype.replaceAll = function(target, replacement) {
return this.split(target).join(replacement);
};

function strToIntLnegth(str){
    return parseInt(str).toString().length;
}

var p = 'AA';
var q = 'BC';
var r = '100';

var p = 'XYZ';
var q = 'XY';
var r = '6PP';

var totalCount = 0;

var re = new RegExp("[A-Z]", "ig");

var charHash = {};
var charArray = [];
var hashKeyArray = [];
var hashIntArray = [];

function textMatchRegExp(){
    charArray = p.match(re);
    charArray = charArray.concat(q.match(re));
    charArray = charArray.concat(r.match(re));

    for(var i=0; i<charArray.length; i++){
        if(charArray[i] != undefined && charArray[i] != null){
            charHash[charArray[i]] = charArray[i]
        }
    }
}


function getUniquePermutation(){
    hashKeyArray = Object.keys(charHash);
    var start = Math.pow(10, hashKeyArray.length-1);
    var end = Math.pow(10, hashKeyArray.length)-1;

    var intHash = {};
    for(var i= start; i<end; i++){
        var textInt = i.toString();
        var uniqeCheck = true;
        for(var j=0; j<textInt.length; j++){
            var re = new RegExp(textInt[j], "ig");
            if(textInt.match(re).length >= 2){
                uniqeCheck = false;
                break;
            }
        }

        if(uniqeCheck == true){
            intHash[i] = i; //중복되지 않는 숫자 해쉬
        }
    }
    hashIntArray = Object.keys(intHash); 
}

function runFormula(){
    for(var i=0; i<hashIntArray.length; i++){
        var hashInt = hashIntArray[i];
        var strHash = hashInt.toString();
        var temp_p = p;
        var temp_q = q;
        var temp_r = r;
        for(var j=0; j<strHash.length; j++ ){
    
            temp_p = temp_p.replaceAll(hashKeyArray[j], strHash[j]);
            temp_q = temp_q.replaceAll(hashKeyArray[j], strHash[j]);
            temp_r = temp_r.replaceAll(hashKeyArray[j], strHash[j]);
        }
    
        if(parseInt(temp_p) + parseInt(temp_q) == parseInt(temp_r)){//계산식 확인 
            if(strToIntLnegth(temp_p) == p.length && strToIntLnegth(temp_q) == q.length && strToIntLnegth(temp_r) == r.length){ //자릿수 확인
                console.log(temp_p ,"+", temp_q,"=", temp_r)
                totalCount++;
            }
        }
    }
}


function run(){
    textMatchRegExp();
    getUniquePermutation();
    runFormula();
    console.log("totalCount", totalCount);
}

run();


24 + 87 = 111
25 + 86 = 111
26 + 85 = 111
27 + 84 = 111
32 + 79 = 111
35 + 76 = 111
36 + 75 = 111
39 + 72 = 111
42 + 69 = 111
43 + 68 = 111
48 + 63 = 111
49 + 62 = 111
62 + 49 = 111
63 + 48 = 111
68 + 43 = 111
69 + 42 = 111
72 + 39 = 111
75 + 36 = 111
76 + 35 = 111
79 + 32 = 111
84 + 27 = 111
85 + 26 = 111
86 + 25 = 111
87 + 24 = 111
totalCount 24


```
