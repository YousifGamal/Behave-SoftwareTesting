from behave import *
from numbers import *

@given('A and B')
def step_impl(context):
    context.num = Numbers(1,2)

@when('add A and B')
def step_impl(context):
    context.result = context.num.add()


@then('result is A+B')
def step_impl(context):
    assert (context.result == 3)
