```



var vertexList = ['0', '1', '2', '3', '4', '5', '6']
var edgeList = [[0,1], [0,2], [1,0], [1,3], [2,0], [2,4], [2,5], [3,1], [4,2], [4,6],[5,2], [6,4]]

function dfs(start){
  var visitedList = []
  var adjacencyList = [];
  
  for(var i=0; i<vertexList.length; i++){
    adjacencyList.push([]);
  }

  edgeList.forEach(function(val){
    adjacencyList[val[0]].push(val[1])
  });
  
  var stack = [start];
  while(stack.length > 0){
    var current = stack.pop();
    adjacencyList[current].forEach(function(neighbor){
      if ( visitedList.indexOf(neighbor) < 0){
        stack.push(neighbor);
      }
    })
    visitedList.push(current);
  }
  return visitedList;
}
    

console.log(dfs(0))



```
