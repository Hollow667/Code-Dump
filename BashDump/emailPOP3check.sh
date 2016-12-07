#!/bin/bash
#################################################################################
# ActiveXperts Network Monitor  - shell script checks
#
# For more information about ActiveXperts Network Monitor and SSH, please
# visit the online ActiveXperts Network Monitor Shell Script Guidelines at:
#   http://www.activexperts.com/support/network-monitor/online/linux/
#################################################################################
# Script
#     email-pop3.sh
# Description
#     Checks if the POP3 server is available
# Declare Parameters
#     1) sHost (string) - Host to check
# Usage
#     email-pop3.sh sHost
# Sample
#     email-pop3.sh pop3.activexperts.com
#################################################################################

# Validate number of arguments
if [ $# -ne 1 ] ; then
  echo "UNCERTAIN: Invalid number of arguments  Usage: email-pop3 host"
  exit 1
fi

# Check the connection
sNcOutput=`sleep 1 | nc $1 110 2>&1`
sOKResult=`echo $sNcOutput | sed -n 's/+OK/+OK/p'`
if [ "$sOKResult" = "" ]; then
  echo "ERROR: Failed to connect to [$1] DATA:0"
  exit 0
fi

echo "SUCCESS: +OK Response received from $1 DATA:1"
exit 0
