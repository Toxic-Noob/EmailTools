import requests
import sys
import time
import os
import random
import shutil

def psb(z):
    for p in z + "\n":
        sys.stdout.write(p)
        sys.stdout.flush()
        time.sleep(0.01)

##SomeAdditionalFunctions##
columns = shutil.get_terminal_size().columns

#GetTargetEmailAddress
def target_mail():
    target = input("\n\033[92m    [\033[37m*\033[92m] Enter Victim's Email Address:> \033[37m").lower()
    while not "@" in target:
        psb("\n\033[92m    [\033[91m!\033[92m] You Must Enter a Valid Email Address!!")
        target = input("\n\033[92m    [\033[37m*\033[92m] Enter Victim's Email Address:> \033[37m").lower()
    return target

#GetAmount
def target_amount():
    amount = input("\n\033[92m    [\033[37m*\033[92m] Enter Amount (\033[37mDefault 10\033[92m):> \033[37m")
    try:
        int(amount)
    except:
        amount = 10
    if (amount == ""):
        amount = 10
    return amount

#PrintBombingText
def print_bomb(type):
    if (type == "custom"):
        psb("\033[92m    [\033[37m*\033[92m] Auto Delay : \033[37m3 \033[92mSeconds...")
    psb("\n\033[92m    [\033[37m*\033[92m] Please Wait...")
    psb("\033[92m    [\033[37m*\033[92m] Bombing In Progress...\n")

#CheckLimit
def check_limit(sent, amount, target, type):
    print("\r\033[92m    [\033[37m*\033[92m] Email Sent : \033[93m[\033[37m"+str(sent)+"\033[93m]", end="")
    if (sent == amount):
        psb("\n\n\033[92m    [\033[37m*\033[92m] Bombing Finished Successfully!!")
        psb("\033[92m    [\033[37m*\033[92m] Sent \033[37m"+str(amount)+"\033[92m Emails To \033[37m"+target+"\033[92m By EmailTools...")
        return True
    else:
        if (type == "custom"):
            time.sleep(3)
        return False
    

#AutoBombing
def auto():
    logo()
    target = target_mail()
    amount = int(target_amount())
    print_bomb("auto")
    sent = 0
    while True:
        response = bomb_send_auto(target)
        if (response == 200):
            sent = sent + 1
            if (check_limit(sent, amount, target, type = "auto")):
                sys.exit("\033[37m")


#CustomEmail
def custom():
    logo()
    target = target_mail()
    amount = int(target_amount())
    name = input("\n\033[92m    [\033[37m*\033[92m] Enter Anonymous Name:> \033[37m").replace(" ", "+")
    if (name == ""):
        name = "No+One"
    subject = input("\n\033[92m    [\033[37m*\033[92m] Enter Subject:> \033[37m").replace(" ", "+")
    if (subject == ""):
        subject = "Checking"
    message = input("\n\033[92m    [\033[37m*\033[92m] Enter Your Message:> \033[37m").replace(" ", "+")
    if (message == ""):
        message = "What's+Up??"
    print_bomb("custom")
    sent = 0
    while True:
        response = bomb_send(target, name, subject+"_"+str(sent), message)
        if ("success" in response.lower()):
            sent = sent + 1
            if (check_limit(sent, amount, target, type = "custom")):
                sys.exit("\033[37m")

#MailBombingOptions
def bomb():
    logo()
    psb("\n\033[92m    [\033[37m*\033[92m] Select Your Opotion:")
    print("\n\033[92m    [\033[37m01\033[92m] Automated Bombing (\033[37mFast\033[92m)")
    print("\033[92m    [\033[37m02\033[92m] Custom Mail Bombing (\033[37mSlow\033[92m)")
    print("\033[92m    [\033[37m03\033[92m] Go Back")
    op = input("\n\033[92m    [\033[37m*\033[92m] Enter Your Choice:> \033[37m").replace("0", "")
    while not op in ["1", "2", "3"]:
        psb("\n\033[92m    [\033[91m!\033[92m] Choose a Correct Option!")
        op = input("\n\033[92m    [\033[37m*\033[92m] Enter Your Choice:> \033[37m").replace("0", "")
    if (op == "1"):
        auto()
    elif (op == "2"):
        custom()
    elif (op =="3"):
        main()

