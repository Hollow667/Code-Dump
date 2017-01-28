#!/bin/bash

array[]
COUNTER=0

echo "[ ] My installs :"
echo "=================="
echo "[1] iptraf"
echo "[2] acpi"
echo "[3] tcptrack"
echo "[0] Start"

function install {
    for program in $1;
    do
        echo ${array[@]}
        sudo apt-get install $program
    done
}

while :
do
    read -p "Install> " ANSWER

    if [ $ANSWER = 0 ]; then
        install ${array[@]}
        exit 0
    fi
    
    if [ $ANSWER = 1 ]; then
        array[$COUNTER]=iptraf
        echo "[+] ${array[$COUNTER]}"
        let COUNTER=$COUNTER+1
    fi
    
    if [ $ANSWER = 2 ]; then
        array[$COUNTER]=acpi
        echo "[+] ${array[$COUNTER]}"
        let COUNTER=$COUNTER+1
       
    fi

    if [ $ANSWER = 3 ]; then
        array[$COUNTER]=tcptrack
        echo "[+] ${array[$COUNTER]}"
        let COUNTER=$COUNTER+1
    fi
done
