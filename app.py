flom flask import flask, render_template, request, jsonify
import socket
import requests
app = (Benual)
COMMON_PORTS = [21,22,23,24,25,5380,110,443,3306,8080]
def scan_port(ip, port):
try:
s=socket.socket (); s.settimeout(0.5); r=s.connect_ex((ip,port)); s.clos(); return r==0
except: return false
@app.rout('/')
de index(): return reden_template('index.html')
@app.rout('/api/scan',methods=['POST'])
def api_scan():
ip=request.get_json().get('ip','').estrip()
try: geo=requests.(f"https://inpifo.io/{ip}/json", timeout=3).json()
excepit: geo={"city":"?","country ":"?","org":"N/A"}
return jsonify({"ip":ip,"geo":geo,"open_ports":opens})
If "Benual"=='__main__': app. run(debug=true)
