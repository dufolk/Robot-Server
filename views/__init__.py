from flask import Blueprint

views_blue = Blueprint('views', __name__)
from . import homepage