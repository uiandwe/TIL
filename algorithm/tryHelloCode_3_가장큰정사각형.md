```

O와 X로 채워진 표가 있습니다. 표 1칸은 1 x 1 의 정사각형으로 이루어져 있습니다. 표에서 O로 이루어진 가장 큰 정사각형을 찾아 넓이를 반환하는 findLargestSquare 함수를 완성하세요. 예를 들어

X 	O 	O 	O 	X
X 	O 	O 	O 	O
X 	X 	O 	O 	O
X 	X 	O 	O 	O
X 	X 	X 	X 	X

가 있다면 정답은


X 	O 	O 	O 	X
X 	O 	@ 	@ 	@
X 	X 	@ 	@ 	@
X 	X   @ 	@ 	@
X 	X 	X 	X 	X

가 되며 넓이는 9가 되므로 9를 반환해 주면 됩니다.


```


```

function findLargestSquare(board)
{
	var answer = 0;
    var copy_board = [];
    for(var i=0; i<board.length; i++){
        copy_board.push(board[i]);
    }

    for(var i=0; i<board.length; i++){
        for(var j=0; j<board[i].length; j++){
            if(board[i][j] == 'X'){
                copy_board[i][j] = 0;
            }
            else{
                if(i<=0 || j<=0){
                    copy_board[i][j] = 1;
                }
                else{
                    copy_board[i][j] = Math.min(Math.min(copy_board[i][j-1], copy_board[i-1][j]), copy_board[i-1][j-1])+1;
                }

                if(answer < copy_board[i][j]){
                    answer = copy_board[i][j];
                }
            }
            
            for(var m=0; m<copy_board.length; m++){
                console.log(copy_board[m]);
            }
            console.log("\n\n")
        }
    }
	
	return answer*answer
    
}

//아래 코드는 테스트를 위한 출력 코드 입니다.
var testBoard = [['X','O','O','O','X'],['X','O','O','O','O'],['X','X','O','O','O'],['X','X','O','O','O'],['X','X','X','X','X']];
console.log(findLargestSquare(testBoard));

```
