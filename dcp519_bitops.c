/* DCP 519 Bit Ops
 * Given three 32-bit integers x, y, and b, return x if b is 1 and y if b is 0, using only
 * mathematical or bit operations. You can assume b can only be 1 or 0.
 */

#include <stdio.h>
#include <stdint.h>

int32_t xyb(int32_t x, int32_t y, int32_t b) {
    return (((-x-y) * b) + y) * (-b | 1);
}

int main() {
    printf("1: %d\n", xyb(123, 456, 1));
    printf("0: %d\n", xyb(123, 456, 0));
    return 0;
}
