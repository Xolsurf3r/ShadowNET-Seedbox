#!/usr/bin/env python
#
#
#  ShadowNET's Seedbox
#    By TheSyndicate ---> https://github.com/The-Syndicate/
#
#
#
# Deluge password generator
#
#   deluge.password.py <password> <salt>
#
#

import hashlib
import sys

password = sys.argv[1]
salt = sys.argv[2]

s = hashlib.sha1()
s.update(salt)
s.update(password)

print s.hexdigest()
