package preo;

import java.util.ArrayList;
import java.util.List;
import java.util.Queue;

class TreeNode {
	int val;
	TreeNode left;
	TreeNode right;
	TreeNode(int x) {
		val = x;
	}
}

class Solution {
	public ArrayList<Integer> preorderTraversal(TreeNode root) {
        ArrayList<TreeNode> nodeSeq = new ArrayList<TreeNode>();
        ArrayList<Integer> resList = new ArrayList<Integer>();
        while(!nodeSeq.isEmpty()||root!=null) {
        	if(root == null) {
        		root = nodeSeq.get(nodeSeq.size() - 1);
        		nodeSeq.remove(nodeSeq.size() - 1);
        		continue;
        	}
        	resList.add(root.val);
        	if(root.right != null) nodeSeq.add(root.right);
        	root = root.left;
        }
        return resList;
    }
}

public class ProOrder {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
