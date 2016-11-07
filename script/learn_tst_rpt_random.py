# learn_tst_rpt_random.py

# This script should learn from these files:
# ../csv/featAUDUSD.csv
# ../csv/featEURUSD.csv
# ../csv/featGBPUSD.csv
# ../csv/featUSDCAD.csv
# ../csv/featUSDJPY.csv
# Then it should generate predictions and write to these files:
# ../csv/predictions_AUDUSD...
# ../csv/predictions_EURUSD...
# ../csv/predictions_GBPUSD...
# ../csv/predictions_USDCAD...
# ../csv/predictions_USDJPY...

import pandas as pd
import numpy  as np
from sklearn import linear_model
import os,glob,random,datetime,pdb

# I should remove unneeded files:
cmd1_s = "rm -f ../csv/predictions_*.csv"
os.system(cmd1_s)

# I should use a nested loop to generate predictions from a window which slides over several pairs.
# Sometimes I call this window the test-window because it should contain test-data.

# I should describe a window which slides from bottom of DF to top.
# The window should make jumps rather than sliding one row at a time.
# The window width should be same width as DF.
# The window length should be wlen_i.
# jump size should be jump_i.
# The number of jumps should be jumpc_i.

wlen_i = 20
jump_i = wlen_i # Avoids prediction 'overlap'
for trainsize_i in range(9000, 109000, 2000):
  print('Busy ooooooooooooooooooooooooooo')
  #trainsize_i = 17000 # Size of training data before the window AKA the test-window.
  # I should define the number of observations I hold a pair after I buy/sell it.
  # Observations are separated by 5 min. One hour is 12 observations:
  duration_i = 12 # Hold for 1 hour then act on next prediction.
  pairs_l    = ['AUDUSD','EURUSD','GBPUSD','USDCAD','USDJPY']
  for pair_s in pairs_l:
    p0_df      = pd.read_csv("../csv/feat"+pair_s+".csv")
    ## test_end_i = len(p0_df)-duration_i # avoid observations where piplead unknown.
    # I should control how many times I jump the window.
    # If each jump is small, I can make more jumps:
    ### jumpc_i    = int((len(p0_df)-trainsize_i-100) / jump_i)-1
    # Above expression keeps my jumps inside of p0_df.
    # Below I hard-code jumpc_i to integer which works well with random sample idea:
    jumpc_i = 300
    for cnt_i in range(jumpc_i,0,-1):
      # I should build a model here from a random sample of data rather than all data:
      test_end_i    = random.randrange(trainsize_i+10*duration_i, (len(p0_df)-duration_i))
      test_start_i  = test_end_i-wlen_i
      train_end_i   = test_start_i - 2*duration_i # Avoid overlap
      train_start_i = train_end_i - trainsize_i
      train_df      = p0_df[train_start_i:train_end_i]
      train_df.to_csv('/tmp/train_df.csv', float_format='%4.4f')
      test_df       = p0_df[test_start_i:test_end_i]
      #test_end_i   -= jump_i
      logr_model    = linear_model.LogisticRegression()
      xtrain_a      = np.array(train_df)[:,3:]
      xtest_a       = np.array(test_df)[:,3:]
      ytrain_sr     = train_df.piplead
      class_train_a = (ytrain_sr > 0.0)
      logr_model.fit(xtrain_a, class_train_a)
      # I should predict
      predictions_df = test_df.copy()[['ts','cp','piplead']]
      predictions_df['prediction'] = logr_model.predict_proba(xtest_a)[:,1].tolist()
      predictions_df['eff'] = np.sign(predictions_df.prediction - 0.5) * predictions_df.piplead
      predictions_df['acc'] = (predictions_df.eff > 0)
      fn_s = "../csv/predictions_"+pair_s+str(1000+cnt_i)+".csv" 
      predictions_df.to_csv(fn_s, float_format='%4.4f', index=False)
  eff_sum_f = 0
  for pair_s in pairs_l:
    fn_l = glob.glob("../csv/predictions_"+pair_s+"*.csv")
    # For this pair I should sort and make uniq and output to single file
    # inspiration:
    # sort -u ../csv/predictions_AUDUSD*.csv|grep 0> ../csv/predictionsAUDUSD.csv
    if len(fn_l) > 0 :
      cmd0_s = "sort -u ../csv/predictions_"+pair_s+"*.csv|grep 0 > "
      fn_s   = "../csv/predictions"+str(trainsize_i)+pair_s+".csv"
      os.system(cmd0_s + fn_s)
      p0_df = pd.read_csv(fn_s,names=['ts','cp','piplead','prediction','eff','acc'])
      print(pair_s+" Effectiveness:")
      eff_pair = np.sum(p0_df.eff)
      print(eff_pair)
      eff_sum_f = eff_sum_f + eff_pair
      print(pair_s+" Accuracy:")
      print(str(100 * np.sum(p0_df.acc) / len(p0_df.acc))+' %')
  print('trainsize_i:')
  print(trainsize_i)
  print('eff_sum_f:')
  print(eff_sum_f)
  # I should remove unneeded files:
  cmd1_s = "rm -f ../csv/predictions_*.csv"
  os.system(cmd1_s)

'bye'
