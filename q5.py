###########################################################################
# Number 5
###########################################################################

import sys
import os

path=sys.argv[1]

file = open('readlengths.txt', 'w')

# Passed reads
# Template

os.system('poretools winner --type fwd '+path+'downloads/pass/ >'+path+'downloads/pass/longTempPass.txt')

f = open(''+path+'downloads/pass/longTempPass.txt')
lines = f.readlines()
file.write('Longest passed template: ' + lines[0])
file.write('Length: ' + str(len(lines[1])))
file.write('')

# Complement

os.system('poretools winner --type rev '+path+'downloads/pass/ >'+path+'downloads/pass/longCompPass.txt')

f = open(''+path+'downloads/pass/longCompPass.txt')
lines = f.readlines()
file.write('Longest passed complement: ' + lines[0])
file.write('Length: ' + str(len(lines[1])))
file.write('')

# 2D

os.system('poretools winner --type 2D '+path+'downloads/pass/ >'+path+'downloads/pass/long2DPass.txt')

f = open(''+path+'downloads/pass/long2DPass.txt')
lines = f.readlines()
file.write('Longest passed 2D: ' + lines[0])
file.write('Length: ' + str(len(lines[1])))
file.write('')

# Failed reads
# Template

os.system('poretools winner --type fwd '+path+'downloads/fail/ >'+path+'downloads/pass/longTempFail.txt')

f = open(''+path+'downloads/pass/longTempFail.txt')
lines = f.readlines()
file.write('Longest failed template: ' + lines[0])
file.write('Length: ' + str(len(lines[1])))
file.write('')

# Complement

os.system('poretools winner --type rev '+path+'downloads/fail/ >'+path+'downloads/pass/longCompFail.txt')

f = open(''+path+'downloads/pass/longCompFail.txt')
lines = f.readlines()
file.write('Longest failed complement: ' + lines[0])
file.write('Length: ' + str(len(lines[1])))
file.write('')

# 2D

os.system('poretools winner --type 2D '+path+'downloads/fail/ >'+path+'downloads/pass/long2DFail.txt')

f = open(''+path+'downloads/pass/long2DFail.txt')
lines = f.readlines()
file.write('Longest failed 2D: ' + lines[0])
file.write('Length: ' + str(len(lines[1])))
file.write('')

file.close()


