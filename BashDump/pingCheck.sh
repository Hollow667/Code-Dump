#!/bin/bash
#################################################################################
# ActiveXperts Network Monitor - Shell script checks
#
# For more information about ActiveXperts Network Monitor and SSH, please
# visit the online ActiveXperts Network Monitor Shell Script Guidelines at:
#   http://www.activexperts.com/support/network-monitor/online/linux/
#################################################################################
# Script
#     ping.sh
# Description
#     Tries to ping a host
# Declare Parameters
#     1) sHost (string) - Host to ping
# Usage
#     ping.sh sHost
# Sample
#     ping.sh activexperts.com
#################################################################################


# Validate number of arguments
if [ $# -ne 1 ] ; then
  echo "UNCERTAIN: Invalid number of arguments  Usage: ping "
  exit 1
fi

ping $1 -c1 &> /dev/null
if [ $? -eq 0 ] ; then
  echo "SUCCESS: Ping successful, packet sent 1, received 1, lost 0 DATA:1"
else
  echo "ERROR: Ping failed, packet sent 1, received 0, lost 1 DATA:0"
fi


    
