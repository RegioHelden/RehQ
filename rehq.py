import sublime
import sublime_plugin
import os

from jinja2 import Template

from .utilities import log, commands, snippets
from .settings import BASE_DIR, SNIPPET_DIR


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
        sublime_snippets = self._parse_snippets(SNIPPET_DIR)

        with open(os.path.join(BASE_DIR, 'snippet_list.html'), encoding='utf8') as f:
            template = Template(f.read().strip())
        html = template.render(snippets=[x.to_dict() for x in sublime_snippets])
        self.view.show_popup(html, max_width=512, max_height=400)

    def _parse_snippets(self, snippet_dir):
        snippet_list = []
        for filename in os.listdir(snippet_dir):
            if filename.endswith(".sublime-snippet") or filename.endswith(".sublime-snippet.test"):
                snippet = snippets.SublimeSnippet(os.path.join(snippet_dir, filename))
                if snippet.is_valid():
                    snippet_list.append(snippet)
        return snippet_list

class RehqTestSnippetsCommand(sublime_plugin.ApplicationCommand):
    def run(self):
        log.info("Testing snippets in {}...".format(SNIPPET_DIR))
        for filename in os.listdir(SNIPPET_DIR):
            if filename.endswith(".sublime-snippet"):
                snippet = snippets.SublimeSnippet(os.path.join(SNIPPET_DIR, filename))
                snippet.check_for_missing_elements()
        log.info("... done testing snippets.")
