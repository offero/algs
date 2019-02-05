/*
You are given a starting state start, a list of transition probabilities for a Markov chain, and a
number of steps num_steps. Run the Markov chain starting from start for num_steps and compute the
number of times we visited each state.

For example, given the starting state a, number of steps 5000, and the following transition
probabilities:

[
  ('a', 'a', 0.9),
  ('a', 'b', 0.075),
  ('a', 'c', 0.025),
  ('b', 'a', 0.15),
  ('b', 'b', 0.8),
  ('b', 'c', 0.05),
  ('c', 'a', 0.25),
  ('c', 'b', 0.25),
  ('c', 'c', 0.5)
]
One instance of running this Markov chain might produce { 'a': 3012, 'b': 1656, 'c': 332 }.
*/

function makeTransitionProbMap(transProbArray) {
    const transProbMap = {};
    for (let [f, t, p] of transProbArray) {
        if (!transProbMap[f]) transProbMap[f] = {};
        transProbMap[f][t] = p;
    }
    return transProbMap;
}

function transition(from, probMap) {
    // {a: 0.9, b: 0.075, c: 0.025}
    let tot = 0;
    const rand = Math.random();
    for (let [to, prob] of Object.entries(probMap)) {
        tot += prob;
        if (rand <= tot) {
            return to;
        }
    }
    throw new Error('should not be reachable');
}

function runChain(startingState, transProbMap, steps) {
    const stateVisits = {};

    for (const state of Object.keys(transProbMap)) {
        stateVisits[state] = 0;
    }

    stateVisits[startingState] = 1;

    let state = startingState;
    for (let i = 0; i < steps; i++) {
        state = transition(state, transProbMap[state]);
        stateVisits[state]++;
    }

    return stateVisits;
}

function run(startingState, transProbArray, steps) {
    const transProbMap = makeTransitionProbMap(transProbArray);
    const visits = runChain(startingState, transProbMap, steps);
    console.log(visits);
}

const ex1 = [
  [ 'a', 'a', 0.9 ],
  [ 'a', 'b', 0.075 ],
  [ 'a', 'c', 0.025 ],
  [ 'b', 'a', 0.15 ],
  [ 'b', 'b', 0.8 ],
  [ 'b', 'c', 0.05 ],
  [ 'c', 'a', 0.25 ],
  [ 'c', 'b', 0.25 ],
  [ 'c', 'c', 0.5 ]
];

run('a', ex1, 5000);
