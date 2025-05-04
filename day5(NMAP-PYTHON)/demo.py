import nmap
scan = nmap.PortScanner()
print(scan.scan('127.0.0.1','1-500'))