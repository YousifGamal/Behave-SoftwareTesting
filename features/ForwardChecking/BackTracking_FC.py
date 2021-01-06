'''
Forward Checking
'''
import numpy as np

class Forward_Checking:

    #Forward Checking
    def Forward_Check(self,var,color,domain,assignment,N,graph,k):
        for j in range(0,N):
            #remove the assigned color of the current node from the domain of its unassigned neighbours
            if(graph[var][j] == 1 and color in domain[j] and assignment[j] == -1): 
                domain[j].remove(color)
                if(len(domain[j]) == 0): #FC would fail if on the neighbours domain space became empty
                    return False
        return True

    def Reverse_Forward_Check(self,var,color,domain,assignment,N,graph,k):
        for j in range(0,N):
            #reverse the Forward Checking by appending the current colors to the unassigned neighbours
            if(graph[var][j] == 1 and color not in domain[j] and assignment[j] == -1):
                domain[j].append(color)

    def isConsistent(self,var,color,assignment,N,graph,k):
        for j in range(0,N):
            #check if the assigned color of this node is consistent with its' assigned neighbours
            if(graph[var][j] == 1 and assignment[j] == color):
                return False
        return True

    def Backtracking_FC(self,length,assignment,domain,N,graph,k):
        if(length == N):
            return assignment
        var = length #pick node number/order var
        for color in domain[var]: #loop on the node's domain of colors
            #check if this color is consistent with the given node as it may get conflicted with one of the assigned neighbours of this node
            if(self.isConsistent(var,color,assignment,N,graph,k)):
                assignment[var] = color
                if(self.Forward_Check(var,color,domain,assignment,N,graph,k)): #check if the FC has failed or not
                    result = self.Backtracking_FC(length+1,assignment,domain,N,graph,k)
                    if(result is not None):
                        return result
                    else:
                        self.Reverse_Forward_Check(var,color,domain,assignment,N,graph,k) #reset the domain in case of failure
                else:
                    self.Reverse_Forward_Check(var,color,domain,assignment,N,graph,k) #reset the domain in case of failure
        assignment[var] = -1 #reset the color of the node
        return None
    def Solve_Backtracking_FC(self,assignment,domain,N,graph,k):
        return self.Backtracking_FC(0,assignment,domain,N,graph,k)