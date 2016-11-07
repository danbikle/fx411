# plotbg10.py

# This script should transform a csv file into a DataFrame and then into blue-green-visualization.

import pandas as pd
import pdb

p0_df = pd.read_csv("../csv/plothis.csv",names=['ts','cp','piplead','prediction','eff','acc'])
p1_df       = p0_df.copy()[['ts','cp']]
p1_df['dt'] = pd.to_datetime(p1_df.ts, unit='s')
print(p1_df.head())

'bye'

