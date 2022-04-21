from behave import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

driver = webdriver.Firefox(executable_path=r'/usr/local/bin/geckodriver') #geckodriver MUST be inside the /usr/local/bin folder

def setUp(context):
    context.driver = driver

@given('I go to the cryptotutor home page')
def step_impl(context):
    driver.get('http://localhost:8000/cryptotutor')

@when('I click on the home link')
def step_impl(context):
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/aside/div[2]/nav/a[1]")))
    driver.find_element_by_xpath("/html/body/div[1]/aside/div[2]/nav/a[1]").click()

@then('I will go to the home page')
def step_impl(context):
    assert driver.current_url == "http://localhost:8000/cryptotutor/"

@when('I click on the question submission link')
def step_impl(context):
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/aside/div[2]/nav/a[2]")))
    driver.find_element_by_xpath("/html/body/div[1]/aside/div[2]/nav/a[2]").click()

@then('I will go to the question submission page')
def step_impl(context):
    assert driver.current_url == "http://localhost:8000/cryptotutor/question-form/"

@when('I click on the compare code link')
def step_impl(context):
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/aside/div[2]/nav/a[3]")))
    driver.find_element_by_xpath("/html/body/div[1]/aside/div[2]/nav/a[3]").click()

@then('I will go to the code comparison form')
def step_impl(context):
    assert driver.current_url == "http://localhost:8000/cryptotutor/code-form/"

@when('I click on the GitHub link')
def step_impl(context):
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/aside/div[2]/nav/a[4]")))
    driver.find_element_by_xpath("/html/body/div[1]/aside/div[2]/nav/a[4]").click()

@then('I will go to the GitHub')
def step_impl(context):
    assert driver.current_url == "https://github.com/davidlentsch/bit-by-bit-capstone"

# def tearDown(context):
    driver.close()