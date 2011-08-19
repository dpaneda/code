#!/bin/zsh
mkdir -p ~/.old_config/.config

function link_with_backup {
    config=$1
    backup_dir=$2

    if [ -L ~/$config ]
    then
        echo "Already linked: $config"
        return
    elif [ ! -e $backup_dir/$config ] && [ -e ~/$config ]
    then
        echo "Backuping $config on $backup_dir" 
        mv ~/$config $backup_dir
    fi
    echo "Linking $config"
    ln -s $PWD/$config ~/$config
}

cd home
for config in .*
do
    # We .config dir because we don't want to link them itself
    [[ $config == ".config" ]] && continue
    link_with_backup $config ~/.old_config
done

for config in .config/*
do
    link_with_backup $config ~/.old_config/.config
done

# Also link shared dir
link_with_backup shared ~/shared

cd -
