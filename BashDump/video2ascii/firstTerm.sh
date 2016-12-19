#!/bin/bash

read -p "VideoPath> " PATH

mplayer -vo jpeg -x 640 -y 480 -ni -fps 5 $PATH
