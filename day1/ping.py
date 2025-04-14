
import socket
import os

hostname = socket.gethostname() #it get the our system host name set by os
local_ip = socket.gethostbyname(hostname)#returns ip address
print(f"Your local IP address is: {local_ip}")


website = input("enter the site name or ip:")
print(f"Pinging {website}...")
response = os.system(f"ping -c 2 {website}") 


if response == 0:
    print(f"Ping to {website} was successful!") 
else:
    print(f"Ping to {website} failed.")
#response - exit status:
#0 = success
#Any other value = error or failure is 1