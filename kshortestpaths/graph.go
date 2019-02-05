package kshortestpaths

import (
	"math"
)

// Primary Interfaces

type Node interface {
	Id() string
}

type Graph interface {
	Distance(Node, Node) int
	Neighbors(Node) chan Node
	Node(string) Node // Get node by name/id
	// EstimatedDistance(Node, Node) int
}

// Station Impl

type StationNode struct {
	id     string
	latlon []float64
}

func (s StationNode) Id() string {
	return s.id
}

func (s *StationNode) Lat() float64 {
	return s.latlon[0]
}

func (s *StationNode) Lon() float64 {
	return s.latlon[1]
}

type StationGraph struct {
	nodes map[string]StationNode
	edges map[string][]StationNode
}

// Interface functions

func (s StationGraph) Distance(a Node, b Node) int {
	as := s.nodes[a.Id()]
	bs := s.nodes[b.Id()]
	return int(Haversine(as.Lat(), as.Lon(), bs.Lat(), bs.Lon()))
}

// Iterator via channel
func (s StationGraph) Neighbors(a Node) chan Node {
	nodes := make(chan Node)

	go func() {
		for _, stationNode := range s.edges[a.Id()] {
			nodes <- stationNode
		}
		close(nodes)
	}()

	return nodes
}

func (s StationGraph) Node(id string) Node {
	return s.nodes[id]
}

func (s *StationGraph) AddEdge(a Node, b Node) {
	s.nodes[a.Id()] = a.(StationNode)
	s.nodes[b.Id()] = b.(StationNode)
	s.edges[a.Id()] = append(s.edges[a.Id()], b.(StationNode))
}

func PathDistance(g Graph, path []Node) int {
	dist := 0
	for i := 1; i < len(path); i++ {
		dist += g.Distance(path[i-1], path[i])
	}
	return dist
}

func MakeStationGraph() StationGraph {
	sg := StationGraph{}
	sg.nodes = make(map[string]StationNode)
	sg.edges = make(map[string][]StationNode)
	return sg
}

func MakeStation(id string, lat, lon float64) StationNode {
	return StationNode{id, []float64{lat, lon}}
}

var EARTH_RADIUS_IN_METERS float64 = 6378100

// lat1, lon1, lat2, lon2: Point coordinates in degrees
// Returns distance in meters
// http://www.movable-type.co.uk/scripts/latlong.html
func Haversine(lat1, lon1, lat2, lon2 float64) float64 {
	lat1r := lat1 * (math.Pi / 180)
	lat2r := lat2 * (math.Pi / 180)

	dlat := (lat2 - lat1) * (math.Pi / 180)
	dlon := (lon2 - lon1) * (math.Pi / 180)

	a := math.Sin(dlat/2)*math.Sin(dlat/2) +
		math.Sin(dlon/2)*math.Sin(dlon/2)*math.Cos(lat1r)*math.Cos(lat2r)

	c := 2 * math.Atan2(math.Sqrt(a), math.Sqrt(1-a))

	return EARTH_RADIUS_IN_METERS * c
}
