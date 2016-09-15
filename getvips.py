# run script with: python getvips.py [F5 ltm ip] [admin username]
# returns list of VIP ips

import bigsuds
import sys

a = sys.argv[1:]

try:
    b = bigsuds.BIGIP(
    hostname = a[0],
    username = a[1],
    password = "M",
    )
except Exception, e:
    print e

def get_VIPs(obj):
    try:
        return obj.LocalLB.VirtualServer.get_list()
    except Exception, e:
        print e

def get_all_VIPs_ip(obj):
    try:
        pool = get_VIPs(obj)
        return pool, obj.LocalLB.VirtualServer.get_destination_v2(pool)
    except Exception, e:
        print e

pl, pl_status = get_all_VIPs_ip(b)
combined = zip(pl, pl_status)

i = 0
viplist = []
for x in combined:
    if x[1]['address'].find("0.0.0.0") == -1:
        viplist.append(1)
        viplist[i] =  x[1]['address'].replace("/Common/", "")
        i += 1

viplist.sort()

print viplist
