#!/bin/zsh
# Script to see a series of pictures over http, as feh does not support ranges

for arg in $*
do
    dir=`mktemp -d`

    cd $dir
    curl -O $arg
    feh -F *
    cd -
done
