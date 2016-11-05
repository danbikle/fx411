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
from sklearn import linear_model

import pdb

# I should use a nested loop to generate predictions from a window which slides over several pairs.
# Sometimes I call this window the test-window because it should contain test-data.

# I should describe a window which slides from bottom of DF to top.
# The window should make jumps rather than sliding one row at a time.
# The window width should be same width as DF.
# The window length should be wlen_i.
# jump size should be jump_i.
# The number of jumps should be jumpc_i.
  
wlen_i      = 1000
jump_i      = wlen_i # Avoids prediction 'overlap'
trainsize_i = 4000 # Size of training data before the window AKA the test-window.
# I should define the number of observations I hold a pair after I buy/sell it.
# Observations are separated by 5 min. One hour is 12 observations:
duration_i = 12 # Hold for 1 hour then act on next prediction.
pairs_l    = ['AUDUSD','EURUSD']#,'GBPUSD','USDCAD','USDJPY']
for pair_s in pairs_l:
  print(pair_s)
  p0_df      = pd.read_csv("../csv/feat"+pair_s+".csv")
  test_end_i = len(p0_df)
  # I should control how many times I jump the window.
  # If each jump is small, I can make more jumps:
  jumpc_i    = int((len(p0_df)-trainsize_i-100) / jump_i)-1
  # Above expression keeps my jumps inside of p0_df.
for cnt_i in range(jumpc_i,0,-1):
    # I should build a model here
    test_start_i  = test_end_i-wlen_i
    train_end_i   = test_start_i - 2*duration_i # Avoid overlap
    train_start_i = train_end_i - trainsize_i
    train_df      = p0_df[train_start_i:train_end_i]
    train_df.to_csv('/tmp/train_df.csv', float_format='%4.4f')
    test_df       = p0_df[test_start_i:test_end_i]
    test_end_i   -= jump_i
    logr_model    = linear_model.LogisticRegression()
    xtrain_a      = np.array(train_df)[:,3:]
    xtest_a      = np.array(test_df)[:,3:]
    ytrain_sr     = train_df.piplead
    class_train_a = (ytrain_sr > 0.0)
    logr_model.fit(xtrain_a, class_train_a)
    # I should predict
    predictions_l = logr_model.predict_proba(xtest_a)[:,1].tolist()
    predictions_df = test_df.copy()[['ts','cp','piplead']]
    predictions_df['prediction'] = predictions_l
    predictions_df['eff'] = np.sign(predictions_df.prediction - 0.5) * predictions_df.piplead
    predictions_df['acc'] = (predictions_df.eff > 0)
    fn_s = "../csv/predictions_"+pair_s+str(1000+cnt_i)+".csv" 
    predictions_df.to_csv(fn_s, float_format='%4.4f', index=False)
    print(fn_s)

'bye'

