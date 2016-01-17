import Tkinter

class Entry(Tkinter.Entry):
    def __init__(self, *args, **kwargs):
        Tkinter.Entry.__init__(self, *args, **kwargs)
        self.pack()

    def set(self, text):
        self.delete(0, Tkinter.END)
        self.insert(0, text)