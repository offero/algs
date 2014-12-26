/* jshint node: true */
"use strict";

// TODO: Rotations for balanced TST
// TODO: Hybrid: R-way at the root and TST afterwards

var util = require('util');

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

/* Non-recursive, stack-based put */
TST.prototype.put = function put(key, val){
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

/* get the value associated with key */
TST.prototype.get = function get(key){
    var i = 0,
        c = key.charAt(i),
        n = this.root;

    while(i < key.length){
        if(n === null || n.c === null){
            return null;
        }
        if(c === n.c){
            if(i === key.length-1){
                return n.val;
            }
            c = key.charAt(++i); // next char
            n = n.mid;           // next node
        }
        else if(c < n.c){
            n = n.left;
        }
        else { //if(c > n.c){
            n = n.right;
        }
    }
    return null; // IE. searching for a blank
};

var LEFT='left', MID='mid', RIGHT='right';

/* Delete a key, returning its current value if it has one.  */
TST.prototype.del = function del(key){
    var i = 0,
        c = key.charAt(i),
        n = this.root;
    var stack = [], tmp, m;
    var pos = null;
    while(i < key.length){
        if(c === n.c){
            stack.push([pos, n]);  // a stack of the path to the current node
            if(i === key.length-1){
                n.val = null;
            }
            c = key.charAt(++i); // next char
            // c = key.charAt(stack.length-1);
            pos = MID;
            n = n.mid;           // next node
        }
        else if(c < n.c){
            stack.push([pos, n]);
            pos = LEFT;
            n = n.left;
        }
        else{
            stack.push([pos, n]);
            pos = RIGHT;
            n = n.right;
        }
    }

    tmp = stack.pop(); pos = tmp[0]; n = tmp[1];
    // for(i = stack.length-1; i >= 0; i--){
    while(stack.length > 0){
        tmp = stack.pop(); m = tmp[1];
        // i = stack.length-1; // last element (m) is the parent of the current (n)

        /* if n is the root node (no parent) */
        if(m === undefined){
            this.root = null;
            break;
        }

        /* if we have no value and we are a leaf node */
        if(n.val === null &&
                n.left === null &&
                n.right === null &&
                n.mid === null){
                    m[pos] = null;  /* unlink from parent */
        }
        /* we have value or are an intermediate node of another value */
        else {
            break;
        }
        n = m;
        pos = tmp[0];
    }

};

module.exports = {
    TST: TST,
    TNode: TNode
};
