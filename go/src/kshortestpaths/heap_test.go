package kshortestpaths

import (
	"fmt"
	"testing"
)

/* Tree of heap indices:
 *             1
 *       2            3
 *    4     5      6      7
 *   8 9  10 11  12 13  14 15
 */

func TestParentIndexing(t *testing.T) {

	// (in, out) pairs
	tests := [][]int{{2, 1}, {3, 1}, {4, 2}, {5, 2}, {6, 3}, {7, 3},
		{8, 4}, {9, 4}, {10, 5}, {11, 5}, {12, 6}, {13, 6}, {14, 7}, {15, 7}}

	for _, testCase := range tests {
		idx, parentIdx := testCase[0], testCase[1]
		if parent(idx) != parentIdx {
			t.Errorf("parent(%d) = %d Expected %d", idx, parent(idx), parentIdx)
		}
		fmt.Printf("parent(%d) = %d\n", idx, parentIdx)
	}

}

func TestChildIndexing(t *testing.T) {

	// (idx, leftChildIdx, rightChildIdx) pairs
	tests := [][]int{{1, 2, 3}, {2, 4, 5}, {3, 6, 7}, {4, 8, 9}, {5, 10, 11},
		{6, 12, 13}, {7, 14, 15}}

	for _, testCase := range tests {
		idx, leftChildIdx, rightChildIdx := testCase[0], testCase[1], testCase[2]

		if leftChild(idx) != leftChildIdx {
			t.Errorf("leftChild(%d) = %d Expected %d", idx, leftChild(idx), leftChildIdx)
		}

		if rightChild(idx) != rightChildIdx {
			t.Errorf("rightChild(%d) = %d Expected %d", idx, rightChild(idx), rightChildIdx)
		}

		fmt.Printf("leftChild(%d) = %d : rightChild(%d) = %d\n", idx, leftChild(idx),
			idx, rightChild(idx))
	}

}

func TestHeapPushPop(t *testing.T) {
	heap := MakeHeap()
	heap.Push(5, "five")
	heap.Push(4, "four")
	heap.Push(10, "ten")
	heap.Push(1, "one")
	heap.Push(2, "two")
	heap.Push(4, "four-2")

	for _, expectedPriority := range []int{1, 2, 4, 4, 5, 10} {
		fmt.Println(heap)
		prio, val := heap.Pop()
		fmt.Printf("val: %s type: %T\n", val, val)
		if prio != expectedPriority {
			t.Errorf("Pop failed. Found: %d Expected: %d", prio, expectedPriority)
		}
	}
	fmt.Println(heap)

	_, val := heap.Pop()

	if val != nil {
		t.Errorf("Popping with an empty heap should return a nil value")
	}
}
