import sublime
import unittest


class SublimeCommandTestCase(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		cls.window = sublime.active_window()
		cls.active_view = cls.window.active_view()
