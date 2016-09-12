#!/bin/bash

telnet 4.ifcfg.me 2>&1 | grep IPv4 | cut -d' ' -f4
