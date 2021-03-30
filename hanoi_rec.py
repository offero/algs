def h(towers, n, src, tgt):
  """Move n items from the tower specified by `src` to the tower specified by `tgt`.

  towers: A list of 3 lists representing the stacks of towers in the game.
  n: the number of items to move
  src: the source stack index
  tgt: the target stack index
  """
  if n == 1:
    towers[tgt].append(towers[src].pop())
    return
  aux = list({0, 1, 2} - {src, tgt})[0]
  h(towers, n-1, src, aux)
  h(towers, 1, src, tgt)
  h(towers, n-1, aux, tgt)
  
towers = [
  [5, 4, 3, 2, 1],
  [],
  [],
]

h(towers, 5, 0, 1)
print(towers)
