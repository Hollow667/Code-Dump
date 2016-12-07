
#!/bin/bash
#################################################################################
# ActiveXperts Network Monitor - Shell script checks
# � 1999-2016, ActiveXperts Software B.V.
#
# For more information about ActiveXperts Network Monitor and SSH, please
# visit the online ActiveXperts Network Monitor Shell Script Guidelines at:
#   http://www.activexperts.com/support/network-monitor/online/linux/
#################################################################################
# Script
#     disk-used-mb.sh
# Description
#     Checks the available free space on a disk
# Declare Parameters
#     1) sDrive (string) - Mounted drive
#     2) nMaxUsedMB (number) - Maximum used space
# Usage
#     disk-used-mb.sh sDrive nMaxUsedMB
# Sample
#     bash ./disk-used-mb.sh /dev/sda1 1000
#################################################################################

# This script is based on the 'df' command
# df -T output is like this:
# Filesystem     Type     1K-blocks    Used Available Use% Mounted on
# udev           devtmpfs   2001860       0   2001860   0% /dev
# tmpfs          tmpfs       403844   26368    377476   7% /run
# /dev/sda1      ext4     126820132 3797080 116557928   4% /
# tmpfs          tmpfs      2019208     156   2019052   1% /dev/shm
# tmpfs          tmpfs         5120       0      5120   0% /run/lock
# tmpfs          tmpfs      2019208       0   2019208   0% /sys/fs/cgroup
# cgmfs          tmpfs          100       0       100   0% /run/cgmanager/fs
# tmpfs          tmpfs       403844      64    403780   1% /run/user/1000


sDrive=$1
nMaxUsedMB=$2

# Validate number of arguments
if [ $# -ne 2 ] ; then
  echo "UNCERTAIN: Invalid number of arguments - Usage: disk-used-mb sDrive nMaxUsedMB"
  exit 1
fi

# Validate numeric parameter nMaxUsedMB
regExpNumber='^[0-9]+$'
if ! [[ $2 =~ $regExpNumber ]] ; then
  echo "UNCERTAIN: Invalid argument: nMaxUsedMB (number expected)"
  exit 1
fi

# Execute a command like this (assuming /dev/sda1). Note that slashes need to be escaped in AWK:
# df -T | awk '/\/dev\/sda1/ { print $5; }'
sDriveEsc=`echo $sDrive | sed 's/\//\\\\\//g'`        # e.g.: "\/dev\/sda1" <- "/dev/sda1"
sCommand="df -T | awk '/$sDriveEsc/ { print \$4; }'"  # e.g.: df -T | awk '/\/dev\/sda1/ { print $4; }'

# Get number of free blocks (1K)
nBlocksUsed=`eval $sCommand`
if [ -z "$nBlocksUsed" ]; then
  echo "UNCERTAIN: Drive [$sDrive] does not exist"
  exit 1
fi

# Get number of used MB (assuming a block is 1K)
let nMBUsed="nBlocksUsed/1024"

# Print final result. ActiveXperts will interpret the line, expected format is like this:
# [SUCCESS|ERROR|UNCERTAIN]  DATA:[]
if [ $nMBUsed -le $nMaxUsedMB ] ; then
  echo "SUCCESS: Used disk space on drive $sDrive=[$nMBUsed MB], maximum allowed=[$nMaxUsedMB MB] DATA:$nMBUsed"
else
  echo "ERROR: Used disk space on drive $sDrive=[$nMBUsed MB], maximum allowed=[$nMaxUsedMB MB] DATA:$nMBUsed"
fi	

# Exit script
exit 0
