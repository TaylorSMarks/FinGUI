import tk
from event import event, eventSource
from popup import Popup

# Someday:
# 1 - Add padding all around.
# 2 - Make mouse movement more reliable on OS X.
#         Best bet might just be to poll winfo_pointerx() and y.
#         It exists on the root window. It might also exist on other objects.

@eventSource
class Menu(object):
    def __init__(self, items, x, y, alwaysHighlight = False, delegate = None, *args, **kwargs):
        # activestyle = tk.None suppresses the box in OS X and underline elsewhere.
        defaults = {'activestyle':      tk.NONE,
                    'borderwidth':      0,
                    'exportselection':  False,
                    # Approximate the colors used in OS X:
                    'selectbackground': '#0950CF',
                    'selectforeground': '#FFF',
                    # Normally tk has a weird fake-3D effect - remove that.
                    'relief':           tk.FLAT}
        self._popup   = Popup(x = x, y = y)
        self._listbox = tk.Listbox(self._popup, *args, **dict(defaults, **kwargs))
        self._listbox.pack()

        self.alwaysHighlight = alwaysHighlight
        self._priorSelection = None
        self.delegate = delegate
        self.items = items

        self._listbox.bind('<<ListboxSelect>>', self._selectionChanged)
        self._listbox.bind('<Return>',          self.selectHighlighted)
        self._listbox.bind('<Button-1>',        self.selectHighlighted)
        self._listbox.bind('<Enter>',           self._snapHighlightToMouse)
        self._listbox.bind('<Motion>',          self._snapHighlightToMouse)
        if not self.alwaysHighlight:
            self._listbox.bind('<Leave>', self.unhighlight)

    @property
    def items(self):
        return self.__items

    @items.setter
    def items(self, items):
        if items == getattr(self, '__items', None):
            return

        self._listbox['height'] = len(items)
        self._listbox['width' ] = max(len(item) for item in items)
        self.__items = items

        self._listbox.delete(0, tk.END)
        for item in items:
            self._listbox.insert(tk.END, str(item))

        if self.alwaysHighlight:
            self._listbox.selection_set(0)
            self._selectionChanged()

    @property
    def columns(self):
        return self._listbox['width']

    @columns.setter
    def columns(self, columns):
        self._listbox['width'] = columns

    def destroy(self):
        self._listbox.destroy()
        self._popup  .destroy()

    def _snapHighlightToMouse(self, event):
        ''' This is a private method. Don't touch it. '''
        self._setHighlight(self._listbox.nearest(event.y))

    def _setHighlight(self, index):
        ''' This is a private method. Don't touch it. '''
        self._listbox.selection_clear(0, tk.END)
        self._listbox.selection_set(index)
        self._selectionChanged()

    def unhighlight(self, *args):
        self._listbox.selection_clear(0, tk.END)

    def _selectionChanged(self, *args):
        ''' This is a private method. Don't touch it. '''
        currentSelection = self.items[self._listbox.curselection()[0]]
        if currentSelection == self._priorSelection:
            return
        self._priorSelection = currentSelection
        self.onHighlight(currentSelection)

    def selectHighlighted(self, *args):
        '''
        Triggers onSelect for the highlighted item.
        '''
        self.onSelect(self.items[self._listbox.curselection()[0]])

    def moveHighlight(self, amount):
        newIndex = self._listbox.curselection()[0] + amount
        newIndex = max(0, min(newIndex, len(self.items) - 1))
        self._setHighlight(newIndex)

    def hide(self):
        self._popup.withdraw()

    def show(self):
        self._popup.deiconify()

    @event
    def onHighlight(self, item):
        pass

    @event
    def onSelect(self, item):
        pass