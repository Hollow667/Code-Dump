#!/bin/bash

#echo "File title :"
read -p "File title> " TITLE

#echo "Line length :"
read -p "Line length> " LENGTH

#echo "Number of tabs :"
read -p "Number of tabs> " TABS


z=1

echo
echo "    $TITLE"
echo "    $(date)"
echo

while [ $z -le $TABS ]
do
	for ((a=0;a<=6;a++))
	do
		for ((i=0;i<=$LENGTH;i++))
		do
			printf -
		done
		echo
	done
	echo
	((z++))
done


