# plotbg10.py

# This script should transform a csv file into a DataFrame and then into blue-green-visualization.

import pandas as pd
import matplotlib.pyplot as plt
import pdb

p0_df = pd.read_csv("../csv/plothis.csv",names=['ts','cp','piplead','prediction','eff','acc'])
p1_df       = p0_df.copy()[['ts','cp','eff']]
p1_df['dt'] = pd.to_datetime(p1_df.ts, unit='s')

# I should build the green data; it should start at same place as blue data:
green_l = [p1_df.cp[0]]
len_i   = len(p1_df)
# Integer navigator.
row_i = 0
while row_i < len_i-1:
    # I should track where I am.
    row_i += 1
    # I should track blue_line delta:
    blue_delt_f = abs(p1_df.cp[row_i] - p1_df.cp[row_i-1])
    # I should add to the green line:
    if p1_df.eff[row_i-1] > 0 :
        green_l.append( green_l[row_i-1] + blue_delt_f )
    else:
        green_l.append( green_l[row_i-1] - blue_delt_f )
p1_df['Logistic_Regression'] = green_l
# In pandas, how to create index from column?
p2_df = p1_df.set_index(['dt'])
p3_df = p2_df[['cp','Logistic_Regression']]
p3_df.columns = [['Price','Logistic_Regression']]
p3_df.plot.line(title="EUR/USD Price vs. Logistic Regression Predictions")
plt.show()
'bye'
