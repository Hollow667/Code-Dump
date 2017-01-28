#!/usr/bin/bash

filename="$1"
counter=$((1))
pre=$((1))

read -p "Start lines> " START
read -p "Sleep time> " SLEEP
read -p "Pre timer> " PRE
echo

while [[ $pre -le $PRE ]]
do
    printf "...$pre"
    pre=$((pre+1))
sleep 1
done

echo
echo

while read -r line
do
    if [[ $counter -lt $START ]]
    then
	name="$line"
	echo "$counter - $name"
	counter=$((counter+1))
    else
    	name="$line"
    	echo "$counter - $name"
    	counter=$((counter+1))
    	sleep $SLEEP
    fi
done < "$filename"
