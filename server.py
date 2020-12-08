from flask import Flask,session,request
from logzero import logger

from flask_cors import CORS

import user
import disk
import json

logger.info("正在开启应用")
app = Flask("file_manage")
app.debug = True
cors = CORS(app, resources={r"*": {
    "origins": "*",
    "methods": "GET,POST,OPTIONS,PUT,DELETE,PATCH",
    "expose_headers": "*",
    "allow_headers": "*",
    "supports_credentials": "*",
    "max_age": "*",
}})



# 返回json
def get_json(obj):
    return json.dumps(obj)


# 返回success的info
def return_success_data(data):
    return json.dumps({
        "success": True,
        "data": data
    })


# 返回失败的info
def return_failed_data(msg):
    return json.dumps({
        "success": False,
        "message": msg
    })


# 返回需要登录的头
def return_unauthorized():
    return json.dumps({"needAuth": True})

@app.route('/*',methods=['OPTIONS'])
def fake():
    return ""


@app.route('/ls',methods=['GET'])
def list_dirs():
    data = request.args.get("path")
    path = disk.find_dic_item(data)
    res = []
    for i in path.dic:
        res.append({
            "name": i.file_name,
            "create_time": i.create_time,
            "tag": i.tag
        })
    return return_success_data(res)


@app.route('/del',methods=['GET'])
def del_file():
    data = request.args.get("path")
    disk.delete_command(['', data])
    return return_success_data("success")


@app.route('/mkdir',methods=['GET'])
def mkdir():
    data = request.args.get("path")
    disk.mkdir(['', data])
    return return_success_data("success")


@app.route('/create',methods=['GET'])
def mkdir():
    data = request.args.get("path")
    disk.create(['', data])
    return return_success_data("success")

if __name__ == "__main__":
    logger.info("读取配置文件")
    app.run(host='0.0.0.0', threaded=False)