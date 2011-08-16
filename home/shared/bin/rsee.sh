#!/bin/zsh
# Script to see a series of pictures over http, as feh does not support ranges

dir=`mktemp -d`

cd $dir
curl -O $*
feh -F *
cd -
