'use strict';

function countWordsInText(text) {
    let count = {};
    let popularity = [];  // maybe this should be an object due to JS array expansion logic

    function updateWord(word, ct) {
        if (popularity[ct-1]) {
            popularity[ct-1].delete(word);
        }
        if (!popularity[ct]) {
            popularity[ct] = new Set();
        }
        popularity[ct].add(word);
    }

    for(let word of text.split(' ')) {
        word = word.replace(/[^a-zA-Z]/g, '').toLowerCase();
        let ct = count[word] = (count[word] || 0) + 1;
        updateWord(word, ct);
    }

    return popularity;
}

function printSortedWordsAndCounts(popularity) {
    for(let i = popularity.length; i > 0; i--) {
        if(popularity[i] && popularity[i].size) {
            console.log(i, popularity[i]);
        }
    }
}

module.exports = {
    countWordsInText,
    printSortedWordsAndCounts
};
