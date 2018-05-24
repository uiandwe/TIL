```



수열 A가 주어졌을 때, 그 수열의 증가 부분 수열 중에서 합이 가장 큰 것을 구하는 프로그램을 작성하시오.

예를 들어, 수열 A = {1, 100, 2, 50, 60, 3, 5, 6, 7, 8} 인 경우에 합이 

가장 큰 증가 부분 수열은 A = {1, 100, 2, 50, 60, 3, 5, 6, 7, 8} 이고, 합은 113이다.


첫째 줄에 수열 A의 합이 가장 큰 증가 부분 수열의 합을 출력한다.

```


```



var array = [1, 100, 2, 50, 60, 3, 5, 6, 7, 8];
var dp = [1];
for(var i=1; i<array.length; i++){
    dp.push(0);
}


var max = 0;
var path = [];
var dd = [];
for(var i=1;i<array.length;i++) {
    dp[i] = array[i];
    // i 를 기준으로 인덱스 0 에서부터 i-1까지 체크한다 
    // 길이를 기준
    path.push(array[i]);
    for(var j=0;j<i;j++) {
        if (array[i] > array[j] && dp[j] + array[i] > dp[i]) {
            // 증가 수열
            dp[i] = dp[j] + array[i];
            path.push(array[j]);
            
        }
    }
    
    if (max < dp[i]) {
        max = dp[i];
    }
    console.log(path);
    path = [];
}

console.log(dp);
console.log(max);


````


```




수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.

예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.



첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.

```


```




var array = [3,2,5,2,3,1,4];

var max = 0;
var dp = [1];
for(var i=1;i<array.length;i++) {
    dp[i] = 1;
    // i 를 기준으로 인덱스 0 에서부터 i-1까지 체크한다 
    // 길이를 기준
    for(var j=0;j<i;j++) {
        if (array[i] > array[j] && dp[j] + 1 > dp[i]) {
            // 증가 수열
            dp[i] = dp[j] + 1;
            
        }
    }

    
    
    if (max < dp[i]) {
        max = dp[i];
    }
}

console.log(dp);
var path = [];
var point = 0;
for(var i=dp.length-1; i>=0; i--){
    if(dp[i] == max && point == 0){
        path.push(array[i]);
        point = i;
    }
    else if(dp[i] == dp[point]-1){
        path.push(array[i]);
        point = i;
    }
}
console.log(path.reverse());
console.log(max);





```

