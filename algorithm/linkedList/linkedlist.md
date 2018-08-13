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
}


var list = new LinkedList();

list.append(15);
list.append(10);

console.log(list);




```