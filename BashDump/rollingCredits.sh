
filename=$1

while read line
do
    echo $line
    sleep 0.1
done < $filename
