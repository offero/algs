package kshortestpaths

import (
	"fmt"
	// "time"
)

func KShortestDijkstra(graph Graph, source Node, target Node,
	maxPaths, maxPathLength int) chan []Node {

	candidatePaths := MakeHeap()

	foundPaths := make(chan []Node)

	// Initial path just contains the start node
	initialPath := []Node{source}
	candidatePaths.Push(0, initialPath)
	nfound := 0

	npushes := 0
	npops := 0

	go func() {
		for {
			pathCost, ipath := candidatePaths.Pop()
			_ = pathCost
			npops++
			if ipath == nil {
				// fmt.Println("candidatePaths empty")
				break
			}
			path := ipath.([]Node)
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
				// costOfPathWithNeighbor := pathCost + graph.Distance(lastNode, neighbor)
				pathWithNeighbor := make([]Node, len(path))
				copy(pathWithNeighbor, path)
				pathWithNeighbor = append(pathWithNeighbor, neighbor)

				if len(pathWithNeighbor) > maxPathLength {
					continue
				}
				// fmt.Println("Adding path", pathWithNeighbor)

				costOfPathWithNeighbor := PathDistance(graph, pathWithNeighbor) +
					graph.Distance(neighbor, target)
				candidatePaths.Push(costOfPathWithNeighbor, pathWithNeighbor)
				npushes++
			}
		}

		fmt.Println(npushes, "pushes", npops, "pops")

		close(foundPaths)
	}()

	return foundPaths
}
