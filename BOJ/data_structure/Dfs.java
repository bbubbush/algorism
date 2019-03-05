import java.util.LinkedList;
import java.util.ArrayList;
import java.util.Stack;

class Graph {
    class Node {
        int data;
        LinkedList<Node> adjacent;
        boolean marked;
        Node (int data) {
            this.data = data;
            this.marked = false;
            adjacent = new LinkedList<Node>();
        }
    }

    Node[] nodes;
    Graph(int size) {
        nodes = new Node[size];
        for (int i = 0; i < size; i++) {
            nodes[i] = new Node(i);
        }
    }

    void addEdge (int i1, int i2) {
        Node n1 = nodes[i1];
        Node n2 = nodes[i2];
        if (!n1.adjacent.contains(n2)) {
            n1.adjacent.add(n2);
        }
        if (!n2.adjacent.contains(n1)) {
            n2.adjacent.add(n1);
        }
    }
    void dfs() {
        dfs(0);
    }
    void dfs(int index) {
        Node root = nodes[index];
        Stack<Node> stack = new Stack<Node>();
        stack.push(root);
        root.marked = true;
        while (!stack.isEmpty()) {
            Node r = stack.pop();
            for (Node n : r.adjacent) {
                if (n.marked == false) {
                    n.marked = true;
                    stack.push(n);
                }
            }
            visit(r);
        }
    }

    void visit(Node n) {
        System.out.print(n.data + " ");
    }


    public static void main(String[] args) {
        int result = 0;
        int size = 8;
        int[] intArr = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
        int[] arr = {2, 1, 3, 4, 5, 6, 7, 9, 10, 8};
        ArrayList<Integer> numLst = new ArrayList<Integer>();
        ArrayList<Integer> lst = new ArrayList<Integer>();
        for (int i = 0; i < arr.length; i++) {
            if (i+1 != arr[i]) {
                numLst.add(intArr[i]);
                lst.add(arr[i]);
            } else {
                result++;
            }
        }
        System.out.println("result >> " + result);
        
        Graph g = new Graph(lst.size()); // 총 5개의 노드를 사용
        for (int i = 0; i < lst.size(); i++) {
            System.out.println(numLst.get(i) + ", " + lst.get(i));
            g.addEdge(numLst.get(i) - 1, lst.get(i) - 1);
        }



        // g.addEdge(0, 1);
        // g.addEdge(1, 4);
        // g.addEdge(1, 3);

        // g.dfs();
    }
}