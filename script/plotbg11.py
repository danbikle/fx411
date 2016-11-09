# plotbg11.py

# This script should transform a csv file into a DataFrame and then into blue-green-visualization.

import pandas as pd
import matplotlib.pyplot as plt
import pdb

# I should get the filename from the command line.

# I should check cmd line args
import sys
if (len(sys.argv) != 2):
  print('You typed something wrong:')
  print('Demo:')
  print("~/anaconda3/bin/python plotbg11.py ../csv/predictions31000AUDUSD.csv")
  sys.exit()

csv_s = sys.argv[1]
p0_df  = pd.read_csv(csv_s, names=['ts','cp','piplead','problr','eff','acc'])
print(p0_df.head())

'bye'
