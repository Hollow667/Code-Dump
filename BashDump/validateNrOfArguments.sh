#!/bin/bash
# Validate number of arguments
if [ $# -ne 2 ] ; then
  echo "UNCERTAIN: Invalid number of arguments - Usage: directory-size sDirectory nMaxSizeMB"
  exit 1
fi

# Validate numeric parameter nMaxSizeMB
regExpNumber='^[0-9]+$'
if ! [[ $2 =~ $regExpNumber ]] ; then
  echo "UNCERTAIN: Invalid argument: nMaxSizeMB (number expected)"
  exit 1
fi

# Check the size of the directory specified
if [ ! -d "$1" ]; then
  echo "UNCERTAIN: Directory [$1] does not exist"
  exit 0
fi

nSizeKB=`du -s "$1" | awk '{ print $1; }'`
nSizeMB=$( echo "$nSizeKB / 1024" | bc )

# Round a float to an integer value
nRoundSizeMB=$( echo "$nSizeMB / 1" | bc )

# Round a float to an integer value
nRoundMaxMB=$( echo "$2 / 1" | bc )

if [ $nRoundSizeMB -le $nRoundMaxMB ] ; then
  echo "SUCCESS: Size=[$nRoundSizeMB MB], max. allowed=[$nRoundMaxMB MB] DATA:$nRoundSizeMB"
else
  echo "ERROR: Size=[$nRoundSizeMB MB], max. allowed=[$nRoundMaxMB MB] DATA:$nRoundSizeMB"
fi

exit 0
