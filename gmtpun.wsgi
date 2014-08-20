#!/usr/env/python
import os
import sys

# Change working directory so relative paths (and template lookup) work again
basedir = os.path.dirname('/home/cristian/Scrivania/Progetti/lmftoufy/gmtpun/public_html/')
os.chdir(basedir)

if basedir not in sys.path:
  sys.path.append(basedir)

import gmtpun
# ... build or import your bottle application here ...
# Do NOT use bottle.run() with mod_wsgi
application = gmtpun.GmtPun
