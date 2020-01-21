#!/usr/bin/python3

import os

os.system("ip a")
ip_add=input("Enter the Network IP address of the system : ")

os.system("chattr -i /etc/resolv.conf")
os.system("rm -f /etc/resolv.conf")
os.system('echo "domain	example.com" >>/etc/resolv.conf')
os.system('echo "search	example.com" >> /etc/resolv.conf')
os.system('echo "nameserver	%s" >> /etc/resolv.conf'%ip_add)

f=open("/etc/hostname","w+")
f.write("client1")
f.close()

f=open("/etc/hosts","a+")
f.write("%s	client1.example.com	client1"%ip_add)
f.close()
os.system("chattr +i /etc/resolv.conf")
os.system("reboot")
