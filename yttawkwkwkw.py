import sys
import urllib.request
import urllib.parse
import re,os

os.system('clear')

print ("""


▒██   ██▒▒██   ██▒ ██ ▄█▀▓█████  ███▄    █ ▒██   ██▒▓██   ██▓▒███████▒
▒▒ █ █ ▒░▒▒ █ █ ▒░ ██▄█▒ ▓█   ▀  ██ ▀█   █ ▒▒ █ █ ▒░ ▒██  ██▒▒ ▒ ▒ ▄▀░
░░  █   ░░░  █   ░▓███▄░ ▒███   ▓██  ▀█ ██▒░░  █   ░  ▒██ ██░░ ▒ ▄▀▒░ 
 ░ █ █ ▒  ░ █ █ ▒ ▓██ █▄ ▒▓█  ▄ ▓██▒  ▐▌██▒ ░ █ █ ▒   ░ ▐██▓░  ▄▀▒   ░
▒██▒ ▒██▒▒██▒ ▒██▒▒██▒ █▄░▒████▒▒██░   ▓██░▒██▒ ▒██▒  ░ ██▒▓░▒███████▒
▒▒ ░ ░▓ ░▒▒ ░ ░▓ ░▒ ▒▒ ▓▒░░ ▒░ ░░ ▒░   ▒ ▒ ▒▒ ░ ░▓ ░   ██▒▒▒ ░▒▒ ▓░▒░▒
░░   ░▒ ░░░   ░▒ ░░ ░▒ ▒░ ░ ░  ░░ ░░   ░ ▒░░░   ░▒ ░ ▓██ ░▒░ ░░▒ ▒ ░ ▒
 ░    ░   ░    ░  ░ ░░ ░    ░      ░   ░ ░  ░    ░   ▒ ▒ ░░  ░ ░ ░ ░ ░
 ░    ░   ░    ░  ░  ░      ░  ░         ░  ░    ░   ░ ░       ░ ░    

	""")
print ("Scanning Subdomain For", sys.argv[1])
print ("masukan ip atau domain yang mau di scan ")
for i, arg in enumerate(sys.argv, 1):
	domains = set()
	with urllib.request.urlopen('https://crt.sh/?q=' + urllib.parse.quote('%.' + arg)) as r:
		code = r.read().decode('utf-8')
		for cert, domain in re.findall('<tr>(?:\s|\S)*?href="\?id=([0-9]+?)"(?:\s|\S)*?<td>([*_a-zA-Z0-9.-]+?\.' + re.escape(arg) + ')</td>(?:\s|\S)*?</tr>', code, re.IGNORECASE):
			domain = domain.split('@')[-1]
			if not domain in domains:
				domains.add(domain)
				print(domain)
