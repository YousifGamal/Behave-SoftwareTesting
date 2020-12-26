from behave import *
from number import *

@given('A = {a:d} and B = {b:d}')
def step_impl(context,a,b):
    context.num = Numbers(a,b)


@when('A + B')
def step_impl(context):
    context.result = context.num.add()

@when('A / B')
def step_impl(context):
    context.result = context.num.divison()


@then('result is {result:d}')
def step_impl(context,result):
    assert (context.result == result)
#-----------------------------------------------
def parse_number(text):
    """
    Convert parsed text into a number.
    :param text: Parsed text, called by :py:meth:`parse.Parser.parse()`.
    :return: Number instance (integer), created from parsed text.
    """
    return float(text)
# -- REGISTER: User-defined type converter (parse_type).
register_type(Number=parse_number)

@given('A = {a:Number}, B = {b:Number}')
def step_impl(context,a,b):
    context.num = Numbers(a,b)

@when('A divided by B')
def step_impl(context):
    context.result = context.num.divison()
  
@then('result = {r:Number}')
def step_impl(context,r):
    assert(context.result == r)

#--------------------------------------------------------


@given('wir haben "behave" installiert')
def step_impl(context):
    context.worked = False

@when('wir einen Test implementieren')
def step_impl(context):
    context.worked = True

@then(u'wird "behave" ihn für uns testen!')
def step_impl(context):
    assert(context.worked)