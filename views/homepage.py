from . import views_blue
from flask import render_template

# Author : ZP
# 用于启动服务
@views_blue.route('/')
def index():
    return render_template('templates/index.html')