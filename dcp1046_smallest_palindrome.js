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

main();
