import java.util.ArrayList;

class Solution {
    int k, i, ret;
    
    public void inOrder(TreeNode node){
        if(node == null) return;
        if(node.left != null) inOrder(node.left);
        if(++i == k){
            ret = node.val;
            return;
        }
        if(node.right != null) inOrder(node.right);
        
    }
    
    public int kthSmallest(TreeNode root, int k) {
        this.k = k;
        this.i = 0;
        inOrder(root);    
        return ret;
    }
}
