#see https://behave.readthedocs.io/en/stable/tutorial.html

# Feature: showing off behave

# Scenario: run a simple test
#     Given we have behave installed
#     When we implement a test
#     Then behave will test it for us!


Feature: checking links from home

#failing, need to look into errors why
Scenario: reload the home page
    Given I go to the cryptotutor home page
    When I click on the home link
    Then I will go to the home page