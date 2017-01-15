# conding=utf8

from flask import render_template
from . import mainofindex

@mainofindex.app_errorhandler(404)
def page_not_fount(e):
    return render_template('/404.html'), 404


@mainofindex.app_errorhandler(500)
def intelnal_server_error(e):
    return render_template('/500.html'), 500