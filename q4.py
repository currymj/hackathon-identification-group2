###########################################################################
# Number 4
###########################################################################

import sys
import os

path=sys.argv[1]

# Failed 1D reads

os.system('poretools hist --theme-bw --saveas plot4_fail_1D.png '+path+'downloads/fail/1D/')

# Failed 2D reads

os.system('poretools hist --theme-bw --saveas plot4_fail_2D.png '+path+'downloads/fail/2D/')

# Passed 1D reads

os.system('poretools hist --theme-bw --saveas plot4_pass_1D.png '+path+'downloads/pass/1D/')

# Passed 2D reads

os.system('poretools hist --theme-bw --saveas plot4_pass_2D.png '+path+'downloads/pass/2D/')


