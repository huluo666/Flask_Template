from flask import Blueprint

#Blueprint必须指定两个参数，admin表示蓝图的名称，__name__表示蓝图所在模块
index_blu = Blueprint('index', __name__)

@index_blu.route("/")
def index():
    return "Hello World!"