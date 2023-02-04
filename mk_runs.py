#! /usr/bin/env python
#
#   script generator for project="2023-S1-UM-10"
#


import os
import sys

# in prep of the new lmtoy module
try:
    lmtoy = os.environ['LMTOY']
    sys.path.append(lmtoy + '/lmtoy')
    import runs
except:
    print("No LMTOY with runs.py")
    sys.exit(0)

project="2023-S1-UM-10"

#        obsnums per source (make it negative if not added to the final combination)
on = {}
on['J081907.23+602317.0'] = [ 104429, 104430, 104431, 104433, 104434, 104435,   # 2-feb
                              104535, 104536, 104537                        ]   # 3-feb
on['J083055.00+253123.9'] = [ 104439, 104440, 104441, 104443, 104444, 104445]   # 2 feb
on['J094713.51-070858.4'] = [ 104449, 104450, 104451, 104453, 104454, 104455]   # 2 feb
on['J082823.34+254129.1'] = [ 104540, 104541, 104542, 104544, 104545, 104546]   # 3-feb
on['J081035.73+535048.8'] = [ 104551, 104552, 104553, 104555, 104556, 104557]   # 3-feb
on['J084728.61+723353.7'] = [ 104560, 104561, 104562, 104564, 104565, 104566]   # 3-feb

#        common parameters per source on the first dryrun (run1a, run2a)
pars1 = {}
pars1['J081907.23+602317.0']   = ""
pars1['J083055.00+253123.9']   = ""
pars1['J094713.51-070858.4']   = ""
pars1['J082823.34+254129.1']   = ""
pars1['J081035.73+535048.8']   = ""
pars1['J084728.61+723353.7']   = ""

#        common parameters per source on subsequent runs (run1b, run2b)
pars2 = {}
pars2['J081907.23+602317.0']   = "srdp=1 admit=0"
pars2['J083055.00+253123.9']   = "srdp=1 admit=0"
pars2['J094713.51-070858.4']   = "srdp=1 admit=0"
pars2['J082823.34+254129.1']   = "srdp=1 admit=0"
pars2['J081035.73+535048.8']   = "srdp=1 admit=0"
pars2['J084728.61+723353.7']   = "srdp=1 admit=0"

runs.mk_runs(project, on, pars1, pars2)
