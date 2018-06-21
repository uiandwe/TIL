```

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
