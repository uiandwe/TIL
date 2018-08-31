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

function hashMap(){
    this.hash = {};
    this.defaultModuler = 24;
    this.set = function(data){

    }
    this.moduler = function(data){
        if(!this.isNumber(data)){
            var sum = 0;
            data.split("").forEach(element => {
                sum += element.charCodeAt(0)
            });
            return sum%this.defaultModuler;
        }
        else{
            return data%this.defaultModuler;
        }
        
    }
    this.isNumber = function(s) {
        s += ''; 
        s = s.replace(/^\s*|\s*$/g, '');
        if (s == '' || isNaN(s)) return false;
        return true;
    }
    this.insert = function(data){
        var key = this.moduler(data);
        if(this.hash[key]){
            var list = this.hash[key];
            list.append(data);
        }
        else{
            var list = new LinkedList();
            list.append(data);
            this.hash[key] = list;
        }
    }
    this.getItem = function(data){
        if(this.hash[data]){
            var hash = this.hash[data];
            return hash.toString();
        }
        else{
            return -1;
        }
        
    }
}





var h = new hashMap();
h.insert(1);
h.insert(1);
h.insert("1");
h.insert("asdf");
console.log(h.getItem(1));