```


var m, n;
var a = [[0, 0, 0, 0, 0],
[0, 0, 1, 1, 0],
[0, 1, 0, 1, 1],
[0, 1, 1, 0, 1],
[0, 0, 1, 1, 0]];
var path = [];
var check = [];

for(var i=0; i<100; i++){
    path.push(0);
    check.push(false);
}

function HC(vertex, idx){
    path[idx] = vertex;

    var i;
    if(idx == n && path[0] == path[n]){
        console.log(path[0]);
        for(i=1; i<= n; i++){
            console.log(path[i])
        }
        return true;
    }

    for(i=1; i<=n; i++){
        if(a[vertex][i] == 1 && !check[i]){
            a[vertex][i] = a[i][vertex] = 0;
            check[i] = true;
            if(HC(i, idx+1)){
                return true;
            }
            a[vertex][i] = a[i][vertex] = 1;
            check = false;
        }
    }
    return false;
}

n = 4;
m = 5;
for(var i=0; i<=n; i++){
    if(HC(i, 0)){
        break;
    }
}

```
