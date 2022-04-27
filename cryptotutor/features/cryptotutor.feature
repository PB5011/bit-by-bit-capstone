#see https://behave.readthedocs.io/en/stable/tutorial.html

Feature: checking links from home

Scenario: reload the home page
    Given I go to the cryptotutor home page
    When I click on the home link
    Then I will go to the home page

Scenario: load the question form
    Given I go to the cryptotutor home page
    When I click on the question submission link
    Then I will go to the question submission page

Scenario: load the code comparison form
    Given I go to the cryptotutor home page
    When I click on the compare code link
    Then I will go to the code comparison form

Scenario: load the github
    Given I go to the cryptotutor home page
    When I click on the GitHub link
    Then I will go to the GitHub



# Feature: form submissions
#multiple features in one file not supported; either split into multiple or leave as is
#not sure if the scenarios below make sense/are compatible w the steps, but they should cover the general idea... open for change as necessary
# Scenario: submit a question
#     Given I go to the cryptotutor home page
#     When I click on the question submission link
#     When I enter information into the form
#     When I press submit
#     Then I will go to the home page
#     Then I will see my question on the home page

# Scenario: compare code
#     Given I go to the cryptotutor home page
#     When I click on the compare code link
#     When I enter information into the form
#     Then I will go to the code selection page
#     Then I will see my code there
#     When I select code
#     When I press submit
#     Then I will go to the diff viewer
#     Then I will see the diff view
#     Then I will see my code