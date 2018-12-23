from SearchAlgorithm import SearchAlgorithm
import heapq

# A* class inheres SearchAlgorithm class
class AStar(SearchAlgorithm):
    def init(self):
        SearchAlgorithm.init(self, [])
        self.g = {}
        self.f = {}

    def doAStar(self, state, root, heuristic):
        parent = {}
        heapq.heappush(self.frontier, (heuristic(root, self.end, state), root))
        self.visited.add(root)
        self.g[root] = 0

        while self.frontier:
            crnt = heapq.heappop(self.frontier)[1]
            self.visited.add(crnt)
            # check if a goal was reached
            if crnt == self.end:
                return SearchAlgorithm.backtrace(self, parent, root), self.visited

            for adj in state.getNext(crnt):
                self.g[adj] = self.g[crnt] + 1
                h = heuristic(adj,self.end, state)
                if adj in self.f:
                    old_cost = self.f[adj]
                else:
                    old_cost = -1
                if adj not in self.visited and (old_cost, adj) not in self.frontier:
                    heapq.heappush(self.frontier, (h + self.g[adj], adj))
                    self.f[adj] = h + self.g[adj]
                    parent[adj] = crnt
                elif (old_cost, adj) in self.frontier and (h + self.g[adj]) < old_cost:
                    self.frontier.remove((old_cost, adj))
                    heapq.heappush(self.frontier, (h + self.g[adj], adj)) # decrease key
                    self.f[adj] = h + self.g[adj]
                    parent[adj] = crnt

