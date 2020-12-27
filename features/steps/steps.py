from behave import *
from number import *

def parse_ffloatt(text):

    return float(text)
# -- REGISTER: User-defined type converter (parse_type).
register_type(Ffloat=parse_ffloatt)

@given('A = {a:d} and B = {b:d}')
def step_impl(context,a,b):
    context.num = Numbers(a,b)
    
@given('Int A = {a:d}, B = {b:d}')
def step_impl(context,a,b):
    print(a,b)
    print("dummy")
    context.num = Numbers(a,b)

@given('Float A = {a:Ffloat}, B = {b:Ffloat}')
def step_impl(context,a,b):
    context.num = Numbers(a,b)
    
@given('A and B')
def step_impl(context):
    context.num = Numbers(1,2)

@given('wir haben "behave" installiert')
def step_impl(context):
    context.worked = False



    
@given('A and B lists')
def step_impl(context):
    A = []
    B = []
    for row in context.table:
        A.append(int(row["a"]))
        B.append(int(row["b"]))
    context.num = Numbers(A, B)

#-----------------------------------------------    

@when('A + B')
def step_impl(context):
    context.result = context.num.add()

@when('A / B')
def step_impl(context):
    context.result = context.num.divison()

    
@when('A plus B')
def step_impl(context):
    context.result = context.num.add()
    
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


@when('wir einen Test implementieren')
def step_impl(context):
    context.worked = True

# -----------------------------------------------    


@then('result is {result:d}')
def step_impl(context,result):
    assert (context.result == result)

@then('result = {r:Ffloat}')
def step_impl(context,r):
    assert(context.result == r)

@then(u'wird "behave" ihn für uns testen!')
def step_impl(context):
    assert(context.worked)
    
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
