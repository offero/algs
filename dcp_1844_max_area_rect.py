'''
You are given a histogram consisting of rectangles of different heights. These
heights are represented in an input list, such that [1, 3, 2, 5] corresponds to
the following diagram:

      x
      x
  x   x
  x x x
x x x x

Determine the area of the largest rectangle that can be formed only from the
bars of the histogram. For the diagram above, for example, this would be six,
representing the 2 x 3 area at the bottom right.

min(height of columns from i to j * number of cols)

  1 2 3 4
1 1 1 1 1
2 X 3 2 2
3 X X 2 2
4 X X X 5

How should we iterate?
i = 0 .. N
j = i .. N

Keep track of the max height as we go
'''

def max_area_in_graph(hist):
    max_area = None
    for i in range(len(hist)):
        min_height = None # min height in range i..j
        for j in range(i, len(hist)):
            h = hist[j]
            if min_height is None or h < min_height:
                min_height = h
            current_area = (min_height * (j-i+1))
            if max_area is None or current_area > max_area:
                max_area = current_area
    return max_area


examples = [
    [1, 3, 2, 5],
    [1, 0, 1, 1],
    [0, 0, 9, 0],
    [4, 4, 9, 0],
]

for ex in examples:
    print(max_area_in_graph(ex))

