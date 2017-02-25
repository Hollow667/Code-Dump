#!/data/data/com.termux/files/usr/bin/bash

espeak -a199 -v croak -s150 -w tmpAudio "Initiating local area ping sweep. Please stand by."
mpv tmpAudio

nmap -o lanscan.txt -sn 192.168.0.1/24
cat lanscan.txt | grep 192.168.0.1 | cut -d' ' -f5 > hosts.txt
cat hosts.txt | wc -l hosts.txt | cut -d' ' -f0 > count.txt
rm lanscan.txt

echo "$(cat count.txt) minus one hot machines discovered" | espeak -a 199 -v croak -s150 -w tmpAudio
mpv tmpAudio
rm count.txt
espeak -a 199 -v croak -s150 -w tmpAudio "The following Local Area hosts are active"
mpv tmpAudio

cat hosts.txt | espeak -a 199 -v croak -s150 -w tmpAudio 
mpv tmpAudio

#############################################
# PORT SCANNING
##########################

echo "Initiating top port scan for previously listed machines." | espeak -a199 -v croak -s150 -w tmpAudio
mpv tmpAudio
nmap -o ports.txt -top-ports 1000 `cat hosts.txt | grep 192.168.0.1`
cat ports.txt | grep -e report -e all -e tcp | espeak -a199 -v croak -s150 -w tmpAudio
mpv tmpAudio

espeak -a199 -v croak -s150 -w tmpAudio "Objective achieved. Terminating script."
mpv tmpAudio
rm tmpAudio
