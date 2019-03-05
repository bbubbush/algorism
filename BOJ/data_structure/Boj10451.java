import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Scanner;
import java.util.Stack;

class Grp {
    class Node {
        int data;
        LinkedList<Node> adjacent;
        boolean isChecked;
        Node(int idx) {
            data = idx;
            adjacent = new LinkedList<Node>();
            isChecked = false;
        }
    }

    ArrayList<Node> nodes = new ArrayList<Node>();
    Grp(int size) {
        for (int i = 0; i < size; i++) {
            nodes.add(new Node(i));
        }
    }

    void addAdjacent(int first, int second) {
        Node n1 = nodes.get(first);
        Node n2 = nodes.get(second);

        if (!n1.adjacent.contains(n2)) {
            n1.adjacent.add(n2);
        }
        if (!n2.adjacent.contains(n1)) {
            n2.adjacent.add(n1);
        }
    }
    int cnt = 0;
    int dfs() {
        
        Stack<Node> stack = new Stack<Node>();
        boolean isFinished = false;
        
        while (!isFinished) {
            for (Node temp : nodes) {
                if (!temp.isChecked) {
                    stack.push(temp);
                    temp.isChecked = true;
                    break;
                }
            }
            while (!stack.isEmpty()) {
                Node n = stack.pop();
                for (Node node : n.adjacent) {
                    if (!node.isChecked) {
                        stack.push(node);
                        node.isChecked = true;
                    }
                }
            }
            cnt++;
            for (int i = 0; i < nodes.size(); i++) {
                if (!nodes.get(i).isChecked) {
                    break;
                }
                if (i == nodes.size() - 1) {
                    isFinished = true;
                }
            }
            
        }
        return cnt;
    }
}

public class Boj10451 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int testCase = Integer.parseInt(sc.nextLine());
        // int testCase = 1;
        ArrayList<Integer> result = new ArrayList<>();
        for (int i = 0; i < testCase; i++) {
            int size = Integer.parseInt(sc.nextLine());
            // int size = 5;
            String text = sc.nextLine();
            String[] cycle = text.split(" ");
            
            Grp g = new Grp(size);
            for (int j = 0; j < cycle.length; j++) {
                int second = Integer.parseInt(cycle[j]);
                g.addAdjacent(j, second - 1);
            }
            result.add(g.dfs());
        }

        for (int data : result) {
            System.out.println(data);
        }
    }
}