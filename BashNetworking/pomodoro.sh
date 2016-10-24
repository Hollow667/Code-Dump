#!/bin/bash

POMODORO=$((1))
CICLES=$((1))

while :
do
    # If you finished 4, 8, 16 pomodoro's you get a long 15 min break
    if [ $((POMODORO % 4)) -eq 0 ]
    then

    echo "        _             _   
    ___| |_ __ _ _ __| |_ 
   / __| __/ _  | '__| __| 
===\__ \ || (_| | |  | |_  ===== Pomodoro $((POMODORO)) START =====
===|___/\__\__,_|_|   \__| $(date)"
    sleep 1500 #25 minutes
    echo "    _                    _    
   | |__  _ __ ___  __ _| | __
   | '_ \| '__/ _ \/ _  | |/ / 
===| |_) | | |  __/ (_| |   <  Pomodoro $((POMODORO)) LONG BREAK num $((CICLES)) 
===|_.__/|_|  \___|\__,_|_|\_\ $(date)"
    sleep 900 #15 minutes
    POMODORO=$((POMODORO+1))
    CICLES=$((CICLES+1))

    else
    # If not, you get a short 5 min break
    echo "        _             _   
    ___| |_ __ _ _ __| |_ 
   / __| __/ _  | '__| __| 
===\__ \ || (_| | |  | |_  ===== Pomodoro $((POMODORO)) START =====
===|___/\__\__,_|_|   \__| $(date)"
    sleep 1500 #25 minutes
    echo "    _                    _    
   | |__  _ __ ___  __ _| | __
   | '_ \| '__/ _ \/ _  | |/ / 
===| |_) | | |  __/ (_| |   <  ===== Pomodoro $((POMODORO)) BREAK =====
===|_.__/|_|  \___|\__,_|_|\_\ $(date)"
    sleep 300 #5 minutes
    POMODORO=$((POMODORO+1))

fi
done 

