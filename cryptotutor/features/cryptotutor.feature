#see https://behave.readthedocs.io/en/stable/tutorial.html

Feature: cryptotutor tests

#Sub-Feature: checking links
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



#Sub-Feature: form submissions

Scenario: submit a question
    Given I go to the cryptotutor home page
    Given I am logged in
    When I click on the question submission link
    When I enter information into the question submission form
    Then I will go to the home page sorted by newest
    Then I will see my question on the home page

Scenario: answer a question
    Given I go to the cryptotutor home page
    Given I am logged in
    When I click on a question and type in an answer
    Then I will see my answer

#note that this code was written when the test files consisted of files using System.out.println; may need to be changed to successfully
#get a clone from NiCad when the comparison files are more robust
Scenario: compare code
    Given I go to the cryptotutor home page
    When I click on the compare code link
    When I enter information into the code submission form
    When I go to the code selection page and select code
    Then I will go to the diff viewer and see my code

Scenario: submit code that will give no clones
    Given I go to the cryptotutor home page
    When I click on the compare code link
    When I enter not enough information into the code submission form
    Then I should get an AttributeError error