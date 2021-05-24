from sys import maxsize as PLUS_INF

class Node(object):
    def __init__(self, name):
        self.name = name
    def getName(self):
        return self.name
    def __str__(self):
        return self.name
class Edge(object):
    def __init__(self, src_nm, dest_nm):
        self.src_nm = src_nm
        self.dest_nm = dest_nm
    def getSource_nm(self):
        return self.src_nm
    def getDestination_nm(self):
        return self.dest_nm
    def __str__(self):
        return "{:3}->{:3}".format(self.src_nm, self.dest_nm)

class WeightedEdge(Edge):
    def __init__(self, src_nm, dest_nm, weight=1.0):
        Edge.__init__(self, src_nm, dest_nm)
        self.weight = weight
    def getWeight(self):
        return self.weight
    def __str__(self):
        return "{:3}->({:3})->{}".format(self.src_nm, self.weight, self.dest_nm)

class Digraph(object):
    def __init__(self):
        self.nodes = []
        self.node_names = []
        self.wedges = []
        self.adjacencyList = {}
        self.edgeWeights = {}
    def addNode(self, node):
        if node in self.nodes:
            raise ValueError("Duplicated node")
        else:
            self.nodes.append(node)
            node_nm = node.getName()
            self.node_names.append(node_nm)
            self.adjacencyList[node_nm] = []
    def addEdge(self, weighted_edge):
        src_nm = weighted_edge.getSource_nm()
        dest_nm = weighted_edge.getDestination_nm()
        if not (src_nm in self.node_names and dest_nm in self.node_names):
            raise ValueError("Node not in Graph")
        self.wedges.append(weighted_edge)
        self.adjacencyList[src_nm].append(dest_nm)
        self.edgeWeights[(src_nm, dest_nm)] = weighted_edge.getWeight()
    def getNeighbors(self, node_nm):
        return self.adjacencyList[node_nm]
    def getAdjacencyList(self):
        return self.adjacencyList
    def getNode_NMs(self):
        return self.node_names
    def getWEdges(self):
        return self.wedges
    def getEdgeWeight(self, edge):
        if (edge.src_nm, edge.dest_nm) in self.edgeWeights:
            return self.edgeWeights[(edge.src_nm, edge.dest_nm)]
        else:
            None
    def printConnectivity(self):
        for node_nm in self.node_names:
            print("AdjacencyList[{}] = {}".format(node_nm, self.adjacencyList[node_nm]))
    def printEdges(self):
        eCount = 0
        for e in self.wedges:
            print(" {}".format(e), end=', ')
            eCount += 1
            if eCount % 5 == 0:
                print()

    def __str__(self):
        result = ''
        for src in self.nodes:
            for dest in self.edges[src]:
                result = result + src.getName() + '->'\
                    + dest.getName() + '\n'
        return result[:-1] # omit final newline

        




def Dijkstra(G, start_nm, end_nm):
    errorInLoop = False
    nodeAccWeight= {}
    nodeStatus = {}
    prevNodes_nm = {} # previous node in the path from the start to the end
    selectedNodes = []
    remainingNodes = []
    wEdges = G.getWEdges()

    for node_nm in G.node_names:
        e = Edge(start_nm, node_nm)
        if node_nm == start_nm:
            eWeight = 0
        else: 
            eWeight = G.getEdgeWeight(e)
            if eWeight == None:
                eWeight = PLUS_INF
        nodeAccWeight[node_nm] = eWeight
        nodeStatus[node_nm] = False
        prevNodes_nm[node_nm] = start_nm
        if node_nm != start_nm:
            remainingNodes.append(node_nm)

    nodeAccWeight[start_nm] = 0
    nodeStatus[start_nm] = True
    selectedNodes.append(start_nm)
    count = 1
    while len(remainingNodes) != 0:
        minAccWeight = PLUS_INF
        minNode = None
        for n in remainingNodes:
            nAccWeight = nodeAccWeight[n]
            if nAccWeight != None and nAccWeight < minAccWeight:
                    minNode, minAccWeight = n, nodeAccWeight[n]
        if minNode == None:
            print("No minNode was selected at this round !!")
            print("Error - graph is not fully connected !!")
            errorInLoop = True
            break
        else:
            selectedNodes.append(minNode)
            minAccWeight = nodeAccWeight[minNode]
            for rn in remainingNodes:
                if rn == minNode:
                    continue
                e = Edge(minNode, rn)
                eWeight = G.getEdgeWeight(e)
                if eWeight == None:
                    continue
                if nodeAccWeight[rn] > minAccWeight + eWeight:
                    nodeAccWeight[rn] = minAccWeight + eWeight
                    prevNodes_nm[rn] = minNode
                if minNode == end_nm:
                    break
                count += 1
    
    if errorInLoop == True:
        return None
    path = [end_nm]
    cur_node_nm = end_nm
    while cur_node_nm in selectedNodes:
        if cur_node_nm == start_nm:
            break
        else:
            cur_node_nm = prevNodes_nm[cur_node_nm]
            path.insert(0,cur_node_nm)
    return path, nodeAccWeight[end_nm]




