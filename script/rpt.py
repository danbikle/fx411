# rpt.py

# This script should help me find most predictable pair.
# This script should help me find optimal training sizes.


# The predictions are in files which look like this:
#   -rw-rw-r--  1 fx411 fx411   274782 Nov  7 08:28 predictions93000EURUSD.csv

# The columns are listed below:
# ts, price, piplead, eff, acc

import pandas as pd
import numpy  as np
import pdb
import glob

fn_l = glob.glob('../csv/predictions*.csv')

all_sum = 0
pair_trainsize_eff_acc_l = []
for fn in sorted(fn_l):
    r0_df = pd.read_csv(fn,names=['ts','price','piplead','prediction','eff','acc'])
    eff_sum     = np.sum(r0_df.eff)
    all_sum     = all_sum+eff_sum
    acc_pct     = np.round(100*np.sum(r0_df.acc) / len(r0_df),1)
    trainsize_i = fn[18:-10]
    pair_s      = fn[-10:-4]
    pair_trainsize_eff_acc_l.append([pair_s,trainsize_i,eff_sum,acc_pct])
# I should convert pair_trainsize_eff_acc_l into a DataFrame.
pair_trainsize_eff_acc_a  = np.array(pair_trainsize_eff_acc_l)
pair_trainsize_eff_acc_df = pd.DataFrame({'pair':  pair_trainsize_eff_acc_a[:,0]
                                      ,'trainsize':pair_trainsize_eff_acc_a[:,1]
                                      ,'eff':      pair_trainsize_eff_acc_a[:,2]
                                      ,'acc':      pair_trainsize_eff_acc_a[:,3]
})
print(pair_trainsize_eff_acc_df.head())


'bye'
