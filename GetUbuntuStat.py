#!/usr/bin/python3
# coding: UTF-8

import subprocess

def print_result(item, result):
    num_lines = result.count("\n")
    print("====================================================================================================")
    if isinstance(result, list):
        print(item + ":")
        for result_in_list in result:
            print(result_in_list)
        print("")

    elif num_lines == 0:
        print(item + ":" + result.strip() + "\n")
    else:
        print(item + ":")
        print(result.strip() + "\n")

print("====================================================================================================")
print("---------------------------------Get Server Status for UbuntuServer---------------------------------")

hostname = subprocess.getoutput("hostname")
print_result("Hostname", hostname)

version = subprocess.getoutput("cat /proc/version")
print_result("Version", version)

uptime = subprocess.getoutput("uptime")
print_result("Uptime", uptime)

users = subprocess.getoutput("users")
print_result("Login Users", users)

last = subprocess.getoutput("last | egrep -v '^wtmp begin' | head -10")
print_result("Last Logins", last)

vmstat = subprocess.getoutput("vmstat 1 5")
print_result("VMStat", vmstat)

free = subprocess.getoutput("free -h")
print_result("Free", free)

free_list = (subprocess.getoutput("free")).split()
if int(free_list[12]) / int(free_list[7]) <= 0.2:
    print("WARNING:Memory usage too high.\n")

try:
    if int(free_list[16]) / int(free_list[15]) <= 0.5:
        print("WARNING:Swap usage too high.\n")
except ZeroDivisionError:
    pass

df = subprocess.getoutput("df -h")
print_result("Disk Usage", df)
df_list = df.split("\n")
del df_list[0]
for i in df_list:
    df_split = i.split()
    if int((df_split[4])[0:-1]) >= 80:
        print("WARNING:Filesystem " + df_split[0] + " usage too high.\n")

fdisk = subprocess.getoutput("fdisk -l")
print_result("Disk Information", fdisk)

netstatr = subprocess.getoutput("netstat -r")
print_result("Routing Information", netstatr)

iplink = subprocess.getoutput("ip link")
print_result("Network Interfaces", iplink)

ssltn = subprocess.getoutput("ss -ltn4")
print_result("Listen Port", ssltn)
ssltn_list = ssltn.split("\n")
del ssltn_list[0]
for i in ssltn_list:
    ssltn_split = i.split()
    ssltn_addressport = ssltn_split[3].split(":")
    lsof = subprocess.getoutput("lsof -i:" + ssltn_addressport[1] + " | grep -v ^COMMAND")
    print(lsof)

print("")

psaux = subprocess.getoutput("ps -aux --sort s | head -20")
print_result("Top 20 Processes", psaux)

netstati = subprocess.getoutput("netstat -i")
print_result("Interface Status", netstati)

ifconfig = subprocess.getoutput("ifconfig")
print_result("Ifconfig", ifconfig)

netstataon = subprocess.getoutput('netstat -aon | egrep "^Active Internet connections|^Proto Recv-Q|^tcp|^tcp6|^udp"')
print_result("Netstat", netstataon)

vmstatd = subprocess.getoutput("vmstat -d")
print_result("Disk Status", vmstatd)

cpunum = subprocess.getoutput("cat /proc/cpuinfo | grep -w ^processor | wc -l")
print_result("CPU Number", cpunum)

cpumodels = subprocess.getoutput('cat /proc/cpuinfo | grep "model name" | cut -d ":" -f 2 | sort | uniq')
print_result("CPU Model", cpumodels)

serviceson = subprocess.getoutput('service --status-all | egrep -w "^ \[ \+ \]" | sed s/"\[ + \]"/""/')
serviceson_list = serviceson.split()
print_result("Running Services", serviceson_list)

servicesoff = subprocess.getoutput('service --status-all | egrep -w "^ \[ - \]" | sed s/"\[ - \]"/""/')
servicesoff_list = servicesoff.split()
print_result("Stopped Services", servicesoff_list)