#EmailSpoofing
def spoof():
    logo()
    target = target_mail()
    mail = input("\n\033[92m    [\033[37m*\033[92m] Enter Spoofing Mail:> \033[37m").replace(" ", "+")
    while (mail == "") and not "@" in mail:
        psb("\n\033[92m    [\033[91m!\033[92m] Please Enter a Valid Spoofing Mail Address!!")
        mail = input("\n\033[92m    [\033[37m*\033[92m] Enter Spoofing Mail:> \033[37m").replace(" ", "+")
    name = input("\n\033[92m    [\033[37m*\033[92m] Enter Anonymous Name:> \033[37m").replace(" ", "+")
    if (name == ""):
        name = "No+One"
    subject = input("\n\033[92m    [\033[37m*\033[92m] Enter Subject:> \033[37m").replace(" ", "+")
    if (subject == ""):
        subject = "Hey+There"
    message = input("\n\033[92m    [\033[37m*\033[92m] Enter Your Message:> \033[37m").replace(" ", "+")
    if (message == ""):
        message = "What's+Up??"
    
    psb("\n\033[92m    [\033[37m#\033[92m] Please Wait...")
    psb("\033[92m    [\033[37m#\033[92m] Spoofing Your Mail...")
    
    response = spoof_send(target, mail, name, subject, message).lower()
    if ("success" in response):
        psb("\n\033[92m    [\033[37m*\033[92m] Successfully Spoofed Mail To \033[37m"+target+"\033[92m From \033[37m"+mail+"\033[92m By EmailTools...")
        sys.exit("\033[37m")
    else:
        psb("\n\033[92m    [\033[91m!\033[92m] There Was a Probleam Spoofing Your Mail!")
        psb("\n\033[92m    [\033[91m!\033[92m] Please Try Again After Some Time or Contact with ToxicNoob!")
        sys.exit("\033[37m")

#MainMenu
def main():
    logo()
    psb("\n\033[92m    [\033[37m*\033[92m] Select Your Option:")
    print("\n\033[92m    [\033[37m01\033[92m] Email Spoofing")
    print("\033[92m    [\033[37m02\033[92m] Email Bombing")
    print("\033[92m    [\033[37m03\033[92m] Genarate Temp Email")
    print("\033[92m    [\033[37m04\033[92m] Contact")
    print("\033[92m    [\033[37m##\033[92m] Exit")
    op = input("\n\033[92m    [\033[37m*\033[92m] Enter Your Choice:> \033[37m").replace("0", "") 
    while not op in ["1", "2", "3", "4", "#"]:
        psb("\n\033[92m    [\033[91m!\033[92m] Choose a Correct Option!")
        op = input("\n\033[92m    [\033[37m*\033[92m] Enter Your Choice:> \033[37m").replace("0", "")
    if (op == "1"):
        spoof()
    elif (op == "2"):
        bomb()
    elif (op == "3"):
        temp_mail()
    elif (op == "4"):
        contact()
        main()
    elif (op == "#"):
        logout()


##ProcessStartsFromHere###
if __name__ == "__main__":
    try:
        ver_do = sys.argv[1:][0]
    except:
        ver_do = ""
    os.system("clear")
    print("\033[92m _____         _      _   _             _     \n|_   _|____  _(_) ___| \ | | ___   ___ | |__  \n  | |/ _ \ \/ / |/ __|  \| |/ _ \ / _ \| '_ \ \n  | | (_) >  <| | (__| |\  | (_) | (_) | |_) |\n  |_|\___/_/\_\_|\___|_| \_|\___/ \___/|_.__/ \n                                              ")
    print("\033[3;90m                     A Product Of ToxicNoob\033[0;92m")
    psb("\n\033[92m    [\033[37m*\033[92m] Please Wait.... \033[37m")
    psb("\033[92m    [\033[37m*\033[92m] Fetching Data.... \033[37m")
    try:
        from lib.more import *
        from lib.addon import *
        from lib.mail import *
        if not (ver_do == "-f"):
            check_version()
        psb("\n\033[92m    [\033[37m*\033[92m] Successfully Fetched Data.... \033[37m")
        psb("\033[92m    [\033[37m*\033[92m] Welcome.... \033[37m")
        time.sleep(0.8)
    except:
        psb("\033[92m    [\033[91m!\033[92m] There Was a Probleam Fetching Data.... \033[37m")
        psb("\033[92m    [\033[91m!\033[92m] Please Contact ToxicNoob or Try Again After Some Time.... \033[37m\n")
        time.sleep(0.8)
        sys.exit()
    main()
