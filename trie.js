/* jshint node: true */
"use strict";

// TODO: Rotations for balanced TST
// TODO: Hybrid: R-way at the root and TST afterwards

function TNode(val){
    // Node pointers
    this.left = null;
    this.mid = null;
    this.right = null;

    // Value stored at this node
    this.val = null;
    this.c = null;
    if(val !== undefined){ this.val = val; }
}

function TST(){
    this.root = null;
}

/* Recursive put
TST.prototype._rput = function _rput(n, i, key, val){};
TST.prototype.rput = function rput(key, val){};
*/

TST.prototype.put = function put(key, val){
    // recursive routine? or stack?
    var i, c, n;
    this.root = this.root || new TNode();

    n = this.root;
    i = 0;
    c = key.charAt(i);

    while(i < key.length){
        // does this always need to be populated before hand?
        if(c === n.c || n.c === null){
            n.c = c;
            if(i !== key.length-1){
                if(n.mid === null){ n.mid = new TNode(); }
                n = n.mid;
            }
            c = key.charAt(++i);
        }
        else if(c < n.c){
            if(n.left === null){ n.left = new TNode(); }
            n = n.left;
        }
        else /* c > n.c */ {
            if(n.right === null){ n.right = new TNode(); }
            n = n.right;
        }

    }
    n.val = val;
};

TST.prototype.print = function print(){
    // return JSON.stringify(this, null, 2);
    return util.inspect(this, {showHidden: false, depth: null});
};

TST.prototype.get = function get(key){
};

/* Delete a key, returning its current value if it has one.  */
TST.prototype.del = function del(key){
};

module.exports = {
    TST: TST,
    TNode: TNode
};
