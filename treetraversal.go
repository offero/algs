package main

import (
	"fmt"
	"strings"
)

type Node struct {
	val       int
	neighbors []*Node
}

func makeNode(val int) Node {
	return Node{val, make([]*Node, 0)}
}

func makeNodes(vals []int) []Node {
	res := make([]Node, 0, len(vals))
	for _, val := range vals {
		res = append(res, makeNode(val))
	}
	return res
}

func (t *Node) addNeighbor(n *Node) {
	t.neighbors = append(t.neighbors, n)
}

func (t *Node) printNode() {
	// fmt.Printf("Neighbors: %d\n", len(t.neighbors))
	fmt.Printf("%d ", t.val)
	// nvals := make([]string, len(t.neighbors), len(t.neighbors))
	nvals := make([]string, 0, len(t.neighbors))
	// nvals := [len(t.neighbors)]string
	for _, neigh := range t.neighbors {
		// neigh.printNode()
		nvals = append(nvals, fmt.Sprintf("%d", neigh.val))
	}
	fmt.Printf("Neighbors: %s\n", strings.Join(nvals, ", "))
}

type Something struct{}

var something = Something{}

func (t *Node) isTree() bool {
	// func isTree(t *Node) bool {
	// create a set of visited nodes
	visited := make(map[int]Something)
	queue := make([]*Node, 0)
	queue = append(queue, t)

	for len(queue) > 0 {
		// take the first node
		node := queue[0]
		// leave the rest in the queue
		queue = queue[1:len(queue)]

		// if we've visited this before, false
		if _, ok := visited[node.val]; ok {
			return false
		}

		// mark it visited
		// fmt.Println("Visiting", node.val)
		visited[node.val] = something

		for _, neigh := range node.neighbors {
			queue = append(queue, neigh)
		}
	}
	return true
}

func printNodes(nodes []*Node) {
	res := make([]string, 0, len(nodes))
	for _, node := range nodes {
		res = append(res, fmt.Sprintf("%d", node.val))
	}
	fmt.Println(strings.Join(res, ", "))
}

func reverse(nodes []*Node) []*Node {
	res := make([]*Node, len(nodes))
	for i := 0; i < len(nodes); i++ {
		res[len(nodes)-i-1] = nodes[i]
	}
	return res
}

/* Return a list of nodes visited using pre-order traversal. */
func (t *Node) preOrder() []*Node {
	res := make([]*Node, 0)
	visited := make(map[int]Something)
	queue := make([]*Node, 0)
	queue = append(queue, t)

	for len(queue) > 0 {
		node := queue[0]
		queue = queue[1:len(queue)]

		// if we haven't visisted it yet,
		if _, ok := visited[node.val]; !ok {
			// add it to the result list
			res = append(res, node)
			// visit as soon as we see a node
			visited[node.val] = something
			// for each neighbor of node, add to queue
			for _, neigh := range reverse(node.neighbors) {
				queue = append([]*Node{neigh}, queue...)
			}
		}
	}
	return res
}

// TODO: postOrder, inOrder (binary only)

func main() {
	nodes := makeNodes([]int{0, 1, 2, 3, 4, 5})
	/*
		    0
		   / \
		  1   2
		 / \  \
		3   4   5
	*/
	nodes[0].addNeighbor(&nodes[1])
	nodes[0].addNeighbor(&nodes[2])
	nodes[1].addNeighbor(&nodes[3])
	nodes[1].addNeighbor(&nodes[4])
	nodes[2].addNeighbor(&nodes[5])

	fmt.Println(nodes[0].isTree())
	printNodes(nodes[0].preOrder())

	/*
		    0
		   / \
		  1   2
		 /|\
		3 4 5
	*/
	nodes2 := makeNodes([]int{0, 1, 2, 3, 4, 5})
	nodes2[0].addNeighbor(&nodes2[1])
	nodes2[0].addNeighbor(&nodes2[2])
	nodes2[1].addNeighbor(&nodes2[3])
	nodes2[1].addNeighbor(&nodes2[4])
	nodes2[1].addNeighbor(&nodes2[5])

	fmt.Println(nodes2[0].isTree())
	printNodes(nodes2[0].preOrder())
}
