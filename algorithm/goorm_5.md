```


Making queue using stack
사용할 수 있는 자료구조가 오직 Stack밖에 없다고 할 때 Stack을 이용해서 효율적인 Queue를 구현하시오. ( enqueue, dequeue 함수 ) 

문제를 간단히 하기위해 가득차있거나 비어있는 Stack, queue에 대한 처리는 하지 않아도 된다. 

숫자는 0~255 사이의 정수이다. 

(Hint: Stack은 몇개든지 만들어서 사용할 수 있다.)

Assuming that a stack is the only available data structure, provide an efficient implementation of queues using stacks. (enqueue, dequeue function) 

To simplify the question, do not process full or empty stacks and queues. 

Numbers are integers from 0 to 255. 

(Hint: You can make and use stacks as many as you want.)

Input format

* 명령은 “ENQUEUE”와 “DEQUEUE” 두가지다. 데이터는 정수이다.
* 첫줄에는 명령 갯수가 입력된다.
* 각줄에 “ENQUEUE” 명령과 space 숫자가 들어가거나 “DEQUEUE”명령이 나온다.
* Commands are of two types - “ENQUEUE” and “DEQUEUE”. Data is of integer type.
* In the first line, the number of commands is entered.
* In the following each line, “ENQUEUE” command, space, and a number are put in. Or, “DEQUEUE” command is put in.
Output format

* DEQUEUE 명령일때만 빼낸 데이터를 한줄에 하나씩 출력한다.
* Take out the data only when the command is DEQUEUE and output the data, one in each line.
Input example

5

ENQUEUE 6

DEQUEUE 

ENQUEUE 3

ENQUEUE 2

DEQUEUE

Output example

6

3 



입력1
5
ENQUEUE 6
DEQUEUE
ENQUEUE 3
ENQUEUE 2
DEQUEUE


출력1
6
3


입력1
16
ENQUEUE 45
ENQUEUE 27
DEQUEUE
ENQUEUE 12
ENQUEUE 28
ENQUEUE 39
DEQUEUE
DEQUEUE
ENQUEUE 34
ENQUEUE 12
ENQUEUE 6
ENQUEUE 42
DEQUEUE
DEQUEUE
DEQUEUE
ENQUEUE 25


출력2
45
27
12
28
39
34



입력 3
17
ENQUEUE 42
ENQUEUE 3
DEQUEUE
ENQUEUE 33
DEQUEUE
ENQUEUE 6
DEQUEUE
ENQUEUE 36
DEQUEUE
ENQUEUE 46
DEQUEUE
ENQUEUE 47
ENQUEUE 28
DEQUEUE
ENQUEUE 3
ENQUEUE 8
DEQUEUE



출력3

42
3
33
6
36
46
47



입력4
20
ENQUEUE 22
DEQUEUE
ENQUEUE 2
DEQUEUE
ENQUEUE 21
DEQUEUE
ENQUEUE 21
DEQUEUE
ENQUEUE 10
DEQUEUE
ENQUEUE 13
DEQUEUE
ENQUEUE 33
DEQUEUE
ENQUEUE 27
DEQUEUE
ENQUEUE 0
DEQUEUE
ENQUEUE 1
DEQUEUE



출력4
22
2
21
21
10
13
33
27
0
1



입력5
20
ENQUEUE 29
ENQUEUE 37
ENQUEUE 8
ENQUEUE 16
ENQUEUE 1
ENQUEUE 14
ENQUEUE 10
ENQUEUE 6
ENQUEUE 6
ENQUEUE 1
DEQUEUE
DEQUEUE
DEQUEUE
DEQUEUE
DEQUEUE
DEQUEUE
DEQUEUE
DEQUEUE
DEQUEUE
DEQUEUE



출력5
29
37
8
16
1
14
10
6
6
1






function Stack(){
    this.stac = new Array();
    this.pop = function(){
        return this.stac.pop();
    }
    this.push = function(item){
        this.stac.push(item);
    }
    this.len = function(){
        return this.stac.length;
    }
}


function Queue(){
    var stack1 = new Stack();
    var stack2 = new Stack();    

    this.enqueue = function(item){
        var len = stack2.len();
        for(var i=0; i<len; i++){
            var temp = stack2.pop();
            stack1.push(temp);
        }

        stack1.push(item);
        len = stack1.len();
        for(var i=0; i<len; i++){
            var temp = stack1.pop();
            stack2.push(temp);
        }
    }

    this.dequeue = function(){
        return stack2.pop();
    }
}


var q = new Queue();

q.enqueue("6");
console.log(q.dequeue());
q.enqueue("3");
q.enqueue("2");
console.log(q.dequeue());

delete q;


var q = new Queue();

q.enqueue("45");
q.enqueue("27");
console.log(q.dequeue());
q.enqueue("12");
q.enqueue("28");
q.enqueue("39");
console.log(q.dequeue());
console.log(q.dequeue());
q.enqueue("34");
q.enqueue("12");
q.enqueue("6");
q.enqueue("42");
console.log(q.dequeue());
console.log(q.dequeue());
console.log(q.dequeue());


```
