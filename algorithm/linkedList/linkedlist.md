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
    this.remove = function(data){
        var index = this.indexOf(data);
        return this.removeAt(index);
    }
    this.removeAt = function(pos){
        if(pos > -1 && pos < this._length){
            var curr = this._head;
            var prev, index = 0;

            if(pos == 0){
                this._head = curr.next;
            }
            else{
                while(index++ < pos){
                    prev = curr;
                    curr = prev.next;
                }

                prev.next = curr.next;
            }
            this._length --;
            curr.next = null;
            return curr.data;
        }
        else{
            return null;    
        }
    }
    this.toString = function(){
        var curr = this._head;
        var str = "";

        while(curr){
            str += curr.data;
            curr = curr.next;
        }

        return str;
    }
    this.isEmpty = function(){
        return this._length === 0;
    }
    this.size = function(){
        return this._length;
    }
        
}


var list = new LinkedList();
console.log(list.isEmpty());
console.log(list.size());
list.append(15);
list.append(10);
list.append(2);

console.log(list);
console.log(list.indexOf(11));
console.log(list.indexOf(2));
console.log(list.indexOf(10));
console.log(list.indexOf(15));
console.log(list.size());
list.remove(2);
console.log(list);
console.log(list.toString());
console.log(list.isEmpty());
console.log(list.size());
