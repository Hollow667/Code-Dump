
#!/bin/bash
#################################################################################
# ActiveXperts Network Monitor - Shell script checks
#
# For more information about ActiveXperts Network Monitor and SSH, please
# visit the online ActiveXperts Network Monitor Shell Script Guidelines at:
#   http://www.activexperts.com/support/network-monitor/online/linux/
#################################################################################
# Script
#     disk-exists.sh
# Description
#     Checks the existence of a disk
# Declare Parameters
#     1) sDrive (string) - Mounted drive
# Usage
#     disk-exists.sh sDrive
# Sample
#     bash ./disk-exists.sh /dev/sda1
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

# Validate number of arguments
if [ $# -ne 1 ] ; then
  echo "UNCERTAIN: Invalid number of arguments - Usage: disk-exists sDrive"
  exit 1
fi

# Execute a command like this (assuming /dev/sda1). Note that slashes need to be escaped in AWK:
# df -T | awk '/\/dev\/sda1/ { print $1; }'
sDriveEsc=`echo $sDrive | sed 's/\//\\\\\//g'`        # e.g.: "\/dev\/sda1" <- "/dev/sda1"
sCommand="df -T | awk '/$sDriveEsc/ { print \$1; }'"  # e.g.: df -T | awk '/\/dev\/sda1/ { print $1; }'

# Get number of free blocks (1K)
sRetrievedDisk=`eval $sCommand`
if [ -z "$sRetrievedDisk" ]; then
  echo "ERROR: Disk $sDrive does not exist DATA:0"
else
  echo "SUCCESS: Disk $sDrive does exist DATA:1"
fi

exit 0
