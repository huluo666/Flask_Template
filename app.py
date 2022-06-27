#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2022/6/24
# @Author  : jenkins
# @Version : V1.0
# @Features: 标准模板

from app import create_app
app = create_app()

# 启动Flask Web服务
if __name__ == '__main__':
#   app.run()
#   app.run(port=5000)
    app.run(host='0.0.0.0', port=5000)
    