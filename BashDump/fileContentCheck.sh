#!/bin/bash
#################################################################################
# ActiveXperts Network Monitor - Shell script checks
#
# For more information about ActiveXperts Network Monitor and SSH, please
# visit the online ActiveXperts Network Monitor Shell Script Guidelines at:
#   http://www.activexperts.com/support/network-monitor/online/linux/
#################################################################################
# Script
#     file-content.sh
# Description
#     Checks the used space on a disk
# Parameters
#     1) sFilename (string)  - Path to file
#     2) sPattern (string)  - Pattern to match in the file
# Usage
#     file-content.sh sFilename sPattern
# Sample
#     file-content.sh /etc/hosts 127.0.0.1
#################################################################################

# Validate number of arguments
if [ $# -ne 2 ] ; then
  echo "UNCERTAIN: Invalid number of arguments - Usage: file-content sFilename sPattern"
  exit 1
fi

if [ ! -f "$1" ] ; then
  echo "UNCERTAIN: File [$1] does not exist"
  exit 0
fi 

nResult=0
nResult=`cat $1 | awk 'index(tolower($0),"'"$2"'")!=0 { print "1" ; }'`
if [ "$nResult" = "1" ] ; then
  echo "SUCCESS: File [$1] contains [$2] DATA:1"
else
  echo "ERROR: File [$1] does not contain [$2] DATA:0"	    
fi

exit 0
