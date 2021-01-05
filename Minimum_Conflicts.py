# Dependencies needed for the code

import random
import networkx as nx
import matplotlib.pyplot as plt
import math
import time


class MapColoring:
    def __init__(self, graph, K_colors=None, points=None, steps=False, colors=None):

        self.K_colors = K_colors  # number of colors
        self.graph = graph  # graph
        self.vertexNum = len(graph)  # no of vertices
        self.vertexColors = (
            [-1 for V in range(len(graph))] if colors == None else colors
        )  # the colors of the graph vertices
        self.points = points  # points co-ordinate of the graph
        self.steps = steps  # boolean to print solution steps
        self.exTime = 0  # execuation time

    def show_Colors(self):
        """ Function that returns current vertices colors"""

        return self.vertexColors

    ########################################## Min-conflicts ##################################################################

    def Min_Conflicts(self, k, maxSteps):
        """Performs min conflicts algorithm and return true if it have solution"""

        # an initial complete assignment for csp
        # for i in range(len(self.vertexColors)):
        #     self.vertexColors[i] = random.randint(0, self.K_colors - 1)
        self.K_colors = k
        print("The Inital colors of the graph")
        PlotGraph(self.graph, self.show_Colors(), self.points)
        print("\n\n\n")

        start_time = time.time()

        for i in range(maxSteps):
            if self.Check_Solution():
                # sol found return
                self.exTime = time.time() - start_time
                print("--- %s seconds ---" % (self.exTime))
                print("The final colors of the graph")
                PlotGraph(self.graph, self.show_Colors(), self.points)
                return True
            else:
                # check for a random conflicted variable
                # change value to minimize  conflict
                self.Minmize_Conflict()

        # loop finised no sol found return failure
        self.exTime = time.time() - start_time
        print("--- %s seconds ---" % (self.exTime))
        print("The final colors of the graph")

        PlotGraph(self.graph, self.show_Colors(), self.points)

        return False

    def Check_Solution(self):
        """checks if this graph satisfes constraints"""

        for i in range(self.vertexNum):
            for j in range(self.vertexNum):
                if (
                    self.graph[i][j] == 1
                    and self.vertexColors[i] == self.vertexColors[j]
                ):  # conflict happen no solution yet
                    return False
        return True

    def Minmize_Conflict(self):
        """checks for a random conflicted variable and change its value to minmize conflicts"""

        # get conflicted variables
        conflictsVars = []
        for i in range(self.vertexNum):
            for j in range(self.vertexNum):
                if (
                    self.graph[i][j] == 1
                    and self.vertexColors[i] == self.vertexColors[j]
                ):
                    conflictsVars.append(i)

        # choose a random variable from conflicted variable
        cVar = random.choice(conflictsVars)

        # check conflicts for each color and choose which gives the least conflicts
        neighbours = self.graph[cVar]

        conflicts = {}
        for i in range(self.K_colors):
            conflicts[i] = 0
            for j in range(self.vertexNum):
                if neighbours[j] == 1 and i == self.vertexColors[j]:
                    conflicts[i] += 1

        # get min conflicts  and change value
        minColorConflict = min(conflicts, key=conflicts.get)

        # choose a random color if more than one color gives minimum conflict
        # minColorConflict = random.choice([k for k,v in conflicts.items() if v == Conflicts[minColorConflict]])

        self.vertexColors[cVar] = minColorConflict


"""

    Utility Functions to plot the graphs

"""


def getEdges(graph):

    edges = []
    for i in range(len(graph)):
        for j in range(len(graph)):
            if graph[i][j] == 1:
                edges.append((i, j))
    return edges


def PlotGraph(graph, colors=None, points=None):
    """Utility function to plot graph """

    some_colors = {
        0: "red",
        1: "blue",
        2: "green",
        3: "yellow",
        4: "pink",
        5: "brown",
        -1: "grey",
    }
    edges = getEdges(graph)
    G = nx.Graph()
    color_map = []
    G.add_nodes_from([i for i in range(len(graph))])
    G.add_edges_from(edges)
    for node in G:
        color_map.append(some_colors[colors[node]])
    if points is None:
        my_pos = nx.circular_layout(G)
    else:
        positions = {}
        for i in range(len(points)):
            positions[i] = list(points[i])
        my_pos = positions
    nx.draw(
        G,
        pos=my_pos,
        with_labels=True,
        node_color=color_map,
        node_size=400,
        edge_color="black",
        linewidths=1,
        font_size=15,
    )
    plt.show()
