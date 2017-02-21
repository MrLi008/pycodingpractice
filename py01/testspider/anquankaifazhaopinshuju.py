# coding=utf8

import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# for spider
import requests
import re



# database
db = SQLAlchemy()
basedir = os.path.abspath(os.path.dirname(__file__))

# config
class ConfigSpiderPost:
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

class DevelopmentConfig(ConfigSpiderPost):
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = True


config_spiderpost = {
    'default': DevelopmentConfig
}


# app

def create_app(configname='default'):
    app = Flask(__name__)

    app.config.from_object(config_spiderpost[configname])

    db.init_app(app)
    return app


configname = 'default'
app = create_app(configname=configname)


@app.route('/', methods=['GET', 'POST'])
def index(result):
    return render_template('/index.html', result=result)



def getdatafromurl(url):
    data = requests.get(url)
    encoding = requests.utils.get_encodings_from_content(data.content)[0]
    data.encoding = encoding

    print data.text

    t = r'<table .{40,50} class="newlist">.{2500,3500}</table>'

    # t = u'''>京.*</a>'''
    pattern = re.compile(t, re.U|re.S)

    print pattern
    match = pattern.findall(data.text)
    #
    # print match
    if match is not None:

        for m in match:
            print m,'----------------------------------------------------------'




if __name__ == '__main__':

    url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&isadv=0&sg=4c3a8272bbd046e99594b322e7704142&p=9'
    getdatafromurl(url)


