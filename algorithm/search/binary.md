```

function binarySearch(array, val){
    var first = 0;
    var last = array.length;

    while(first<=last){
        var mid = Math.floor((first+last)/2);
        if(array[mid] == val){
            return mid;
        }
        else if(array[mid] > val){
            last = mid-1;
        }
        else{
            first = mid+1;
        }
    }

    return -1;
}

var a = [1,2,3,4,5,6,7,8,9,10];
console.log(binarySearch(a, 2));





```
