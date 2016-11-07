# plotbg10.py

# This script should transform a csv file into a DataFrame and then into blue-green-visualization.

import pandas as pd
import matplotlib.pyplot as plt
import pdb

p0_df = pd.read_csv("../csv/plothis.csv",names=['ts','cp','piplead','prediction','eff','acc'])
p1_df       = p0_df.copy()[['ts','cp']]
p1_df['dt'] = pd.to_datetime(p1_df.ts, unit='s')
# In pandas, how to create index from column?
p2_df = p1_df.set_index(['dt'])
p3_df = p2_df[['cp']]
print(p3_df.head())
p3_df.plot.line(title="Long vs. Logistic Regression")
plt.show()
'bye'
