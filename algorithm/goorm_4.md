```



가장 가까운 두 점
 1차원 직선상에 존재하는 여러 개의 점의 좌표가 주어진다. 주어지는 점들 중 가장 가까운 거리에 있는 두 점 쌍을 하나 출력하시오.



입력 형식

 첫 줄에는 1차원 직선상에 존재하는 점들의 수를 나타내는 2이상 10이하의 자연수 N이 주어진다.

 두 번째 줄에는 N개의  점의 좌표가 공백으로 구분되어 주어진다.

* 모든 좌표는 최대 10자리의 자연수다.


출력 형식

 서로 거리가 가장 가까운 두 좌표를 한 줄에 공백으로 구분하여 출력한다.

* 두 좌표 중 작은 값을 앞에 출력하고 더 큰 값을 뒤에 출력한다.
* 거리가 같은 쌍이 여러개가 존재할 경우 두 좌표의 합이 최소가 되는 쌍만을 출력한디.




입력 1
6
6 20 34 8 38 40

출력 1
6 8

입력 2
7
20 16 10 45 30 28 47

출력 2
28 30

var quicksort = function(arr, left, right) {
  
    if (left < right) {
        var i =  position(arr, left, right);
        quicksort(arr, left, i - 1);
        quicksort(arr, i + 1, right);
    }
 
    return arr;
};

var position = function(arr, left, right) {
    var i = left;
    var j = right;
    var pivot = arr[left];

    while (i < j) {
        while (arr[j] > pivot) j--;
        while (i < j && arr[i] <= pivot) i++;

        tmp = arr[i];
        arr[i] = arr[j];
        arr[j] = tmp;
    }
    arr[left] = arr[j];
    arr[j] = pivot;

    return j;
}


var arr = [6,20,34,8,38,40];
var arr = [20, 16, 10, 45, 30, 28, 47];
quicksort(arr, 0, arr.length-1);
console.log(arr);
var min_close = Number.MAX_VALUE;
var close_point = "";
for(var i=1; i<arr.length; i++){
    var temp_min_close = Math.abs(arr[i]-arr[i-1]);
    if(temp_min_close < min_close){
        min_close = temp_min_close;
        close_point = arr[i-1]+" "+arr[i];
    }
}

console.log(close_point);

```
