/* jshint node: true */
"use strict";

/* Topological Sort
 *
 * Author: Chris K.
 * Date: 11-23-2014
 */

var _ = require('underscore');

function DirectedWeightedGraph(){
    this.edges = {};  // map from source to list of edges
    this.n = 0;
}

DirectedWeightedGraph.prototype.addEdge = function addEdge(a, b, wt){
    if(wt === undefined) { wt = 1; }
    if(this.edges[a] === undefined){
        this.edges[a] = {};
        this.n++;
    }
    if(this.edges[b] === undefined){
        this.edges[b] = {};
        this.n++;
    }
    this.edges[a][b] = wt;
};

DirectedWeightedGraph.prototype.getEdges = function getEdges(){
    var self = this;
    var edgelist = [];
    _.each(_.keys(self.edges), function(a){
        _.each(_.pairs(self.edges[a]), function(bwt){
            edgelist.push([a, bwt[0], bwt[1]]);
        });
        // _.each(_.keys(this.edges[a]), function(b) {
        //     var wt = this.edges[a][b];
        //     edgelist.push([a, b, wt]);
        // });
    });
    return edgelist;
};

DirectedWeightedGraph.prototype.length = function length(){ return this.n; };

function detectCycles(G){
    // BFS without returning to a visited node.
}

function inDegrees(dag){
    // { node: degree } map
    var indegs = {};
    // for each node a
    _.each(_.keys(dag.edges), function(a){
        // for each neighbor b
        if(indegs[a] === undefined){ indegs[a] = 0; }
        _.each(_.keys(dag.edges[a]), function(b){
            if(indegs[b] === undefined){ indegs[b] = 0; }
            // increment the indegree count for b
            indegs[b]++;
        });
    });
    return indegs;
}

/* The root of a DAG has in-degree 0 */
function findRoot(dag){
    // return the first node we find in indegree of 0
    var root = _.find(_.pairs(inDegrees(dag)), function(ind){
        return ind[1] === 0;
    })[0];
    return root;
}

function topologicalSort(dag){
    // perform depth-first-search adding each node to list in post-order
    // return array
    var a = findRoot(dag);  // src
    // var edgeTo = {a: null};
    // var distTo = {a: 0};
    var unvisited = [];
    var visited = {};

    var stack = [];
    stack.push(a);

    // result: nodes topologically ordered
    var topo = [];

    function visit(a, b){
        // if(visited[b] === true){ return; }
        // var dist;
        // dist = distTo[a] + dag.edges[a][b];
        // edgeTo[b] = a;
        // distTo[b] = dist;
        stack.push(b);
        // visited, in this case, means that we have added it to our stack
        // once already
        visited[b] = true;
    }

    function unvisitedNeighbors(a){
        var neighbors;
        var unvisited;
        neighbors = _.keys(dag.edges[a]);
        unvisited = _.filter(neighbors, function(b){
            return visited[b] !== true;
        });
        return unvisited;
    }

    while(stack.length > 0){
        a = stack[stack.length-1];
        unvisited = unvisitedNeighbors(a);
        if(unvisited.length === 0){
            // this is as deep as DFS can go
            stack.pop();
            topo.push(a);
        } else {
            // push each neighbor onto the stack
            _.each(unvisited, _.partial(visit, a));
        }
    }

    return topo;
}

/* Utilize topological sorting property of DAG to perform shortest path
 * in in time E+V.
 */
function DAGSP(dag){
    this.dag = dag;
    this.distTo = {};
    this.edgeTo = {};
}

DAGSP.prototype.calculateShortestPaths = function calculateShortestPaths(){
    var self = this;
    var topoOrder = topologicalSort(self.dag);
    var a, neighbors;
    self.distTo = {};
    self.edgeTo = {};

    function _relax(a, b){
        self.relax([a, b, self.dag.edges[a][b]]);
    }

    while(topoOrder.length > 0){
        a = topoOrder.pop();
        neighbors = _.keys(self.dag.edges[a]);
        _.each(neighbors, _.partial(_relax, a));
    }
};

DAGSP.prototype.relax = function relax(e){
    // a should already have a distance entry
    console.log(e);
    var a, b, wt, dist;
    a = e[0];
    b = e[1];
    wt = e[2];
    dist = this.distTo[a] + wt;
    // if there is no entry for b or if the new distance is better
    if(!this.distTo[b] || dist < this.distTo[b]){
        this.edgeTo[b] = a;
        this.distTo[b] = wt;
    }
};

module.exports = {
    DirectedWeightedGraph: DirectedWeightedGraph,
    DAGSP: DAGSP,
    topologicalSort: topologicalSort,
    findRoot: findRoot,
    inDegrees: inDegrees
};
