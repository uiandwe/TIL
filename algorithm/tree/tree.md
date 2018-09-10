```

var Tree = (function() {
    function Tree() {
      this.count = 0;
      this.root;
    }
    function Node(data) {
      this.data = data;
      this.left;
      this.right;
    }
    function _insert(root, node) {
      if (!root) return node;
      if (node.data < root.data) {
        root.left = _insert(root.left, node);
        return root;
      } else {
        root.right = _insert(root.right, node);
        return root;
      }
      return root;
    }
    Tree.prototype.add = function(data) {
      var node = new Node(data);
      if (this.count == 0) {
        this.root = node;
      } else {
        _insert(this.root, node);
      }
      return ++this.count;
    };
    function _get(data, node) {
      if (node) {
        if (data < node.data) {
          return _get(data, node.left);
        } else if (data > node.data) {
          return _get(data, node.right);
        } else {
          return node;
        }
      } else {
        return null;
      }
    }
    Tree.prototype.get = function(data) {
      if (this.root) {
        return _get(data, this.root);
      } else {
        return null;
      }
    };
    function _remove(root, data) {
      var newRoot, exchange, temp;
      if (!root) return false;
      if (data < root.data) {
        root.left = _remove(root.left, data);
      } else if (data > root.data) {
        root.right = _remove(root.right, data);
      } else {
        if (!root.left) {
          newRoot = root.right;
          // root 메모리 정리
          return newRoot;
        } else if (!root.right) {
          newRoot = root.left;
          // root 메모리 정리
          return newRoot;
        } else {
          exchange = root.left;
          while (exchange.right) exchange = exchange.right;
          temp = root.data;
          root.data = exchange.data;
          exchange.data = temp;
          root.left = _remove(root.left, exchange.data);
        }
      }
      return root;
    }
    Tree.prototype.remove = function(key) {
      var node = _remove(this.root, key);
      if (node) {
        this.root = node;
        this.count--;
        if (this.count == 0) this.root = null;
      }
      return true;
    };
    return Tree;
  })();



  var tree = new Tree();
tree.add(5); // 1
tree.add(3); // 2
tree.add(4); // 3
tree.add(2); // 4
tree.add(7); // 5
tree.add(6); // 6
tree.add(1); // 6
console.log(tree.root.left.left.left);;


```
