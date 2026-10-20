from flask import Flask, render_template, request, jsonify
import requests, time
from urllib.parse import urlparse
app = Flask(__name__, template_folder='.')
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/scan', methods=['POST'])
def scan():
    data=request.get_json()
    url=data.get('url','').strip()
    if not url:
        return jsonify({"error":"Digite um site!"})
    if not url.startswith('http'):
        url='https://'+url
    try:
        s=time.time()
        r=requests.get(url,timeout=10,headers={'User-Agent':'Mozilla/5.0'})
        elapsed=int((time.time()-s)*1000)
        title="N/A"
        if "<title>" in r.text.lower():
            try:
                title=r.text.lower().split("<title>")[1].split("</title>")[0][:80]
            except:
                pass
        is_https=urlparse(url).scheme=='https'
        return jsonify({"url":url,"status":r.status_code,"time":elapsed,"size":round(len(r.content)/1024,1),"https":is_https,"title":title,"headers":{"Server":r.headers.get("Server","N/A")}})
    except Exception as e:
        return jsonify({"error":str(e)})
if __name__=='__main__':
    app.run(host='0.0.0.0',port=10000)