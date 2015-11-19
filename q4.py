###########################################################################
# Number 4
###########################################################################

import sys
import os

path=sys.argv[1]

# Failed 2D reads

os.system('poretools hist --saveas plot4_fail_2D.png '+path+'downloads/fail/')

# Passed 2D reads

os.system('poretools hist --saveas plot4_pass_2D.png '+path+'downloads/pass/')


