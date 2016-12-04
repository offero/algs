package kshortestpaths

import (
	"fmt"
)

func KShortestDijkstra(graph Graph, source Node, target Node,
	maxPaths, maxPathLength int) chan []Node {

	candidatePaths := MakeHeap()

	foundPaths := make(chan []Node)

	// Initial path just contains the start node
	initialPath := []Node{source}
	candidatePaths.Push(0, initialPath)
	nfound := 0

	go func() {
		for {
			pathCost, ipath := candidatePaths.Pop()
			if ipath == nil {
				// fmt.Println("candidatePaths empty")
				break
			}
			path := (ipath).([]Node)
			lastNode := path[len(path)-1]

			if lastNode.Id() == target.Id() {
				// fmt.Println("found", path)
				foundPaths <- path
				nfound++
				if nfound >= maxPaths {
					fmt.Println("maxPaths reached")
					break
				}
			}

			for neighbor := range graph.Neighbors(lastNode) {
				costOfPathWithNeighbor := pathCost + graph.Distance(lastNode, neighbor)
				pathWithNeighbor := make([]Node, len(path))
				copy(pathWithNeighbor, path)
				pathWithNeighbor = append(pathWithNeighbor, neighbor)
				if len(pathWithNeighbor) > maxPathLength {
					continue
				}
				// fmt.Println("Adding path", pathWithNeighbor)
				candidatePaths.Push(costOfPathWithNeighbor, pathWithNeighbor)
			}
		}

		close(foundPaths)
	}()

	return foundPaths
}
