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

# I should aggregate
eff_sum = np.sum(r0_df.eff)

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
pair_trainsize_eff_acc_a  = np.array(pair_trainsize_eff_acc_l)
pair_trainsize_eff_acc_df = pd.DataFrame({'pair':  pair_trainsize_eff_acc_a[:,0]
                                      ,'trainsize':pair_trainsize_eff_acc_a[:,1]
                                      ,'eff':      pair_trainsize_eff_acc_a[:,2]
                                      ,'acc':      pair_trainsize_eff_acc_a[:,3]
})
print(pair_trainsize_eff_acc_df.head())

# I should change eff and acc to floats:
eff_l    = [float(my_s) for my_s in pair_trainsize_eff_acc_df.eff]
acc_l    = [float(my_s) for my_s in pair_trainsize_eff_acc_df.acc]
ptea1_df = pair_trainsize_eff_acc_df.copy()[['pair','trainsize']]
ptea1_df['eff'] = eff_l
ptea1_df['acc'] = acc_l

# I should search for best trainsize
gb1_df = ptea1_df.groupby(['trainsize']).eff.sum()
print(gb1_df.head())
print(gb1_df.sort_values().tail())

gb2_df = ptea1_df.groupby(['trainsize']).acc.mean()
print(gb2_df.sort_values().tail())

# I should search for best pair,trainsize
print(ptea1_df.head())
print(ptea1_df.sort_values(by='eff').tail(22))

'bye'

