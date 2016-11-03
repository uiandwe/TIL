'use strict';

class tree{
    constructor(key){
        this.key = key;

    }

    getKey(){
        return this.key;
    }


}



class bst extends tree{
    construct(){
        this.left = null;
        this.right = null;
        this.parent = null;
    }

    setLeft(tree){
        this.left = tree;
    }

    setRight(tree){
        this.right = tree;
    }

    getLeft(){
        return this.left;
    }

    getRight(){
        return this.right;
    }

    insertTree(tree, key){
        if (key < tree.key){
            if(tree.getLeft() == null){
                return tree.setLeft(new bst(key));
            }

            return this.insertTree(tree.getLeft(), key);
        }
        else{
            if(tree.getRight() == null){
                return tree.setRight(new bst(key));
            }

            return this.insertTree(tree.getRight(), key);
        }
    }

    searchTree(tree, key){
        if ( tree == null || tree.key == key ){
            return tree
        }

        if ( key < tree.key ){
            return this.searchTree(tree.getLeft(), key);
        }
        else{
            return this.searchTree(tree.getRight(), key);
        }

    }

    deleteTree(tree, key, parent_tree){

        if ( tree.key == key ){
            //자식이 없을 때
            if ( tree.getLeft() == null && tree.getRight() == null  ){
                if ( parent_tree == null ){
                    return tree = undefined;
                }
                if ( parent_tree.getLeft().key == key ){
                    return parent_tree.setLeft(undefined);
                }
                else{
                    return parent_tree.setRight(undefined);
                }
            }
            else if ( tree.key == key)

        }
        else{
            if ( key < tree.key ){
                return this.deleteTree(tree.getLeft(), key, tree);
            }
            else{
                return this.deleteTree(tree.getRight(), key, tree);
            }
        }
    }
}



var root_tree = new bst(10);

root_tree.insertTree(root_tree, 12);
root_tree.insertTree(root_tree, 11);




console.log(root_tree.getKey());
console.log(root_tree.getRight().getKey());
console.log(root_tree.getRight().getLeft().getKey());

console.log(root_tree.searchTree(root_tree, 11));
console.log(root_tree.searchTree(root_tree, 20));

console.log(root_tree.deleteTree(root_tree, 11, null));

console.log(root_tree.searchTree(root_tree, 11));

root_tree.insertTree(root_tree, 11);

console.log(root_tree.searchTree(root_tree, 11));


