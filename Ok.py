import os, platform
try:
   import requests
except:
   os.system('pip2 install requests')

import requests
bit = platform.architecture()[0]
if bit == '64bit':
    from killer9 import ___Killer___
    ___Killer___()
elif bit == '32bit':
    from killer9 import ___Killer___
    ___Killer___()
