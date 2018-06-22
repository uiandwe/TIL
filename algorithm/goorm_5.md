```





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
