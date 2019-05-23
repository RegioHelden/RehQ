import sublime
import sublime_plugin
import os

from .utilities import log, commands

BASE_DIR = os.path.dirname(__file__)


def plugin_loaded():
    log.info('Snippets are ready to use.')
   

class RehqFontBoldCommand(commands.FontFormattingCommand):
    FORMATTING_CHARACTER = "*"
        

class RehqFontItalicCommand(commands.FontFormattingCommand):
    FORMATTING_CHARACTER = "_"


class RehqFontUnderlineCommand(commands.FontFormattingCommand):
    FORMATTING_CHARACTER = "+"


class RehqFontStrikeThroughCommand(commands.FontFormattingCommand):
    FORMATTING_CHARACTER = "-"


class RehqFontSuperscriptCommand(commands.FontFormattingCommand):
    FORMATTING_CHARACTER = "^"


class RehqFontSubscriptCommand(commands.FontFormattingCommand):
    FORMATTING_CHARACTER = "~"


class RehqFontMonospaceCommand(commands.FontFormattingCommand):
    FORMATTING_CHARACTER = "@"


class RehqListSnippetsCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        scope = self.view.scope_name(self.view.sel()[-1].b)
        
        with open(os.path.join(BASE_DIR, 'snippet_list.html'), encoding='utf8') as f:
            html = f.read().strip()

        self.view.show_popup(html, max_width=512)