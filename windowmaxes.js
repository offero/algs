/*
Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of each subarray of length k.

For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:

10 = max(10, 5, 2)
7 = max(5, 2, 7)
8 = max(2, 7, 8)
8 = max(7, 8, 7)
Do this in O(n) time and O(k) space. You can modify the input array in-place and you do not need to store the results. You can simply print them out as you compute them.
*/

const assert = require('assert');

function findMaxes(arr, k) {
    const result = [];  // O(k) space for the result
    let windowMax = 0;

    // O(n) time because we only increment both head and windowMax
    for(head=0; head <= arr.length; head++) {
        let start = head-(k-1); // start of window

        if (start > 0) {
            // window seeks forward, record max
            result.push(arr[windowMax]);
        }

        if (start > windowMax) {
            // window has gone past the windowMax, seek windowMax forward to
            // just before head
            windowMax = start;
            for(start; start<head; start++) {
                if(arr[start] > arr[windowMax]) {
                    windowMax = start;
                }
            }
        }

        // compare head against windowMax to see if we should update windowMax
        if (arr[head] > arr[windowMax]) {
            windowMax = head;
        }
    }

    return result;
}

function main() {
    const ex1 = [6, 2, 9, 1, 7, 3, 9, 2, 0];
    const expected1 = [9, 9, 9, 7, 9, 9, 9];
    assert.deepEqual(findMaxes(ex1, 3), expected1);

    const ex2 = [10, 5, 2, 7, 8, 7];
    const expected2 = [10, 7, 8, 8];
    assert.deepEqual(findMaxes(ex2, 3), expected2);

    const ex3 = [10, 5, 2, 7, 8, 7];
    const expected3 = [10, 5, 7, 8, 8];
    assert.deepEqual(findMaxes(ex3, 2), expected3);
}

main();
