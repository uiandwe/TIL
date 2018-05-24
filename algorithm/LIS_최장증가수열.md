```



수열 A가 주어졌을 때, 그 수열의 증가 부분 수열 중에서 합이 가장 큰 것을 구하는 프로그램을 작성하시오.

예를 들어, 수열 A = {1, 100, 2, 50, 60, 3, 5, 6, 7, 8} 인 경우에 합이 가장 큰 증가 부분 수열은 A = {1, 100, 2, 50, 60, 3, 5, 6, 7, 8} 이고, 합은 113이다.


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


