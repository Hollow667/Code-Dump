#!/bin/bash

while true :
do
    cat log | uniq -u > log
    netstat | grep ESTABLISHED >> log
    echo $(date) >> dump
    cat log | uniq -u >> dump
    cat log | uniq -u
    sleep 3
    clear
done
