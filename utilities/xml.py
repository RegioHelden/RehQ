import xml.etree.ElementTree as ET


class SublimeSnippet(object):

    def __init__(self, snippet_path):
        tree = ET.parse(snippet_path)
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
        expected_elements = ['title', 'hint', 'tabTrigger']
        for element_name in expected_elements:
            if self._root.find(element_name) is None:
                return False 
        return True

    def to_dict(self):
        if self.is_valid():
            return {
                "title": self.title,
                "hint": self.hint,
                "trigger": self.trigger,
            }
        return {}