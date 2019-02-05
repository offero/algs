package kshortestpaths

import (
	"fmt"
	"testing"
)

func TestGraphCreation(t *testing.T) {
	g := MakeStationGraph()
	s1 := MakeStation("BOSSST", 42.361829, -71.05599)
	s2 := MakeStation("NYCPAS", 40.750315, -73.992865)
	g.AddEdge(s1, s2)
	// fmt.Println(g)
	fmt.Println(g.Distance(s1, s2))
}
