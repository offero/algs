package kshortestpaths

func KShortestDijkstra(g Graph, s Node, t Node) [][]Node {
	candidatePaths := MakeHeap()

	// Initial path just contains the start node
	// initialPath := Path{[]Node{s}}
	initialPath := []Node{s}
	candidatePaths.Push(0, initialPath)

	foundPaths := make([][]Node, 0)

	for {
		pathCost, ipath := candidatePaths.Pop()
		if ipath == nil {
			break
		}
		path := (ipath).([]Node)
		lastNode := path[len(path)-1]

		if lastNode.Id() == t.Id() {
			foundPaths = append(foundPaths, path)
		}

		for _, neighbor := range g.Edges(lastNode) {
			costOfPathWithNeighbor := pathCost + g.Distance(lastNode, neighbor)
			pathWithNeighbor := make([]Node, len(path))
			copy(pathWithNeighbor, path)
			pathWithNeighbor = append(pathWithNeighbor, neighbor)
			candidatePaths.Push(costOfPathWithNeighbor, pathWithNeighbor)
		}
	}

	return foundPaths
}
