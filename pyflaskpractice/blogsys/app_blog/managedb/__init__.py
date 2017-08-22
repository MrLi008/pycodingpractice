# coding=utf8
from flask import Blueprint
print __name__


managedb = Blueprint('managedb', __name__)

from . import views


