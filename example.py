from fingui import Entry, Menu
from glob   import glob

class AutocompletePathEntry(Entry):
    menu = None

    def showSuggestions(self, newValue):
        suggestions = glob(newValue + '*')
        if not newValue or newValue[-1] != '/':
            suggestions += glob(newValue + '/*')
        if newValue in suggestions:
            suggestions.remove(newValue)

        if not suggestions:
            if self.menu:
                self.menu.hide()
            return

        if not self.menu:
            self.menu = Menu(suggestions, self.x, self.y + self.height, alwaysHighlight = True, delegate = self)
        else:
            self.menu.items = suggestions
        self.menu.show()
        self.menu.columns = self.columns = max(20, self.menu.columns, len(self.get()))

    def onChange(self, oldValue, newValue):
        self.showSuggestions(newValue)

    def onSelect(self, item):
        self.set(item)

    def onReturn(self):
        if self.menu:
            self.menu.selectHighlighted()

    def onDown(self):
        if self.menu:
            self.menu.moveHighlight(1)

    def onUp(self):
        if self.menu:
            self.menu.moveHighlight(-1)

    def onFocus(self):
        self.showSuggestions(self.get())

    def onFocusLost(self):
        self.menu.hide()

AutocompletePathEntry()