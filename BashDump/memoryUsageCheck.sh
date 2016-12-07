#################################################################################
# ActiveXperts Network Monitor - Shell script checks
#
# For more information about ActiveXperts Network Monitor and SSH, please
# visit the online ActiveXperts Network Monitor Shell Script Guidelines at:
#   http://www.activexperts.com/support/network-monitor/online/linux/
#################################################################################
# Script
#     memory.sh
# Description
#     Checks memory usage on the computer.
# Declare Parameters
#     1) nMaxMemoryUsage (number) - maximum allowed CPU usage (%)
# Usage
#     memory.sh nMaxMemoryUsage
# Sample
#     memory.sh 80
#################################################################################

nMaxMemoryUsage=$1

# Validate number of arguments
if [ $# -ne 1 ] ; then
  echo "UNCERTAIN: Invalid number of arguments - Usage: memory nMaxMemoryUsage"
  exit 1
fi

# Validate numeric parameter nMaxMemoryUsage
regExpNumber='^[0-9]+$'
if ! [[ $1 =~ $regExpNumber ]] ; then
  echo "UNCERTAIN: Invalid argument: nMaxMemoryUsage (number expected)"
  exit 1
fi

# Check the memory usage
nMemoryPercentage=`ps -A -o pmem | tail -n+2 | paste -sd+ | bc`
nMemoryPercentage=$( echo "$nMemoryPercentage / 1" | bc )

if [ $nMemoryPercentage -le $nMaxMemoryUsage ] ; then
  echo "SUCCESS: Memory usage is [$nMemoryPercentage%], minimum allowed=[$1%] DATA:$nMemoryPercentage"
else
  echo "ERROR: Memory usage is [$nMemoryPercentage%], minimum allowed=[$1%] DATA:$nMemoryPercentage"
fi
 
exit 0
