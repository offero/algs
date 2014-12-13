/* jshint node: true */
"use strict";

var KIC = require('./keyindexedct');

var strings = [
    "Bxyz",
    "BBxyz",
    "BBwxyz",
    "BBBxyz",
    "Axyz",
    "AAxyz",
    "AAwxyz",
    "AAvwxyz",
    "AAAxyz",
    "AAAAxyz",
    "AAAAAxyz",
    "AAAAAAxyz",
    "Cxyz",
    "CCxyz"
];

function test1(){
    console.log(KIC.countingSort(strings));
}

test1();
