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
   
pairs_l    = ['AUDUSD','EURUSD']#,'GBPUSD','USDCAD','USDJPY']
for pair_s in pairs_l:
  print(pair_s)
  p0_df = pd.read_csv("../csv/feat"+pair_s+".csv")
  # I should build a window which slides from bottom of DF to top.
  # The window should make jumps rather than sliding one row at a time.
  # The window width should be same width as DF.
  # The window length should be wlen_i.
  # jump size should be jump_i.
  # The number of jumps should be jumpc_i.
  
print(p0_df.tail())

wlen_i     = 100
jump_i     = wlen_i # Avoids prediction 'overlap'
test_end_i = len(p0_df)
jumpc_i    = 3
for cnt_i in range(jumpc_i,0,-1):
    # I should build a model here
    p1_df = p0_df[(test_end_i-wlen_i):test_end_i]
    print(p1_df.tail())
    
    test_end_i -= jump_i

    
'bye'

