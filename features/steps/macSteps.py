from behave import *
from number import *
#from hamcrest import assert_that, equal_to, is_not
from mac import *


@given("this graph n = {n:d}, c = {c:d}")
def step_impl(context, n, c):
    graph = []
    context.colors = [0]*n
    available_colors = []
    for i in range(n):
        available_colors.append([])
    for i in range(n):
        for j in range(c):
            available_colors[i].append(j+1)
    context.available_colors = available_colors
    node_count = n
    for n in range(n):
        graph.append([])
    for row in context.table:
        for i in range(n+1):
            col = "n"+str(i)
            graph[i].append(int(row[col]))
    context.graph = graph
    
@when('coloring the map with mac algo')
def step_impl(context):
    context.result = MAC(context.graph,context.colors,0, context.available_colors)
    
    
@then('mac solution is')
def step_imp(context):
    i = 0
    for row in context.table:
        if int(row["C"]) != context.colors[i]:
            assert(False)
        i += 1
    assert(True)
