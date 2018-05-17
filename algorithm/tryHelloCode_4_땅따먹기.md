```


영희는 땅따먹기 게임에 푹 빠졌습니다. 땅따먹기 게임의 땅은 총 N행 4열로 나누어져 있고, 모든 칸에는 점수가 쓰여 있습니다. 

땅을 밟으면서 한 행씩 내려올 때, 영희는 각 행의 4칸 중 1칸만 밟으면서 내려올 수 있습니다. 

땅따먹기 게임에는 같은 열을 연속해서 밟을 수가 없는 특수 규칙이 있습니다. 

즉, 1행에서 (5)를 밟았다면, 2행의 (8)은 밟을 수가 없게 됩니다. 

마지막 행까지 모두 내려왔을 때, 점수가 가장 높은 사람이 게임의 승자가 됩니다. 

여러분이 hopscotch 함수를 제작하여 영희가 최대 몇 점을 얻을 수 있는지 알려주세요. 예를 들어

1 2 3 5
5 6 7 8
4 3 2 1

의 땅이 있다면, 영희는 각 줄에서 (5), (7), (4) 땅을 밟아 16점을 최고점으로 받을 수 있으며, 

hopscotch 함수에서는 16을 반환해주면 됩니다.


```

```

var board = [[3,9,2,1],[5,5,4,3],[5,10,6,5],[1,3,10,6],[6,2,1,3],[2,1,5,6],[4,6,9,4],[8,10,6,2],[5,2,6,10],[9,6,10,2]];


function hopscotch(board, size) {
    var result = 0;
    for(var i=1; i<size; i++){
        board[i][0] += Math.max(...board[i-1]);
        board[i][1] += Math.max(board[i-1][0], board[i-1][2], board[i-1][3]);
        board[i][2] += Math.max(board[i-1][1], board[i-1][0], board[i-1][3]);
        board[i][3] += Math.max(board[i-1][1], board[i-1][2], board[i-1][0]);
    }

    result = Math.max(board[size-1][0], board[size-1][1], board[size-1][2], board[size-1][3])
    return result;
}

console.log(hopscotch(board, 10));

var board = [[ 1, 2, 3, 5 ], [ 5, 6, 7, 8 ], [ 4, 3, 2, 1]];
console.log(hopscotch(board, 3));

```
