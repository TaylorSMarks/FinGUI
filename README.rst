FinGUI
======
*A Pythonic Wrapper for Tkinter*

I've always had a love/hate relationship with Tkinter. On the one hand, it
almost always comes with Python, which makes it the easiest option for making a
GUI in Python. On the other hand, it's one of the least Pythonic modules in
existance.

So I've decided to write and share this - FinGUI. It's a GUI package for Python
written in pure Python, meaning it's trivial to install, unlike pretty much
every other GUI package for Python.

Installation
------------
Install via pip:

.. code-block:: bash

    $ pip install fingui

Done.

If you insist on the (slightly) harder way of installing, from source,
you know how to do it already and don't need my help.

The most up-to-date version of this library can be found on github at
https://github.com/TaylorSMarks/FinGUI

Quick Start
-----------
Once you've installed, you can really quickly verified that it works with just this:

.. code-block:: python

    >>> from fingui import Entry
    >>> e = Entry()
    >>> e.set('Hello World!')
    
That'll work right from your command line.
You can also drop the same code into a script and run it with no modification.

Note the boilerpoint we didn't deal with, because it's all automatically handled:
 * We didn't call ``mainloop()``.
 * We didn't need to create a root object (although we could have).
 * We didn't need to call ``pack()``.

Also note that ``Entry`` has a ``set()`` method! Unlike the variant in ``Tkinter``, ours has the methods you would expect.

Documentation
-------------
I've tried to include docstrings with all the functions and classes, so things like this should work:

.. code-block:: python

    >>> import fingui
    >>> help(fingui)
    
If this project grows large enough, I'll try to create some more formal documentation for it.

Requirements
------------
FinGUI has been tested on Python 2.7 on OS X 10.11 and Windows 7.
It is intended to work on both Python 2.6+ and 3.2+, with any OS that supports Tkinter.
It probably falls short on Python 3; I wouldn't know because of how rarely I touch it.
Please submit pull requests to fix anything that doesn't work on Python 3.

Copyright
---------
This software is Copyright (c) 2016 Taylor Marks <taylor@marksfam.com>.

See the bundled LICENSE file for more information.
