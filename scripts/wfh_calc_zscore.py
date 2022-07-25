# Import modules

import pandas as pd
import numpy as np
import math
import calc # Import user defined functions

# Variable Input
# TODO to be replaced with values from form input
length = 78.9 # height/length in cm
weight = 8.5 # weight in kg
age = 2
muac = 110 # MUAC in mm
zscore = -3.1

#zscore = calc.zscore(length, weight, age)

if zscore < -3:
    zscore_con = True
    else:
        zscore_con = False


###
muac = float(muac)

if muac < 115:
    muac_con = True
else:
    muac_con = False

if zscore_con | muac_con == True
    status = "SAM"
el

