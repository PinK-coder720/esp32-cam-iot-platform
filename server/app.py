import os
import uuid

from flask import Flask, jsonify, request, send_from_directory,send_file

app = Flask(__name__)
os.makedirs("uploads",exist_ok=True)

@app.route("/api/health",methods=["GET"]) #服务健康监测
def health():
    return jsonify(ok=True,message="server is alive")

@app.route("/api/upload",methods=["POST"]) # 上传图片接口
def upload():
    data = request.get_data()
    filename = uuid.uuid4().hex + ".jpg"
    with open(os.path.join("uploads",filename),"wb") as f:
        f.write(data)
    return jsonify(ok=True,filename=filename)

@app.route("/api/photos",methods=["GET"]) # 列出图片
def photos():
    files = sorted(os.listdir("uploads"))
    return jsonify(ok=True,photos=files)

@app.route("/images/<filename>",methods=["GET"]) # 获取图片
def get_image(filename):
    return send_from_directory("uploads",filename)

@app.route("/",methods=["GET"])
def index():
    return send_file("index.html")
    
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)
