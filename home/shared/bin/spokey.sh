#!/bin/bash

# detects current mouse coordinates
export MOUSEX=`xdotool getmouselocation | awk '{print $1}' | sed -e 's/^x://'`
export MOUSEY=`xdotool getmouselocation | awk '{print $2}' | sed -e 's/^y://'`

# detects Spotify tray icon coordinates
export TRAY=`wmctrl -l -p | grep "lateral superior" | awk '{print $1}'`
export SPTFP=`xwininfo -id $TRAY -tree | grep "explorer.exe" | awk '{print $8}'`
export SPTFX=`echo $SPTFP | awk -F "+" '{print $2+=9}'`
export SPTFY=`echo $SPTFP | awk -F "+" '{print $3+=12}'`

# moves mouse to Spotify tray icon and simulates right click
xte "mousemove $SPTFX $SPTFY" "mousedown 3" "mouseup 3"

# waits for menu to open
sleep 0.01

# generates new X position
let NSPTFX=$SPTFX+50

# generates new Y position
let NSPTFY=$SPTFY+15
case $1 in
	'open')
		desp=30
		;;	

	'play')
		desp=60
		;;

	'stop')
		desp=60
		;;	

	'next')
		desp=80
		;;

	'prev')
		desp=100
		;;
esac

NSPTFY=$((NSPTFY + desp))

# moves mouse to menu item an simulates left click
xte "mousemove $NSPTFX $NSPTFY" "mousedown 1" "mouseup 1"

# restores previous mouse coordinates
xte "mousemove $MOUSEX $MOUSEY"
