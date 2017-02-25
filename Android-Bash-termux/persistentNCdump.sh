echo "Starting Persistent Netcat Dump"
echo "==============================="

conection=1

echo "[-] Moving to sdcard"
cd /sdcard

echo "[-] Checking for persistentNC directory..."
if [ ! -d "persistentNC" ]
then
	echo "[-] Creating persistentNC directory"
	mkdir persistentNC
else
	echo "[-] Directory found"
fi

while :
do
	nc -l -p 8080 > persistentNC/dumpNC[$(date)].tar
	echo "Terminating conection [$conection] at $(date)" >> persistentNC/persistentNC.log
	echo "Terminating conection [$conection] at $(date)"
	let conection++
done
