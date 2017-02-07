#!/bin/bash

# truefx_get.bash

cd ~/fx411/
export PATH=${HOME}/fx411/bin:$PATH
# The script below should fail because it has wrong user/pass:
bin/rspec spec/features/truefx_spec.rb
# You should get account at truefx.com
# Next, you should enhance:
# bin/rspec spec/features/truefx_spec.rb
# Then,
# bin/rspec spec/features/truefx_spec.rb
# should succeed.
exit
