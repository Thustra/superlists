__author__ = 'Peter'

from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
    
    def tearDown(self):
        self.browser.quit()
    
    def test_can_start_a_list_and_retrieve_it_as_it_was(self):
        # Person opens the browseer
        # Visit the homepage
        self.browser.get('http://localhost:8000')

        # Title mentions TO-DO lists
        self.assertIn('To-Do',self.browser.title)
        self.fail('Finish the test')

        # Invited to enter a TO-DO item

        # Enter "Buy peacock feathers"

        # When hitting enter the page updates and displays
        # "1: Buy peacock feathers" as an item on the list

        # There is still a text inviting to add another item
        # Enter "Use peacock feathers to make fly"

        # Page updates again and shows an updated TO-DO list

        # Unique URL is generated for this user, with some explanation about it

        # When visiting the URL the list is still there.

        # Stop browsing

if __name__ == '__main__':
    unittest.main(warnings='ignore')