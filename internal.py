import socket 

computerName = socket.gethostname()
IP = socket.gethostbyname(computerName)
print("Your Computer Name is : {}".format(computerName))
print("Your interanl Ip Address is : {}".format(IP)) 