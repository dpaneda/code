#!/bin/zsh
# Script to see a series of pictures over http, as feh does not support ranges

cd /tmp
for arg in $*
do
    dir=`md5sum <<<"$arg"`

    if [ -d $dir ]
    then
        cd $dir
    else
        mkdir -p $dir
        cd $dir
        curl -O $arg
    fi

    feh -F *
done
cd -
