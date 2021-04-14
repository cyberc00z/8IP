import socket 
IP = input("Enter ip address : ")
try:
   socket.inet_aton(IP)
   print("Valid IP address")
except socket.error:
   print("Invalid IP")