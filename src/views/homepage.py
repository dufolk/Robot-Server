from flask import render_template
from flask import Blueprint

views_blue = Blueprint('views', __name__)

# Author : ZP
# 用于启动服务
@views_blue.route('/')
def index():
    return render_template('index.html')

# @views_blue.on('connect')
# def connect():
#     print('connect')