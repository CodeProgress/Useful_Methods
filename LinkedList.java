
public class LinkedList {
    private Node head = null;
    private int count = 0;

    public static void main(String[] args) {
        LinkedList myLinkedList = new LinkedList();
        myLinkedList.add("a");
        myLinkedList.add("b");
        myLinkedList.add("c");
        myLinkedList.add("d");
        myLinkedList.add("e");
        System.out.println("List size = " + myLinkedList.length());
        System.out.println(myLinkedList.popHead());
        myLinkedList.print();
        System.out.println("List size = " + myLinkedList.length());

        myLinkedList.reverse();
        myLinkedList.print();
    }

    private void add(String data){
        this.head = new Node(data, this.head);
        count++;
    }

    private boolean isEmpty(){
        return this.head == null;
    }

    private int length(){
        return count;
    }

    private void print(){
        Node node = this.head;
        while (node != null) {
            System.out.println(node.getData());
            node = node.getNextNode();
        }
    }

    private String popHead(){
        if (this.isEmpty()){
            return null;
        }
        Node first = head;
        head = first.getNextNode();
        count--;
        return first.getData();
    }

    private void reverse(){
        Node newHead = null;
        while (head != null){
            Node next = head.getNextNode();
            head.setNextNode(newHead);
            newHead = head;
            head = next;
        }
        head = newHead;
    }
}

class Node {
    private String data;

    void setNextNode(Node nextNode) {
        this.nextNode = nextNode;
    }

    private Node nextNode;

    Node(String data, Node nextNode) {
        this.data = data;
        this.nextNode = nextNode;
    }

    String getData() {
        return data;
    }

    Node getNextNode() {
        return nextNode;
    }
}
