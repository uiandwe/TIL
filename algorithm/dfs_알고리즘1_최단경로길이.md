```


var n = 5, cnt= 0;
var a = [[1,1,1,0,0],
[0,0,1,1,1],
[1,1,1,0,1],
[1,0,0,0,1],
[1,1,1,1,1]];
var path = Number.MAX_VALUE;
var temp_path = 0;
function DFS(y, x){

    for(var i=0; i<n; i++){
        console.log(a[i]);
    }
    console.log("---------------")



    if(y == n-1 && x == n-1){
        cnt++;
        if(path > temp_path+1){
            path = temp_path+1;
        }
        return;
    }

    a[y][x] = 0;
    temp_path++;

    if(y > 0   && a[y-1][x] == 1) DFS(y-1, x);
    if(y < n-1 && a[y+1][x] == 1) DFS(y+1, x);
    if(x > 0   && a[y][x-1] == 1) DFS(y, x-1);
    if(x < n-1 && a[y][x+1] == 1) DFS(y, x+1);

    a[y][x] = 1;
    temp_path--;

}

DFS(0, 0);
console.log(cnt, path);



```
