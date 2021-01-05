# | 3              | 6      |
#   | 4              | 24     |
#   | 5              | 120    |
#   | 6              | 720    |
#   | 7              | 5040   |

from behave import *
from Minimum_Conflicts import *
#from hamcrest import assert_that, equal_to, is_not


# @given("number {number:d}")
# def init_num(context, number):
#     context.num = Numbers(number)


@given("graph nodes colors is {colors} and adjacency matrix is {graphs}")
def init_graph(context, colors, graphs):
    graphTemp = graphs.split("-")
    graph = [list(map(int, graphTemp[i].split(","))) for i in range(len(graphTemp))]
    colors = newnumbers = list(map(int, colors.split(",")))
    context.graph = MapColoring(graph=graph, colors=colors)


@when("I check for solution")
def check_solution(context):
    context.result = context.graph.Check_Solution()


@when("I call Min_Conflicts with k {k:d}")
def check_solution(context, k):
    context.result = context.graph.Min_Conflicts(k, 1000)


@then("It returns {result}")
def show_result(context, result):
    # PlotGraph(context.graph.graph, context.graph.vertexColors)
    solnFound = True if result == "True" else False
    assert(solnFound==context.result)
