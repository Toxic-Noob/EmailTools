import os
import sys
import time
import json
import random
import requests
import shutil
from lib.addon import *

columns = shutil.get_terminal_size().columns

def psb(z):
    for p in z+"\n":
        sys.stdout.write(p)
        sys.stdout.flush()
        time.sleep(0.02)


#RandomMail
def random_mail():
    mail_url = "https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1"
    re = requests.get(mail_url).text
    data = json.loads(re)[0]
    return data

#CheckInbox
def invox(mdata):
    mdata = mdata.split("@")
    name = mdata[0]
    domain = mdata[1]
    psb("\033[92m\n    [\033[37m*\033[92m] Press ctrl Then c To Go Back To Stop...\n")
    psb("\033[33m[\033[34m*\033[33m] \033[92mInbox \033[33m[\033[34m*\033[33m] \033[37m".center(columns+37))
    mail_url = "https://www.1secmail.com/api/v1/?action=getMessages&login="+name+"&domain="+domain
    invox.name = name
    invox.domain = domain
    em_cont = 1
    while True:
        try:
            re = requests.get(mail_url).text
            if not re == "[]":
                if (check_mail(re, str(em_cont))):
                    em_cont = em_cont + 1
            time.sleep(0.5)
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(e)

#ProcessAttachmentData
def get_attc(data, id_data):
    name = invox.name
    domain = invox.domain
    filename = data["filename"]
    size = data["size"]
    
    mail_url = "https://www.1secmail.com/api/v1/?action=download%26login="+name+"%26domain="+domain+"%26id="+id_data+"%26file="+filename
    
    new_url = short_url(mail_url)
    
    return filename, size, new_url

#PrintMailData
def print_mail(id_data, count):
    name = invox.name
    domain = invox.domain
    mail_url = "https://www.1secmail.com/api/v1/?action=readMessage&login="+name+"&domain="+domain+"&id="+id_data
    mail_data = json.loads(requests.get(mail_url).text)
    to_data = name+"@"+domain
    from_data = mail_data["from"]
    subject_data = mail_data["subject"]
    date_data = mail_data["date"]
    attc_data = mail_data["attachments"]
    message_data = mail_data["textBody"]
    psb("\033[93m\n\n[\033[37m*\033[93m]\033[92m Inbox   : \033[93m[\033[37m0"+count+"\033[93m]")
    print("\033[92m\n[\033[37m*\033[92m] From    : \033[37m"+from_data)
    print("\033[92m\n[\033[37m*\033[92m] To      : \033[37m"+to_data)
    print("\033[92m\n[\033[37m*\033[92m] Date    : \033[37m"+date_data)
    print("\033[92m\n[\033[37m*\033[92m] Subject : \033[37m"+subject_data)
    print("\n\033[92m[\033[37m*\033[92m] Mail    : \n\n\033[37m"+message_data)
    if not (attc_data == "[]"):
        atc_num = 1
        for atc in attc_data:
            attc_rec = get_attc(atc, id_data)
            file_name = attc_rec[0]
            file_size = str(attc_rec[1])
            file_url = attc_rec[2]
            print("\033[92m[\033[37m*\033[92m] Attachment No : \033[37m0"+str(atc_num))
            print("\033[92m\n[\033[37m*\033[92m] File Name : \033[37m"+file_name)
            print("\033[92m\n[\033[37m*\033[92m] File Size : \033[37m"+file_size+"\033[92m  [\033[37m Bytes \033[92m]")
            print("\033[92m\n[\033[37m*\033[92m] Download From Here : \033[37m"+file_url)
            atc_num = atc_num + 1
    

#CheckMailData
def check_mail(data, em_cont):
    data = json.loads(data)
    if not os.path.exists(".tmp"):
        os.system("touch .tmp")
    for em_data in data:
        id_data = str(em_data["id"])
        opn = open(".tmp", "r").read()
        if id_data in opn:
            continue
        wrt = open(".tmp", "w")
        wrt.write(opn+"\n"+id_data)
        wrt.close()
        print_mail(id_data, str(em_cont))
        return True


#ProcessMailData
def do_mail(mdata):
    if not os.path.exists(".mail"):
        os.system("touch .mail")
    fmopn = open(".mail", "r").read()
    fmout = open(".mail", "w")
    if not (fmopn == "") and not (mdata in fmopn):
        fmout.write(fmopn+"\n"+mdata)
    elif (fmopn == ""):
        fmout.write(mdata)
    else:
        fmout.write(fmopn)
    fmout.close()
    logo()
    psb("\033[92m\n    [\033[37m*\033[92m] Your Created Mail : \033[37m"+mdata)
    invox(mdata)

#SeeOldMails
def see_mail():
    logo()
    if os.path.exists(".mail"):
        old_mails = open(".mail", "r").readlines()
        mn = 1
        psb("\033[92m\n    [\033[37m*\033[92m] Your Created Emails : \n")
        time.sleep(0.6)
        for mail in old_mails:
            psb("\033[92m    [\033[37m0"+str(mn)+"\033[92m] \033[37m"+mail)
            mn = mn + 1
    else:
        time.sleep(0.8)
        psb("\n\033[92m    [\033[91m!\033[92m] You Currently Have No Old Mail Address")

