/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class BSTIterator {

    List<Integer> l = null;
    Iterator<Integer> it = null;
    public BSTIterator(TreeNode root) {
        l = new LinkedList<>();
        inOrder(root);
        it = l.iterator();
    }
    
    public void inOrder(TreeNode node){
        if(node == null) return;
        if(node.left != null) inOrder(node.left);
        l.add(node.val);
        if(node.right != null) inOrder(node.right);
    }
    
    /** @return the next smallest number */
    public int next() {
        return it.next();
    }
    
    /** @return whether we have a next smallest number */
    public boolean hasNext() {
        return it.hasNext();
    }
} 

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator obj = new BSTIterator(root);
 * int param_1 = obj.next();
 * boolean param_2 = obj.hasNext();
 */
