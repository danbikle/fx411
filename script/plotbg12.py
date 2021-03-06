# plotbg12.py

# This script should transform csv files into blue-green-visualizations.

import pandas as pd
import numpy  as np
import glob

fn_l = glob.glob('../csv/predictions*.csv')
pair_trainsize_eff_acc_l = []
for fn in sorted(fn_l):
    r0_df = pd.read_csv(fn,names=['ts','price','piplead','prediction','eff','acc'])
    eff_sum     = np.sum(r0_df.eff)
    acc_pct     = np.round(100*np.sum(r0_df.acc) / len(r0_df),1)
    trainsize_i = fn[18:-10]
    pair_s      = fn[-10:-4]
    pair_trainsize_eff_acc_l.append([pair_s,trainsize_i,eff_sum,acc_pct])
# I should convert pair_trainsize_eff_acc_l into a DataFrame.
pair_trainsize_eff_acc_a  = np.array(pair_trainsize_eff_acc_l)
pair_trainsize_eff_acc_df = pd.DataFrame({'pair':  pair_trainsize_eff_acc_a[:,0]
                                      ,'trainsize':pair_trainsize_eff_acc_a[:,1]
                                      ,'eff':      pair_trainsize_eff_acc_a[:,2]
                                      ,'acc':      pair_trainsize_eff_acc_a[:,3]
})

# I should change eff and acc to floats:
eff_l    = [float(my_s) for my_s in pair_trainsize_eff_acc_df.eff]
acc_l    = [float(my_s) for my_s in pair_trainsize_eff_acc_df.acc]
ptea1_df = pair_trainsize_eff_acc_df.copy()[['pair','trainsize']]
ptea1_df['eff'] = eff_l
ptea1_df['acc'] = acc_l

# To see the most effective combinations of pair and trainsize, I should sort:
print(ptea1_df.sort_values(by='eff', ascending=False).head(30))

ptea2_df = ptea1_df.sort_values(by='eff', ascending=False).head(30)[['trainsize','pair']]
print(ptea2_df.head())

for idx_i in ptea2_df.index:
  row         = ptea2_df.loc[idx_i]
  trainsize_s = row.trainsize
  pair_s      = row.pair
  csv_s       = '../csv/predictions'+trainsize_s+pair_s+'.csv'

  p0_df  = pd.read_csv(csv_s, names=['ts','cp','piplead','problr','eff','acc'])
  p1_df       = p0_df.copy()[['ts','cp','eff']]
  p1_df['Date'] = pd.to_datetime(p1_df.ts, unit='s')
  
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
  p2_df         = p1_df.set_index(['Date'])
  p3_df         = p2_df[['cp','Logistic_Regression']]
  p3_df.columns = [['Price','Logistic_Regression']]
  trainsize_i   = csv_s[18:-10]
  pair_s        = csv_s[-10:-4]
  # Now I should plot the visualization:
  import matplotlib
  matplotlib.use('Agg')
  # Order is important here.
  # Do not move the next import:
  import matplotlib.pyplot as plt
  title_s =pair_s+" Price and Logistic Regression Predictions From "+str(trainsize_i)+" Row Training Set"
  p3_df.plot.line(title=title_s, figsize=(11,7))
  png_s = '../public/plots/img'+str(trainsize_i)+pair_s+'.png'
  plt.savefig(png_s)
  plt.close()
  print('We should have a new plot now: '+png_s)
  'bye'
