import nmap

scanner = nmap.PortScanner()
print("Nmap Scanner....")
print("<----------------------------------->")

ip_addr = input("Enter the IP address to scan: ").strip()
print("Your target IP address is:", ip_addr)

response = input("""
Enter the type of scan you want to perform:
1. SYN Scan
2. UDP Scan
3. Comprehensive Scan
>> """)

print("You have entered:", response)

if response == '1':
    print("Performing SYN Scan...")
    print("Nmap Version:", scanner.nmap_version())
    scanner.scan(ip_addr, '1-65500', '-v -sS')
    if 'tcp' in scanner[ip_addr]:
        print("Open TCP ports:", scanner[ip_addr]['tcp'].keys())
    else:
        print("No open TCP ports found!")

elif response == '2':
    print("Performing UDP Scan...")
    print("Nmap Version:", scanner.nmap_version())
    scanner.scan(ip_addr, '1-65500', '-v -sU')
    if 'udp' in scanner[ip_addr]:
        print("Open UDP ports:", scanner[ip_addr]['udp'].keys())
    else:
        print("No open UDP ports found!")

elif response == '3':
    print("Performing Comprehensive Scan...")
    print("Nmap Version:", scanner.nmap_version())
    scanner.scan(ip_addr, '1-65500', '-v -sS -sV -sC -A')
    if 'tcp' in scanner[ip_addr]:
        print("Open TCP ports:", scanner[ip_addr]['tcp'].keys())
    else:
        print("No open TCP ports found!")

else:
    print("Invalid option selected. Please enter 1, 2, or 3.")

