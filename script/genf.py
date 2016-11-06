# genf.py

# This script should generate features from timestamps and prices.
import pandas as pd
import numpy  as np
# I should specify duration I hold a pair after I act on a prediction:
duration_i = 12 # 12 means 12 * 5 which is 1 hour
duration_i = 1  # 1  means 1  * 5 which is 5 min
slopes_a   = np.array([2,3,4,5,6,7,8,9]) * duration_i
pairs_l    = ['AUDUSD','EURUSD','GBPUSD','USDCAD','USDJPY']
for pair_s in pairs_l:
  print(pair_s)
  g0_df = pd.read_csv("../csv/"+pair_s+".csv", names=['ts','cp'])
  # I should compute dependent variable, piplead:
  g0_df['piplead'] = (10000.0*(g0_df.cp.shift(-duration_i) - g0_df.cp) / g0_df.cp).fillna(0)
  # I should compute mvgavg-slope for each slope_i
  # ref:
  # http://www.ml4.us/cclasses/class03pd41
  # http://pandas.pydata.org/pandas-docs/stable/computation.html#rolling-windows
  # http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.rolling.html#pandas.DataFrame.rolling
  for slope_i in slopes_a:
    rollx        = g0_df.rolling(window=slope_i)
    col_s        = 'slope'+str(slope_i)
    slope_sr     = 10000.0 * (rollx.mean().cp - rollx.mean().cp.shift(duration_i))/rollx.mean().cp
    g0_df[col_s] = slope_sr
  print(g0_df.tail())
  # I should write to CSV file to be used later:
  g0_df.to_csv("../csv/feat"+pair_s+".csv", float_format='%4.4f', index=False)
  
  
'bye'
