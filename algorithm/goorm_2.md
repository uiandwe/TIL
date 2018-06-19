

```




 여러 개의 자연수가 주어질 때, 그 수들을 모두 이어 붙여서 만들 수 있는 가장 큰 수와 가장 작은 수의 합을 
 계산하는 프로그램을 작성하시오. 
 순서는 마음대로 변경할 수 있다.
 예를 들어서 입력으로 주어진 자연수가 { 1, 2, 3 }일 경우, 
 각 숫자들을 이어붙여서 만들 수 있는 가장 큰 수는 321이고 가장 작은 수는 123이다.
 그러므로 이 경우 정답은 444를 출력하면 된다. 


입력 형식
 첫 줄에는 사용할 자연수의 갯수를 나타내는 1이상 10이하의 자연수 N이 주어진다.

두 번째 줄에는 N개의 자연수가 공백으로 구분되어 주어진다.

* 가장 앞 자리가 0인 숫자는 들어오지 않는다.
* 주어지는 N개의 자연수는 모두 1이상 99이하다
 단, 정답은 항상 64비트 정수형 변수로 저장할 수 있도록 입력이 주어진다.



출력 형식

 문제 설명에서 요구한 결과를 한 줄에 자연수로 출력한다.  


입력 1
3
1 2 3

출력 
444

입력 2
5
2 9 10 21 24

출력 2
102634359


```



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
