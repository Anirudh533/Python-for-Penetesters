import sys
import nmap
target = str(sys.argv[1])
ports = [21,22,80,139,443,8080]
scan = nmap.PortScanner()

print("\nScanning",target,"for ports 21,22,80,139,443 and 8080 ..\n")
for port in ports:
    portscan = scan.scan(target,str(port))
    print("Port",port," is ",portscan['scan'][target]['tcp'][port]['state'])

print("\nHost",target, "is",portscan['scan'][target]['status']['state'])