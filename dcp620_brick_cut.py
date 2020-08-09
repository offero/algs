# A wall consists of several rows of bricks of various integer lengths and uniform height. Your goal
# is to find a vertical line going from the top to the bottom of the wall that cuts through the fewest
# number of bricks. If the line goes through the edge between two bricks, this does not count as a
# cut.

# For example, suppose the input is as follows, where values in each row represent the lengths of
# bricks in that row:

# [
    # [3, 5, 1, 1],
    # [2, 3, 3, 2],
    # [5, 5],
    # [4, 4, 2],
    # [1, 3, 3, 3],
    # [1, 1, 6, 1, 1]
# ]

# The best we can we do
# here is to draw a line after the eighth brick, which will only require cutting through the bricks in
# the third and fifth row.

# Given an input consisting of brick lengths for each row such as the one above, return the fewest
# number of bricks that must be cut to create a vertical line.

######################

# Solution Strategy:
# Count the number of bricks that share an edge
# Count the running sum along each row. Each sum point is an edge.
# Keep a count of which edge has the highest running sum
# The solution is obtained by subtracting the highest shared edge count
# from the number of rows.
# The time is O(n) where n is the number of cells.
# (size of input, touch each val once).
# or O(nxm) where n,m are rows, cols.

def min_bricks(bricks):
    wall_length = sum(bricks[0])
    edge_counts = [0] * (wall_length+1)
    max_shared_edge_ct = 0
    for row in bricks:
        running_sum = 0
        for val in row:
            running_sum += val
            edge_counts[running_sum] += 1
            if edge_counts[running_sum] > max_shared_edge_ct \
                    and running_sum != wall_length:
                max_shared_edge_ct = edge_counts[running_sum]
    num_rows = len(bricks)
    return num_rows - max_shared_edge_ct


def test1():
    bricks = [
        [3, 5, 1, 1],
        [2, 3, 3, 2],
        [5, 5],
        [4, 4, 2],
        [1, 3, 3, 3],
        [1, 1, 6, 1, 1]
    ]
    print(min_bricks(bricks))

if __name__ == "__main__":
    test1()
