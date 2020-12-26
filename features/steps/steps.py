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

def parse_ffloatt(text):
    """
    Convert parsed text into a number.
    :param text: Parsed text, called by :py:meth:`parse.Parser.parse()`.
    :return: Number instance (integer), created from parsed text.
    """
    return float(text)
# -- REGISTER: User-defined type converter (parse_type).
register_type(Ffloat=parse_ffloatt)




@given('Int A = {a:d}, B = {b:d}')
def step_impl(context,a,b):
    print(a,b)
    print("dummy")
    context.num = Numbers(a,b)

@given('Float A = {a:Ffloat}, B = {b:Ffloat}')
def step_impl(context,a,b):
    context.num = Numbers(a,b)

@when('A plus B')
def step_impl(context):
    context.result = context.num.add()
  
@then('result = {r:Ffloat}')
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