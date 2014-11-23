/* jshint node: true */
"use strict";

var U = require('underscore');
var T = require('./toposort');
var DAG = T.DirectedWeightedGraph;
var DAGSP = T.DAGSP;

/*
┌────┐  1   ┌───┐  1   ┌───┐  1   ┌───┐
│ 1  │ ───> │ 2 │ ───> │ 4 │ ───> │ 6 │
└────┘      └───┘      └───┘      └───┘
  │                      ∧
  │ 1                    │
  ∨                      │
┌────┐  1                │
│ 3  │ ──────────────────┘
└────┘
  │
  │ 1
  ∨
┌────┐
│ 5  │
└────┘
*/

var dag = new DAG();
var edges = [
    [1, 2, 5],
    [1, 3, 1],
    [2, 4, 5],
    [3, 4, 1],
    [3, 5, 1],
    [4, 6, 1],
];

U.each(edges, function(e){
    dag.addEdge(e[0], e[1], e[2]);
});

var dagsp = new DAGSP(dag);
dagsp.calculateShortestPaths();

// .load toposort.test.js

