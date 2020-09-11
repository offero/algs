'''
You are given a histogram consisting of rectangles of different heights.
These heights are represented in an input list, such that [1, 3, 2, 5]
corresponds to the following diagram:

      x
      x
  x   x
  x x x
x x x x

Determine the area of the largest rectangle that can be formed only from the
bars of the histogram. For the diagram above, for example, this would be six,
representing the 2 x 3 area at the bottom right.
'''

def find_max_area(heights):
    max_area = 0
    for i in range(0, len(heights)):
        for j in range(i, len(heights)):
            height = min(heights[i:j+1])
            width = j-i+1
            area = width * height
            if area > max_area:
                max_area = area
    return max_area

if __name__ == "__main__":
    test1 = [1, 3, 2, 5]
    print(find_max_area(test1))
