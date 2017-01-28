#!/bin/bash

POMODORO=1
CICLES=1

while :
do
    if [ $((POMODORO % 4)) -eq 0 ]; then
        echo "[+] Pomodoro $POMODORO START : $(date)"
        sleep 25m
        clear
        echo "[-] Pomodoro $POMODORO LONG BREAK num $CICLES : $(date)"
        sleep 15m
        clear
        let POMODORO=$POMODORO+1
        let CICLES=$CICLES+1
    else
        echo "[+] Pomodoro $POMODORO START : $(date)"
        sleep 25m
        clear
        echo "[-] Pomodoro $POMODORO BREAK : $(date)"
        sleep 5m
        clear
        let POMODORO=$POMODORO+1
    fi
done
