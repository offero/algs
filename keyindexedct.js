/* jshint node: true */
"use strict";

var punycode = require('punycode');  // unicode code point look-up

/* Key-Indexed Counting Sort
 *
 * Take advantage of the fact that the prefixes are directly mappable
 * to ordered integers. IE. ASCII numeric values or even Unicode
 * number, Genome data (A, C, T, G), etc.
 */

/* For a given item, reuturn its 0-based index integer key.
 * This should be a constant-time function mapping an item/prefix
 * to its array index.
 */
function key(itm){
    // return itm.charCodeAt(0);
    return punycode.ucs2.decode(itm)[0];
}

/* Make all undefined entries in the array 0s. */
function init0(arr){
    var i;
    for(i=0; i<arr.length; i++){
        if(arr[i] === undefined){
            arr[i] = 0;
        }
    }
    return arr;
}

/* Make an array of numbers a cumulative sum. */
function accumulate(arr){
    var i;
    for(i=1; i<arr.length; i++){
        arr[i] += arr[i-1];
    }
    return arr;
}

function countingSort(stringArr){
    var i, k;
    var sortedArr = [];
    var counts = [];

    var p = 0; // the current prefix index

    for(i=0; i<stringArr.length; i++){
        k = key(stringArr[i][p]); // find the prefix index
        if(counts[k+1] === undefined){ counts[k+1]=0; }
        counts[k+1]++;
    }

    counts = init0(counts);
    counts = accumulate(counts);

    for(i=0; i<stringArr.length; i++){
        k = key(stringArr[i][p]); // find the prefix index
        sortedArr[counts[k]] = stringArr[i];
        counts[k]++;
    }

    return sortedArr;
}

module.exports = {
    init0: init0,
    key: key,
    accumulate: accumulate,
    countingSort: countingSort
};
