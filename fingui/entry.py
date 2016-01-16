import Tkinter

class Entry(Tkinter.Entry):
    def __init__(self, onChange = None, *args, **kwargs):
        Tkinter.Entry.__init__(self, *args, **kwargs)
        self.pack()
        if onChange:
            self.bind('<KeyRelease>', lambda _: onChange())

    def set(self, text):
        self.delete(0, Tkinter.END)
        self.insert(0, text)

class AutocompletePathEntry(Entry):
    def __init__(self, *args, **kwargs):
        Entry.__init__(self, onChange = lambda self = self: self.onChange(), *args, **kwargs)

    def onChange(self):
        print('A change occured in PathAutocompleteEntry')