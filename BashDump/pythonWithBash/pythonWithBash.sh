echo "Execute python script?"
echo
echo "[1] Yes"
echo "[2] No"
echo
read -p "> " ANSWER

if [ $((ANSWER)) -eq 1 ]
then
	python print.py
	exit
else
	exit
fi
