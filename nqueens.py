'''
N-Queens backtracking. My reproduction after watching a video yesterday.

state: an array of column placements (row x col)

Eg.  0 1 2 3
    [ | |Q| ]  Row 0 column 2
    [Q| | | ]  Row 1 column 0
    [ | | |Q]  Row 2 column 3
    [ |Q| | ]  Row 3 column 1

state: [2, 0, 3, 1]

Approach: Iterate each row, place in column.

Pseudocode:
    check base case
    for every row
        find possible queen placements
        place queen
        recurse
        unplace queen
'''

def solve(n):
    state = []
    solutions = []
    return search(state, solutions, n)

def find_candidate_cols(state, n):
    '''
    Returns: Set of possible column values for next placement position
    '''
    i = len(state) # how many we have placed so far = next placement position
    candidates = set(range(n)) - set(state) # all possible places minus the columns already taken
    # remove candidates on diagonals
    # find the column the diagonal on row 0, row 1, row 2, ... row i-1 from the current position
    for row, col in enumerate(state):
        dist = i - row
        # a Queen cannot exist (row-dist, col-dist) back or (row+dist, col+dist) back from this
        # position. It won't exist in row-dist back because we are iterating rows in order.
        bad_pos = col - dist
        bad_pos2 = col + dist
        candidates.discard(bad_pos)
        candidates.discard(bad_pos2)
    return candidates

def is_valid_state(state, n):
    # a valid placement for all n queens has been found
    return len(state) == n

def state_string(state):
    return ','.join(map(str, state))

def search(state, solutions, n):
    # base case
    if is_valid_state(state, n):
        solutions.append(state_string(state))
        return solutions

    candidates = find_candidate_cols(state, n)
    # print('state', state, 'candidates', candidates)
    for col in candidates:
        state.append(col)
        search(state, solutions, n)
        state.pop()

    return solutions

def main():
    solutions = solve(4)
    print('solutions:', solutions)

if __name__ == "__main__":
    main()

