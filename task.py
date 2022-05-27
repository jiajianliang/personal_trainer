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
        return jsonify(code="null", msg="请传入参数key [value为1、2、3]")
    key = request.args.get("key", None)
    if len(request.args) > 1 or (request.args == 1 and not key):
        return jsonify(code=key, msg="请不要传递多余的参数")
    if key is None:
        return jsonify(code=key, msg="参数必须为key")
    if color.get(key):
        return jsonify(code=key, msg=color.get(key))
    return jsonify(code=key, msg="您查询的key不存在")


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
