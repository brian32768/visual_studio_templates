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

class $safeitemname%(object):


# ===================================================================================
if __name__ == "__main__":

    import config

    MYNAME  = os.path.splitext(os.path.split(__file__)[1])[0]
    LOGFILE = MYNAME + ".log"
    logging.basicConfig(filename=LOGFILE, level=logging.DEBUG, format=config.LOGFORMAT)
    print("Writing log to %s" % LOGFILE)


# That's all!
