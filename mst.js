/* jshint node: true */
"use strict";

/* UnionFind (Conencted Components) and Kruskal's MST algorithm.
 *
 * Author: Chris K.
 * Date: 11-9-2014
 */

var _ = require("underscore");

function UnionFind(n){
    this.arr = [];
    // initialize
    for(var i=0; i<n; i++){
        this.arr[i] = i;
    }
}

UnionFind.prototype.union = function union(a, b){
    // make b's root the same as a's
    this.arr[this.findRoot(b)] = this.findRoot(a);
};

UnionFind.prototype.connected = function connected(a, b){
    return this.findRoot(a) === this.findRoot(b);
};

UnionFind.prototype.count = function count(){
    return _.uniq(_.map(this.arr, this.findRoot, this)).length;
};

UnionFind.prototype.findRoot = function findRoot(a){
    // O(n) worst case for long trees
    var r = a;
    while(true){
        if(this.arr[r] === r){
            // element is it's own root
            break;
        }
        r = this.arr[r];
    }
    return r;
};

function QuickUnionFind(n){
    UnionFind.call(this, n);
    // Array that holds the size of each component.
    // The root of a tree knows its size.
    this.sz = [];
    for(var i=0; i<n; i++){
        this.sz[i] = 1;
    }
}
QuickUnionFind.prototype = Object.create(UnionFind.prototype);
QuickUnionFind.prototype.constructor = QuickUnionFind;

QuickUnionFind.prototype.union = function union(a, b){
    var ra = this.findRoot(a);
    var rb = this.findRoot(b);
    // make the smaller sized tree a child of the larger tree to keep it
    // balanced
    if(this.sz[ra] < this.sz[rb]){
        this.arr[ra] = rb;          // make a's root the root of b
        this.sz[rb] += this.sz[ra]; // b's tree size now includes a's tree size
    }else{
        this.arr[rb] = ra;  // make b's root the root of a
        this.sz[ra] += this.sz[rb]; // a's tree size now includes b's tree size
    }
};

QuickUnionFind.prototype.findRoot = function findRoot(a){
    // O(lg(n)) with balanced tree
    // Using root rewrite technique.
    var r = a;
    var nodes = [];
    while(true){
        if(this.arr[r] === r){
            // element is it's own root
            break;
        }
        nodes.push[r];
        r = this.arr[r];
    }
    // flatten the tree as a side-effect
    for(var i=0; i<nodes.length; i++){
        this.arr[nodes[i]] = r;
    }
    return r;
};

function QuickUnionFind2(n){
    QuickUnionFind.call(this, n);
}
QuickUnionFind2.prototype = Object.create(QuickUnionFind.prototype);
QuickUnionFind2.prototype.constructor = QuickUnionFind2;

QuickUnionFind2.prototype.findRoot = function findRoot(a){
    // O(lg(n)) with balanced tree
    // Using flatten-ancestor technique
    var r = a;
    while(true){
        if(this.arr[r] === r){
            // element is it's own root
            break;
        }
        // flatten tree as side-effect by 1 ancestor at a time
        // This node's ancestor is it's ancestor's ancestor.
        this.arr[r] = this.arr[this.arr[r]];
        r = this.arr[r];
    }
    return r;
};



function WeightedGraph(){
    this.edges = {};
    this.nodes = {};
    this.n = 0;
}

WeightedGraph.prototype.addEdge = function(a, b, wt){
    if(this.edges[a] === undefined){ this.edges[a] = {}; }
    // if(this.edges[b] === undefined){ this.edges[b] = {}; }
    this.edges[a][b] = wt;

    if(!this.nodes[a]){  // in order to make length lookup O(1)
        this.nodes[a] = true;
        this.n++;
    }
    if(!this.nodes[b]){
        this.nodes[b] = true;
        this.n++;
    }
};

WeightedGraph.prototype.length = function(){
    var self = this;
    // return _.keys(self.nodes).length;  // this is O(n)
    return self.n;  // O(1)
};

WeightedGraph.prototype.getEdges = function getEdges(){
    var self = this;
    var allEdges = [];
    _.each(_.keys(self.edges), function(a){
        _.each(_.pairs(self.edges[a]), function(bwt){
            allEdges.push([a, bwt[0], bwt[1]]);
        });
    });
    return allEdges;
};

WeightedGraph.prototype.adj = function adj(a){
    var self = this;
    var adjEdges = [];
    _.each(_.pairs(self.edges[a]), function(e){
        adjEdges.push([
            // a, b, wt
            a, e[0], parseInt(e[1])
        ]);
    });
    return adjEdges;
};

// Create an MST from a WeightedGraph
function MST(wg, UF){
    var self = this;
    var e, i, a, b;
    self.wg = wg;
    // Create new UF
    if(UF === undefined){
        UF = UnionFind;
    }
    self.uf = new UF(wg.length());
    self.stedges = [];
    // sort edges by weight in ascending order, O(n*lg(n))
    var sortedEdges = _.sortBy(wg.getEdges(), function(e) { return e[2]; });
    var n = wg.length();
    for(i=0; i<sortedEdges.length; i++){  // O(E)
        e = sortedEdges[i];
        a = sortedEdges[i][0];
        b = sortedEdges[i][1];
        if(!self.uf.connected(a, b)){
            self.uf.union(a, b);
            self.stedges.push(e);
        }
        // there are exactly N-1 edges in the MST. When we hit that number,
        // we are done.
        if(self.stedges.length === n-1){
            break;
        }
    }
}

module.exports.UnionFind = UnionFind;
module.exports.QuickUnionFind = QuickUnionFind;
module.exports.QuickUnionFind2= QuickUnionFind2;
module.exports.WeightedGraph = WeightedGraph;
module.exports.MST = MST;
