# agg_zip.py

# This script should read a zip file.
# Then it should groupby timestamp and find the mean of (bid+ask)/2
# Finally it should output a CSV file with aggregated current_price.

import pandas as pd
pairmo = 'USDJPY-2016-09'
zipf   = '/home/fx411/truefx/'+pairmo+'.zip'
f10_df = pd.read_csv('/home/fx411/truefx/USDJPY-2016-09.zip', names=['pair','ts0','bid','ask'])
f11_df       =  f10_df.copy()[['pair','ts0']]
f11_df['cp'] = (f10_df.bid+f10_df.ask)/2
ts1_l        = [ts[:14] for ts in f11_df.ts0]
ts2_sr       = pd.to_datetime(ts1_l, utc=True)
f11_df['ts'] = [5*60*int(int(ts.strftime("%s"))/5/60) for ts in ts2_sr]
f12_df       = f11_df.copy()[['ts','cp']]
print(f12_df.tail())
f13_df = f12_df.groupby(['ts']).cp.mean()
print(f13_df.head())
print(f13_df.tail())

f13_df.to_csv('/home/fx411/csv/'+pairmo+'.csv', float_format='%4.6f')

'bye'
