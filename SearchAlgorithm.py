from State import State

class SearchAlgorithm:
    def init(self, frontier):
        self.frontier = frontier
        self.visited = set()    # visited bodes set
        self.end = "0,1,2,3,4,5,6,7,8" # target state

    # returns the right path from the source to the goal
    def backtrace(self, parent, root):
        path = [self.end]
        while path[-1] != root:
            path.append(parent[path[-1]])
        path.reverse()
        return path, len(path)
