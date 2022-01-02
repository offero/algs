/*
 * Given a 2D boolean array, find the largest square subarray of
 * true values. The return value should be the side length of the
 * largest square subarray subarray
 *
 * - Brute force 1: Consider each square as the top left start of a square.
 *   Expand the square until we hit an edge or until a false is encountered.
 *
 */

const ex1 = [
    [0, 1, 0, 0], // row 0
    [1, 1, 1, 1], // row 1
    [0, 1, 1, 0], // row 2
];

function largestSquareFromPos(arr, [i, j]) {
    if (!arr[i][j]) {
        return 0;
    }
    // start at i, j
    // check all values if we expand to i+1, j+1
    debugger;
    let size = 1
    while (true) {
        // check to see if we are out of bounds
        // if the next row does not exist...
        if (i+size >= arr.length) {
            return size;
        }
        // if the next column does not exist...
        if (j+size >= arr[0].length) {
            return size;
        }
        // check next row i+y from col j to col j+y
        for (let col = j; col < j+size; col++) {
            const row = i + size;
            if (!arr[row]) {
                console.log(row, col);
            }
            if (!arr[row][col]) {
                return size;
            }
        }
        // check next col j+x from row i to row i+x
        for (let row = i; row < i+size; row++) {
            const col = j + size;
            if (!arr[row][col]) {
                return size;
            }
        }
        // expand square
        size++;
    }
    return size;
}
 
function largestSquareSubarray(arr) {
    let largest;
    for (let i = 0; i < arr.length; i++) {
        for (let j = 0; j < arr[0].length; j++) {
            const sizeFromPos = largestSquareFromPos(arr, [i, j]);
            if (!largest || sizeFromPos > largest) {
                largest = sizeFromPos;
            }
        }
    }
    return largest;
}

console.log(largestSquareSubarray(ex1));
