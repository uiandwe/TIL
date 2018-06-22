```

var quicksort = function(arr, left, right) {
  
    if (left < right) {
          
        //기준점을 찾고 기준점을 중심으로 더 작은수, 더 큰수 분류 
        var i =  position(arr, left, right);
        //기준점 기준 좌측 정렬
        quicksort(arr, left, i - 1);
        //기준점 기준 우측 정렬
        quicksort(arr, i + 1, right);
    }
 
    return arr;
};

var position = function(arr, left, right) {
    var i = left;
    var j = right;
    var pivot = arr[left];

    //제자리 더 큰수/더 작은 수 좌우 배치.
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

var arr = [ 4, 5, 1, 2, 11, 8, 3, 1, 2, 5 ];
quicksort(arr, 0, arr.length-1);
console.log(arr);

```


```
캐시를 위한 array 필요

function quick(array){
    if(array.length <= 1){
        return array;
    }

    var pivot = array[parseInt((arr.length-1)/2)];
    var less = [];
    var equal = [];
    var more = [];
    array.forEach(e => {
        if(e < pivot){
            less.push(e);
        }
        else if(e == pivot){
            equal.push(e);
        }
        else {
            more.push(e);
        }
    });

    return quick(less)+equal+quick(more);
}
var arr = [ 4, 5, 1, 2];
console.log(quick(arr));

```
