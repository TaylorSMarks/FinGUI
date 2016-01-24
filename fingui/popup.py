import tk

class Popup(tk.Toplevel):
    '''
    A class for frameless floating popup windows. For example:
    from fingui import Entry, Popup
    p = Popup(Entry, 500, 500)
    p.content.set('Hello World!')
    '''
    def __init__(self, contentClass = None, x = None, y = None, *args, **kwargs):
        '''
        Pass in a class to have initialized with the Popup as its parent.
        *args and **kwargs are passed directly to the contentClass's __init__.
        x and y, if provided, are used to set the initial position of the Popup.
        '''
        tk.Toplevel.__init__(self)
        self.overrideredirect(True)

        if contentClass:
            self.content = contentClass(self, *args, **kwargs)

        if x and y:
            self.setPosition(x, y)

    def setPosition(self, x, y):
        ''' Sets the X and Y coordinates of the Popup. '''
        self.geometry('+{}+{}'.format(x, y))