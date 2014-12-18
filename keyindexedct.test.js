/* jshint node: true */
"use strict";

var KIC = require('./keyindexedct');

var strings = [
    "BBxyz",
    "Bxyz",
    "AAAAAAxyz",
    "BBwxyz",
    "AAxyz",
    "Axyz",
    "AAwxyz",
    "AAAxyz",
    "BBBxyz",
    "AAAAAxyz",
    "AAAAxyz",
    "Cxyz",
    "CCxyz",
    "AAvwxyz"
];

function test1(){
    console.log(KIC.countingSort(strings, 3));
}

test1();