def initGraph(G):
    node_names = ["SL", "CC", "SC", "SW", "WJ", "GR", "DJ", "DG", "PH", "GJ", "BS"]
    w_edges = [
        WeightedEdge("SL", "CC", 71), WeightedEdge("CC", "SL", 71), 
        WeightedEdge("CC", "SC", 79), WeightedEdge("SC", "CC", 79), 
        WeightedEdge("SL", "SW", 34), WeightedEdge("SW", "SL", 34), 
        WeightedEdge("SW", "WJ", 84), WeightedEdge("WJ", "SW", 84), 
        WeightedEdge("CC", "WJ", 47), WeightedEdge("WJ", "CC", 47), 
        WeightedEdge("WJ", "GR", 91), WeightedEdge("GR", "WJ", 91), 
        WeightedEdge("SC", "GR", 42), WeightedEdge("GR", "SC", 42), 
        WeightedEdge("SW", "DJ", 109), WeightedEdge("DJ", "SW", 109), 
        WeightedEdge("WJ", "DG", 174), WeightedEdge("DG", "WJ", 174), 
        WeightedEdge("GR", "PH", 200), WeightedEdge("PH", "GR", 200), 
        WeightedEdge("DJ", "DG", 120), WeightedEdge("DG", "DJ", 120), 
        WeightedEdge("DG", "PH", 66), WeightedEdge("PH", "DG", 66), 
        WeightedEdge("DJ", "GJ", 138), WeightedEdge("GJ", "DJ", 138), 
        WeightedEdge("DG", "GJ", 170), WeightedEdge("GJ", "DG", 170), 
        WeightedEdge("DG", "BS", 87), WeightedEdge("BS", "DG", 87), 
        WeightedEdge("PH", "BS", 93), WeightedEdge("BS", "PH", 93), 
        WeightedEdge("GJ", "BS", 202), WeightedEdge("BS", "GJ", 202)
    ]

    for i in range(len(node_names)):
        v_name = node_names[i]
        node = Node(v_name)
        G.addNode(node)
    for we in w_edges:
        G.addEdge(we)
    return G



def main():
    G = Digraph()
    initGraph(G) # inserts nodes and edges into Digraph G
    nodes = G.getNode_NMs()
    print("Nodes : ", nodes)
    edges = G.getWEdges()
    print("Edges :")
    G.printEdges() # use printEdges() method in class Digraph
    print("Connectivity :")
    G.printConnectivity()
    #print("\nTrying ShortestPath_Dijkstra : ({} -> {})".format("GJ", "SC"))
    path_Dijkstra, path_cost = Dijkstra(G, "GJ", "SC")
    print("ShortestPath_Dijkstra ({} -> {}): {}, path_cost ={}"\
    .format("GJ", "SC", path_Dijkstra, path_cost))
    path_Dijkstra, path_cost = Dijkstra(G, "SC", "GJ")
    print("ShortestPath_Dijkstra ({} -> {}): {}, path_cost ={}"\
    .format("SC", "GJ", path_Dijkstra, path_cost))
    #print("\nTrying ShortestPath_Dijkstra : ({} -> {})".format("SL", "BS"))
    path_Dijkstra, path_cost = Dijkstra(G, "SL", "BS")
    print("ShortestPath_Dijkstra ({} -> {}): {}, path_cost ={}"\
    .format("SL", "BS", path_Dijkstra, path_cost))
    path_Dijkstra, path_cost = Dijkstra(G, "BS", "SL")
    print("ShortestPath_Dijkstra ({} -> {}): {}, path_cost ={}"\
    .format("BS", "SL", path_Dijkstra, path_cost))
if __name__ == "__main__":
    main()