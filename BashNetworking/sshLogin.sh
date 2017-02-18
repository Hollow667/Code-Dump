#!/usr/bin/expect

spawn ssh username@127.0.0.1
expect "username@127.0.0.1's password"
send "password\r"
interact
