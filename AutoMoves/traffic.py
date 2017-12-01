import requests
import pyautogui
import sys
import socks
import socket
import time
# pyautogui.click(50,100)
# pyautogui.click(50,125)

# for i in range(50):
# 	pyautogui.click(50,200)
# 	pyautogui.hotkey('ctrl', 'shift','u')

# 	socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9150)
# 	socket.socket = socks.socksocket
# 	a=requests.get('http://icanhazip.com')
# 	b=requests.get('https://lifechat2017.wordpress.com/about/')
# 	print(a.text)
# a=requests.get('https://lifechat2017.wordpress.com/', headers=headers)
def run(count):
	count+=1
	pyautogui.click(50,200)
	pyautogui.hotkey('ctrl', 'shift','u')
	# headers = {
	#     'Host': 'lifechat2017.wordpress.com',
	#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:52.0) Gecko/20100101 Firefox/52.0',
	#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	#     'Accept-Language': 'en-US,en;q=0.5',
	#     'Referer': 'https://duckduckgo.com/',
	#     'Connection': 'keep-alive',
	#     'Upgrade-Insecure-Requests': '1',
	# }
	# proxies = {
	#     'http': 'socks5h://127.0.0.1:9050',
	#     'https': 'socks5h://127.0.0.1:9050'
	# }

	socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9150)
	socket.socket = socks.socksocket
	a=requests.get('http://icanhazip.com')
	b=requests.get('https://lifechat2017.wordpress.com/about/')
	# print(b.text)
	print(a.text)
	if(b.text and count<=50):
		time.sleep(30)
		run(count)
	else:
		sys.exit()

run(0)