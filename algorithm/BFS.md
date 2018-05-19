```

var vertexList = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
var edgeList = [[0,1], [0,2], [1,0], [1,3], [2,0], [2,4], [2,5], [3,1], [4,2], [4,5], [4,6],[5,2], [5,4], [6,4]]

function bfs(start){
  var visitedList = []
  var queue = [start]
  var adjacencyList = [];
  
  for(var i=0; i<vertexList.length; i++){
    adjacencyList.push([]);
  }

  edgeList.forEach(function(val){
    adjacencyList[val[0]].push(val[1])
  });

  while(queue.length > 0){
    var current = queue.shift();
    adjacencyList[current].forEach(function(neighbor){
      if ( visitedList.indexOf(neighbor) < 0){
        queue.push(neighbor);
      }
    })
    visitedList.push(current);
  }
  return visitedList;
}
    

console.log(bfs(0))


```
