###########################################################################
# Filter 2D reads
# Should be run in the pass and fail folders to create subfolders of 2D reads.
###########################################################################

import sys
from glob import glob
import h5py
import os

dir=sys.argv[1]

fns=glob(dir+'/*.fast5')

try:
    os.mkdir(dir+'/2D’)
except:
    pass
try:
    os.mkdir(dir+’/1D’)
except:
    pass


for fp in fns:
    fn=fp.split('/')[-1]
    f=h5py.File(fp,'r')
    if 'Basecall_2D_000' in f['Analyses'].keys():
       if 'BaseCalled_2D' in f['Analyses']['Basecall_2D_000'].keys():
		os.symlink('../'+fn, dir+'/2D/'+fn)
    else:
        os.symlink('../'+fn, dir+'/1D/'+fn)



