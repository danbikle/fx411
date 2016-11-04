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
   
pairs_l    = ['AUDUSD','EURUSD','GBPUSD','USDCAD','USDJPY']
for pair_s in pairs_l:
  print(pair_s)

'bye'

