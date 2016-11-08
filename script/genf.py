# genf.py

# This script should generate features from timestamps and prices.
import pandas as pd
import numpy  as np
# I should specify duration I hold a pair after I act on a prediction:
duration_i = 12 # 12 means 12 * 5 which is 1 hour which is 3600 seconds
pairs_l    = ['AUDUSD','EURUSD','GBPUSD','USDCAD','USDJPY']
for pair_s in pairs_l:
  print(pair_s+' Busy...')
  g0_df = pd.read_csv("../csv/"+pair_s+".csv", names=['ts','cp'])
  # I should compute dependent variable, piplead:
  g0_df['piplead'] = (10000.0*(g0_df.cp.shift(-duration_i) - g0_df.cp) / g0_df.cp).fillna(0)
  # I should compute piplags 1,2,4,8
  g0_df['piplag1'] = (10000.0*(g0_df.cp - g0_df.cp.shift(duration_i*1)) / g0_df.cp).fillna(0)
  g0_df['piplag2'] = (10000.0*(g0_df.cp - g0_df.cp.shift(duration_i*2)) / g0_df.cp).fillna(0)
  g0_df['piplag3'] = (10000.0*(g0_df.cp - g0_df.cp.shift(duration_i*3)) / g0_df.cp).fillna(0)
  g0_df['piplag4'] = (10000.0*(g0_df.cp - g0_df.cp.shift(duration_i*4)) / g0_df.cp).fillna(0)
  g0_df['piplag5'] = (10000.0*(g0_df.cp - g0_df.cp.shift(duration_i*5)) / g0_df.cp).fillna(0)
  # I should write to CSV file to be used later:
  g0_df.to_csv("../csv/feat"+pair_s+".csv", float_format='%4.4f', index=False)
  
'bye'
