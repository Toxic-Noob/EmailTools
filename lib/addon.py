# Some Additional Codes For EmailTools Script

import os
import sys
import time
import shutil
import requests
try:
    import version
except:
    os.system("pip install tool-version-checker > /dev/null 2>&1")
    import version

columns = shutil.get_terminal_size().columns

def psb(z):
    for p in z + "\n":
        sys.stdout.write(p)
        sys.stdout.flush()
        time.sleep(0.01)

##Logo##
def logo():
    os.system("clear")
    print("\033[94m┌────────────────────────────────────────┐".center(columns+5))
    print("\033[94m│       \033[92m▛▀▘       ▗▜  ▀▛▘     ▜\033[94m          │".center(columns+15))
    print("\033[94m│       \033[92m▙▄ ▛▚▀▖▝▀▖▄▐   ▌▞▀▖▞▀▖▐ ▞▀▘ \033[94m     │".center(columns+15))
    print("\033[94m│       \033[92m▌  ▌▐ ▌▞▀▌▐▐   ▌▌ ▌▌ ▌▐ ▝▀▖\033[94m      │".center(columns+15))
    print("\033[94m│       \033[92m▀▀▘▘▝ ▘▝▀▘▀▘▘  ▘▝▀ ▝▀  ▘▀▀ \033[94m      │".center(columns+15))
    print("\033[94m│                              \033[94m          │".center(columns+9))
    print("\033[94m│ \033[95mAuthor : ToxicNoob                     \033[94m│".center(columns+15))
    print("│ \033[95mTool   : A Email Toolkit               \033[94m│".center(columns+9))
    print("│ \033[95mGitHub : https://github.com/Toxic-Noob \033[94m│".center(columns+9))
    print("│ \033[95mCoder  : HunterSl4d3             \033[37mV1.0  \033[94m│".center(columns+15))
    print("\033[94m└────────────────────────────────────────┘".center(columns+5))


#ContactToxicNoob
def contact():
    logo()
    psb("\n\033[92m    [\033[37m★\033[92m] Thanks For Using Our Tool..")
    psb("\n\033[92m    [\033[37m★\033[92m] Contact with ToxicNoob Via Email:\n")
    print("\033[37m[\033[94m ToxicNoob.Sl4d3.Official@gmail.com \033[37m]".center(columns+13))
    time.sleep(0.6)
    psb("\n\033[92m    [\033[37m★\033[92m] You Can Also Contact Via Facebook Page!")
    l = input("\n\033[92m    [\033[37m★\033[92m] Press Enter To Visit ToxicNoob Facebook Page....")
    os.system("xdg-open https://m.facebook.com/ToxicNoobOfficial")
    l = input("\n\033[92m    [\033[37m★\033[92m] Press Enter To Go Back To Main Menu....")

#ExitTool
def logout():
    psb("\n\033[92m    [\033[37m★\033[92m] Thanks For Using Our Tool..")
    psb("\n\033[92m    [\033[37m★\033[92m] For More Tools, Visit:\n")
    print("\033[94m[\033[37m https://github.com/Toxic-Noob/ \033[94m]".center(columns+13))
    sys.exit("\033[37m")

#ShortURL
def short_url(url):
    short = requests.get("https://is.gd/create.php?format=simple&url="+url).text
    if not ("//is.gd/" in short):
        short = ""
    return short

#CheckUpdate
def check_version():
    version.custom(check = "$blank$", checkSuccess = "$blank$", update = "\033[92m    [\033[37m*\033[92m] Tool Update Found...\n\033[92m    [\033[37m*\033[92m] Updating Tool...", updateSuccess = "\n\033[92m    [\033[37m*\033[92m] Tool Updated Successfully...\n\033[92m    [\033[37m*\033[92m] Starting Tool...", printType = "flush")
    version.check(verFile = "lib/.version", RepoFile = "e-tools.py", RepoURL = "https://github.com/Toxic-Noob/EmailTools")
