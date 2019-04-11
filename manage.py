import uuid
from flask import Flask, render_template, url_for, request, make_response, Response, redirect, abort
from flask_script import Manager
from flask import json

app = Flask(__name__)

manager=Manager(app=app)
@app.route('/')
def hello_world():

    return 'Hello World!'

@app.route("/hello/")
def hello():
    return render_template("hello.html")

#关键字参数
@app.route("/params/<hehe>/")
def params(hehe="默认值",ooo=100):
    print(hehe)
    print(type(hehe))
    return "提取参数"

# @app.route("/get/<path:name>/")
# def get(name):
#     print(name)
#     print(type(name))
#     return "还是获取参数"

@app.route("/get/<uuid:name>/",methods=["GET","POST"])
def get(name):
    print(name)
    print(type(name))
    return "还是获取参数"

@app.route("/getuuid/")
def get_uuid():
    return str(uuid.uuid4())

@app.route('/any/<any(a,d,e):an>/')
def any(an):
    print(an)
    print(type(an))
    return "Any"

@app.route("/url")
def url():
    print(url_for('get_uuid'))
    print(url_for("any",an="e"))
    return "反向解析"

@app.route("/request/",methods=["GET","POSt"])
def req():
    print(request)
    print(type(request))
    print(request.data)
    #arguments 参数，get请求参数
    # print(request.args.get("name"))
    # print(request.args.getlist("password"))
    #post相关请求参数
    print(request.form)
    #
    print(request.files)
    print(request.cookies)
    #远程用户地址
    print(request.remote_addr)
    #浏览器身份
    print(request.user_agent)
    print(request.url)
    return "请求"

@app.route("/response/")
def resp():
    result=render_template("hello.html")
    print(result)
    print(type(result))
    # return "相应", 401
    response=make_response('<h2>这是response的内容</h2>',400)
    # response=Response(response="<h2>德玛西亚之力</h2>",status=403)
    print(response)
    return response

#重定向
@app.route("/redirect/")
def redir():
    # return redirect(url_for("hello"))
    response = redirect(url_for("hello"))
    print(response)
    print(type(response))
    return response

#终止执行
@app.route("/abort/")
def ab():
    abort(403)

@app.route("/json/")
def js_n():
    # result=json.jsonify({'name':"value"})
    # result=json.jsonify(name="value",age=18)#application


    # result=json.dumps({'name':"value","age":18})#text/html
    # print(result)
    # print(type(result))


    result='{"name":"value"}'   #text/html类型
    #换格式
    response=Response(response=result,content_type="application/json")
    return response
    # return result

if __name__ == '__main__':
    # app.run(debug=True,port=8010)
    manager.run()
	
    print("推送")
	print("推送第二次")