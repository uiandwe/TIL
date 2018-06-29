```


최장 공통 부분 수열(LCS) 문제는 두 개의 문자열에서 순서대로 겹치는 문자가 최대 몇 개인지 구하는 문제입니다. 

예를 들어 ABCBDAB와 BDCABA에서 LCS는 BCAB나 BDAB나 BCDB입니다. 

앞에서부터 겹치는 것들을 찾아서 문자열을 만들 때 그것이 가장 길다면 LCS가 되는 거죠.

이 문제는 다음과 같이 분석할 수 있습니다. i라는 문자열과 j라는 문자열이 있다고 칩시다. 

lcs(i,j)는 이 두 문자열의 LCS 길이입니다.

만약 문자열의 마지막 두 문자가 같다면 lcs(i, j) = lcs(i-1, j-1) + 1과 같습니다. 

lcs(ABCBDAB, BDCAB)는 lcs(ABCBDA, BDCA) + 1과 같은 거죠.

만약 두 문자열의 마지막 문자가 다르다면, lcs(i, j) = max(lcs(i, j-1), lcs(i -1, j))가 됩니다. 

lcs(ABCBDAB, BDCABA)는 lcs(ABCBDA, BDCABA)와 c(ABCBDAB, DBCAB) 중 더 큰 값이 되는 겁니다.



function LCS(x, y) {
  var i = x.length;
  var j = y.length;
  var result = [];
  for (var k = 0; k <= i; k++) {
    if (!result[k]) {
      result[k] = []; 
    }
  }
  for (k = 0; k <= i; k++) {
    for (var l = 0; l <= j; l++) {
      if (k === 0 || l === 0) { 
        result[k][l] = 0;
      } else if (x[k - 1] === y[l - 1]) { 
        result[k][l] = result[k - 1][l - 1] + 1;
      } else { 
        result[k][l] = Math.max(result[k - 1][l], result[k][l - 1]);
      }
    }
  }
  return result[i][j];
}
LCS('ABCBDAB', 'BDCABA'); // 4



```
