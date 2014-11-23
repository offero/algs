/* jshint node: true */
"use strict";

var U = require('underscore');
var mst = require('./mst');

var wg = new mst.WeightedGraph();
wg.addEdge(0, 1, 1);
wg.addEdge(1, 2, 10);
wg.addEdge(0, 2, 10);
wg.addEdge(1, 5, 1);
wg.addEdge(5, 3, 1);
wg.addEdge(2, 3, 10);
wg.addEdge(3, 6, 1);
wg.addEdge(4, 6, 1);
wg.addEdge(2, 4, 1);

var sortedEdges = U.sortBy(wg.getEdges(), function(e) { return e[2]; });

var mst1 = new mst.MST(wg);
var mst2 = new mst.MST(wg, mst.QuickUnionFind);
var mst3 = new mst.MST(wg, mst.QuickUnionFind2);
