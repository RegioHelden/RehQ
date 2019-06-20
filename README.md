# RehQ
A Sublime Text 3 plugin for writing Epics and User Stories (in textile markup)

## Installation

You may install the plugin as any other plugin through package control.

If you don't know, what package control is or don't even have Sublime Text installed yet, follow these setps:

1. Download and install the [Sublime Text Editor](https://www.sublimetext.com/)
2. Open Sublime Text and install package control (click _tools_ > _Install Package Control_)
3. Open the Sublime Text Command Palette (_tools_ > _Command Palette..._)
4. Type "Install Package" and hit enter (_Package Control: Install Package_)
5. Wait for the plugins to load, search for "RehQ" and hit enter again

The plugin will now be installed.

## Snippets

The package provides you with some snippets to support the process of writing epics, features and user stories (in textile markup language).

Display the list of available snippets via the context menu (right click in your editor and click _RehQ_ > _Show available snippets_).

To use a snippet, open a textile document, type the trigger and hit tab.
With longer snippets, you may navigate through predefined cursor positions by hitting tab repeatedly. If there is no further cursor position available, hitting tab will position your cursor at the end of the snippet.

### Adding snippets

If you want your own snippets to be listed in the available snippets list, make sure to add them to the SNIPPET_DIR (as configured in the `settings.py`). Also, to be recognized as valid snippets, they need to have the following attributes: `'title', 'hint', 'tabTrigger', 'scope', 'description'`

A check can be run from the context menu, to test if your custom snippets are well-formed (right click > _RehQ_ > _Development_).

Once the well-form snippets exist in the `SNIPPET_DIR`, they will be listed in the _Show available snippets_ window. Currently, the snippets are shown in no particular order.

## Font formatting

For easier formatting, several formatting functions can be used. Right click in your editor and open the _RehQ_ menu to see the available format options. When you click one of the options, the highlighted text will be wrapped with the appropriate formatting characters.

Also, the commonly used shortcuts were added to quickly format text:

Format | Keys
--- | ---
bold | <kbd>Super</kbd> + <kbd>b</kbd>
italic | <kbd>Super</kbd> + <kbd>i</kbd>
underline | <kbd>Super</kbd> + <kbd>u</kbd>

Note: The quick formatting only works in .textile documents!
