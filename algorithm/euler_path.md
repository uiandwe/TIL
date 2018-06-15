```


var m, n;
var a = [[0, 0, 0, 0, 0, 0],
[0, 0, 1, 1, 0, 2],
[0, 1, 0, 1, 1, 3],
[0, 1, 1, 0, 1, 3],
[0, 0, 1, 1, 0, 2]];
var path = [];
var odd = [0,0,1,1,0];

for(var i=0; i<100; i++){
    path.push(0);
}

function EP(vertex, idx){
    path[idx] = vertex;

    var i;
    if(idx == m){
        console.log(path[0]);
        for(i=1; i<= m; i++){
            console.log(path[i])
        }
        return true;
    }

    for(i=1; i<=n; i++){
        if(a[vertex][i] == 1){
            a[vertex][i] = a[i][vertex] = 0;
            
            if(EP(i, idx+1)){
                return true;
            }
            a[vertex][i] = a[i][vertex] = 1;
        }
    }
    return false;
}

n = 4;
m = 5;
for(var i=1; i<=n; i++){
    if(true){
        if(odd[i]){
            if(EP(i, 0)){
                break;
            }
        }
    }
    else if(EP(i, 0)){
        break;
    }
}
console.log("end");




```
