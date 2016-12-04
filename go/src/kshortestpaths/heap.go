package kshortestpaths

import (
	"math"
)

type HeapValue struct {
	priority int
	value    interface{} // anything
}

type Heap struct {
	HeapValues []HeapValue
}

func MakeHeap() Heap {
	h := Heap{}
	h.HeapValues = make([]HeapValue, 1)
	h.HeapValues[0] = HeapValue{}
	return h
}

func (h *Heap) Len() int {
	return len(h.HeapValues)
}

func getHeapIndexComponents(idx int) (int, int, int) {
	level := int(math.Log2(float64(idx)))
	base := int(math.Exp2(float64(level)))
	offset := idx - base
	return level, base, offset
}

/* Returns the index of the parent of the node in the heap array
 * at index idx.
 */
func parent(idx int) int {
	level, _, offset := getHeapIndexComponents(idx)
	parentLevel := level - 1
	parentOffset := int(offset / 2)
	return int(math.Exp2(float64(parentLevel))) + parentOffset
}

func rightChild(idx int) int {
	level, _, offset := getHeapIndexComponents(idx)

	rightChildLevel := level + 1
	rightChildBase := int(math.Exp2(float64(rightChildLevel)))
	rightChildOffset := (2 * offset) + 1

	return rightChildBase + rightChildOffset
}

func leftChild(idx int) int {
	level, _, offset := getHeapIndexComponents(idx)

	leftChildLevel := level + 1
	leftChildBase := int(math.Exp2(float64(leftChildLevel)))
	leftChildOffset := 2 * offset

	return leftChildBase + leftChildOffset
}

func (h *Heap) Push(priority int, value interface{}) {
	hv := HeapValue{priority, value}
	h.HeapValues = append(h.HeapValues, hv)
	idx := len(h.HeapValues) - 1

	// up-heapify
	for idx > 0 {
		parentIdx := parent(idx)
		parentPriority := h.HeapValues[parentIdx].priority

		if priority >= parentPriority {
			break
		}

		// swap values in heap
		h.HeapValues[idx], h.HeapValues[parentIdx] =
			h.HeapValues[parentIdx], h.HeapValues[idx]
		idx = parentIdx
	}
}

func (h *Heap) Pop() (priority int, value interface{}) {
	n := len(h.HeapValues)

	if n <= 1 {
		return 0, nil
	}

	hv := h.HeapValues[1]

	// take the last item and put it in the front, replacing the popped item
	h.HeapValues[1] = h.HeapValues[n-1]

	// remove item from the end
	h.HeapValues = h.HeapValues[:n-1]

	idx := 1
	// down-heapify
	for idx < n-1 {
		priority := h.HeapValues[idx].priority
		leftIdx := leftChild(idx)
		rightIdx := rightChild(idx)

		hasLeftChild := leftIdx < n-1
		hasRightChild := rightIdx < n-1
		hasNoChildren := !hasLeftChild

		swapWithRightChild := func() {
			h.HeapValues[idx], h.HeapValues[rightIdx] =
				h.HeapValues[rightIdx], h.HeapValues[idx]
			idx = rightIdx
		}

		swapWithLeftChild := func() {
			h.HeapValues[idx], h.HeapValues[leftIdx] =
				h.HeapValues[leftIdx], h.HeapValues[idx]
			idx = leftIdx
		}

		if hasNoChildren {
			// already down-heapified all the way
			break
		}

		if hasLeftChild && !hasRightChild {
			// swap with left if left is higher prio
			leftPriority := h.HeapValues[leftIdx].priority
			if leftPriority < priority {
				swapWithLeftChild()
			}
			break
		}

		// if hasLeftChild && hasRightChild {

		// choose the child with the higher priority (lesser number)
		leftPriority := h.HeapValues[leftIdx].priority
		rightPriority := h.HeapValues[rightIdx].priority

		// idxWithWhichToSwap := leftIdx
		priorityOfIdxWithWhichToSwap := leftPriority
		swapFunc := swapWithLeftChild

		if rightPriority < leftPriority {
			swapFunc = swapWithRightChild
			// idxWithWhichToSwap = rightIdx
			priorityOfIdxWithWhichToSwap = rightPriority
		}

		if priorityOfIdxWithWhichToSwap >= priority {
			break
		}
		swapFunc()
	}

	return hv.priority, hv.value
}
