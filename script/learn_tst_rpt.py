# learn_tst_rpt.py

# This script should learn from these files:
# ../csv/featAUDUSD.csv
# ../csv/featEURUSD.csv
# ../csv/featGBPUSD.csv
# ../csv/featUSDCAD.csv
# ../csv/featUSDJPY.csv
# Then it should generate predictions and write to these files:
# ../csv/predictionsAUDUSD.csv
# ../csv/predictionsEURUSD.csv
# ../csv/predictionsGBPUSD.csv
# ../csv/predictionsUSDCAD.csv
# ../csv/predictionsUSDJPY.csv
# Next it should report effectiveness and accuracy of the predictions.

import pandas as pd
import numpy  as np
import pdb

# I should use a nested loop to generate predictions from a window which slides over several pairs.
# Sometimes I call this window the test-window because it should contain test-data.

# I should describe a window which slides from bottom of DF to top.
# The window should make jumps rather than sliding one row at a time.
# The window width should be same width as DF.
# The window length should be wlen_i.
# jump size should be jump_i.
# The number of jumps should be jumpc_i.
  
wlen_i     = 100
jump_i     = wlen_i # Avoids prediction 'overlap'
jumpc_i    = 3
trainsize_i= 4000 # Size of training data before the window AKA the test-window.
# I should define the number of observations I hold a pair after I buy/sell it.
# Observations are separated by 5 min. One hour is 12 observations:
duration_i = 12 # Hold for 1 hour then act on next prediction.

pairs_l    = ['AUDUSD','EURUSD']#,'GBPUSD','USDCAD','USDJPY']
for pair_s in pairs_l:
  print(pair_s)
  p0_df = pd.read_csv("../csv/feat"+pair_s+".csv")
  test_end_i = len(p0_df)
  
print(p0_df.tail())

for cnt_i in range(jumpc_i,0,-1):
    # I should build a model here
    test_start_i  = test_end_i-wlen_i
    train_end_i   = test_start_i - 2*duration_i # Avoid overlap
    train_start_i = train_end_i - trainsize_i
    train_df = p0_df[train_start_i:train_end_i]
    test_df  = p0_df[test_start_i:test_end_i]
    test_end_i -= jump_i
    
'bye'

