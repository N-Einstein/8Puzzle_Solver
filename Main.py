import timeit

from BFS import BFS
from DFS import DFS
from AStar import AStar


from State import State
import math

def manhattanDistance(crnt, end, state):
   currX = state.getX(crnt)
   goalX = state.getX(end)
   currY = state.getY(crnt)
   goalY = state.getY(end)
   h = []
   for x1, x2, y1, y2 in zip(currX, goalX, currY, goalY):
      h.append(abs(x1 - x2) + abs(y1 - y2))
   return sum(h)

def euclideanDistance(crnt, end, state):
   currX = state.getX(crnt)
   goalX = state.getX(end)
   currY = state.getY(crnt)
   goalY = state.getY(end)
   h = []
   for x1, x2, y1, y2 in zip(currX, goalX, currY, goalY):
      h.append(math.sqrt((x1 - x2)**2 + (y1 - y2)**2))
   return sum(h)

def printBoard(s):
   print("")
   x = 0
   while x < 9:
        c = s[x]
        if c == "0":
           c = " "
        if x % 3 == 0:
            print('.---' * 3 + ".")
            print("| " + c + " |", end="")
        elif x % 3 == 1:
            print(" " + c + " |", end="")
        else:
            print(" " + c + " |")
        if x == 8:
            print('.---' * 3 + ".")
        x = x + 1

def BFSAlgo(state):
    bfs = BFS()
    bfs.init()
    start = timeit.default_timer()
    bfsAlgo = bfs.doBFS(state, "1,2,5,3,4,0,6,7,8")
    path = bfsAlgo[0][0]
    depth = bfsAlgo[0][1]
    explored = bfsAlgo[1]
    stop = timeit.default_timer()
    print('============= Time =============')
    print(stop - start)
    print('============= Depth =============')
    print(depth)
    print('============= Explored =============')
    print(explored)
    print('============= Path =============')
    for i in path:
        printBoard(i.split(','))

def DFSAlgo(state):
    dfs = DFS()
    dfs.init()
    start = timeit.default_timer()
    dfsAlgo = dfs.doDFS(state, "1,2,5,3,4,0,6,7,8")
    path = dfsAlgo[0][0]
    depth = dfsAlgo[0][1]
    explored = dfsAlgo[1]
    stop = timeit.default_timer()
    print('============= Time =============')
    print(stop - start)
    print('============= Depth =============')
    print(depth)
    print('============= Explored =============')
    print(explored)
    print('============= Path =============')
    for i in path:
        printBoard(i.split(','))

def AStarAlgo(state, heuristic):
    a = AStar()
    a.init()
    start = timeit.default_timer()
    aAlgo = a.doAStar(state, "1,2,5,3,4,0,6,7,8", heuristic)
    path = aAlgo[0][0]
    depth = aAlgo[0][1]
    explored = aAlgo[1]
    stop = timeit.default_timer()
    print('============= Time =============')
    print(stop - start)
    print('============= Depth =============')
    print(depth)
    print('============= Explored =============')
    print(explored)
    print('============= Path =============')
    for i in path:
        printBoard(i.split(','))

if __name__ == '__main__':
    state = State()
    print('1 : BFS ,   2: DFS ,   3 : A* manhattanDistance ,   4 : A* euclideanDistance')
    n = int(input('choose number of algorithm'))
    if n == 1:
        BFSAlgo(state)
    elif n == 2:
        DFSAlgo(state)
    elif n == 3:
        AStarAlgo(state, manhattanDistance)
    elif n == 4:
        AStarAlgo(state, euclideanDistance)




