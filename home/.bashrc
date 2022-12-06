# ~/.bashrc: executed by bash(1) for non-login shells.
# see /usr/share/doc/bash/examples/startup-files (in the package bash-doc)
# for examples

# If not running interactively, don't do anything
[ -z "$PS1" ] && return

# don't put duplicate lines in the history. See bash(1) for more options
export HISTCONTROL=ignoredups
# ... and ignore same sucessive entries.
export HISTCONTROL=ignoreboth

# check the window size after each command and, if necessary,
# update the values of LINES and COLUMNS.
shopt -s checkwinsize

# make less more friendly for non-text input files, see lesspipe(1)
[ -x /usr/bin/lesspipe ] && eval "$(lesspipe)"

# set variable identifying the chroot you work in (used in the prompt below)
if [ -z "$debian_chroot" ] && [ -r /etc/debian_chroot ]; then
    debian_chroot=$(cat /etc/debian_chroot)
fi

# set a fancy prompt (non-color, unless we know we "want" color)
case "$TERM" in
xterm-color)
    PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '
    ;;
*)
    PS1='${debian_chroot:+($debian_chroot)}\u@\h:\w\$ '
    ;;
esac

# Comment in the above and uncomment this below for a color prompt
#PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '

# If this is an xterm set the title to user@host:dir
case "$TERM" in
xterm*|rxvt*)
    PROMPT_COMMAND='echo -ne "\033]0;${USER}@${HOSTNAME}: ${PWD/$HOME/~}\007"'
    ;;
*)
    ;;
esac

# Alias definitions.
# You may want to put all your additions into a separate file like
# ~/.bash_aliases, instead of adding them here directly.
# See /usr/share/doc/bash-doc/examples in the bash-doc package.

#if [ -f ~/.bash_aliases ]; then
#    . ~/.bash_aliases
#fi

# enable color support of ls and also add handy aliases
if [ "$TERM" != "dumb" ]; then
    #eval "`dircolors -b $HOME/.dircolors`"
    alias ls='ls --color=auto'
    #alias dir='ls --color=auto --format=vertical'
    #alias vdir='ls --color=auto --format=long'
fi

# some more ls aliases
alias ll='exa -l'
alias la='ls -A'
alias l='exa'
alias vi='vim'
alias tree='exa --tree'

# enable programmable completion features (you don't need to enable
# this, if it's already enabled in /etc/bash.bashrc and /etc/profile
# sources /etc/bash.bashrc).
if [ -f /etc/bash_completion ]; then
    . /etc/bash_completion
fi

# Fullscreen only on one monitor
export SDL_VIDEO_FULLSCREEN_HEAD=1
PATH=$PATH:/home/daniel/private_code/go/bin
PATH=$PATH:/home/daniel/go/bin
PATH=$PATH:/home/daniel/bin
PATH=$PATH:/home/daniel/.gem/ruby/1.9.1/bin
export PATH

# Fix to mouse problem on dosbox
export SDL_VIDEO_X11_DGAMOUSE=0

function ranger-cd {
  ranger --choosedir=/tmp/chosen
  if [ -f /tmp/chosen -a "$(cat /tmp/chosen)" != "$(pwd | tr -d "\n")" ]; then
    cd "$(cat /tmp/chosen)"
  fi
  rm -f /tmp/chosen
}
bind '"\C-o":"ranger-cd\C-m"'

alias dotags="ctags-exuberant -f tags -h \".php\" -R --exclude=\"\.hg\" --totals=yes --tag-relative=yes --PHP-kinds=+cf --regex-PHP='/abstract class ([^ ]*)/\1/c/' --regex-PHP='/interface ([^ ]*)/\1/c/' --regex-PHP='/(public |static |a    bstract |protected |private )+function ([^ (]*)/\2/f/'"
alias rgrep="grep -r"
alias cal="LC_ALL=es_ES.UTF-8 cal"

export EDITOR=vim

export MANPAGER="sh -c 'col -bx | bat -l man -p'"

# hdpi stuff
export GDK_SCALE=2
export QT_AUTO_SCREEN_SCALE_FACTOR=1
alias spotify="spotify --force-device-scale-factor=1.75"
alias pycharm="GDK_SCALE=1 pycharm"

export SSH_AUTH_SOCK=/run/user/1000/ssh-agent.socket

source /opt/google-cloud-sdk/completion.bash.inc

eval "$(direnv hook bash)"

function bpi {
    awk -F: ' \
    /^Block count:/ { blocks = $2 } \
    /^Inode count:/ { inodes = $2 } \
    /^Block size:/ { block_size = $2 } \
    END { blocks_per_inode = blocks/inodes; \
          print "blocks per inode:\t", blocks_per_inode, \
                "\nbytes per inode:\t", blocks_per_inode * block_size }'
}
