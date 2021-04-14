import uuid, re

def mac_address():
    try:

        print(" Ususally Mac Address comes in hex but i am giving you simple one :", end="")
        print(':'.join(re.findall('..', '%012x' %uuid.getnode())))
        pass
    except:
        print("n/a")
        pass
            