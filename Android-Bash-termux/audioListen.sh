filename=$1
content=`cat $filename`
espeak -a199 -v croak -s150 -w tmpAudio "Vocalizing the $filename file."
mpv tmpAudio
espeak -a199 -v croak -s150 -w tmpAudio "$content"
mpv tmpAudio
espeak -a199 -v croak -s150 -w tmpAudio "End of file, terminating."
mpv tmpAudio
rm tmpAudio
