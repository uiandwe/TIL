from BinarySearchTree import BinarySearchTree


bst = BinarySearchTree()

bst.insert(5)
bst.insert(3)
bst.insert(8)
bst.insert(1)
bst.insert(4)
bst.insert(2)
bst.insert(7)
bst.insert(6)
bst.insert(9)
bst.insert(10)

print "------preOrder----------"
bst.preOrder(bst.root)
print "------inOrder----------"
bst.inOrder(bst.root)
print "------postOrder----------"
bst.postOrder(bst.root)
print "----------------"
