from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

  def setUp(self):
    self.browser = webdriver.Firefox()
    self.browser.implicitly_wait(3)

  def tearDown(self):
    self.browser.quit()

  def test_can_see_profile_page(self):
    # User visits our site
    self.browser.get('http://localhost:8000')

    # User notices the page title and header mention Bobby Priambodo
    self.assertIn('Bobby Priambodo', self.browser.title)

if __name__ == '__main__':
  unittest.main(warnings='ignore')
