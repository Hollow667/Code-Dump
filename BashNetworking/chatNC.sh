echo "Netcat chat"
echo "==========="

PS3="Mode> "
OPTIONS=( "Server" "Client" "Exit" )

select OPT in "${OPTIONS[@]}"
do
    if [ $OPT = "Exit" ]; then
        echo "Terminating $0..."
        exit 0
    elif [ $OPT = "Server" ]; then
        echo "Initializing server mode"
        read -p "Port> " PORT
        awk -W interactive '$0="Server: "$0' | nc -l -p $PORT
    elif [ $OPT = "Client" ]; then
        echo "Initializing client mode"
        read -p "ServerIP> " IP
        read -p "ServerPORT> " PORT
        awk -W interactive '$0="Client: "$0' | nc $IP $PORT
    else
        echo "[!] Invalid option!"
    fi
done
