function d2b(d) {
    if (d == 0) return "";
    return d2b(Math.floor(d/2)) + String(d%2) ;
}

console.log(d2b(20))
console.log(d2b(233))
