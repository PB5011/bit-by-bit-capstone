# CryptoTutor - A question and answer forum with code comparison capabilities.
# Copyright (C) 2022 Zoe Larson, Maya Lentsch, Tyler Bauer, Daniel Brinkman

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from telnetlib import AUTHENTICATION
from django.test.client import Client
from behave import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import django
django.setup()


driver = webdriver.Firefox(executable_path=r'/usr/local/bin/geckodriver') #geckodriver MUST be inside the /usr/local/bin folder

#note that all links being checked are hosted locally; may need to change URLs

#checking links
@given('I go to the cryptotutor home page')
def step_impl(context):
    """Navigates to the locally hosted cryptotutor main page."""
    driver.get('http://localhost:8000/cryptotutor')

@when('I click on the home link')
def step_impl(context):
    """Waits until a question link is clickable to ensure the page is loaded, then clicks on the link to the home page."""
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "/html/body/main/div[2]/div/div[3]/div[1]/div/div[1]/div[2]/div/a/h4")))
    driver.find_element_by_xpath("/html/body/main/div[1]/ul[1]/li[1]/a").click()

@then('I will go to the home page')
def step_impl(context):
    """Asserts that the current URL is the home page."""
    assert driver.current_url == "http://localhost:8000/cryptotutor/"

@when('I click on the question submission link')
def step_impl(context):
    """Waits until a button is clickable to ensure the page is loaded, then clicks on the question submission link."""
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "/html/body/main/div[1]/ul[1]/li[2]/a")))
    driver.find_element_by_xpath("/html/body/main/div[1]/ul[1]/li[2]/a").click()

@then('I will go to the question submission page')
def step_impl(context):
    """Asserts that the current URL is the question form."""
    assert driver.current_url == "http://localhost:8000/cryptotutor/question-form/"

@when('I click on the compare code link')
def step_impl(context):
    """Waits until a button is clickable to ensure the page is loaded, then clicks on the compare code link."""
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "/html/body/main/div[1]/ul[1]/li[3]/a")))
    driver.find_element_by_xpath("/html/body/main/div[1]/ul[1]/li[3]/a").click()

@then('I will go to the code comparison form')
def step_impl(context):
    """Asserts that the current URL is the code comparison form."""
    assert driver.current_url == "http://localhost:8000/cryptotutor/code-form/"

@when('I click on the GitHub link')
def step_impl(context):
    """Waits until a button is clickable to ensure the page is loaded, then clicks on the GitHub link."""
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "/html/body/main/div[1]/ul[1]/li[4]/a")))
    driver.find_element_by_xpath("/html/body/main/div[1]/ul[1]/li[4]/a").click()

@then('I will go to the GitHub')
def step_impl(context):
    """Asserts that the current URL is the GitHub repository."""
    assert driver.current_url == "https://github.com/davidlentsch/bit-by-bit-capstone"

@given('I am logged in')
def step_impl(context):
    """Logs the user in using cookies under the username capstone."""
    client = Client()
    client.login(username='capstone', password='capstone')
    cookie = client.cookies['sessionid']

    # Selenium will set cookie domain based on current page domain.
    driver.get('http://localhost:8000/cryptotutor/')
    driver.add_cookie({
        'name': 'sessionid',
        'value': cookie.value,
        'secure': False,
        'path': '/',
    })

@when('I enter information into the question submission form')
def step_impl(context):
    """Enters information into the question submission form under the username capstone."""
    title = driver.find_element_by_id("title")
    vcs = driver.find_element_by_id("vcs")
    title.send_keys("Selenium Test")
    vcs.send_keys("https://github.com/davidlentsch/bit-by-bit-capstone")
    driver.switch_to.frame("description_ifr")
    element = driver.find_element_by_id("tinymce")
    element.send_keys("This is a test question made by Selenium and Behave!")
    driver.switch_to.default_content()
    driver.find_element_by_xpath("/html/body/main/div[2]/div/div[2]/form/input[2]").send_keys(Keys.RETURN)

