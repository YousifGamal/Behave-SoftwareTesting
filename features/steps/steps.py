from behave import *
from number import *
from hamcrest import assert_that, equal_to, is_not


@given("A = {a:d} and B = {b:d}")
def step_impl(context, a, b):
    context.num = Numbers(a, b)


@when("A + B")
def step_impl(context):
    context.result = context.num.add()


@when("A / B")
def step_impl(context):
    context.result = context.num.divison()


@then("result is {result:d}")
def step_impl(context, result):
    assert context.result == result


# -----------------------------------------------


def parse_ffloatt(text):

    return float(text)


# -- REGISTER: User-defined type converter (parse_type).
register_type(Ffloat=parse_ffloatt)


@given("Int A = {a:d}, B = {b:d}")
def step_impl(context, a, b):
    print(a, b)
    print("dummy")
    context.num = Numbers(a, b)


@given("Float A = {a:Ffloat}, B = {b:Ffloat}")
def step_impl(context, a, b):
    context.num = Numbers(a, b)


@when("A plus B")
def step_impl(context):
    context.result = context.num.add()


@then("result = {r:Ffloat}")
def step_impl(context, r):
    assert context.result == r


# --------------------------------------------------------


@given('wir haben "behave" installiert')
def step_impl(context):
    context.worked = False


@when("wir einen Test implementieren")
def step_impl(context):
    context.worked = True


@then(u'wird "behave" ihn für uns testen!')
def step_impl(context):
    assert context.worked


## Natural language


@given("the number is ten")
def step_impl(context):
    context.num = Numbers()


@when("the divisor is {divisor}")
def check_divisor(context, divisor):
    context.num.divisor = divisor


@then("we {state} the division")
def complete_or_skip(context, state):
    assert_that(state, equal_to(context.num.divisonDecision()))


## step parameters


@given("I have a list of {numbers}")
def given_list(context, numbers):
    context.num = Numbers()
    context.num.numbers = map(int, numbers.split(","))


@when("I call max on them")
def call_max(context):
    context.num.getMax()


@when("I call min on them")
def call_min(context):
    context.num.getMin()


@then("It should be {result:d}")
def get_result(context, result):
    assert_that(result, equal_to(context.num.result))


## scenerio outline


@given("number {number:d}")
def init_num(context, number):
    context.num = Numbers(number)


@when("I calculate Factorial")
def calculate_factorial(context):
    context.num.factorial()
