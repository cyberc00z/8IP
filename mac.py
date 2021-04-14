import re, uuid
print(" MAC address in less complex and formatted way is :", end="")
print(':'.join(re.findall('..', '%012x' %uuid.getnode())))