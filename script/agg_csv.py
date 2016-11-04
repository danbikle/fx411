# agg_csv.py

# This script should aggregate CSV files into one file for each pair.
import glob
import os
import pandas as pd
pairs_l = ['AUDUSD','EURUSD','GBPUSD','USDCAD','USDJPY']
for pair_s in pairs_l:
    fn_l = glob.glob("../csv/"+pair_s+"-20*csv")
    # For this pair I should sort and make uniq and output to single file
    # inspiration:
    # sort -u ../csv/AUDUSD-20*csv > AUDUSD.csv
    if len(fn_l) > 0 :
        os.system("sort -u ../csv/"+pair_s+"-20*csv > ../csv/"+pair_s+"0.csv")
        p0_df = pd.read_csv("../csv/"+pair_s+"0.csv", names=['ts','cp'])
        # I should use groupby to de-dup and then write to CSV:
        p1_df = p0_df.groupby(['ts']).cp.mean()
        p1_df.to_csv("../csv/"+pair_s+".csv", float_format='%4.6f')

'bye'

