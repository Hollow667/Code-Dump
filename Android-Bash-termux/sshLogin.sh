#!/usr/bin/expect

spawn ssh user@127.0.0.1
expect "user@127.0.0.1's password"
send "mypassword\r"
interact
