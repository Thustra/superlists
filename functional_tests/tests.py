__author__ = 'Peter'

from django.test import LiveServerTestCase

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
    
    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Person opens the browseer
        # Visit the homepage
        self.browser.get(self.live_server_url)

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

        person_list_url = self.browser.current_url
        self.assertRegex(person_list_url, '/lists/.+')

        self.check_for_row_in_list_table('1: Buy peacock feathers')

        # There is still a text inviting to add another item
        # Enter "Use peacock feathers to make fly"

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make fly')

        # Page updates again and shows an updated TO-DO list

        inputbox.send_keys(Keys.ENTER)

        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feathers to make fly')

        # A new user francis comes along and wants to make his own list
        ## use a new browser session for this
        ## double hashes indicate comments about how the test works

        self.browser.quit()
        self.browser = webdriver.Firefox()

        # Francis visits the page and there is no sign of the previous persons list

        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('Use peacock feathers to make fly', page_text)

        # Francis adds an item to his list

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)

        # Francis gets his own url and his lists shows

        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url,'/lists/.+')
        self.assertNotEqual(francis_list_url,person_list_url)

        # No sign of the list made by the previous user

        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)


        self.fail('Finish the test!!')

        # When visiting the URL the list is still there.

        # Stop browsing