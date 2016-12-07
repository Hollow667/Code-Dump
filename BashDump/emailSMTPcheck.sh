
#################################################################################
# ActiveXperts Network Monitor - Shell script checks
#
# For more information about ActiveXperts Network Monitor and SSH, please
# visit the online ActiveXperts Network Monitor Shell Script Guidelines at:
#   http://www.activexperts.com/support/network-monitor/online/linux/
#################################################################################
# Script
#     email-smtp.sh
# Description
#     Checks if the SMTP server is available
# Declare Parameters:
#     1) sHost (string) - Host to check
# Usage
#     email-smtp.sh sHost
# Sample
#     email-smtp.sh smtp.activexperts.com
#################################################################################

#!/bin/sh

# Validate number of arguments
if [ $# -ne 1 ] ; then
  echo "UNCERTAIN: Invalid number of arguments  Usage: email-smtp host"
  exit 1
fi

# Check the connection
sNcOutput=`sleep 1 | nc $1 25 2>&1`
sOKResult=`echo $sNcOutput | sed -n 's/220/220/p'`
if [ "$sOKResult" = "" ]; then
  echo "ERROR: Failed to connect to [$1] DATA:0"
  exit 0
fi

echo "SUCCESS: 220 Response received from $1 DATA:1"
exit 0
