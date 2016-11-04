readme.txt

Setup

I start setup of this repo by enhancing my copy of Ubuntu:

sudo apt-get update
sudo apt-get upgrade

sudo apt-get install autoconf bison build-essential libssl-dev libyaml-dev    \
libreadline6-dev zlib1g-dev libncurses5-dev libffi-dev libgdbm3  sqlite3 curl \
libgdbm-dev libsqlite3-dev gitk postgresql postgresql-server-dev-all aptitude \
libpq-dev emacs wget openssh-server ruby ruby-dev libbz2-dev linux-headers-$(uname -r) \
r-base r-base-dev

Then, I create a Linux account:

sudo useradd -m -s /bin/bash -G sudo fx411
sudo passwd fx411

After I create fx411, I should login to that account and do my work from there.

Next, I install Ruby:

cd /home/fx411/
git clone https://github.com/rbenv/rbenv.git      .rbenv
git clone https://github.com/rbenv/ruby-build.git .rbenv/plugins/ruby-build
echo 'export PATH="${HOME}/.rbenv/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(rbenv init -)"'                 >> ~/.bashrc
echo 'export PATH="${HOME}/fx411/bin:$PATH"'  >> ~/.bashrc

bash

rbenv install 2.3.1; rbenv global  2.3.1; gem install bundler

Then, I clone the fx411 repo:

git clone clone https://github.com/danbikle/fx411
cd /home/fx411/fx411/

Next, I use the bundle command to get fx411-ruby-gems from the web:

bundle install

Then, I should get an account at truefx.com

Next, I enhance /home/fx411/fx411/spec/features/truefx_spec.rb so it has my truefx account info.

Then, I get data from truefx.com with simple shell commands:

cd /home/fx411/
mkdir -p truefx csv
cd /home/fx411/fx411/
bin/rspec spec/features/truefx_spec.rb

The above script should take many hours to run if I use it to download many pairs and months.

The way it is currently written, it should finish in less than five minutes.

The CSV files should appear in this folder:

/home/fx411/Downloads/

I should move them to /home/fx411/truefx/ with these shell commands:

mkdir /home/fx411/truefx/
mv /home/fx411/Downloads/*USD*20*.zip /home/fx411/truefx/

Then, I should install Anaconda Python with these shell commands:

cd /home/fx411/Downloads/
wget https://repo.continuum.io/archive/Anaconda3-4.2.0-Linux-x86_64.sh
bash Anaconda3-4.2.0-Linux-x86_64.sh
echo 'export PATH="${HOME}/anaconda3/bin:$PATH"' >> ~/.bashrc
mv ~/anaconda3/bin/curl  ~/anaconda3/bin/curl_ana
bash





