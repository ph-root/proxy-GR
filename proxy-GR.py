#! python3
import requests , bs4 , os , time , zipfile , random , sys

if sys.platform in ["linux","linux2"]:
	W = '\033[0m'
	G = '\033[32;1m'
	R = '\033[31;1m'
	
else:
	W = ''
	G = ''
	R = ''

urls = []

proxies = []

print(r'''
                                         ____  ____  
  _ __   _ __  ___ __  __ _   _         / ___||  _ \ 
 | '_ \ | '__|/ _ \\ \/ /| | | | _____ | |  _ | |_) |
 | |_) || |  | (_) |>  < | |_| ||_____|| |_| ||  _ < 
 | .__/ |_|   \___//_/\_\ \__, |        \____||_| \_\
 |_|                      |___/                      
''')
print(R +
'''    +++++++++++++++++++++++++++++++++++++++++++++++
    +               PROXY  GRABBER                +
    +               CODER : BEN_TH                +
    +   FB : www.facebook.com/bassem.beso.18659   +
    +++++++++++++++++++++++++++++++++++++++++++++++

'''
	)
print()
print(G + '[X] STAERTING NOW !!')
path = os.getcwd()

os.makedirs('Downloads' , exist_ok=True)

os.chdir('Downloads')
def grap(url):
	resI = requests.get(url)
	parseI = bs4.BeautifulSoup(resI.text , 'lxml')
	elems = parseI.select('a[target="_blank"]')
	if len(elems) > 0:
		try:
			for i in range(len(elems)):
				try:
					linkG = elems[i].get('href')
					if 'google' not in linkG:
						continue
				except:
					continue
				bnamefile = os.path.basename(url)
				namefile = bnamefile[:bnamefile.find('.html')]
				resG = requests.get(linkG)
				with open( namefile+ '.zip', 'wb') as prxfile:
					for chunk in resG.iter_content(100000):
						prxfile.write(chunk)
		except:
			try:
				linkG = elems[1].get('href')
				resG = requests.get(linkG)
				with open('proxy.zip' , 'wb') as prxfile:
					for chunk in resG.iter_content(100000):
						prxfile.write(chunk)
			except:
				pass
	

url = 'http://www.proxyserverlist24.top/'
def prx(url):
	resp = requests.get(url)

# with open('resp.html' , 'wb') as file1:
# 	for chunk in resp.iter_content(100000):
# 		file1.write(chunk)


	parse = bs4.BeautifulSoup(resp.text, 'lxml')

	elems = parse.select('h3[itemprop="name"] a')


	for i in elems:

		urls.append(i.get('href'))

prx(url)

for i in urls:
	resI = requests.get(i)
	parseI = bs4.BeautifulSoup(resI.text , 'lxml')
	elems = parseI.select('span[style="color: #ffffff;"]')
	x = len(elems)
	# print('+++++++++++++++')

	if len(elems) == 0:
		grap(i)
		
	else:
		for i in range(x):
			text = elems[i].getText()
			proxies += text.split('\n')

		# time.sleep(10)


print(R + '[X] %s PROXIES FOUND !!' % (len(proxies)) )

urls = []

url = 'http://www.live-socks.net/'
prx(url)


for i in urls:
	resI = requests.get(i)
	parseI = bs4.BeautifulSoup(resI.text , 'lxml')
	elems = parseI.select('textarea[onclick="this.focus();this.select()"]')
	x = len(elems)
	# print('+++++++++++++++')

	if len(elems) == 0:
		grap(i)
	else:
		for i in range(x):
			text = elems[i].getText()
			proxies += text.split('\n')

		# time.sleep(10)

print('[X] %s PROXIES FOUND !!' % (len(proxies)) )

urls = []

url = 'http://www.socks24.org'

prx(url)

for i in urls:

	grap(i)

print('[X] PROCESSING SOME DOWNLOADS !!')
urls = []

url = 'http://www.vipsocks24.net/'

prx(url)

for i in urls:
	
	grap(i)


print('[X] PROCESSING SOME DOWNLOADS !!')


urls = []

url = 'http://www.socksproxylist24.top/'

prx(url)

for i in urls:
	grap(i)


print('[X] PROCESSING SOME DOWNLOADS !!')


urls = []

url = 'http://www.sslproxies24.top/'

prx(url)

for i in urls:
	grap(i)
print('[X] EXTRACTING THE FILES AND CLEARING !!')

#------------------------------------------##-------------------------------------------------------##
##----------------------------------------##-------------------------------------------------------##



for i in os.listdir():
	# print(i)
	if 'zip' in i:
		try:
			xfile = zipfile.ZipFile(i)
			xfile.extractall()
			xfile.close()
			for i2 in os.listdir():
				if 'txt' in i2:
					# print(i2)
					with open(i2) as afile:
						readx = afile.read()
						listaprx = readx.split('\n')
						proxies += listaprx
						
			
						os.unlink(i2)
						os.unlink(i)

			
		except:
			continue




for i in os.listdir():
	# print(i)
	if 'zip' in i:
		try:
			xfile = zipfile.ZipFile(i)
			xfile.extractall()
			xfile.close()
			for i2 in os.listdir():
				if 'txt' in i2:
					# print(i2)
					with open(i2) as afile:
						readx = afile.read()
						listaprx = readx.split('\n')
						proxies += listaprx
						
			
						os.unlink(i2)
						os.unlink(i)

			
		except:
			continue


for i in os.listdir():
	if 'url' in i:
		os.unlink(i)

os.chdir(path)
os.makedirs('OUTPUT' , exist_ok=True)

print('[X] %s PROXIES FOUND !!' % (len(proxies)) )
random.shuffle(proxies)
numberprx = len(proxies)
numxx = random.randint(1,30)

fileNaME = '%s_proxies%s.txt' % (numberprx , numxx)
savefile = open(os.path.join('OUTPUT' , fileNaME), 'w')

for i in proxies:
	if i.isalnum():
		continue
	savefile.write(i + '\n')

savefile.close()

print(G + '[X] THE PROXIES HAVE BEEN SAVED IN [ %s_proxies%s.txt ] !!' % (numberprx , numxx))
print( '[X] GOODBYE ...')
