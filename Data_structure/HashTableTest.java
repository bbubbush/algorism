import java.util.LinkedList;

class HashTable {
    class Node {
        String key;
        String value;
        public Node(String key, String value){
            this.key = key;
            this.value = value;
        }
        String value(){
            return this.value;
        }
        void value(String value) {
            this.value = value;
        }
    }

    LinkedList<Node>[] data;

    HashTable() {
        this(10);
    }
    HashTable(int size) {
        this.data = new LinkedList[size];
    }

    int makeHash(String key){
        int hashCode = 0;
        for(int i = 0; i < key.length(); i++) {
            hashCode += key.charAt(i) * (key.length() - i);
        }
        return hashCode;
    }
    int hashCodeToIndex(int hashCode) {
        System.out.println("HashCode is " + (hashCode % data.length));

        return hashCode % data.length;
    }
    Node searchKey(LinkedList<Node> list, String key) {
        if (list == null) {
            return null;
        }
        for (Node node : list) {
            if (node.key.equals(key)) {
                return node;
            }
        }
        return null;
    }
   
    void put(String key, String value) {
        int hashCode = makeHash(key);
        int index = hashCodeToIndex(hashCode);
        LinkedList<Node> list = data[index];

        if (list == null) {
            list = new LinkedList<Node>();
            data[index] = list;
        } 
        Node node = searchKey(list, key);
        if (node == null) {
            list.addLast(new Node(key, value));
        } else {
            node.value = value;
        }
    }

    String get(String key) {
        int hashCode = makeHash(key);
        int index = hashCodeToIndex(hashCode);
        LinkedList<Node> list = data[index];
        Node node = searchKey(list, key);
        return node == null ? "Not found" : node.value();
    }


}



public class HashTableTest {
    public static void main(String[] args) {
        HashTable h = new HashTable(2);
        h.put("Lee", "SangHoon");
        h.put("apple", "macbook");
        h.put("fire", "me too");
        System.out.println(h.get("Lee"));
        System.out.println(h.get("apple"));
        System.out.println(h.get("fire"));
        System.out.println(h.get("lee"));

        

    }
}