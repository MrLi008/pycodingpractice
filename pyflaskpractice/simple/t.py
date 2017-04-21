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


# 量刑公共部分
st = [u'法定从轻,减轻 量刑情节共用部分',
      u'法定从轻减轻情节',
      u'酌定从轻处罚情节',
      u'酌定处罚情节']

dataall_share = dict()
dataall_share[st[0]] = {
    u'法定从轻减轻情节':{
        u'盲人聋哑人犯罪': {
            u'盲人聋哑人犯罪':
                [-0.4, 0]
            ,
        },
        u'自首': {
            u'已被发觉未被采取强制措施':
                [-0.3, -0.1, 48.0]
            ,
            u'如实供述不同类罪行,供述罪行相当':
                [-0.2, -0, 48.0]
            ,
            u'如实供述不同类罪行,供述罪行较重':
                [-0.3, -0.1, 48.0]
            ,
            u'亲友规劝、陪同':
                [-0.25, -0, 48.0]
            ,
            u'未被发觉形迹可疑':
                [-0.25, -0, 48.0]
            ,
            u'尚未发觉':
                [-0.4, -0.2, 48.0]
            ,
        },
        u'预备犯': {
            u'预备犯': [-0.6, 0]
        },
        u'未遂犯': {
            u'实行终了+未造成损害后果':
                [-0.4, -0]
            ,
            u'未实行终了+未造成损害后果':
                [-0.5, -0]
            ,
            u'未实行终了+造成损害后果':
                [-0.3, -0]
            ,
            u'实行终了+造成损害后果':
                [-0.2, -0]
            ,
        },

        u'共同犯罪': {
            u'教唆犯+教唆对象为限制行为能力人':
                [-0.2, -0]
            ,
            u'作用相对较小的主犯':
                [-0.2, -0]
            ,
            u'从犯':
                [-0.5, -0.2]
            ,
            u'教唆犯+教唆对象为未成年人':
                [-0.3, -0.1]
            ,
            u'教唆犯+被教唆的人未犯被教唆之罪':
                [-0.5, -0]
            ,
        },
        u'限制行为能力人': {
            u'限制行为能力人':
                [-0.4, -0]
            ,
        },
        u'填写项目为坦白项下选择': {
            u'（2）其他坦白情形':
                [-0.5, -0.1]
            ,
            u'（1）如实供述自己罪行':
                [-0.1, -0]
            ,
        },
        u'填写项目为立功项下选择': {
            u'（2）重大立功':
                [-0.5, -0.2]
            ,
            u'（1）一般立功':
                [-0.2, -0.0, 24.0]
            ,
        },
        u'中止犯': {
            u'造成较重损害':
                [-0.6, -0.3]
            ,
            u'造成较轻损害':
                [-0.8, -0.5]
            ,
        },
    },
    u'酌定从轻处罚情节':{
        u'被害人过错': {
            u'明显过错':
                [-0.4, -0]
            ,
            u'一般过错':
                [-0.2, -0]
            ,
        },
        u'积极赔偿、取得谅解': {
            u'选择积极赔偿+一般犯罪':
                [-0.3, -0]
            ,
            u'选择积极赔偿+取得谅解+一般犯罪':
                [-0.4, -0]
            ,
            u'选择取得谅解+抢劫、强奸等严重危害社会治安犯罪':
                [-0.1, -0, 12.0]
            ,
            u'刑事和解':
                [-0.5, -0]
            ,
            u'选择积极赔偿+抢劫、强奸等严重危害社会治安犯罪':
                [-0.1, -0, 12.0]
            ,
            u'配合追缴违法所得、挽回较大损失':
                [-0.1, -0]
            ,
            u'选择取得谅解+一般犯罪':
                [-0.2, -0]
            ,
            u'选择积极赔偿+取得谅解+抢劫、强奸等严重危害社会治安犯罪':
                [-0.1, -0, 12.0]
            ,
        },
        u'退赃、退赔': {
            u'一般犯罪':
                [-0.3, -0.0],
            u'抢劫等严重危害社会治安犯罪':
                [-0.1, 0, 12.0],
        },

    },
    u'酌定处罚情节':{
        u'累犯': {
            u'累犯':
                [0.1, 0.3, 3.0]
            ,
        }
    },
}
# 数据传输时的标记

status = 'status' # 状态0, 1
msg = 'msg' # 传递的消息
content = 'content' # 页面内容
result = 'result' # 处理结果
title = 'title' # 主题
@app.route('/jsonpage/<id>', methods=['GET','POST'])
def jsonpage(id):
    data = dict()
    if request.method == 'POST':
        print 'in post'

        jsdata = request.form

        print 'jsdata: ', jsdata
        print 'jsdata-data', jsdata

        # if len(jsdata.data) == 0:

        thisstep = int(jsdata['step'])

        if thisstep == 1:
            # 第六条
            postdata = jsdata.get('actions')
            if postdata not in (None, []):
                # 有逮捕标准第六条
                data[status] = 0
                data[msg] = u'建议不批准逮捕'
            else:# 无逮捕标准第六条
                data[status] = 1
                data[content] = [u'涉及数额(元)']
                data[title] = u'犯罪嫌疑人基本信息'

            return jsonify(data)


        elif thisstep == 2:
            # 法定从轻减轻情节
            data[title] = u'法定从轻减轻情节'
            data[status] = 0
            data[content] = dataall_share[st[0]]
            return jsonify(data)
        elif thisstep == 3:
            data[status] = 4
            # 是否未成年人犯罪
            postdata = jsdata['actions']
            if u'未成年犯罪' in postdata.keys():
                data[content] = {u'法定从宽处罚情节':{u'刑事和解':[-0.5,0]}}
            else:
                data[content] = {u'酌定处罚情节':{u'前科':[0,0.1]},
                               u'法定从重处罚情节':{u'累犯':[0,0.3, 3]},
                               u'法定从宽处罚情节':{u'刑事和解':[-0.5,0]}
                               }
            return jsonify(data)



        else:
            data[status] = 0
            data[msg] = 'wrong.......'
            return jsonify(data)
    data[title] = u'逮捕标准第六条'
    data[status] = 1
    data[content] = [u'患有严重疾病、生活不能自理',
                            u'怀孕或者正在哺乳自己婴儿的妇女',
                            u'系生活不能自理的人的唯一抚养人']





    return render_template('step_new.html', json=json.dumps(data), name='jsonpage', id=id)



if __name__ == '__main__':
    app.run(debug=True)