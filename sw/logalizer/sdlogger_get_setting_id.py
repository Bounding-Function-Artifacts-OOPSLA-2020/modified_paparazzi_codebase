#!/usr/bin/env python
<<<<<<< HEAD

from __future__ import print_function
=======
>>>>>>> 5926b573a907e168704d2426ee3d50a02e32d1b3
import sys
from os import path, getenv

# if PAPARAZZI_SRC not set, then assume the tree containing this
# file is a reasonable substitute
PPRZ_SRC = getenv("PAPARAZZI_SRC", path.normpath(path.join(path.dirname(path.abspath(__file__)), '../../')))
sys.path.append(PPRZ_SRC + "/sw/lib/python")
from settings_xml_parse import PaparazziACSettings

if __name__ == '__main__':
    ac_id = int(sys.argv[1])
    command_name = sys.argv[2]
    settings = PaparazziACSettings(ac_id)
<<<<<<< HEAD
    print(settings.name_lookup[command_name].index)
=======
    print settings.name_lookup[command_name].index
>>>>>>> 5926b573a907e168704d2426ee3d50a02e32d1b3
