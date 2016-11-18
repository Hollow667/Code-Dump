#!/usr/bin/bash
filename="$1"
counter=$((1))
while read -r line
do
    name="$line"
    echo "$counter - $name"
    counter=$((counter+1))
    sleep 1
done < "$filename"
