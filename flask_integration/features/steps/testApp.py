from behave import given,when,then

@given('we have assinged name variable with muhammad')
def step_impl(context):
    pass

@when('we run the hello endpoint')
def step_impl(context):
    context.browser.get("http://localhost:7777/helloname/muhammad")

@then('it will return hello muhammad')
def step_impl(context):
    assert context.browser.current_url == 'http://localhost:7777/helloname/muhammad'
    assert 'hello muhammad' in context.browser.page_source

@given('we have assinged name variable with 9.0')
def step_impl(context):
    pass

@when('we run the sqrt endpoint')
def step_impl(context):
    context.browser.get("http://localhost:7777/sqrt/9.0")

@then('it will return 3.0')
def step_impl(context):
    assert context.browser.current_url == 'http://localhost:7777/sqrt/9.0'
    assert 'square root of the number = 3.0' in context.browser.page_source