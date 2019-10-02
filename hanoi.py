# solve the towers of hanoi


def top_of_tower(state, n):
    """
    n: the tower number: 1, 2, 3
    """
    tower_size = len(state) // 3
    idx = tower_size * (n-1)

    for i in range(tower_size*(n-1), tower_size*n):
        if state[i] != '-':
            idx = i
    return idx


def gen_new_state(state, i1, i2):
    new_state = [c for c in state]
    new_state[i2], new_state[i1] = state[i1], '-'
    return ''.join(map(str, new_state))


# states by moving the top of one tower to the other 2
def gen_new_states(state, ifrom, itoa, itob):
    states = []
    v1 = state[ifrom]
    v2 = state[itoa]
    v3 = state[itob]

    if v1 != '-':
        if v2 == '-':
            states.append(gen_new_state(state, ifrom, itoa))
        elif int(v1) < int(v2):
            states.append(gen_new_state(state, ifrom, itoa+1))

        if v3 == '-':
            states.append(gen_new_state(state, ifrom, itob))
        elif int(v1) < int(v3):
            states.append(gen_new_state(state, ifrom, itob+1))

    return states


def gen_next_states(state):
    """
    The next possible states are moves from the tops of the 3 towers
    """
    states = []
    tower_size = len(state) // 3

    i1 = top_of_tower(state, 1)
    i2 = top_of_tower(state, 2)
    i3 = top_of_tower(state, 3)

    states.extend(gen_new_states(state, i1, i2, i3))
    states.extend(gen_new_states(state, i2, i1, i3))
    states.extend(gen_new_states(state, i3, i1, i2))

    return states


def print_states(endstate, frommap):
    states = []
    state = endstate
    while True:
        if state not in frommap:
            break
        states.append(state)
        state = frommap[state]

    for state in reversed(states):
        print_state(state)


def print_state(state):
    n = len(state)//3
    print(state[:n] + ' | ' + state[n:n*2] + ' | ' + state[n*2:])


def hanoi(size=5):
    """
    size: The height of the discs
    """
    countdownstr = ''.join(map(str, range(size, 0, -1)))
    start_state = countdownstr + ('-' * size * 2)

    frommap = {start_state: None}
    visited = set()
    stack = [start_state]

    goalstate = '-' * size * 2 + countdownstr

    while stack:
        state = stack.pop()
        if state == goalstate:
            print_states(state, frommap)
            return True
        visited.add(state)
        new_states = [s for s in gen_next_states(state) if s not in visited]
        for s in new_states:
            frommap[s] = state
        stack.extend(new_states)

    return False

if __name__ == '__main__':
    hanoi(3)
