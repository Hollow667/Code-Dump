echo "Starting Netcat Dump Client"
echo "==========================="

echo "[-] Creating tar ball"
tar cvf dumpNC.tar ./dump

read -p "ServerIP> " IP

echo "[-] Dumping tar ball"
nc -w 15 $IP 8080 < dumpNC.tar

echo "[-] Cleaning device"
rm -rf ./dump dumpNC.tar

echo "[-] Dumping operation complete"
