from behave import *
from numbers import *

@given('A and B')
def step_impl(context):
    context.num = Numbers(1,2)
    
@given('A and B lists')
def step_impl(context):
    A = []
    B = []
    for row in context.table:
        A.append(int(row["a"]))
        B.append(int(row["b"]))
    context.num = Numbers(A, B)
    
@when('add A and B')
def step_impl(context):
    context.result = context.num.add()

@when('subtract A and B')
def step_impl(context):
    context.result = context.num.sub()
    
@when('Merge A, B with working function')
def step_impl(context):
    context.result = context.num.working_merge_lists_sorted()

@when('Merge A, B with wrong function')
def step_impl(context):
    context.result = context.num.wrong_merge_lists_sorted()

@when('Sum elements in A and B')
def step_impl(context):
    context.result = context.num.get_total_sum()
    
@when('Get the minimum number')
def step_impl(context):
    context.min = context.result[0]
    
@when('Merge A and B then get the minimum number')
def step_impl(context):
    context.execute_steps(u"""when Merge A, B with working function""")
    context.min = context.result[0]


@then('result is A+B')
def step_impl(context):
    assert (context.result == 3)
    
@then('result is A-B')
def step_impl(context):
    assert (context.result == -1)
    
@then('we get list C sorted')
def step_impl(context):
    i = 0
    for row in context.table:
        if int(row["C"]) != context.result[i]:
            assert(False)
        i += 1
    assert(True)

@then('total sum is {sum1}')
def step_impl(context, sum1):
    assert(int(sum1) == context.result)
    
@then('minimum number is {min1}')
def step_impl(context, min1):
    assert(int(min1) == context.result[0])