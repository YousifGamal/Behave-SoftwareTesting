from behave import *
from number import *
from hamcrest import assert_that, equal_to, is_not
from backtracking import *

def parse_bool(text):
    if text == "True":
        return True
    else:
        return False

register_type(Bbool=parse_bool)

#BackGround
@given('colors to use')
def step_impl(context):
    colors = []
    for row in context.table:
        colors.append(row["colors"])
    context.colors = colors

#Assignment is complete 

@given('nodes assigned values')
def step_impl(context):
    assignemt = []
    for row in context.table:
        if row["assignemt"] == "-1":
            assignemt.append(-1)
        else:    
            assignemt.append(row["assignemt"])
    context.assignemt = assignemt
@when('check is it complete')
def step_impl(context):
    context.compAssignmet =  completeAssignmet(context.assignemt)

@then('complete assignmet = {r:Bbool}')
def step_imp(context,r):
    assert(r == context.compAssignmet)


#Assignment is consistent


@given('var = {var:d}, and n = {n:d}')
def step_impl(context,var,n):
    context.var = var
    context.n = n
    assignemt = []
    graph = []
    for n in range(n):
        graph.append([])
    for row in context.table:
        if row["assignemt"] == "-1":
            assignemt.append(-1)
        else:    
            assignemt.append(row["assignemt"])
        for i in range(n+1):
            col = "n"+str(i)
            print(col)
            if int(row[col]) != -1:
                graph[i].append(int(row[col]))
    print(graph[2])
    print("lollllllllllllllllllllllllllllllllll")
    print("dummy")
    context.assignemt = assignemt
    context.graph = graph
@when('check is consistent assignemt')
def step_impl(context):
    context.consistent =  consistentAssignment(context.assignemt,context.graph,context.var)

@then('consistent assignment = {r:Bbool}')
def step_imp(context,r):
    assert(r == context.consistent)


#backtracking
@given("the following graph n = {n:d}")
def step_imp(context,n):
    context.n = n
    graph = []
    for n in range(n):
        graph.append([])
    for row in context.table:
        for i in range(n+1):
            col = "n"+str(i)
            print(col)
            if int(row[col]) != -1:
                graph[i].append(int(row[col]))
    context.graph = graph
@when('solve using backtracking')
def step_impl(context):
    context.result =  initializeBacktracking(context.n,context.graph,context.colors)

@then('the solution is')
def step_imp(context):
    i = 0
    for row in context.table:
        if row["result"] != context.result[i]:
            assert(False)
        i += 1
    assert(True)




