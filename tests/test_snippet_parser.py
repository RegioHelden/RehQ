import os
import unittest

from RehQ.utilities.testing import SublimeCommandTestCase
from RehQ.utilities.xml import SublimeSnippet
from RehQ.rehq import RehqListSnippetsCommand, BASE_DIR


class SublimeSnippetObjectTest(unittest.TestCase):

	def setUp(self):
		snippet_file = os.path.join(BASE_DIR, 'tests', 'valid_snippets', 'general.sublime-snippet.test')
		self.snippet = SublimeSnippet(snippet_file)

	def invalidate_snippet_by_removing(self, element_name):
		element = self.snippet._root.find(element_name)
		self.snippet._root.remove(element)
		self.assertFalse(self.snippet.is_valid())

	def test_snippet_without_title_is_invalid(self):
		self.invalidate_snippet_by_removing('title')

	def test_snippet_without_hint_is_invalid(self):
		self.invalidate_snippet_by_removing('hint')

	def test_snippet_without_trigger_is_invalid(self):
		self.invalidate_snippet_by_removing('tabTrigger')

	def test_snippet_with_hint_title_and_trigger_is_valid(self):
		self.assertTrue(self.snippet.is_valid())

	def test_valid_sublime_snippet_is_parsed_to_object(self):
		self.assertEqual(self.snippet.title, "The Title")
		self.assertEqual(self.snippet.hint, "A message shown to the user.")
		self.assertEqual(self.snippet.trigger, "tst")

	def test_sublime_snippet_is_transformed_to_dict(self):
		expected_data = {
			"title": "The Title",
			"hint": "A message shown to the user.",
			"trigger": "tst",
		}
		self.assertDictEqual(self.snippet.to_dict(), expected_data)