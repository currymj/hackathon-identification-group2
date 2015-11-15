###########################################################################
# Number 3
###########################################################################

import sys
import os

path=sys.argv[1]

# Failed reads

os.system('poretools yield_plot --plot-type basepairs --saveas plot2_fail.png '+path+'downloads/fail/2D/')

# Passed reads

os.system('poretools yield_plot --plot-type basepairs --saveas plot2_pass.png '+path+'downloads/pass/2D/')



