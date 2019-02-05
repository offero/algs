/*
I worked on a fun js coding challenge this morning. Given a positive integer, create an array of "building blocks".

Example:
```generateBlocks(1) => ["*"]
generateBlocks(2) => [" * ", "***"]
generateBlocks(3) => ["  *  ", " *** ", "*****"]```
*/

function blocks(n) {
    const width = n + n - 1;
    const blocks = [];
    for (let stars = width; stars > 0; stars -= 2) {
        const space = ' '.repeat((width - stars) / 2);
        blocks.unshift(space + '*'.repeat(stars) + space);
    }
    return blocks;
}

for (let i = 0; i < 6; i++) {
    console.log(blocks(i));
}
