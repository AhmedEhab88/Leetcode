import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class BinaryTreeZigZagLevelOrder {
    List<List<Integer>> result = new ArrayList<>();
    boolean direction = true; //true = right, false = left;

    public static void main(String[] args) {
        TreeNode root = new TreeNode(3);
        TreeNode node9 = new TreeNode(9);
        TreeNode node20 = new TreeNode(20);
        TreeNode node15 = new TreeNode(15);
        TreeNode node7 = new TreeNode(7);
        TreeNode node4 = new TreeNode(4);
        TreeNode node11 = new TreeNode(11);

        root.right = node20;
        root.left = node9;
        node20.right = node7;
        node20.left = node15;
        node9.left = node4;
        node9.right = node11;

//        BinaryTreeZigZagLevelOrder obj = new BinaryTreeZigZagLevelOrder();
//        obj.zigzagLevelOrder(root);
//
//        for (int i = 0; i < obj.result.size(); i++) {
//            for (int j = 0; j < obj.result.get(i).size(); j++) {
//                System.out.println(obj.result.get(i).get(j));
//            }
//        }

        Queue<TreeNode> queue = new LinkedList<TreeNode>();
        queue.add(root);
        while (!queue.isEmpty()) {
            TreeNode temp = queue.poll();
            System.out.print(temp.val + " ");

            /*add left child to the queue */
            if (temp.left != null) {
                queue.add(temp.left);
            }

            /*add right right child to the queue */
            if (temp.right != null) {
                queue.add(temp.right);
            }

        }
    }

    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<Integer> list = new ArrayList<>();
        while (root != null) {
            if (direction) {
                if (root.right != null) list.add(root.right.val);
                if (root.left != null) list.add(root.left.val);
                result.add(list);
                direction = !direction;
                zigzagLevelOrder(root.left);
            } else {
                if (root.right != null) list.add(root.left.val);
                if (root.left != null) list.add(root.right.val);
                result.add(list);
                direction = !direction;
                zigzagLevelOrder(root.right);
            }
        }
        return result;
    }
}
