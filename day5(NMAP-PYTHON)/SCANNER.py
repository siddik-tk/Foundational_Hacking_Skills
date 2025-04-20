from pydoc import stripid

import nmap
scanner = nmap.PortScanner()
print("nmap scanner....")
print("<----------------------------------->")
ip_addr = input("enter the ip address to scan: ").strip()
print("your target ip address is ",ip_addr)
type(ip_addr)
response = input("""enter the type of scan you wan to perform ------------>
1.syn scan
2.udp scan
3.comprehensive scan
""")
print(" you have entered :  ",response)

if int(response) == 1:
    print("performing syn scan...")
    print("version: ",scanner.nmap_version())
    print(scanner.scan(ip_addr,'1-65500','-v -sS'))
    if 'tcp' in scanner[ip_addr]:
        print("open ports: ", scanner[ip_addr]['tcp'].keys())
    else:
        print("no open tcp ports found!")

elif int(response) == 2:
    print("performing UDP scan...")
    print("version: ", scanner.nmap_version())
    print(scanner.scan(ip_addr, '1-65500', '-v -sU'))
    if 'udp' in scanner[ip_addr]:
        print("open ports: ", scanner[ip_addr]['udp'].keys())
    else:
        print("no open udp ports found!")

elif int(response) == 3:
    print("performing UDP scan...")
    print("version: ", scanner.nmap_version())
    print(scanner.scan(ip_addr, '1-65500', '-v -sS -sV -sC  -A '))
    if 'tcp' in scanner[ip_addr]:
        print("open ports: ", scanner[ip_addr]['tcp'].keys())
    else:
        print("no open tcp ports found!")


else:
    print("scan invalid!")

print(scanner.scaninfo())
print("ip status is ",scanner[ip_addr].state())
print(scanner[ip_addr].all_protocols())

