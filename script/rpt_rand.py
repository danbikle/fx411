# rpt_rand.py

# This script should report data in files which look like this:
#   -rw-rw-r--  1 fx411 fx411   274782 Nov  7 08:28 predictions93000EURUSD.csv

# The columns are listed below:
# ts, price, piplead, eff, acc

# I should create a report which has these columns:
# trainsize, eff_sum, acc_pct

import pandas as pd
import numpy  as np
import pdb
import glob

trainsize_i = 93000
pair_s      = 'EURUSD'
r0_df = pd.read_csv('../csv/predictions93000EURUSD.csv',names=['ts','price','piplead','prediction','eff','acc'])
print(r0_df.head())

# I should aggregate
eff_sum = np.sum(r0_df.eff)
print(eff_sum)
acc_pct = np.round(100*np.sum(r0_df.acc) / len(r0_df),1)
print(acc_pct)

fn_l = glob.glob('../csv/predictions*.csv')
print(fn_l[:9])

all_sum = 0
for fn in fn_l:
    r0_df = pd.read_csv(fn,names=['ts','price','piplead','prediction','eff','acc'])
    eff_sum = np.sum(r0_df.eff)
    print(eff_sum)
    all_sum = all_sum+eff_sum
print(all_sum)

'bye'

