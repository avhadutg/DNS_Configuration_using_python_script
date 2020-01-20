#!/usr/bin/python3

import os

os.system("ip a")
ip_add=input("Enter the Network IP Address of the system : ")
os.system("apt install bind9 dnsutils -y")
f=open("/etc/bind/db.local","a+")
f.write("master	IN	A	%s\r\n"%ip_add)
f.close()
f=open("/etc/bind/named.conf.local","a+")
f.write('zone "example.com"{\r\n')
f.write("	type master;\r\n")
f.write('	file "/etc/bind/db.local";\r\n')
f.write("};")
f.close()

os.system("chattr -i /etc/resolv.conf")
os.system("rm -f /etc/resolv.conf")
os.system('echo "domain	example.com">>/etc/resolv.conf')
os.system('echo "search	example.com">>/etc/resolv.conf')
os.system('echo "nameserver	%s">>/etc/resolv.conf'%ip_add)

f=open("/etc/hostname","w+")
f.write("master")
f.close()

f=open("/etc/hosts","a+")
f.write("%s	master.example.com	master"%ip_add)
f.close()

os.system("/etc/init.d/bind9 restart")
os.system("chattr +i /etc/resolv.conf")
os.system("reboot")
os.system("host master")
