from flask import Blueprint,jsonify

admin_blu = Blueprint('admin', __name__,url_prefix="")

@admin_blu.route("/admin")
def admin_index():
    return "admin"

@admin_blu.route("/admin2")
def admin2():
    response = {
        'msg': 'Hello, Python !'
    }
    return jsonify(response)

"""
from flask import Blueprint,render_template,url_for,session,request,redirect
comment = Blueprint('comment',__name__,url_prefix="/comment")  # 创建蓝图对象，其中第一个参数是指蓝图对象名（在jinja模板中可能会用到）。

这样蓝图的创建和注册就都完成了。其中有两个参数需要介绍下：

"comment": 蓝图的名称，这是一个必须的参数，这里的蓝图名称就是构成视图函数 endpoint 的一部分。
url_prefix="/comment": 该蓝图下所有路由的前缀地址，比如这里定义的前缀是 /comment，那么如果这个蓝图下有一个 /hello 路由，那么它的完整 URL 地址就是这样的 127.0.0.1:5000/comment/hello，这里要注意的是，url_prefix 并非是必须的参数.
"""