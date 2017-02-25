#!/bin/bash

espeak -a 199 -v croak -s 150 -w tmpAudio "Initiating secure copy backup to home device."
mpv tmpAudio
scp -P 22 ./* user@<ip address>:./dump
espeak -a 199 -v croak -s 150 -w tmpAudio "All files succesfully transfered, terminating." 
# removing from device."
mpv tmpAudio
# rm ./*
