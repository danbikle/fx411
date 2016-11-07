# rpt_rand.py

# This script should report data in files which look like this:
#   -rw-rw-r--  1 fx411 fx411   274782 Nov  7 08:28 predictions93000EURUSD.csv

# The columns are listed below:
# ts, price, piplead, eff, acc

# I should create a report which has these columns:
# trainsize, pair, eff_sum, acc_pct

import pandas as pd
import pdb
import glob as glob

trainsize_i = 93000
pair_s      = 'EURUSD'
r0_df = pd.read_csv('../csv/predictions93000EURUSD.csv',names=['ts','price','piplead','eff','acc'])
print(r0_df.head())

'bye'

