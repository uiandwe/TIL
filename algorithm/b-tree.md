```



var binaryTree = function(array){
    var tree = {};

    var addNode = function (node, leaf){
        if(node && node.val === undefined){
            node.val = leaf;
            node.left = {};
            node.right = {};
            return true;
        }
        else if(node.val > leaf){
            return addNode(node.left, leaf);
        }
        else{
            return addNode(node.right, leaf);
        }
    }

    var init = function(){
        tree = {
            val: array[0],
            left: {},
            right: {}   
        }
    }

    init();

    for(var i=1; i<array.length; i++){
        addNode(tree, array[i]);
    }

    return tree;
}


var search = function (tree, item){
    var node_check = function(node){
        if(node.val === item){
            console.log(node.val);
        }
        else if(node.val > item){
            node_check(node.left);
        }
        else if(node.val < item){
            node_check(node.right);
        }
        else {
            console.log("없음");
        }
    }

    node_check(tree);
}

var bt = binaryTree([10, 20, 30]);
search(bt, 10);
search(bt, 20);
search(bt, 11);


10
20
없음

````

