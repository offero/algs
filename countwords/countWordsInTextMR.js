'use strict';

function countWordsInText(text) {
    let count = text.split(' ').reduce((count, word) => {
        count[word] = (count[word] || 0) + 1;
        return count;
    }, {});

    let result = Object.keys(count).reduce((arr, key) => arr.concat({
        word: key,
        count: count[key]
    }), []).sort((a,b) => b.count - a.count);

    return result;
}

module.exports = {
    countWordsInText
};
