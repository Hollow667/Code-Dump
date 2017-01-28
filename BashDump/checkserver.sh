#!/bin/bash

is_alive_ping()
{
  ping -c 1 $1 > /dev/null
  [ $? -eq 0 ] && echo "$(date) : Node [ $1 ] : is UP."
  sleep 2
}

while :
do
    is_alive_ping $1
done
