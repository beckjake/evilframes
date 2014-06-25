evilframes
==========

A Python module for making your own Frame Objects.


Making
======
``python setup.py build`` should do it, assuming you have gcc and all that jazz
set up.

Testing
=======
After building, put evilframes.so in your PYTHONPATH and run ``python test.py``.

If it works it will print "OK!". Otherwise you've got problems.

This testing is lame and doesn't cover nearly everything it should, but hey
whattayawant. I've tested it on OSX 10.9.3 and Ubuntu 14.04 with Python 3.4.

Using
=====
Seriously, never use this for anything you care about. I intentionally
removed the documentation to make it difficult. DO NOT USE THIS.

Now that that's out of the way, if you must use it, there is one public
function in the module, "frame".

It takes 4 positional-only arguments:
    - A frame object, or None if you want it to be the top of the stack
    - A code object (you can pull this out of any function's __code__)
    - A dict object (the globals).
    - A dict object (the locals).

Type safety is enforced for the last 3 arguments. I have no idea what happens
if you pass something weird for the first - probably nothing good.
