Feature: Manage Contacts
  As a user
  I want to manage my contacts
  So that I can keep my contact list up to date

  Scenario: Add a new contact
    Given the Contacts app is open
    When I add a new contact with the name "Teste Contato" and phone number "123456789"
    Then the contact list should include a contact with the name "Teste Contato"

  # Scenario: Delete an existing contact
  #   Given the Contacts app is open
  #   And a contact with the name "Teste Contato" exists
  #   When I delete the contact with the name "Teste Contato"
  #   Then the contact list should not include a contact with the name "Teste Contato"