echo "This is a multiple choice menu :"
echo
echo "[1] Option"
echo "[2] Option"
echo "[3] Option"
echo

read -p "> " OPTION

if [ $((OPTION)) -eq 1 ]
then
	echo "You chose Option 1"
	echo "Continue?"
	echo
	echo "[1] Yes"
	echo "[2] No"
	echo
	read -p "> " OPTION2
	if [ $((OPTION2)) -eq 1 ];
	then
		echo "You chose to continue."
		echo "Well fuck off, I dont have time for this shit."
		exit
	else
		exit
	fi
fi

if [ $((OPTION)) -eq 2 ]
then
	echo "You chose option 2"
	echo "Continue?"
	echo
	echo "[1] Yes"
	echo "[2] No"
	echo
	read -p "> " OPTION2
	if [ $((OPTION2)) -eq 1 ];
	then
		echo "You chose to continue."
		echo "Well fuck off, I dont have time for this shit."
		exit
	else
		exit
	fi
fi

if [ $((OPTION)) -eq 3 ]
then
	echo "You chose option 3"
	echo "Continue?"
	echo
	echo "[1] Yes"
	echo "[2] No"
	echo
	read -p "> " OPTION2
	if [ $((OPTION2)) -eq 1 ];
	then
		echo "You chose to continue."
		echo "Well fuck off, I dont have time for this shit."
		exit
	else
		exit
	fi
fi
