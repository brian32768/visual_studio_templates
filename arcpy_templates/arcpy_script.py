"""
@date:   $time$
@author: $username$
"""
from __future__ import print_function
import os
import sys
import logging
import arcpy
from arcpy import mapping as MAP
from collections import namedtuple # Useful for reading feature classes

__version__ = "" # Set this to whatever you want or just delete it.

class $safeitemname$(object):
    def __init__(self):
        return

# ===================================================================================
if __name__ == "__main__":

    import config

    MYNAME  = os.path.splitext(os.path.split(__file__)[1])[0]
    LOGFILE = MYNAME + ".log"
    logging.basicConfig(filename=LOGFILE, level=logging.DEBUG, format=config.LOGFORMAT)
    print("Writing log to %s" % LOGFILE)

    # You can put unit test code here
    # or you can set up this code to run standalone from command line

    s = $safeitemname$()

# That's all!
