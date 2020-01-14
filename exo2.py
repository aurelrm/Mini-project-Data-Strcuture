import sys
 
class Graph():
 
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = [[0 for column in range(vertices)] 
                      for row in range(vertices)]
        self.allPaths = []

    #get the path from src to node
    def getPath(self, src, node, paths, pathToNode):
        if node == src:
            pathToNode.append("g"+str(src+1))
            pathToNode.reverse()
            return pathToNode
        else:
            endpoint = "g" + str(node+1)
            pathToNode.append(endpoint)
            for p in paths:
                if node == p[1]:
                    return self.getPath(src, p[0], paths, pathToNode)
                    
    #show all the paths to all the nodes and their cost
    def printResults(self, distances, src, paths):
        for node in range(self.vertices):
            pathToNode = []
            pathToNode = self.getPath(src, node, paths, pathToNode)
            self.allPaths.append(pathToNode)
            print("The shortest path from", "g"+str(src+1), "to", "g"+str(node+1), "is", pathToNode, "and costs", distances[node])

    #show the paths to the leaves of the 
    def getMinimalNumberOfPaths(self):
        self.allPaths = sorted(self.allPaths, key = len)
        pathsToTake = self.allPaths.copy()
        self.allPaths.reverse()
        pathsToRemove =[]
        
        for path in pathsToTake:
            lastNode = path[len(path)-1]
            for comparedPath in self.allPaths:
                if lastNode in comparedPath and path != comparedPath:
                    pathsToRemove.append(path)
                    break
        pathsToTake = [x for x in pathsToTake if x not in pathsToRemove]
        print("The optimal number of volunteers to send is", len(pathsToTake),".")
        print("They have to follow these paths :"
              )
        for p in pathsToTake:
            print(p)
        print("With these paths, all the endpoints are covered.")

    #get vertice with the minimum distance from src not in the list of seen nodes
    def mindistance(self, distances, seenNodes):
        min = sys.maxsize

        for v in range(self.vertices):
            if distances[v] < min and seenNodes[v] == False:
                min = distances[v]
                min_index = v
 
        return min_index          
        
 
    def dijkstra(self, src):
        distances = [sys.maxsize] * self.vertices
        distances[src] = 0
        seenNodes = [False] * self.vertices

        paths = []
        for cout in range(self.vertices):
       
            u = self.mindistance(distances, seenNodes)
            seenNodes[u] = True

            for v in range(self.vertices):
                if float(self.edges[u][v]) > 0 and seenNodes[v] == False and distances[v] > distances[u] + float(self.edges[u][v]):
                    distances[v] = distances[u] + float(self.edges[u][v])
                    if len(paths) == 0:
                        paths.append([u,v])
                    else:
                        for p in range(len(paths)):
                            a = paths[p-1]
                            if v == a[1]:
                                paths[p-1] = [u,v]
                                break
                        paths.append([u,v])

        self.printResults(distances, src, paths)
        self.getMinimalNumberOfPaths()
      

def read_data(file_name):
    data = []
    file = open(file_name, "r")
    for line in file:
        data.append(line.split())
    return data


if __name__ == "__main__":
    data = read_data("./data_exo_2.txt")      
    g  = Graph(len(data))
    g.edges = data
    g.dijkstra(0)
    input("Appuyer sur une touche pour quitter...")
