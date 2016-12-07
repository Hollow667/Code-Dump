
#################################################################################
# ActiveXperts Network Monitor - Shell script checks
#
# For more information about ActiveXperts Network Monitor and SSH, please
# visit the online ActiveXperts Network Monitor Shell Script Guidelines at:
#   http://www.activexperts.com/support/network-monitor/online/linux/
#################################################################################
# Script
#     user-exists.sh
# Description
#     This script will check if a user account exists
# Declare Parameters
#     1) sUsername (string) - Username to check
# Usage
#     user-exists.sh sUsername
# Sample
#     user-exists.sh axuser
#################################################################################

#!/bin/sh

# Validate number of arguments
if [ $# -ne 1 ] ; then
  echo "UNCERTAIN: Invalid number of arguments - Usage: user-exists sUsername"
  exit 1
fi

# Checks if the user exists
if id -u $1 >/dev/null 2>&1; then
  echo "SUCCESS: User exists DATA:1" 
else
  echo "ERROR: User does not exist DATA:0"
fi

