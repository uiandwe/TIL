var Tree = (function(){
    function Tree(){
        this.count = 0;
        this.root;
    }
    function Node(data){
        this.data = data;
        this.left;
        this.rigth;
    }
    function _insert(root, node){
        if (!root) return node;
        if(node.data < root.data){
            root.left = _insert(root.left, node);
            return root;
        }
        else{
            root.right = _insert(root.rigth, node);
            return root;
        }
        return root;
    }
    Tree.prototype.add = function(data){
        var node = new Node(data);
        if(this.count == 0){
            this.root = node;
        }
        else{
            _insert(this.root, node);
        }
        return ++this.count;
    }
    return Tree;
})();


var tree = new Tree();
tree.add(5);
tree.add(2);
tree.add(0);
tree.add(10);
tree.add(3);
console.log(tree);
