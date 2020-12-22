import random
import sys
from math import log

if sys.version_info < (3, 0):
    input = raw_input

white = '\033[1;97m'
green = '\033[1;32m'
red = '\033[1;31m'
yellow = '\033[1;33m'
end = '\033[1;m'
info = '\033[1;33m[!]\033[1;m'
que =  '\033[1;34m[?]\033[1;m'
bad = '\033[1;31m[-]\033[1;m'
good = '\033[1;32m[+]\033[1;m'
run = '\033[1;97m[~]\033[1;m'
print(yellow+'''
 ____               ____  _                        _   _
|  _ \ __ _ ___ ___/ ___|| |_ _ __ ___ _ __   __ _| |_| |__
| |_) / _` / __/ __\___ \| __| '__/ _ \ '_ \ / _` | __| '_ \ 
|  __/ (_| \__ \__ \___) | |_| | |  __/ | | | (_| | |_| | | |
|_|   \__,_|___/___/____/ \__|_|  \___|_| |_|\__, |\__|_| |_|
                                             |___/''')
                                            
your_pass = input(good+" Your Password: ")
print ('')
print (' %s+------------------------------------+---------------------+%s' % (green, end))
print (' %s| Passwords                          | Entropy             |%s' % (green, end))
print (' %s+------------------------------------+---------------------+%s' % (green, end))
print (' %s|%s %-35s%s|%s %-20s%s|%s' % (green, end, your_pass, green, end, (log(82)/log(2)) * len(your_pass), green, end))
print (' %s+----------------------------------------------------------+%s' % (green, end))