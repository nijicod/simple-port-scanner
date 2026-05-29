# simple-port-scanner

lol idk i was bored and wanted to write sum
This is just a basic TCP port scanner built in Python using the `socket` library. It hits a target IP on a few specific ports to see if anything is listening, kind of like a mini Nmap.

## How it works
It tries to initiate a quick TCP handshake with the target. If `connect_ex()` returns a `0`, the port is open and listening. If it returns anything else, the port is closed or blocked.

## Features
* No external libraries needed (just standard Python `socket` and `sys`).
* Has a 1-second timeout so it doesn't hang forever.
* You can kill it instantly with `Ctrl + C`.

## How to use
1. download the code and open it in vs or whatever
2. edit the script to change the `target` IP and the `ports_to_scan` list to whatever you want.
3. Run code
