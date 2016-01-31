import tk

class Label(tk.Label):
    def __init__(self, *args, **kwargs):
        initialText = ''
        if args[-1].__class__ == ''.__class__:
            initialText = args[-1]
            args = args[:-1]
        tk.Label.__init__(self, *args, **kwargs)
        self['textvariable'] = self._stringvar = tk.StringVar()
        if initialText:
            self.set(initialText)
        self.pack()

    def set(self, text):
        self._stringvar.set(text)