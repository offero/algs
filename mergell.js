class Node {
    constructor(value, next=null) {
        this.value = value;
        this.next = next;
    }
}

/*

l1: 1 -> 3 -> 5 -> 7
    P
l2: 2 -> 4 -> 6 -> 8
    C

1 -> 2 -> 3
          P

          l1
1 -> 3 -> 5 -> 7
     C

     l2
2 -> 4 -> 6 -> 8

*/

function mergeLists(l1, l2) {
    let head, cur, prev;

    prev = l1.value < l2.value ? l1 : l2;
    cur = l1.value < l2.value ? l2 : l1;
    l1 = l1.next;
    l2 = l2.next;
    prev.next = cur;
    head = prev;
    prev = cur;

    while (true) {
        if (!l1 && !l2) {
            break;
        }

        if (!l1) {
            // stitch l2 on to prev and break
            prev.next = l2;
            break;
        }

        if (!l2) {
            // stitch l1 on to prev and break
            prev.next = l1;
            break;
        }

        if (l1.value < l2.value) {
            cur = l1;
            l1 = l1.next;
        } else {
            cur = l2;
            l2 = l2.next;
        }

        prev.next = cur;
        prev = cur;
    }
    return head;
}

function printList(l) {
    const values = [];
    while (l) {
        values.push(l.value);
        l = l.next;
    }
    console.log(values.join(' -> '));
}

function ex1() {
    let a1 = new Node(1);
    let a2 = new Node(3);
    let a3 = new Node(5);
    let a4 = new Node(7);
    let a5 = new Node(9);
    let b1 = new Node(2);
    let b2 = new Node(4);
    let b3 = new Node(6);
    a1.next = a2;
    a2.next = a3;
    a3.next = a4;
    a4.next = a5;
    b1.next = b2;
    b2.next = b3;
    printList(a1);
    printList(b1);

    const m1 = mergeLists(a1, b1);
    printList(m1);
}

ex1();
