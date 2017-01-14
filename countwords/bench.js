'use strict';

const Benchmark = require('benchmark');
let suite = new Benchmark.Suite;

const countWordsInTextChris = require('./countWordsInText').countWordsInText;
const countWordsInTextMR = require('./countWordsInTextMR').countWordsInText;

const text = "There’s an interesting discussion on Quora about the differences between Golang and Scala. As a former academic with tendencies towards functional programming, I used to be very tempted by Scala.1 It offers all the functional goodness without the exoticism of Haskell, and came with reasonably good tools and frameworks. Like Clojure, it’s a functional language you can actually do some work with. The problem with Scala is, the more advanced you get, the more complicated (unreadable?) your code becomes. I remember that back in grad school the dude who was able to doodle the craziest and mathematically most challenging solution to some problem in Haskell was someone everyone looked up to. But it turns out in the “real world” simplicity always trumps virtuosity and sophistication, which is one of the many reasons I love Golang so much. A language with no “magic,” good concurrency support, great documentation and community that compiles into machine code and runs faster than Python? Yes, please. Read the whole Quora thread, though, there’s a lot of interesting stuff there.";

suite.add('Chris', function() {
    return countWordsInTextChris(text);
})
.add('Best', function() {
    return countWordsInTextBest(text);
})
.on('cycle', function(event) {
  console.log(String(event.target));
})
.on('complete', function() {
  console.log('Fastest is ' + this.filter('fastest').map('name'));
})
.run({async: true});
