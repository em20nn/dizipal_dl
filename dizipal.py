import requests
import pyperclip
import time

from selenium.webdriver.common.by import By
from selenium import webdriver
import time

browserProfile = webdriver.FirefoxOptions()
# browserProfile.add_argument("--lang=en-us")
browserProfile.add_argument("--headless")
browserProfile.add_argument("--window-size=1920,1080")
# browserProfile.add_argument("--disable-notifications")
# browserProfile.add_argument("ignore-certificate-errors")
# browserProfile.add_argument('--disable-gpu')
# browserProfile.add_argument('--mute-audio')
# browserProfile.add_argument('--ignore-certificate-errors')
# browserProfile.add_argument('--ignore-ssl-errors')
# browserProfile.add_argument('--disable-infobars')
# browserProfile.add_argument('--ignore-certificate-errors-spki-list')
# browserProfile.add_argument('--no-sandbox')
# browserProfile.add_argument('--no-zygote')
# browserProfile.add_argument('--allow-running-insecure-content')
# browserProfile.add_argument('--disable-web-security')
# browserProfile.add_argument('--disable-features=VizDisplayCompositor')
# browserProfile.add_argument('--disable-breakpad')
# browserProfile.add_argument('--acceptInsecureCerts')
browser=webdriver.Firefox(options=browserProfile)
name="2x110"
browser.get(f"https://dizipal828.com/bolum/konusanlar-{name}-c02")
time.sleep(5)
index=browser.page_source.find("canvascascade.site/multiplayer.php?v=")
id=browser.page_source[index+37:index+69]
burp0_url = f"https://canvascascade.site:443/multiplayer.php?v={id}"
burp0_headers = {"Sec-Ch-Ua": "\"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"", "Sec-Ch-Ua-Mobile": "?0", "Sec-Ch-Ua-Platform": "\"Windows\"", "Accept-Language": "tr-TR,tr;q=0.9", "Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.6778.140 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", "Sec-Fetch-Site": "cross-site", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Dest": "iframe", "Referer": "https://dizipal828.com/", "Accept-Encoding": "gzip, deflate, br", "Priority": "u=0, i"}
r=requests.get(burp0_url, headers=burp0_headers)
start=r.text.find("window.openPlayer('")
end=r.text.find("', '', '', '', 'playPopup',")
info=r.text[start+19:end-36]
burp0_url = f"https://canvascascade.site:443/source2.php?v={info}"
burp0_headers = {"Sec-Ch-Ua-Platform": "\"Windows\"", "X-Requested-With": "XMLHttpRequest", "Accept-Language": "tr-TR,tr;q=0.9", "Accept": "application/json, text/javascript, */*; q=0.01", "Sec-Ch-Ua": "\"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.6778.140 Safari/537.36", "Sec-Ch-Ua-Mobile": "?0", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": f"https://canvascascade.site/multiplayer.php?v={id}", "Accept-Encoding": "gzip, deflate, br", "Priority": "u=1, i"}
r=requests.get(burp0_url, headers=burp0_headers)
json=r.json()
key=json['playlist'][0]['sources'][0]['file']
file_url = json['playlist'][0]['sources'][0]['file']
start_index = file_url.find("m.php?v=") + len("m.php?v=")
key = file_url[start_index:]
pyperclip.copy(f"./N_m3u8DL-RE.exe 'https://canvascascade.site/master.m3u8?v={key}' --header 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0' --header 'Referer: https://canvascascade.site/multiplayer.php?v={id}' --save-name 'konusanlar{name}'")
# 30 ve 164
# 2x5 1x22 