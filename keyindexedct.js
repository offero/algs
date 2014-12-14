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

function countItems(arr, keyfn, start, end){
    if(start === undefined){ start = 0; }
    if(end === undefined){ end = arr.length; }
    var i, k, counts = [];

    for(i=start; i<end; i++){
        k = keyfn(arr[i]);
        if(counts[k+1] === undefined){ counts[k+1]=0; }
        counts[k+1]++;
    }
    return counts;
}

function argsToArray(argObj){
    var k, res = [];
    for(k in argObj){
        if(argObj.hasOwnProperty(k)){
            res.push(argObj[k]);
        }
    }
    return res;
}

function partial(fn, args){
    var self = this;
    // var args = argsToArray(arguments);
    var fn2 = function(){
        var args2 = arguments;
        var argsAll = args.concat(argsToArray(args2));
        // console.log(argsAll);
        return fn.apply(self, argsAll);
    };
    return fn2;
}

function countingSort(arr, idx, start, end){
    var i, counts;
    for(i=start; i<=end; i++){
        counts = countItems(arr, _keyfn, start, end);
    }
}

function countingSort(stringArr, pfxlen){
    if(pfxlen === undefined){ pfxlen = 1; }

    var i, k, p, counts, sortedArr;

    var _keyfn = function(idx, itm){
        // var args = arguments;
        // console.log("keyfn args: " + argsToArray(args));
        return punycode.ucs2.decode(itm[idx])[0];
    };

    // Prefix block method:
    //                  idx, start, end
    var prefixBlocks = [[0, 0, stringArr.length]];
    var block, keyfn, idx, pfx, curPfx, curStart, start, end;

    while(prefixBlocks.length > 0){
        sortedArr = [];
        block = prefixBlocks.pop();
        idx = block[0]; start = block[1]; end = block[2];
        if(idx > pfxlen){ break; }
        if(start === end){ continue; }

        keyfn = partial(_keyfn, [idx]);
        counts = countItems(stringArr, keyfn, start, end);
        counts = init0(counts);
        counts = accumulate(counts);

        curPfx = stringArr[i].slice(0, idx+1);
        curStart = start;
        for(i=start; i<end; i++){
            pfx = stringArr[i].slice(0, idx+1);
            if(pfx !== curPfx || i === end-1){
                prefixBlocks.push([idx+1, curStart, i]);
                curStart = i;
            }

            k = keyfn(stringArr[i]);
            sortedArr[counts[k]] = stringArr[i];
            counts[k]++;
        }

        // copy sorted items back to original array
        for(i=0; i<sortedArr.length; i++){
            stringArr[i+start] = sortedArr[i];
        }

    }

    // original
    for(p=0; p<pfxlen; p++){
        sortedArr = [];
        // get the character code at index p for a given string
        keyfn = partial(_keyfn, [p]);

        counts = countItems(stringArr, keyfn, start, end);
        counts = init0(counts);
        counts = accumulate(counts);

        // Store items in the sorted array
        for(i=0; i<stringArr.length; i++){
            k = keyfn(stringArr[i]);
            sortedArr[counts[k]+start] = stringArr[i];
            counts[k]++;
        }

        stringArr = sortedArr;
        console.log(stringArr);
    }

    return stringArr;
}

module.exports = {
    init0: init0,
    accumulate: accumulate,
    countItems: countItems,
    countingSort: countingSort,
    partial: partial
};
