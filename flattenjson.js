function flatten(ob) {
    const newOb = {};
    for (const key in ob) {
        const value = ob[key];
        if (typeof value === 'object') {
            // recurse, then flatten
            const flattened = flatten(value);
            for (const [fkey, fvalue] of Object.entries(flattened)) {
                newOb[`${key}.${fkey}`] = fvalue;
            }
        } else {
            // assign value
            newOb[key] = value;
        }
    }
    return newOb;
}


function test() {
    const test1 = {
        a: 'A',
        b: [1, 2, {arrObKey1: 'array ob value 1', arrObKey2: 'array ob value 2'}],
        c: null,
        d: 100,
    };
    const flattenedTest1 = flatten(test1);
    console.log(flattenedTest1);
}

test();
