```
기본 

function Node(data){
    this.data = data;
    this.next = null;
}

function LinkedList(){
    this._length = 0;
    this._head = null;
    this.append = function(data){
        var node = new Node(data);
        var curr;

        if(this._head == null){
            this._head = node;
        }
        else{
            curr = this._head;
            while(curr.next){
                curr = curr.next;
            }
            curr.next = node;
        }
        this._length++;
    };
    this.indexOf = function(data){
        var curr = this._head;
        var index = 0;

        while(curr){
            if(curr.data == data){
                return index;
            }

            index++;
            curr = curr.next;
        }

        return -1;
    }
        
}


var list = new LinkedList();

list.append(15);
list.append(10);
list.append(2);

console.log(list);
console.log(list.indexOf(11));
console.log(list.indexOf(2));
console.log(list.indexOf(10));
console.log(list.indexOf(15));







```