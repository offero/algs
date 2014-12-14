/* jshint node: true */
"use strict";

var KIC = require('./keyindexedct');

var strings = [
    "BBxyz",
    "Bxyz",
    "BBBxyz",
    "BBwxyz",
    "AAxyz",
    "AAAAAAxyz",
    "Axyz",
    "AAvwxyz",
    "AAwxyz",
    "AAAxyz",
    "AAAAAxyz",
    "AAAAxyz",
    "Cxyz",
    "CCxyz"
];

function test1(){
    console.log(KIC.countingSort(strings, 2));
}

test1();
