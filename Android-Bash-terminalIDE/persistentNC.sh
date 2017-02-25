echo "Starting Persistent Netcat Listener"
echo "==================================="

conection=1

echo "[-] Moving to sdcard"
cd ~/sdcard

echo "[-] Creating persistentNC directory"
mkdir persistentNC

while :
do
	nc -l -p 8080 >> persistentNC/persistentNC.dump
	echo "Terminating conection [$conection] at $(date)" >> persistentNC/persistentNC.log
	echo "Terminating conection [$conection] at $(date)"
	let conection++
done

