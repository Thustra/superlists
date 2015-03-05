__author__ = 'Peter'

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
    
    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_as_it_was(self):
        # Person opens the browseer
        # Visit the homepage
        self.browser.get('http://localhost:8000')

        # Title and header mention TO-DO lists
        self.assertIn('To-Do',self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do',header_text)

        # Invited to enter a TO-DO item

        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # Enter "Buy peacock feathers"

        inputbox.send_keys('Buy peacock feathers')

        # When hitting enter the page updates and displays
        # "1: Buy peacock feathers" as an item on the list
        inputbox.send_keys(Keys.ENTER)

        self.check_for_row_in_list_table('1: Buy peacock feathers')

        # There is still a text inviting to add another item
        # Enter "Use peacock feathers to make fly"

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make fly')

        # Page updates again and shows an updated TO-DO list

        inputbox.send_keys(Keys.ENTER)

        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feathers to make fly')

        # Unique URL is generated for this user, with some explanation about it

        self.fail('Finish the test!!')

        # When visiting the URL the list is still there.

        # Stop browsing

if __name__ == '__main__':
    unittest.main(warnings='ignore')