"""
Data: 14-April-2021
Author : xadhrit
Description: Tool for Playing around Internet Protocols.

"""


module_name = "8-IP (ip recon tool by Adhrit)"
__version__ = "1.0.0"


# importing libraries
from logging import ERROR, FATAL
import os
import socket
import re
import requests
import uuid
from  pyfiglet import Figlet
from rich import style
from simple_geoip import GeoIP
from rich.console import Console
from rich.progress import track
from rich import print
from time import sleep

def clearConsole():
    cmd = 'clear'
    if os.name in ('nt', 'dos'):
        cmd = 'cls'
    os.system(cmd)


def menu():
    clearConsole()
    pc = Console()
    # banner bro!
    banner = Figlet(font='graffiti',justify='right')

    pc.print(banner.renderText("                           8-IP !!                    "), style="green")
    print('                                                                                 IP recon tool :) Adhrit ')
    pc.print('                                                                github: https://github.com/xadhrit    ', style="bright_black")
    pc.print( "                                              GIVE ME FUCKING STAR ! BECAUSE WE ARE STARS BROS!  ", style="green")
    print ("   ")
    print("    ")
    print ("   ")
    
    pc.print("""                                   
    
     
                                            _____________________________________________________________________________                  
                                            +                                                                            +
                                            +                     WELCOME TO 8-IP's MAIN MENU :                          +                                    
                                            +____________________________________________________________________________+
    
    
    
    
     """, style="yellow")
    pc.print(" > "," Choose you desired operation : \n", style="blue")
   

    pc.print(" > '1' for TARGET SERVER IP :    \n", style="bold magenta")
    pc.print(" > '2' for IP LOOKUP  :    \n", style="bold magenta")
    pc.print(" > '3' for PUBLIC IP  :    \n", style="bold magenta")
    pc.print(" > '4' for DOMAIN NAME :    \n", style="bold magenta")
    pc.print(" > '5' for PRIVATE IP :    \n", style="bold magenta")
    pc.print(" > '6' for VAILDITY :    \n", style="bold magenta")
    pc.print(" > '7' for MAC ADDRESS :    \n", style="bold magenta")
    pc.print(" > '0' for Exit :    \n", style="bold magenta")

    user_input = int()
    user_input = input("Enter Your Choose : ")
    


    if (user_input == '1'):
        host = input("Enter target's domain name : ")
        if (socket.getaddrinfo==FATAL):
            pc.print(ERROR, style="red")
        try:
            hostname = host
            addr = socket.gethostbyname(hostname)
            for step in track(range(100), description="loading results"):
                sleep(0.01)
                
            pc.print("""
            
            ++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                        IP of {} is {}                       
            ++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            
            
            
            """.format(hostname, addr))

            pc.print("Enter 'r' for main menu \n", style="bright_white")
            pc.print("Enter 'exit' for exit. \n", style="bright_white")
            u_input = input()
            if (u_input == 'r'):
                clearConsole()
                menu()

            elif (u_input == 'exit'):
                exit(0)           
            else:
                pc.print("Invalid Option . killing program.")
            pass
        except Exception as error:
            pc.print(error)
            pass

    elif (user_input == '2'):
        IP = input("Enter target's IP : ")
        try:
            geoip = GeoIP("at_5Hu01r2V5jKlck1HVJJyuZFY0OB3S") #it's my apikey make sure after 1000 queries it will be expired so go to 'https://ip-geolocation.whoisxmlapi.com/' for new one.
            data = geoip.lookup(IP)
            fp = open("data.txt", "w")
            data = str(data)
            fp.write(data)
            for step in track(range(100), description="loading results"):
                sleep(0.08)
            print(data)
            pc.print("Also writing data in data.txt file.", style="bright_black")
            
            pc.print("Enter 'r' for main menu \n", style="bright_white")
            pc.print("Enter 'exit' for exit. \n", style="bright_white")
            u_input = input()
            if (u_input == 'r'):
                clearConsole()
                menu()

            elif (u_input == 'exit'):
                exit(0)           
            else:
                pc.print("Invalid Option . killing program.", style="red")
            pass 
        except Exception as err:
            pc.print(err, style="red")
            pass

    elif (user_input == '3'):
        # from stackoverflow : ('https://stackoverflow.com/questions/2311510/getting-a-machines-external-ip-address-with-python#:~:text=As%20mentioned%20before%2C%20one%20can%20use%20an%20external,external_ip%20%3D%20urllib.request.urlopen%20%28%27https%3A%2F%2Fident.me%27%29.read%20%28%29.decode%20%28%27utf8%27%29%20print%20%28external_ip%29)
        try:
            res = requests.get("https://api.ipify.org")
            myIp = re.compile('(\d{1,3}\.){3}\d{1,3}').search(res.text).group()
            if myIp != "":
                for step in track(range(100), description="fetching IPV4"):
                    sleep(0.05)
                pc.print(""" 
                
                ---------------------------------------------------------------------------------
                        Your Public IP is {}
                ---------------------------------------------------------------------------------     
                
                """.format(myIp), style="green")
            pc.print("Enter 'r' for main menu \n", style="bright_white")
            pc.print("Enter 'exit' for exit. \n", style="bright_white")
            u_input = input()
            if (u_input == 'r'):
                clearConsole() 
                menu()

            elif (u_input == 'exit'):
                exit(0)           
            else:
                pc.print("Invalid Option . killing program.", style="red")
            pass
        except:
            pass
        
    
    elif (user_input == '4'):
        

        try:
            ip = input("Enter target's IP address : ")
            domainName = socket.gethostbyaddr(ip)
            for step in track(range(100), description="finding dns"):
                sleep(0.06)
            pc.print("""
            
                +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                        Domain name of IP {} is {}
                +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
            
            """.format(ip, domainName), style="green")
            pc.print("Enter 'r' for main menu \n", style="bright_white")
            pc.print("Enter 'exit' for exit. \n", style="bright_white")
            u_input = input()
            if (u_input == 'r'):
                clearConsole() 
                menu()

            elif (u_input == 'exit'):
                exit(0)           
            else:
                pc.print("""    |---------------------------------------------------| 
                                |        INVALID OPTION !                           | 
                                |---------------------------------------------------|
                """, style="red")
            pass
        except Exception as error :
            for step in track(range(100), description="loading results"):
                sleep(0.01)
            pc.print(error,style="red")
            pass
        
    
    
    elif (user_input == '5'):
        computerName = socket.gethostname()
        try:
            IP = socket.gethostbyname(computerName)
            for step in track(range(100), description="loading results"):
                sleep(0.01)
            pc.print("Your Computer Name is : {}".format(computerName), style="yellow")
            pc.print("Internal IP is : {}".format(IP), style="yellow")
            
            pc.print("Enter 'r' for main menu \n", style="bright_white")
            pc.print("Enter 'exit' for exit. \n", style="bright_white")
            u_input = input()
            if (u_input == 'r'):
                clearConsole() 
                menu()

            elif (u_input == 'exit'):
                exit(0)           
            else:
                pc.print("Invalid Option . killing program.", style="red")
            pass
        except:
            pass
        return "n/a"
            
    elif (user_input == '6'):
        IP = input("Enter doudtable ip address : ")
        try:
            socket.inet_aton(IP)
            for step in track(range(100), description="check validity"):
                sleep(0.01)
            pc.print("Valid IP address", style="green")
            pc.print("Enter 'r' for main menu \n", style="bright_white")
            pc.print("Enter 'exit' for exit. \n", style="bright_white")
            u_input = input()
            if (u_input == 'r'):
                clearConsole() 
                menu()

            elif (u_input == 'exit'):
                exit(0)           
            else:
                pc.print("Invalid Option . killing program.", style="red")
            pass
        except:
            pass
        return "Invalid IP address"

    elif (user_input == '7'):
        try:
            pc.print(" Ususally Mac Address comes in hex but i am giving you simple one - ", end="", style="white")
            pc.print(':'.join(re.findall('..', '%012x' %uuid.getnode())), style="green")
            pc.print("Enter 'r' for main menu \n", style="bright_white")
            pc.print("Enter 'exit' for exit. \n", style="bright_white")
            u_input = input()
            if (u_input == 'r'):
                clearConsole() 
                menu()

            elif (u_input == 'exit'):
                exit(0)           
            else:
                pc.print("Invalid Option . killing program.", style="red")
            pass
        except:
           pass

    elif (user_input == '0'):
        pc.print("""
           _____________________________________________________________   
        
                     : ABOUT THE AUTHOR : 
           ______________________________________________________________          
                     
        """, style="yellow")
        pc.print(" Adhrit is a noob but he don't want to kill himself with noob thinking. He write this program today because he is sad from 2 day . \n", style="yellow")
        pc.print(" github : https://github.com/xadhrit  ", style="bright_cyan")
        pc.print(" twitter: https://twitter.com/xadhrit  ", style="bright_cyan")
        pc.print( " GIVE ME FUCKING STAR ! BECAUSE WE ARE STARS BROS!  ", style="green")
        for step in track(range(100), description="Hope you really enjoy this session.."):
                sleep(0.1)
        exit(0)
        
    
    elif (EOFError , KeyboardInterrupt,KeyError):
        pc.print("Key Interruption! ", style="deep_pink3")

    else:
        pc.print("Invalid Option selected!, eXiting..... ", style="red")

      

def main():
    menu()

if __name__ == "__main__":
    main()




        
