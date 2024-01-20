
initialState = [1,2,5,
                3,4,0,
                6,7,8]

goalState = [1,2,3,
             4,5,6,
             7,8,0]

def print_state(state):
    print(state[0], "|", state[1], "|", state[2])
    print(state[3], "|", state[4], "|", state[5])
    print(state[6], "|", state[7], "|", state[8], "\n")

print("Initial state of the board is: \n")
print_state(initialState)
print("Goal state of the board is: \n")
print_state(goalState)

DOWN = 3
UP = -3
RIGHT = 1
LEFT = -1
MOVES = { UP : "UP"  , DOWN : "DOWN" , RIGHT : "RIGHT" , LEFT : "LEFT" }

def actions(state):
    index = state.index(0)
    moves = []
    if index > 2:
        moves.append(UP)
    if index < 6:
        moves.append(DOWN)
    if (index + 1) % 3 != 0:
        moves.append(RIGHT)
    if index % 3 != 0:
        moves.append(LEFT)
    return moves

# testSate = [1,2,3,
#             4,5,0,
#             7,6,8]
# for i in actions(testSate):
#     print(MOVES[i])

def result(state, move):
  temp = state.copy()
  index = temp.index(0)
  temp[index], temp[index+move] = temp[index+ move], temp[index]
  return temp

def is_goal(state):
    return state == goalState


class Node:
  def __init__(self, state, m=[]):
    self.state = state.copy()
    self.moves= m.copy()

  def __str__(self):
    print_state(self.state)
    print(self.moves)
    return ""

def BFS(state):
  node = Node(state)
  open = [node]
  closed = []
  while open:
    N = open.pop(0)
    if is_goal(N.state):
      print(N)
      return
    closed.append(N.state)
    for m in actions(N.state):
      tempState = result(N.state,m)
      if tempState not in closed:
        ms =N.moves.copy()
        ms.append(MOVES[m])
        n = Node(tempState, ms)
        open.append(n)

BFS([1,5,3,4,0,7,2,8,6])