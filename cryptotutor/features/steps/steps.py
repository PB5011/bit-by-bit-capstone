from behave import *
from selenium import webdriver

driver = webdriver.Firefox(executable_path=r'/usr/local/bin/geckodriver') #geckodriver MUST be inside the /usr/local/bin folder

#Feature: showing off behave
@given('we have behave installed')
def step_impl(context):
    pass

@when('we implement a test')
def step_impl(context):
    assert True is not False

@then('behave will test it for us!')
def step_impl(context):
    assert context.failed is False


#Feature: checking links from home
@given('I go to the cryptotutor home page')
def step_impl(context):
    driver.get('http://localhost:8000/cryptotutor')

@when('I click on the home link')
def step_impl(context):
    driver.find_elements_by_css_selector('mdc-deprecated-list-item')

@then('I will go to the home page')
def step_impl(context):
    assert driver.current_url == "http://localhost:8000/cryptotutor"

driver.close()