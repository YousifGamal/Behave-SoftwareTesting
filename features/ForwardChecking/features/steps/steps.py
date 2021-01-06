from behave import *
from BackTracking_FC import *


@given('the following graph with N = 5')
def step_impl(context):
    N0 = []
    N1 = []
    N2 = []
    N3 = []
    N4 = []
    N5 = []
    context.graph = []
    for row in context.table:
        N0.append(int(row["N0"]))
        N1.append(int(row["N1"]))
        N2.append(int(row["N2"]))
        N3.append(int(row["N3"]))
        N4.append(int(row["N4"]))
        N5.append(int(row["N5"]))
    context.graph.append(N0)
    context.graph.append(N1)
    context.graph.append(N2)
    context.graph.append(N3)
    context.graph.append(N4)
    context.graph.append(N5) 
    context.k = 3
    context.N = 6
    context.assignment = [-1,-1,-1,-1,-1,-1]
    context.domain = [ [ i for i in range(0,context.k)] for i in range(0,context.N)]
    context.obj = Forward_Checking()
    

#-----------------------------------------------    

@when('Test the graph with the forward checking')
def step_impl(context):
    context.colors = Forward_Checking.Backtracking_FC(
    context.obj,
    0,
    context.assignment,
    context.domain,
    context.N,
    context.graph,
    context.k)

@then('we check that the colors assigned to each node')
def step_impl(context):
    print(context.colors)
    i = 0
    for row in context.table:
        if int(row["Colors"]) != context.colors[i]:
            assert(False)
        i += 1
    print(context.colors)