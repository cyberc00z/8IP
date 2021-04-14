import socket

def website_ip():
    host = input("Enter target's domain name : ")
    try:
        hostname = host
        IP = socket.gethostbyname(hostname)
        print("IP of {} is {}".format(hostname, IP))
        pass
    except Exception as error:
        print(error)
        pass