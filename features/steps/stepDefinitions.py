from behave import given
from behave import then
from behave import when
from selenium import webdriver
@given(u'open website')
def step_impl(context):
    #raise NotImplementedError(u'STEP: Given open website')
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://www.google.com")


@given(u'enter user id')
def step_impl(context):
    #raise NotImplementedError(u'STEP: Given enter user id')
    print('enter user id')


@given(u'enter password')
def step_impl(context):
    #raise NotImplementedError(u'STEP: Given enter password')
    print('enter password')


@when(u'click on submit button')
def step_impl(context):
    #raise NotImplementedError(u'STEP: When click on submit button')
    print('click on submit button')


@then(u'verify the user dashboard')
def step_impl(context):
    #raise NotImplementedError(u'STEP: Then verify the user dashboard')
    print('verify dashboard')
    assert False