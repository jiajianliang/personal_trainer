# coding:utf-8
__author__ = '贾建亮'

from flask import Flask, request, jsonify

app = Flask(__name__)


# 定义color接口，参数key值为"0"时返回red，为"1"时返回green,为"2"时返回yello
@app.route('/color', methods=["GET"])
def get_color():
    color = {
        "0": "red",
        "1": "green",
        "2": "yello"
    }
    if not request.args:
        return jsonify(code="null", msg="请传入参数key")
    key = request.args.get("key")
    if not key:
        return jsonify(code=key, msg="查询参数必须是key")
    if color.get(key):
        return jsonify(code=key, msg=color.get(key))
    return jsonify(code=key, msg="您查询的key不存在")


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
