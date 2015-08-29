/* jshint node: true */
"use strict";

/* Sub-string search with Robin-Karp algorithm
 */

var punycode = require('punycode');

/* Return the integer numbers for each character in str.
 * > punycode.ucs2.decode('abc')
     [ 97, 98, 99 ]
 */
function strToInts(str){
    return punycode.ucs2.decode(str);
}

/* simple primality test
 */
function isPrime(x){
    var i;
    if(x % 2 === 0 || x % 3 === 0) { return false; }
    // Each int represented as 6k + i (i in [-1, 4]).
    // The previous divisibility chcek for 2 and 3 take care of i = 0, 2, 3, 4.
    // We only have to check that a number is not divisible by either
    // 6k-1 or 6k+1.
    // IE. 5 is 6*1-1
    //     7 is 6*1-1+2 = 6*1+1
    // We have to check each number of the form 6k+-1 from 5 (6*1-1) to
    // ceil(sqrt(x)) to see if it divides x.
    for(i=5; i*i<=x; i+=6){
        if(x % i === 0 || x % (i+2) === 0){
            return false;
        }
    }
    return true;
}

function getLargePrime(min){
    // TODO: This is a naive method, use a sieve.
    var p = min%2 === 0 ? min+1 : min+2;  // only odd numbers
    while(true){
        if(isPrime(p)){ return p; }
        p += 2;
    }
}

/* Get the closest prime number less than `max`.
 * getMaxPrime(Math.pow(2, 52)) === 4503599627370449
 */
function getMaxPrime(max){
    var p = max%2 === 0 ? max-1 : max;  // only odd numbers
    while(true){
        if(isPrime(p)){ return p; }
        p -= 2;
    }
}

function digits(x){
    return String(x).length;
    /* There are overflow problems with the following method:
       return Math.ceil(Math.log(x)/Math.LN10);
       IE.
        > Math.log(1)/Math.LN10;
        0
        > Math.log(10)/Math.LN10;
        1
        > Math.log(100)/Math.LN10;
        2
        > Math.log(1000)/Math.LN10;
        2.9999999999999996
        > Math.log(10000)/Math.LN10;
        4
        > Math.log(100000)/Math.LN10;
        5

       This would have to be mitigated by something like
        > Math.round((Math.log(1000) / Math.LN10) * 1e6) / 1e6
        3
   */
}

function digits2(x){
    var ct = 0;
    while(x > 0){  // or while(x >= 1){x=x/10;}
        x = Math.floor(x/10);
        ct++;
    }
    return ct;
}

// var P = getMaxPrime(Math.pow(2, 52));
// The prime should be just smaller than the max long value to prevent
// overflow.
// It should be a "sufficiently large random prime" ~ M(N^2)
// Then the probability of collision is about 1/P
var P = 4503599627370449;

function textToInt(txt){ return strToInts(txt).join(""); }

function hash(txt, P){
    return parseInt(textToInt(txt), 10) % P;
}

/* The robin karp algorithm represents the pattern as a hash.
 * Each character in the pattern must map to a positive integer to be hashed.
 * It scans through the text keeping a current hash computed as
 * n = x * 10 + x'
 * h = n mod P
 * Updating the hash for the next x (x''), we take
 * n = [n - n/(10*digits(n)-1)]*10 + x''
 * h = n mod P
 * Basically chopping off the first number, shifting over and adding the next.
 * If the hashes of the pattern and h match perform a string comparison.
 *
 * Rolling hash function choice:
 *     1. Sum of the numbers representing the characters in the string
 *     2. Sum of each number multiplied by a base B^x where x is the
*         position of the character.
*         h  = (a * B^2) + (b * B^1) + (c * B^0)
*              Remove the first character (a) and shift, add the next char (d)
*         h' = [(h - (a * B^2)) * B] + d
*         TODO: Find a suitable base B. IE. 101 for ASCII
*/
function robinkarp(text, pattern){
    // Translate pattern into series of numbers
    var pat_s = strToInts(pattern).join("");
    var pat_i = parseInt(pat_s, 10);
    var H = hash(pat_i, P);

    // load the first string
    var val_t = text.substr(0, pattern.length);
    var val_a = strToInts(val);  // array of code points
    var val_s = val_a.join("");
    var val_i = parseInt(val_s, 10);
    var i, d;
    // Scan the text
    for(i=d; i<text.length; i++){
        // how many digits are we chopping off the front of the number?
        d = digits(val_a.shift());
        // push the next code point onto array
        val_a.push(strToInts(text[i])[0]);


    }

}

module.exports = {
    isPrime: isPrime,
    strToInts: strToInts,
    textToInt: textToInt,
    getLargePrime: getLargePrime,
    getMaxPrime: getMaxPrime,
    robinkarp: robinkarp
};
