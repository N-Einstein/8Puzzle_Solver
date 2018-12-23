from SearchAlgorithm import SearchAlgorithm

# DFS class inheres SearchAlgorithm class
class DFS(SearchAlgorithm):
    def init(self):
        SearchAlgorithm.init(self, [])

    def doDFS(self, state,root):
        parent = {}
        self.frontier.append(root)
        self.visited.add(root)
        while self.frontier:
            crnt = self.frontier.pop()
            self.visited.add(crnt)
            if crnt == self.end: # check if the goal was reached
                return SearchAlgorithm.backtrace(self, parent, root), self.visited
            for adj in state.getNext(crnt): # add the adj node to the frontier list
                if adj not in self.visited and adj not in self.frontier:
                    parent[adj] = crnt
                    self.frontier.append(adj)
