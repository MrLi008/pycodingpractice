# coding=utf8
from flask import Flask, render_template, request, Response, jsonify

from flask_bootstrap import Bootstrap

from flask_moment import Moment
import json

app = Flask(__name__)

bootstrap = Bootstrap(app)
moment = Moment(app)

def f():
    print 'fafa'

@app.route('/a/<name>')
def index(name):
    return render_template('t.html', name=name, f=f)


@app.route('/t/<count>', methods=['GET', 'POST'])
def test(count):
    print count
    print request

    if request.is_json():
        data = request.POST.get('count')
        print data
        return


@app.route('/jsonpage', methods=['GET','POST'])
def jsonpage():

    if request.method == 'POST':
        print 'in post'
        # data = dict()
        # data['data'] = []
        # jsondata = json.dumps(data)
        # print jsondata
        # return render_template('step_new.html', json=jsondata)


        jsdata = request

        print 'jsdata: ', jsdata
        print ''

        # 第六条
        data = dict()
        data[u'输入'] = [(u'涉及数额', u'元'), ]
        data['step'] = 2



        return jsonify(data)



    return render_template('step_new.html', json=json.dumps('hahahahahahahahah'), name='jsonpage')



if __name__ == '__main__':
    app.run(debug=True)