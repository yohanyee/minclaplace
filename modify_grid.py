#!/usr/bin/python

import argparse
import numpy as np
from pyminc.volumes.factory import *
import skfmm

#infile = "/axiom2/projects/software/cortical-thickness/MWM/c57bl6_laplacian_grid_fixed.mnc"
infile = "/hpf/largeprojects/MICe/yyee/projects/Grandjean_cortical_recon/animal1/reg_mwm/laplacian_grid_on_JG_standard.mnc"
invol = volumeFromFile(infile)
outfile = "/hpf/largeprojects/MICe/yyee/projects/Grandjean_cortical_recon/animal1/minclaplace_test/laplacian_grid_on_JG_standard_modified_19.mnc"


"""
#outer_expansion = np.ma.masked_array(data=(invol.data-10), mask=(invol.data < -10))
print("Working on outer expansion")
outer_expansion = (invol.data - 10)
outer_fmm = skfmm.distance(outer_expansion)

print("Working on inner expansion")
inner_expansion = (invol.data)
inner_expansion[(invol.data >= 10) & (invol.data < 19)]
inner_fmm = skfmm.distance(inner_expansion)
"""

print("Working on expansion")
expansion = -np.ones_like(invol.data)
expansion[(invol.data >= 10) & (invol.data < 19)] = 1
expansion[(invol.data <= 0)] = 1
fmm = skfmm.distance(expansion)

print("Writing data")
outvol = volumeLikeFile(infile, outfile)
outvol.data = invol.data
outvol.data[(invol.data >= 10) & (invol.data < 19) & (fmm < 9)] = (fmm + 10)[(invol.data >= 10) & (invol.data < 19) & (fmm < 9)]
outvol.data[(invol.data <= 0) & (fmm < 9)] = (-fmm)[(invol.data <= 0) & (fmm < 9)]
outvol.writeFile()
outvol.closeVolume()

