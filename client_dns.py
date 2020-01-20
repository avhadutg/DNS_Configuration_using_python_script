#!/usr/bin/python3

import os

ip_add=input("Enter the Client System IP address : ")
f=open("/etc/bind/db.local","a+")
f.write("client1	IN	A	%s\r\n"%ip_add)
f.close()

os.system("/etc/init.d/bind9 restart")
os.system("ping client1")
