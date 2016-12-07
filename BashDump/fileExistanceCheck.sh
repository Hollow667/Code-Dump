#################################################################################
# ActiveXperts Network Monitor - Shell script checks
#
# For more information about ActiveXperts Network Monitor and SSH, please
# visit the online ActiveXperts Network Monitor Shell Script Guidelines at:
#   http://www.activexperts.com/support/network-monitor/online/linux/
#################################################################################
# Script
#     file_exists.sh
# Description
#     Checks the used space on a disk
# Declare Parameters
#     1) sFileName (string) - Path to file
# Usage
#     file_exists.sh sFileName
# Sample
#     file_exists.sh test.sh
#################################################################################

#!/bin/sh

# Validate number of arguments
if [ $# -ne 1 ] ; then
  echo "UNCERTAIN: Invalid number arguments - Usage: file_exists sFileName"
  exit 1
fi

# Check if the specified file exists
if [ -f "$1" ] ; then
  echo "SUCCESS: File [$1] exists DATA:1"
else
  echo "ERROR: File [$1] does not exist DATA:0"
fi

    