@then('I will go to the home page sorted by newest')
def step_impl(context):
    """Waits for a question link to be clickable to ensure the page is loaded, then asserts that the URL is the home page sorted by newest."""
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "/html/body/main/div[2]/div/div[3]/div[1]/div/div[1]/div[2]/div/a/h4")))
    print(driver.current_url)
    assert driver.current_url == "http://localhost:8000/cryptotutor/newest"

@then('I will see my question on the home page')
def step_impl(context):
    """Checks the top question to ensure it is what was submitted by the test case."""
    assert driver.find_element_by_xpath("/html/body/main/div[2]/div/div[3]/div[1]/div/div[1]/div[2]/div/a/h4").text == "Selenium Test"
    assert driver.find_element_by_xpath("/html/body/main/div[2]/div/div[3]/div[1]/div/div[1]/div[2]/div/p[2]").text == "This is a test question made by Selenium and Behave!"

@when('I click on a question and type in an answer')
def step_impl(context):
    """Navigates to the first question on the forum page and adds an answer."""
    driver.find_element_by_xpath("/html/body/main/div[2]/div/div[3]/div[1]/div/div/div[2]/div/a/h4").click()
    driver.switch_to.frame("solution_ifr")
    element = driver.find_element_by_id("tinymce")
    element.send_keys("This is a test answer made by Selenium and Behave!")
    driver.switch_to.default_content()
    driver.find_element_by_xpath("/html/body/main/div[2]/div/div/div[3]/form/input[2]").send_keys(Keys.RETURN)

@then('I will see my answer')
def step_impl(context):
    """Waits until the answer is visible, then asserts that the body of the answer is what was input."""
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '/html/body/main/div[2]/div/div[1]/div[3]/div/div/p[2]')))
    assert driver.find_element_by_xpath("/html/body/main/div[2]/div/div[1]/div[3]/div/div/p[2]").text == "This is a test answer made by Selenium and Behave!"

#may need to be changed depending on the files being compared to
@when('I enter information into the code submission form')
def step_impl(context):
    """Enters information into the code submission form under the username capstone."""
    for i in range(10):
        driver.find_element_by_id("code").send_keys("System.out.println(\"Testing!\");")
        driver.find_element_by_id("code").send_keys(Keys.RETURN)
    dropdown = Select(driver.find_element_by_id("threshold"))
    dropdown.select_by_value("80")
    driver.find_element_by_xpath("/html/body/main/div[2]/div/div[2]/form/button").send_keys(Keys.RETURN)

@when('I go to the code selection page and select code')
def step_impl(context):
    """Waits until a radio button is clickable to ensure the page is loaded, then clicks a radio button and submits the selection."""
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "/html/body/main/div[2]/div/div[2]/form/div[1]/div/div[2]/input")))
    driver.find_element_by_xpath("/html/body/main/div[2]/div/div[2]/form/div[2]/div/div[2]/input").click()
    driver.find_element_by_xpath("/html/body/main/div[2]/div/div[2]/form/input[2]").send_keys(Keys.RETURN)

#may need to be changed depending on the files being compared to
@then('I will go to the diff viewer and see my code')
def step_impl(context):
    """Waits until a button on the diff viewer page is loaded in, then asserts that the URL is correct and that the table contains the submitted test code."""
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "/html/body/main/div[2]/div/div[2]/a/button")))
    assert driver.current_url == "http://localhost:8000/cryptotutor/diff-viewer/"
    #TODO: assert text inside table matches text submitted in form

@when('I enter not enough information into the code submission form')
def step_impl(context):
    """Enters in information that will result in no clones found in NiCad."""
    driver.find_element_by_id("code").send_keys("test")
    driver.find_element_by_xpath("/html/body/main/div[2]/div/div[2]/form/button").send_keys(Keys.RETURN)

@then('I should get an AttributeError error')
def step_impl(context):
    """Asserts that finding no clones gets an AttributeError."""
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "/html/body/main/div[2]/div/div[2]/a/button")))
    assert driver.current_url == "http://localhost:8000/cryptotutor/code-selection/"
    assert "Type: AttributeError" in driver.find_element_by_xpath("/html/body/main/div[2]/div/div[2]/p[5]").text
    