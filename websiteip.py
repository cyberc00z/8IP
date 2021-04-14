import socket

host = input("Enter target's domain name : ")

if __name__ == "__main__":
    hostname = host
    addr = socket.gethostbyname(hostname)
    print("The IP of {} is {}".format(hostname, addr))