#LogInToOldMails
def log_old():
    logo()
    try:
        old_mails = open(".mail", "r").readlines()
    except:
        psb("\033[92m\n    [\033[91m!\033[92m] You Currently Have No Old Mail Address [\033[91m!\033[92m]")
        return None
    if not (old_mails == "[]"):
        psb("\033[92m\n    [\033[37m*\033[92m] Copy The Mail You Want To Restore and Past Below...\n")
        time.sleep(0.6)
        for mail in old_mails:
            if (mail == ""):
                continue
            psb("\033[92m    [\033[37m#\033[92m] \033[37m"+mail)
        mold = input("\033[92m\n    [\033[37m*\033[92m] Past Your Mail:> \033[37m")
        while not mold in old_mails and not mold in old_mails and not mold == "":
            psb("\n\033[92m    [\033[91m!\033[92m] Only Past Emails From Above...\033[37m")
            mold = input("\033[92m\n    [\033[37m*\033[92m] Past your Mail:> \033[37m")
        return mold
    else:
        psb("\033[92m\n    [\033[91m!\033[92m] You Currently Have No Old Mail Address [\033[91m!\033[92m]")
        return None

#DomainChoose
def domain_choose():
    print("\033[92m\n    [\033[37m01\033[92m] 1secmail.com")
    print("    [\033[37m02\033[92m] 1secmail.org")
    print("    [\033[37m03\033[92m] 1secmail.net")
    print("    [\033[37m04\033[92m] xojxe.com")
    print("    [\033[37m05\033[92m] yoggm.com")
    print("    [\033[37m06\033[92m] wwjmp.com")
    print("    [\033[37m07\033[92m] esiix.com")
    print("    [\033[37m08\033[92m] oosln.com")
    print("    [\033[37m09\033[92m] vddaz.com")
    
    dom = input("\033[92m\n    [\033[37m*\033[92m] Enter Your Domain Choice:> \033[37m")
    if not (dom == "10"):
        dom = dom.replace("0", "")
    while not dom in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        print("\n\033[92m    [\033[91m!\033[92m] Enter a Correct Choice!!\033[37m")
        dom = input("\033[92m\n    [\033[37m*\033[92m] Enter Your Domain Choice:> \033[37m")
        if not (dom == "10"):
            dom = dom.replace("0", "")
    if (dom == "1"):
        doms = "1secmail.com"
    elif (dom == "2"):
        doms = "1secmail.org"
    elif (dom == "3"):
        doms = "1secmail.net"
    elif (dom == "4"):
        doms = "xojxe.com"
    elif (dom == "5"):
        doms = "yoggm.com"
    elif (dom == "6"):
        doms = "wwjmp.com"
    elif (dom == "7"):
        doms = "esiix.com"
    elif (dom == "8"):
        doms = "oosln.com"
    elif (dom == "9"):
        doms = "vddaz.com"
    
    return doms

#CreateAnEmailAddress
def create_mail():
    name = input("\033[92m\n    [\033[37m*\033[92m] Enter Email Name:> \033[37m")
    while (name == ""):
        print("\n\033[92m    [\033[91m!\033[92m] You Must Enter a Name!!\033[37m")
        name = input("\033[92m\n    [\033[37m*\033[92m] Enter Email Name:> \033[37m")
    domain = domain_choose()
    data = name+"@"+domain
    return data


#MainProcess
def temp_mail():
    logo()
    psb("\033[92m\n    [\033[37m*\033[92m] Choose Your Method...")
    print("\n    [\033[37m01\033[92m] Genarate Random Mail")
    print("    [\033[37m02\033[92m] Desine An Email Address")
    print("    [\033[37m03\033[92m] See Mails You Created")
    print("    [\033[37m04\033[92m] Log In To Old Mails")
    print("    [\033[37m05\033[92m] Remove All Old Mail's Data")
    print("    [\033[37m##\033[92m] Exit")
    op = input("\033[92m\n    [\033[37m*\033[92m] Choose Your Option:> \033[37m").replace("0", "").replace("##", "#")
    while not op in ["1", "2", "3", "4", "5", "#"]:
        print("\n\033[92m    [\033[91m!\033[92m] Choose a Correct Option!!\033[37m")
        op = input("\033[92m\n    [\033[37m*\033[92m] Choose Your Option:> \033[37m").replace("0", "").replace("##", "#")
    if (op == "1"):
        mdata = random_mail()
        do_mail(mdata)
        psb("\n\033[92m    [\033[37m*\033[92m] Thanks For Using Our Tool....\n\033[37m")
        sys.exit()
    elif (op == "2"):
        mdata = create_mail()
        do_mail(mdata)
        psb("\n\033[92m    [\033[37m*\033[92m] Thanks For Using Our Tool....\n\033[37m")
        sys.exit()
    elif (op == "3"):
        see_mail()
        o = input("\n\033[92m    [\033[37m*\033[92m] Press Enter To Go Back....")
        temp_mail()
    elif (op == "4"):
        mdata = log_old()
        do_mail(mdata)
        psb("\n\033[92m    [\033[37m*\033[92m] Thanks For Using Our Tool....\n\033[37m")
        sys.exit()
    elif (op == "5"):
        remove()
        o = input("\n\033[92m    [\033[37m*\033[92m] Press Enter To Go Back....")
        temp_mail()
    elif (op == "#"):
        logout()


##NoRemove##


