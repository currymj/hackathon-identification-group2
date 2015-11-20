###########################################################################
# Number 4
# Usage: (python) group2_report1_question4.py <BitTorrent Sync folder>
###########################################################################

import sys
import os

path=sys.argv[1]

# Failed 2D reads

os.system('poretools hist --saveas plot4_fail_2D.png '+path+'fail/')

# Passed 2D reads

os.system('poretools hist --saveas plot4_pass_2D.png '+path+'pass/')


