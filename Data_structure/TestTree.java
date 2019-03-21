class BinaryTree {
    class Node {
        public int value;
        Node left;
        Node right;
        public Node (int value) {
            this.value = value;
        }
    }

    Node root;

    public BinaryTree() {

    }

    // 중위 순회법
    void inOrderTraversal(Node node) {
        if (node != null) {
            inOrderTraversal(node.left);
            visit(node);
            inOrderTraversal(node.right);
        }
    }
    // 전위 순회
    void preOrderTraversal(Node node) {
        if (node != null) {
            visit(node);
            preOrderTraversal(node.left);
            preOrderTraversal(node.right);
        }
    }

    // 후휘 순회
    void postOrderTraversal(Node node) {
        if (node != null) {
            postOrderTraversal(node.left);
            postOrderTraversal(node.right);
            visit(node);
        }
    }

    void visit(Node node) {
        System.out.println(node.value);
    }

}


class Tree {
    class Node {
        int data;
        Node left;
        Node right;
        Node(int data) {
            this.data = data;
            System.out.println(data);
        }
    }

    Node root;

    public void makeTree(int[] a) {
        root = makeTreeR(a, 0, a.length -1);

    }

    public Node makeTreeR(int[] a, int start, int end) {
        if (start > end ) return null;
        int mid = (start + end ) /2 ;
        Node node = new Node(a[mid]);
        node.left = makeTreeR(a, start, mid -1);
        node.right = makeTreeR(a, mid + 1, end);

        return node;
    }

    public void searchBTree(Node n, int find) {

        if (find < n.data) {
            System.out.println("Data is smaller than " + n.data);
            searchBTree(n.left, find);
        } else if (find > n.data) {
            System.out.println("Data is bigger than " + n.data);
            searchBTree(n.right, find);
        } else if (find == n.data) {
            System.out.println("Find !");
        }

    }
}

public class TestTree {
    public static void main(String[] args) {
        int[] arr = new int[10];
        for (int i = 0; i < arr.length; i++) {
            arr[i] = i;
        }
        Tree t = new Tree();
        t.makeTree(arr);
        t.searchBTree(t.root, 8);

    }
}
