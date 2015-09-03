from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest

from lists.views import home_page


class HomePageTest(TestCase):

  def test_root_url_resolves_to_home_page_view(self):
    found = resolve('/')
    self.assertEqual(found.func, home_page)

  def test_home_page_returns_correct_html(self):
    request = HttpRequest()
    response = home_page(request)

    # Starts with DOCTYPE tag
    self.assertTrue(response.content.startswith(b'<!DOCTYPE html>'))
    
    # Has head and body tag
    self.assertIn(b'<head>', response.content)
    self.assertIn(b'<body>', response.content)

    # Shows correct title
    self.assertIn(b'<title>Bobby Priambodo</title>', response.content)

    # Shows correct site header
    self.assertIn(b'<h1>Bobby Priambodo\'s Profile</h1>', response.content)

    # Mentions Bobby's real name
    self.assertIn(b'Widyanto Bagus Priambodo', response.content)

    # Ends with html close tag
    self.assertTrue(response.content.endswith(b'</html>'))
