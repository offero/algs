/* Instructions:
 *
 * Given a string, find the palindrome that can be made by inserting the fewest number of characters as
 * possible anywhere in the word. If there is more than one palindrome of minimum length that can be
 * made, return the lexicographically earliest one (the first one alphabetically).
 * 
 * For example, given the string "race", you should return "ecarace", since we can add three letters to
 * it (which is the smallest amount to make a palindrome). There are seven other palindromes that can
 * be made from "race" by adding three letters, but "ecarace" comes first alphabetically.
 * 
 * As another example, given the string "google", you should return "elgoogle".
*/

/* Notes
 *
 * Palindome: string S where the i'th letter and the len(S)-1-i'th letter are the same, 
 * for i = 0..n/2
 *
 *   i=0 S[0] == S[len(S)-1-0]
 *   i=1 S[1] == S[len(S)-1-1]
 *   ...
 *   i=len(S)//2
 *
 *   abcba (len=5)
 *   01234
 *
 *   abccba (len=6)
 *   012345
 *
 * Palindrome (2): String S where S == reversed(S)
 *
 * Create a palindrome from the given input text with the fewest number of insertions possible.
 *
 * You can always form a palindrome by reversing the current word and inserting it in the front
 *
 * word:     abcdefg
 * reversed: gfedcba
 * palindrome: gfedcba abcdefg
 * palindrome: abcdefg gfedcba
 *
 * There is a mid-point
 * Idea: Select the midpoint with the shortest number of insertions required
 *
 * # Ex 1
 * race
 * 3 ecarace
 * 3 racecar
 * 3 recacer
 *
 * ecarace (midpoint is r, add eca to the left)
 * recacer (midpoint is a, add c,e to the left of a. add r to the right of a.
 * cerarce (midpoint is a, ...)
 * raecear (midpoint is c, add e to the left, add a,r to the right.
 *
 * Minimum number of insertions will be at most n-1
 *
 * identify midpoint, copy left of the midpoint to the right
 * same midpoint, copy right of the midpoint and insert to the immediate left of the midpoint.
 * copy left of the midpoint to the end of the right of the midpoint
 *
 * Handle if the midpoint has a duplicate to the left/right.
 *
 * Handle overlap
 *
 * abcbd
 * abccbd
*/

function reversed(word) {
    return word.split('').reverse().join('');
}

function findMiddle(word, midpoint) {
    // expand from midpoint until opposing characters do not match
    let i = j = midpoint;
    if (word[midpoint] === word[midpoint+1]) {  // undefined for out of bounds checks is okay
        j = midpoint+1;
    }
    while(i >= 0 && j < word.length) {
        if (word[i] === undefined || word[j] === undefined || word[i] !== word[j]) {
            break;
        }
        i--;
        j++;
    }
    return [i+1, j-1];
}

function partition(word, midpoint) {
    const [ml, mr] = findMiddle(word, midpoint)
    const middle = word.substring(ml, mr+1);
    const left = word.substring(0, ml);
    const right = word.substring(mr+1);
    return [left, middle, right];
}

function lperm(word, midpoint) {
    const [left, middle, right] = partition(word, midpoint);
    return [reversed(right), left, middle, reversed(left), right].join('');
}

function rperm(word, midpoint) {
    const [left, middle, right] = partition(word, midpoint);
    return [left, reversed(right), middle, right, reversed(left)].join('');
}

function findBestPalindrome(word) {
    let best;
    for (let midpoint = 0; midpoint < word.length; midpoint++) {
        const l = lperm(word, midpoint);
        if (best === undefined || l.length < best.length || (l.length === best.length && l < best)) {
            best = l;
        }
        const r = rperm(word, midpoint);
        if (best === undefined || r.length < best.length || (r.length === best.length && r < best)) {
            best = r;
        }
    }
    return best;
}

function main() {
    const ex1 = 'abcddcxy';
    console.log(ex1, '->', findBestPalindrome(ex1));

    const ex2 = 'abcdcxy';
    console.log(ex2, '->', findBestPalindrome(ex2));
}

/* Second attempt after sleep.
 *
 * I realized that the above does not exactly solve the problem as there are more possible
 * permutations.
 *
 * The next approach is to have a recursive approach where we take the left, right or middle.
 *
 *
 * abc d cxy
 *
 */

function bestPalindrome(left, middle, right) {
    // console.log(left, '|', middle, '|', right);

    if (left.length === 0 && right.length === 0) {
        return middle;
    }

    if (left.length === 0) {
        return reversed(right) + middle + right;
    }

    if (right.length === 0) {
        return left + middle + reversed(left);
    }

    // constrint: middle is a palindrome
    const lchar = left[left.length-1];
    const rchar = right[0];

    if (lchar && rchar && lchar === rchar) {
        const newLeft = left.substring(0, left.length-1); // up to the last character
        const newRight = right.substring(1); // without the first character
        const newMiddle = lchar + middle + rchar;
        return bestPalindrome(newLeft, newMiddle, newRight);
    }

    // choose to add the left character to the palindrome
    const newLeft = left.substring(0, left.length-1);
    const newMiddleL = lchar + middle + lchar;
    const optionL = bestPalindrome(newLeft, newMiddleL, right);

    // choose to add the right character to the palindrome
    const newRight = right.substring(1);
    const newMiddleR = rchar + middle + rchar;
    const optionR = bestPalindrome(left, newMiddleR, newRight);

    if (optionL.length < optionR.length) {
        return optionL;
    }

    if (optionR.length < optionL.length) {
        return optionR;
    }

    // equal length
    if (optionL < optionR) return optionL;
    return optionR;
}

function findBestPalindromeTake2(word) {
    let best;
    for (let i = 0; i < word.length; i++) {
        let j = i;
        while(word[i] == word[j]) {
            j++;
        }
        let middle = word.substring(i, j);
        let left = word.substring(0, i);
        let right = word.substring(j);

        const candidate = bestPalindrome(left, middle, right);

        if (best === undefined || candidate.length < best.length) {
            best = candidate;
        }

        if (candidate.length === best.length) {
            best = candidate < best ? candidate : best;
        }
    }
    return best;
}


function mainTake2() {
    let ex;

    ex = 'a';
    console.log(ex, '->', findBestPalindromeTake2(ex));

    ex = 'aa';
    console.log(ex, '->', findBestPalindromeTake2(ex));

    ex = 'aaa';
    console.log(ex, '->', findBestPalindromeTake2(ex));

    ex = 'abcddcxy';
    console.log(ex, '->', findBestPalindromeTake2(ex));

    ex = 'abcdcxy';
    console.log(ex, '->', findBestPalindromeTake2(ex));
}

mainTake2();

