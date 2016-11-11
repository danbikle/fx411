#!/bin/bash

# runem.bash

# This script should run some python scripts in the correct order.

# Actually I start with a Ruby script but I comment it out.

# I need to edit it first and place a username and password in it which will work on the truefx.com website.
# It is easy to get one, just visit this url:
# https://truefx.com/?page=register

# cd ~fx411/fx411/
# bin/rspec spec/features/truefx_spec.rb
# After I enhance the above script with user/pass, I should run it.
# The above script should take a long time.

# Then AFTER I run truefx_spec.rb, I should run runem.bash (the script you are looking at).

# The above ruby script should download many zip files into ~fx411/Downloads/
# I should do this next:
mkdir -p  ~fx411/csv                    ~fx411/truefx
rsync -av ~fx411/Downloads/*USD*20*.zip ~fx411/truefx

# I should cd to the right place
cd ~fx411/fx411/script/

# I should aggregate data into CSV files which are easier to learn from:
~/anaconda3/bin/python agg_zip.py
# The above script should take a long time.
~/anaconda3/bin/python agg_csv.py

# I should generate features:
~/anaconda3/bin/python genf.py

# I should generate models/predictions from features:
~/anaconda3/bin/python learn_tst_rpt_random.py
# The above script should take a long time.

# I should report predictions effectiveness sum, grouped by pair and training size:
~/anaconda3/bin/python rpt.py

exit

