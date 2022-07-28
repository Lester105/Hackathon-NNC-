# Import modules

import pandas as pd
import numpy as np
import math
import calc  # Import user defined functions

# Variable Input
# TODO to be replaced with values from form input
length = 78.9  # height/length in cm
weight = 8.5  # weight in kg
age = 2
muac = 110  # MUAC in mm
edema = True

zscore = -3.1
#zscore = calc.zscore(length, weight, age)

status = calc.am_classify(zscore, muac, edema)
