# rpt.py

# This script should report accuracy and effectiveness of predictions in ../csv/predictions_*.csv

import os,glob
import pandas as pd
import numpy  as np
import pdb

pairs_l = ['AUDUSD','EURUSD','GBPUSD','USDCAD','USDJPY']
for pair_s in pairs_l:
  fn_l = glob.glob("../csv/predictions_"+pair_s+"*.csv")
  # For this pair I should sort and make uniq and output to single file
  # inspiration:
  # sort -u ../csv/predictions_AUDUSD*.csv|grep 0> ../csv/predictionsAUDUSD.csv
  if len(fn_l) > 0 :
    cmd0_s = "sort -u ../csv/predictions_"+pair_s+"*.csv|grep 0 > "
    fn_s   = "../csv/predictions"+pair_s+".csv"
    os.system(cmd0_s + fn_s)
    p0_df = pd.read_csv(fn_s,names=['ts','cp','piplead','prediction','eff','acc'])
    print(p0_df.head())
    print(pair_s+" Effectiveness:")
    print(np.sum(p0_df.eff))
    print(pair_s+" Accuracy:")
    print(100 * np.sum(p0_df.acc) / len(p0_df.acc))

'bye'
