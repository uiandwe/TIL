```

var board = [
    ['U','R','L','P','M'],
    ['X','P','R','E','T'],
    ['G','I','A','E','T'],
    ['X','T','N','Z','Y'],
    ['X','O','Q','R','S']
];

var dx = [-1, -1, -1, 1, 1, 1, 0, 0];
var dy = [-1, 0,1, -1, 0, 1, -1, 1];

function inRange(y, x){
    if(y < 0 || x < 0 || y >= 5 || x >= 5){
        return false;
    }
    else{
        return true;
    }
}

function hasWord(y, x, word){
    if(!inRange(y, x)) return false;
    if(board[y][x] != word[0]) return false;
    if(word.length == 1) return true;
    
    for(var direction = 0; direction < 8; ++direction){
        var nextY = y + dy[direction], nextX = x + dx[direction];
        if(hasWord(nextY, nextX, word.substr(1))) return true;
    }

    return false;
}

console.log(hasWord(1, 1, "PRETTY"))
console.log(hasWord(2, 0, "GIRL"))

```
