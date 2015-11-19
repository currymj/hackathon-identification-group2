###########################################################################
# Number 5
# Usage: (python) group2_report1_question5.py <BitTorrent Sync folder>
###########################################################################

import sys
import os

path=sys.argv[1]

file = open('Q5readlengths.txt', 'w')

# Passed reads - 2D

os.system('poretools winner --type 2D '+path+'downloads/pass/ >'+path+'downloads/pass/long2DPass.txt')

f = open(''+path+'downloads/pass/long2DPass.txt')
lines = f.readlines()
file.write('Longest passed 2D: ' + lines[0] + '\nLength: ' + str(len(lines[1])))

# Failed reads - 2D

os.system('poretools winner --type 2D '+path+'downloads/fail/ >'+path+'downloads/fail/long2DFail.txt')

f = open(''+path+'downloads/fail/long2DFail.txt')
lines = f.readlines()
file.write('\nLongest failed 2D: ' + lines[0] + '\nLength: ' + str(len(lines[1])))

file.close()

