/* jshint node: true */
"use strict";

var assert = require('assert');
var TST = require('./trie').TST;

var words1 = ['aaa', 'aab', 'abb', 'bbb'];

/* words1 should look like this after insertion:
 *
 *       _a__________
 *      / |          \
 *        a_____      b
 *        |     \     |
 *        a(0)   b    b
 *         \     |    |
 *          b(1) b(2) b(3)
 */

/* Apply fn to each item in array.
 * Pass in array value and index number to each function.
 * Optionally pass in provided argument list.
 */
function each(arr, fn, ctx, args){
    if(ctx === undefined) { ctx = this; }
    if(args === undefined){ args = []; }
    var i;
    for(i=0; i<arr.length; i++){
        fn.apply(ctx, [arr[i], i].concat(args));
    }
}

function test1(){
    var t = new TST();
    each(words1, t.put, t);
    assert.strictEqual(t.root.c, "a");
    assert.strictEqual(t.root.mid.c, "a");
    assert.strictEqual(t.root.mid.mid.c, "a");
    assert.strictEqual(t.root.mid.mid.val, 0);
    assert.strictEqual(t.root.mid.mid.right.c, "b");
    assert.strictEqual(t.root.mid.mid.right.val, 1);
    assert.strictEqual(t.root.mid.right.c, "b");
    assert.strictEqual(t.root.mid.right.val, null);
    assert.strictEqual(t.root.mid.right.mid.c, "b");
    assert.strictEqual(t.root.mid.right.mid.val, 2);
    assert.strictEqual(t.root.right.c, "b");
    assert.strictEqual(t.root.right.mid.c, "b");
    assert.strictEqual(t.root.right.mid.val, null);
    assert.strictEqual(t.root.right.mid.mid.c, "b");
    assert.strictEqual(t.root.right.mid.mid.val, 3);

    assert.strictEqual(t.get("a"), null);
    assert.strictEqual(t.get("aa"), null);
    assert.strictEqual(t.get("aaa"), 0);
    assert.strictEqual(t.get("aab"), 1);
    assert.strictEqual(t.get("abb"), 2);
    assert.strictEqual(t.get("bbb"), 3);

    assert.strictEqual(t.get(""), null);
    assert.strictEqual(t.get("somethinglong"), null);

    // console.log(t.print());
    t.del("abb");
    /* Trie should look like this now:
    *
    *       _a__________
    *      / |          \
    *        a           b
    *        |           |
    *        a(0)        b
    *         \          |
    *          b(1)      b(3)
    */
    assert.strictEqual(t.get("aaa"), 0);
    assert.strictEqual(t.get("aab"), 1);
    assert.strictEqual(t.get("abb"), null);
    assert.strictEqual(t.get("bbb"), 3);

    t.put("ccc", 4);
    /* Trie should look like this now:
    *
    *       _a______
    *      / |      \
    *        a       b____
    *        |       |    \
    *        a(0)    b     c
    *         \      |     |
    *          b(1)  b(3)  c
    *                      |
    *                      c (4)
    */
    assert.strictEqual(t.root.right.right.c, "c");
    assert.strictEqual(t.root.right.right.val, null);
    assert.strictEqual(t.root.right.right.mid.c, "c");
    assert.strictEqual(t.root.right.right.mid.mid.c, "c");
    assert.strictEqual(t.root.right.right.mid.mid.val, 4);

    t.put("Aa", 5);
    /* Trie should look like this now:
    *
    *       ___ a______
    *      /    |      \
    *      A    a       b____
    *      |    |       |    \
    *      a(5) a(0)    b     c
    *            \      |     |
    *             b(1)  b(3)  c
    *                         |
    *                         c (4)
    */
    assert.strictEqual(t.root.left.c, "A");
    assert.strictEqual(t.root.left.val, null);
    assert.strictEqual(t.root.left.mid.c, "a");
    assert.strictEqual(t.root.left.mid.val, 5);
    assert.strictEqual(t.get("Aa"), 5);
    assert.strictEqual(t.get("Ab"), null);
}

test1();
