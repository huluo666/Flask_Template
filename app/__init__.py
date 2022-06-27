#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2022/6/24
# @Author  : jenkins
# @Version : V1.0
# @Features: 初始化配置

from flask import Flask
import settings
from app.dbs import db

from app.views.index.index_module import index_blu
from app.views.admin.admin_module import admin_blu

def create_app():
	app = Flask(__name__, template_folder='../templates', static_folder='../static')
	app.config.from_object(settings.DevelopmentConfig)
	# 注册蓝图到app
	app.register_blueprint(index_blu)
	app.register_blueprint(admin_blu)

	# 绑定数据库到app中
	db.init_app(app)
	# migrate = Migrate(app, db)  # 新版本只需这一句话即可
	return app


