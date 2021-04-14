import socket

def check_validilty():
    IP = input("Enter doudtable ip address : ")
    try:
        socket.inet_aton(IP)
        print("Valid IP address")

    except:
        pass
    return "Invalid IP address"

