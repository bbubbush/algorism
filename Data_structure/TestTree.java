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

        }
    }

    Node root;

    // 생성자
    public Tree() {
        this(10);
    }

    public Tree(int a) {
        int[] arr = new int[a];
        for (int i = 0; i < arr.length; i++) {
            arr[i] = i;
        }
        makeTree(arr);
    }

    // 트리 생성
    public void makeTree(int[] a) {
        root = makeTreeR(a, 0, a.length -1);
    }

    // Tree를 밸런스를 맞춰서 생성
    public Node makeTreeR(int[] a, int start, int end) {
        if (start > end ) {
            return null;
        }

        int mid = (start + end ) /2 ;
        Node node = new Node(a[mid]);
        node.left = makeTreeR(a, start, mid -1);
        node.right = makeTreeR(a, mid + 1, end);
        // 관계를 텍스트로 출력
        System.out.println("data is " + (node != null ? node.data : "None")
                + ", left child node data is " + (node.left != null ? node.left.data : "None")
                + ", right child node data is " + (node.right != null ? node.right.data : "None"));
        return node;
    }

    // Tree의 특정 Node를 탐색
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

    // Check Balance
    public boolean isBalanced(Node node) {
        if (node == null) {
            return true;
        }
        int heightDiff = getHeight(node.left) - getHeight(node.right);
        if (Math.abs(heightDiff) > 1) {
            return false;
        }
        else {
            return isBalanced(node.left) && isBalanced(node.right);
        }
    }

    // Node의 깊이를 탐색
    public int getHeight(Node node) {
        if (node == null) {
            return -1;
        }
        return Math.max(getHeight(node.left), getHeight(node.right));
    }
}

public class TestTree {
    public static void main(String[] args) {
        // 최소 높이 트리 만들기 & 검색
        Tree t = new Tree(10);
        t.searchBTree(t.root, 5);

        System.out.println("\n\n");

        // 밸런스 트리인지 확인하기
//        Tree t2 = new Tree(10);
//        System.out.println("Tree balanced is " + t2.isBalanced(t2.root));
    }
}
