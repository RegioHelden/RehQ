import sublime_plugin


class FontFormattingCommand(sublime_plugin.TextCommand):
    """
    Wraps / unwraps the selected string with a given character.
    """
    FORMATTING_CHARACTER = ""

    def run(self, edit):
        for region in self.view.sel():
            selection = self.view.substr(region)
            formatted_text = self._format_text(selection)
            self.view.replace(edit, region, formatted_text)

    def _format_text(self, text):
        text_is_formatted = text.startswith(self.FORMATTING_CHARACTER) and text.endswith(self.FORMATTING_CHARACTER)
        if text_is_formatted:
            # trim first and last character, as the string is already formatted
            return text[1:-1]
        return "{formatting_char}{text}{formatting_char}".format(text=text, formatting_char=self.FORMATTING_CHARACTER)
        
