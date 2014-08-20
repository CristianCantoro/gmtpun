#!/usr/env/python
import os
import sys

# activate virtualenv
activate_this = os.path.expanduser("/home/cristian/.virtualenvs/gmtpun/bin/activate_this.py")
execfile(activate_this, dict(__file__=activate_this))

# Change working directory so relative paths (and template lookup) work again
basedir = os.path.dirname(os.path.realpath(__file__))
os.chdir(basedir)

if basedir not in sys.path:
  sys.path.append(basedir)

import gmtpun
application = gmtpun.GmtPun
