```


var activity = [[1,1,3], [2,2,5], [3,4,7], [4,1,8], [5,5,9], [6,8,10], [7,9,11], [8,11,14], [9,13,16]];
function activitySelection(act) {
  var result = [];
  var sorted = act.sort(function(prev, cur) {
    return prev[2] - cur[2]; // 끝나는 시간 순으로 정렬
  });
  console.log(sorted)
  var last = 0;
  sorted.forEach(function(item) {
    if (last < item[1]) { // 조건 만족 시 결과 집합에 추가
      last = item[2];
      result.push(item);
    }
  });
  console.log(result);
  return result.map(function(r) {
    return r[0]; // map을 한 이유는 그냥 몇 번째 행동이 선택되었는지 보여주기 위함.
  });
}
activitySelection(activity); // [1, 3, 6, 8]


```
