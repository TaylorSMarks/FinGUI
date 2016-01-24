import tk
from event import event, eventSource

@eventSource
class Entry(object):
    '''
    A widget for text entry.
    Has get and set methods that do what you expect.
    Subclasses can implement onChange to easily monitor the content.
    '''
    def __init__(self, *args, **kwargs):
        self._entry = tk.Entry(*args, **kwargs)
        self._priorValue = ''
        self._stringvarChangedSuppressed = False
        self._stringvar = tk.StringVar()
        self._entry['textvariable'] = self._stringvar
        self._stringvar.trace('w', self._stringvarChanged)
        self._entry.pack()

        self._entry.bind('<Return>'  , lambda event: self.onReturn   ())
        self._entry.bind('<Up>'      , lambda event: self.onUp       ())
        self._entry.bind('<Down>'    , lambda event: self.onDown     ())
        self._entry.bind('<FocusIn>' , lambda event: self.onFocus    ())
        self._entry.bind('<FocusOut>', lambda event: self.onFocusLost())

    @property
    def x(self):
        return self._entry.winfo_rootx()

    @property
    def y(self):
        return self._entry.winfo_rooty()

    @property
    def height(self):
        return self._entry.winfo_height()

    @property
    def columns(self):
        return self._entry['width']

    @columns.setter
    def columns(self, columns):
        self._entry['width'] = columns

    # Symbols triggered by buttons that normally don't type anything,
    # but for some reason do type something, at least on OS X.
    blacklist = set((63232, 63233)) # Up and Down arrow keys.

    def _stringvarChanged(self, *args):
        '''
        This is a private method. Don't touch it.
        '''
        if self._stringvarChangedSuppressed:
            self._stringvarChangedSuppressed = False
            return

        newValue = self.get()
        filtered = ''
        hadToFilter = False
        for char in self.get():
            if ord(char) in Entry.blacklist:
                hadToFilter = True
            else:
                filtered += char

        if hadToFilter:
            self.set(filtered)
            return

        if self._priorValue == newValue:
            return

        self.onChange(self._priorValue, newValue)
        self._priorValue = newValue

    def get(self):
        return self._entry.get()

    def set(self, text):
        '''
        Replaces the content of the Entry and triggers onChange.
        '''
        self._stringvarChangedSuppressed = True
        self._stringvar.set(text)
        self._entry.update()
        self._stringvarChanged()
        self._entry.icursor(tk.END) 

    def suggest(self, text):
        '''
        Insert and select text at the cursor.
        The user stops typing if they like it, thus it stays.
        The user continues typing, thus it is overwritten, if they don't like it.
        '''
        startingInsert = self._entry.index(tk.INSERT)
        self._entry.insert(tk.INSERT, text)
        self._entry.select_range(startingInsert, tk.END)

    @event
    def onChange(self, oldValue, newValue):
        '''
        onChange gets called with oldValue and newValue whenever the contents change.
        '''
        pass

    @event
    def onReturn(self):
        pass

    @event
    def onUp(self):
        pass

    @event
    def onDown(self):
        pass

    @event
    def onFocus(self):
        pass

    @event
    def onFocusLost(self):
        pass