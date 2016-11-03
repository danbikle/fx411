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
echo 'export PATH="${HOME}/bin:$PATH"'        >> ~/.bashrc

bash

rbenv install 2.3.1; rbenv global  2.3.1; gem install bundler

Then, I clone fx411

git clone clone https://github.com/danbikle/fx411



