from SearchAlgorithm import SearchAlgorithm
from collections import deque

# BFS class inheres SearchAlgorithm class
class BFS(SearchAlgorithm):

    #initialize the BFS setting the frontier list to be a queue
    def init(self):
        SearchAlgorithm.init(self, deque([]))

    def doBFS(self, state, root):
        parent = {} # init the parent dictionary
        self.frontier.append(root)
        self.visited.add(root)
        while self.frontier:
            crnt = self.frontier.popleft()
            self.visited.add(crnt)
            if crnt == self.end:  # the goal is reached
                return SearchAlgorithm.backtrace(self,parent, root), self.visited
            for adj in state.getNext(crnt): # loop on adj nodes and add in the queue
                if adj not in self.visited and adj not in self.frontier:
                    parent[adj] = crnt
                    self.frontier.append(adj)

