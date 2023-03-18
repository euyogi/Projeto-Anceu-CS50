# Set the version of Pmw to use for the tests based on the directory
# name.

import importlib
import os
import string
import Pmw

file = importlib.util.find_spec(__name__).origin
if not os.path.isabs(file):
    file = os.path.join(os.getcwd(), file)
file = os.path.normpath(file)

dir = os.path.dirname(file)
dir = os.path.dirname(dir)
dir = os.path.basename(dir)

version = str.replace(dir[4:], '_', '.')
Pmw.setversion(version)
