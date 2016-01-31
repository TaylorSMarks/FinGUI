import tk

class ProgressBar(tk.ttk.Progressbar):
    '''
    Set maximum to 0 to use an indeterminate style.
    Use the step method to increment the filled portion of the ProgressBar.
    '''
    def __init__(self, maximum = 100.0, length = 100.0, *args, **kwargs):
        if maximum:
            tk.ttk.Progressbar.__init__(self, length = length, mode = 'determinate', maximum = maximum, *args, **kwargs)
        else:
            tk.ttk.Progressbar.__init__(self, length = length, mode = 'indeterminate', *args, **kwargs)
            self.step(1)  # Otherwise it doesn't animate properly on OS X.
        self.pack()