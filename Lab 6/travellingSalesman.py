from itertools import permutations

class Graph:
    def __init__(self, numberOfVertices, vertices):
        self.vertices = vertices
        self.numberOfVertices = numberOfVertices
        self.adjacencyMatrix = [[0 for j in range(numberOfVertices)] for i in range(numberOfVertices)]


    def insertWeight(self, x, y, weight):
        self.adjacencyMatrix[x][y] = weight
        self.adjacencyMatrix[y][x] = weight

    def printGraph(self):
        for i in range(self.numberOfVertices):
            for j in range(self.numberOfVertices):
                print(self.adjacencyMatrix[i][j], end="   ")
            print()

    def getHamiltonianMinimumWeight(self):
        minimumCost = float("inf")
        startingPoint = 0
        verticesWithoutFirstVertex = self.vertices[1:]
        possibleCycles = [list(p) for p in permutations(verticesWithoutFirstVertex)]
        cycleWithMinimumCost = []
        for cycle in possibleCycles:
            cycle.insert(0, 1)
            cycle.append(1)
            cost = 0
            for i in range(len(cycle) - 1):
                vertex = cycle[i] - 1
                nextVertex = cycle[i+1] - 1
                cost += self.adjacencyMatrix[vertex][nextVertex]
            if cost < minimumCost:
                minimumCost = cost
                cycleWithMinimumCost = [item for item in cycle]

        return {"minimumCost": minimumCost, "cycle": cycleWithMinimumCost}

if __name__ == '__main__':
    newGraph = Graph(4, [1, 2, 3, 4])
    newGraph.insertWeight(0, 1, 10)
    newGraph.insertWeight(0, 3, 20)
    newGraph.insertWeight(0, 2, 15)
    newGraph.insertWeight(1, 3, 25)
    newGraph.insertWeight(3, 2, 30)
    newGraph.insertWeight(1, 2, 35)
    newGraph.printGraph()
    print(newGraph.getHamiltonianMinimumWeight())
