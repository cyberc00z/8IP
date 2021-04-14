import socket

IP  = input("Enter target's Address : ")

if __name__ == "__main__":
    domain = socket.gethostbyaddr(IP)
    print("Domain name of {} address is {}.".format(IP, domain))
    