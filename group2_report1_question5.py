###########################################################################
# Number 5
###########################################################################

import sys
import os

path=sys.argv[1]

file = open('Q5readlengths.txt', 'w')

# Passed reads - 2D

os.system('poretools winner --type 2D '+path+'pass/ >'+path+'pass/long2DPass.txt')

f = open(''+path+'pass/long2DPass.txt')
lines = f.readlines()
file.write('Longest passed 2D: ' + lines[0] + '\nLength: ' + str(len(lines[1])))

# Failed reads - 2D

os.system('poretools winner --type 2D '+path+'fail/ >'+path+'fail/long2DFail.txt')

f = open(''+path+'fail/long2DFail.txt')
lines = f.readlines()
file.write('\n\nLongest failed 2D: ' + lines[0] + '\nLength: ' + str(len(lines[1])))

file.close()


