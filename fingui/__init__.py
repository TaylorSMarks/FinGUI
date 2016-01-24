from entry import Entry
from menu  import Menu
from popup import Popup

import sys

def _setupMainloop():
    '''
    This will set up mainloop to run if the following conditions are met:
    1 - fingui was used
    2 - sys.exit() was not called
    3 - No uncaught exceptions were raised
    '''
    from atexit import register

    originalExit                = sys.exit
    originalExcepthook          = sys.excepthook
    _setupMainloop.shouldTkloop = True

    def tkloop():
        if _setupMainloop.shouldTkloop:
            from tk import mainloop
            try:
                mainloop()
            except AttributeError:
                # Happens if fingui was imported but not used at all...
                # Just pass - there's nothing to mainloop on.
                pass

    def newExit(*args, **kwargs):
        _setupMainloop.shouldTkloop = False
        originalExit(*args, **kwargs)

    def newExcepthook(*args, **kwargs):
        _setupMainloop.shouldTkloop = False
        originalExcepthook(*args, **kwargs)

    sys.exit       = newExit
    sys.excepthook = newExcepthook
    register(tkloop)

if sys.argv[0] and not sys.flags.interactive:
    '''
    The above checks ensure Python is not and will not enter interactive mode.
    Interactive mode renders mainloop unnecessary - it exists only to keep
    a "non-interactive" script from exiting while Tk is still running.
    '''
    _setupMainloop()

del sys