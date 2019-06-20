import xml.etree.ElementTree as ET

from RehQ.utilities import log

class SublimeSnippet(object):

    def __init__(self, snippet_path):
        self.snippet_path = snippet_path
        tree = ET.parse(self.snippet_path)
        self._root = tree.getroot()

    @property
    def title(self):
        return self._root.find('title').text

    @property
    def hint(self):
        return self._root.find('hint').text

    @property
    def trigger(self):
        return self._root.find('tabTrigger').text
    
    def is_valid(self):
        expected_elements = ['title', 'hint', 'tabTrigger', 'scope', 'description']
        for element_name in expected_elements:
            if self._root.find(element_name) is None:
                return False 
        return True

    def check_for_missing_elements(self):
        expected_elements = ['title', 'hint', 'tabTrigger', 'scope', 'description']
        for element_name in expected_elements:
            if self._root.find(element_name) is None:
                log.error("{} misses {} element.".format(self.snippet_path, element_name))

    def to_dict(self):
        if self.is_valid():
            return {
                "title": self.title,
                "hint": self.hint,
                "trigger": self.trigger,
            }
        return {}