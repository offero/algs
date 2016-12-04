package kshortestpaths

import (
	"fmt"
	"testing"
)

func MakeTestGraph() Graph {
	g := MakeStationGraph()
	bossst := MakeStation("BOSSST", 42.361829, -71.05599)
	nycpas := MakeStation("NYCPAS", 40.750315, -73.992865)
	alxamt := MakeStation("ALXAMT", 38.800388, -77.071363)
	dcaust := MakeStation("DCAUST", 38.911407, -77.044637)
	g.AddEdge(bossst, nycpas)
	g.AddEdge(nycpas, alxamt)
	g.AddEdge(alxamt, dcaust)
	g.AddEdge(bossst, dcaust)
	g.AddEdge(nycpas, dcaust)
	return g
}

func TestKSD(t *testing.T) {
	g := MakeTestGraph()
	bossst := g.Node("BOSSST")
	// nycpas := g.Node("NYCPAS")
	// alxamt := g.Node("ALXAMT")
	dcaust := g.Node("DCAUST")
	paths := KShortestDijkstra(g, bossst, dcaust)
	for _, path := range paths {
		fmt.Println(PathDistance(g, path), path)
	}
}
