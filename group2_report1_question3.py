###########################################################################
# Number 3
###########################################################################

import sys
import os
import pandas as pd
import datetime
import os.path
import glob
import csv
import re

path=sys.argv[1]

# Failed reads

#os.system('poretools yield_plot --plot-type basepairs --theme-bw --saveas plot3_fail.png '+path+'downloads/fail/2D/')

counts = []
dates = []
with open('pass.tsv', 'rb') as passtsv:
    passreader = csv.reader(passtsv, delimiter='\t')
    passreader.next()
    for line in passreader:
        counts.append(int(line[0]))
        fname = 'downloads/' + re.search(r'pass/.*fast5', line[1]).group()
        dates.append(datetime.datetime.fromtimestamp(os.path.getctime(fname)))
df = pd.DataFrame({ "times": dates, "bases": counts}).set_index('times').sort_index()
#df = pd.DataFrame({"times": dates, "bases": counts}).sort("times")
df['cumulative'] = df.bases.cumsum()
print df
p = df['cumulative'].plot()
fig = p.get_figure()
fig.savefig('./passbases.png')

p.cla()
# failed reads

counts = []
dates = []
with open('fail.tsv', 'rb') as failtsv:
    failreader = csv.reader(failtsv, delimiter='\t')
    failreader.next()
    for line in failreader:
        counts.append(int(line[0]))
        fname = 'downloads/' + re.search(r'fail/.*fast5', line[1]).group()
        dates.append(datetime.datetime.fromtimestamp(os.path.getctime(fname)))
dffail = pd.DataFrame({ "times": dates, "bases": counts}).set_index('times').sort_index()
#df = pd.DataFrame({"times": dates, "bases": counts}).sort("times")
dffail['cumulative'] = dffail.bases.cumsum()
print dffail
p = dffail['cumulative'].plot()
fig = p.get_figure()
fig.savefig('./failbases.png')
#os.system('poretools yield_plot --plot-type basepairs --theme-bw --saveas plot3_pass.png '+path+'downloads/pass/2D/')



# get all files in pass/fail dirs
# sort on key of ctime
# pandas dataframe of times and basepair lengths
# cumulative sum
# plot using pandas
