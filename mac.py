# A function to remove conflicts from the available colors for each node
def removeConflictingColors(graph, colors, available_colors):
    for i in range(len(graph)):
        if colors[i] != 0:
            for j in range(len(graph)):
                if graph[i][j] == 1 and colors[j]== 0:       
                    if colors[i] in available_colors[j]:
                        temp_colors = available_colors[j].copy()
                        temp_colors.remove(colors[i])
                        available_colors[j] = temp_colors.copy()

    return available_colors.copy()

#Recursive function to apply arc consistency for a given node
def arcConsistency(graph, node, colors, available_colors):
    neighbours = []
    changed = False
    for i in range(len(graph)):
        if graph[node][i] == 1 and colors[i]==0:
            neighbours.append(i)
            if len(available_colors[i]) == 1:
                if available_colors[i][0] in available_colors[node]:
                    temp_colors = available_colors[node].copy()
                    temp_colors.remove(available_colors[i][0])
                    available_colors[node] = temp_colors.copy()
                    changed = True

    #apply arc consistency for node neighbours if available colors of the node changed           
    if changed:
        for n in neighbours:
            temp_availabe_colors = arcConsistency(graph, n, colors, available_colors)
        
    return available_colors

#A function to apply arc consistency for all nodes 
def applyArcConsistency(graph, colors, available_colors):
    for i in range(len(colors)):
        if colors[i] == 0:
            available_colors = arcConsistency(graph, i, colors, available_colors)
            if len(available_colors[i]) == 0:
                return False, available_colors
    return True, available_colors

#MAC algorithm 
def MAC(graph, colors, node, available_colors):
    if node == len(graph):
        return True
    
    temp_colors = available_colors[node].copy()
    for c in temp_colors:
        colors[node] = c
        temp_available_colors = available_colors.copy()
        available_colors = removeConflictingColors(graph, colors, available_colors)
        result, available_colors = applyArcConsistency(graph, colors, available_colors)
        if result:
            if MAC(graph, colors, node+1, available_colors):
                return True
        available_colors = temp_available_colors.copy()
    colors[node] = 0     
    return False
