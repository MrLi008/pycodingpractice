# coding=utf8

'''
基准刑 = 量刑起点 + 应增加的刑法量
benchmark punishment = sentencing starting point
        + the amount of penalty should be increased
'''


import numpy as np
import pandas as pd
columns = [u'普通盗窃', u'入户盗窃', u'携带凶器盗窃', u'扒窃', u'多次扒窃', u'二条1到8项之一', u'二条3到8项之一']
# indexes = ['0-1000', '1000-2000', '2000-25000', '25000-50000', '50000-200000', '200000-400000', '400000以上']
#
# data = pd.DataFrame(data=lambda x:x+1, index=indexes, columns=columns)

# 量刑标准
# 计算公式 描述各种情节及金额下, 量刑增加量
# data = pd.read_excel('calculationformula.xlsx')
# data.index = indexes
# 描述量刑起点的表格
# data2 = pd.read_excel('sentencingstart.xlsx')
# data2.index = indexes


# print data

# test_data =
# amountoftheft = 50200
# 描述罪犯<<解释>>中, 规定的情形
# actionoftheft = [u'入户盗窃']


# 确认数额范围
def confirmrangeofamount(amount):
    if isinstance(amount, int):
        if amount <= 1000:
            return 0
        if amount <= 2000:
            return 1
        if amount <= 25000:
            return 2
        if amount <= 50000:
            return 3
        if amount <= 200000:
            return 4
        if amount <= 400000:
            return 5
        return 6
    elif isinstance(amount, str):
        if amount == u'数额较大':
            return confirmrangeofamount(25000)
        if amount == u'数额巨大':
            return confirmrangeofamount(50000)
        if amount == u'数额特别巨大':
            return confirmrangeofamount(200000)
    # if isinstance(amount, int):
    #     if amount <= 1000:
    #         return '0-1000'
    #     if amount <= 2000:
    #         return '1000-2000'
    #     if amount <= 25000:
    #         return '2000-25000'
    #     if amount <= 50000:
    #         return '25000-50000'
    #     if amount <= 200000:
    #         return '50000-200000'
    #     if amount <= 400000:
    #         return '200000-400000'
    #     return u'400000以上'
    # elif isinstance(amount, str):
    #     if amount == u'数额较大':
    #         return confirmrangeofamount(25000)
    #     if amount == u'数额巨大':
    #         return confirmrangeofamount(50000)
    #     if amount == u'数额特别巨大':
    #         return confirmrangeofamount(200000)


# 解释第二条项



# 确认盗窃情节归属,
# 因素分析!!!
def confirmascriptionplotoftheft(actionoftheft):
    res = u'普通犯罪'
    flag = True
    for act in actionoftheft[0:4]:
        if act in columns:
            res = act
            flag = False

    return res





# 量刑起点
def getSentencingStartingPoint(amountoftheft, actionoftheft, zuiming):
    standard = pd.read_excel('pibu/sentencingstart.xlsx', sheetname=zuiming)
    # standard.index = indexes
    print standard.columns
    try:
        res = standard.loc[confirmrangeofamount(amountoftheft),
                       confirmascriptionplotoftheft(actionoftheft)]
        # print res, list(res.split('[')[1].split(']')[0].split(u','))
        res = [int(x) for x in list(res.split('[')[1].split(']')[0].split(',')) if x not in (u'',)]
        # print res
    except Exception, e:
        res = [1,12]
        print e, '读取量刑点出错'
    return res





# 应增加的刑罚量
# 系数
def getPenaltyAmount(amountoftheft, actionoftheft, zuiming):
    standard = pd.read_excel('pibu/calculationformula.xlsx', sheetname=zuiming)
    # standard.index = indexes
    print standard.columns
    try:
        temp_res = standard.loc[confirmrangeofamount(amountoftheft),
                           confirmascriptionplotoftheft(actionoftheft)].replace('m', str(amountoftheft))

        '''
        :warnning 可能被恶意利用
        '''
        res = eval(temp_res)

    # print res

    except Exception, e:
        res = [0, 0]
        print e, '计算应增加的刑罚量出错'
    return res




# calculationformula = data.loc[confirmrangeofamount(amountoftheft), actionoftheft]
# res = calculationformula[0].replace('m', str(amountoftheft ))
# # print type(calculationformula),  res
# print '基准刑: '
# print '量刑起点: ', getSentencingStartingPoint(amountoftheft, actionoftheft)
# print '应增加的刑罚量: ', getPenaltyAmount(amountoftheft, actionoftheft)


# 设定量刑起点的标准




base_data = {u'项目名称':{u'行为':[0.6, 1]},}
base_data = {
    u'未成年犯罪':{u'未成年犯罪':[-0.5,-0.1]},
    u'老年人犯罪':{u'老年人犯罪':[-0.2, 0]},
    u'盲人聋哑人犯罪':{u'盲人聋哑人犯罪':[-0.4,0]},
    u'限制行为能力人犯罪':{u'限制行为能力人犯罪':[-0.4,0]},
    u'预备犯':{u'预备犯':[-0.4, 0]},
    u'中止犯':{u'中止犯':[-0.6, -0.3]},
    u'未遂犯':{u'未遂犯':[-0.2, 0]},
    u'从犯':{u'从犯':[-0.5, -0.2]},
    u'胁从犯':{u'胁从犯':[-0.5,0]},
    u'自首':{u'自首':[-0.4,-0.2]},
    u'立功':{u'立功':[-0.2,0]},
    u'坦白':{u'坦白':[-0.1,0]},
    u'前科':{u'前科':[0,0.1]},
    u'累犯':{u'累犯':[0,0.3, 3]},
    u'刑事和解':{u'刑事和解':[-0.5,0]},
    u'退赃退赔':{u'退赃退赔':[-0.3,0]},
    u'积极赔偿':{u'积极赔偿':[-0.3,0]},
    u'取得谅解':{u'取得谅解':[-0.2,0]},
    u'被害人有过错':{u'被害人有过错':[-0.2,0]},
    u'配合追缴违法所得 晚会叫法损失':{u'配合追缴违法做的 挽回较大损失':[-0.1,0]},
    u'盗窃近亲属财务':{u'盗窃近亲属财务':[-0.5,0.2]},
    u'确因生活学习治病继续而盗窃':{u'确因生活学习治病继续而盗窃':[-0.2,0]},
    u'初次 偶然':{u'初次 偶然':[-0.2,0]},
    u'盗窃家庭成员或近亲属财务':{u'盗窃家庭成员或近亲属财务':[-0.2,0]},
    u'却因生活学习治病急需而盗窃':{u'却因生活学习治病急需而盗窃':[0,0.2]},
    u'赃款赃物已返还或者被公安机关扣押':{u'赃款赃物已返还或者被公安机关扣押':[0,0.2]},
    u'被害人明确表示谅解':{u'被害人明确表示谅解':[0,0.2]},
    u'入户盗窃 携带凶器盗窃 扒窃一次且数额在500元以下':{u'入户盗窃 携带凶器盗窃 扒窃一次且数额在500元以下':[0,0.2]},
    u'入户盗窃 携带凶器盗窃 扒窃一次且数额在1000元以下':{u'入户盗窃 携带凶器盗窃 扒窃一次且数额在1000元以下':[0,0.2]},
    u'盗窃财务数额10000元以上':{u'盗窃财务数额10000元以上':[0,0.2]},
    u'以破坏性手段盗窃造成公司财产损失':{u'以破坏性手段盗窃造成公司财产损失':[0,0.2]},
    u'盗窃残疾人 孤寡老人 未成年人或者用于紧急治病的款物':{u'盗窃残疾人 孤寡老人 未成年人或者用于紧急治病的款物':[0,0.2]},
    u'盗窃用于救灾 抢险 防汛 扶贫 移民 救济等款物':{u'盗窃用于救灾 抢险 防汛 扶贫 移民 救济等款物':[0,0.2]},
    u'为实施吸毒 赌博等其他违法犯罪活动而盗窃':{u'为实施吸毒 赌博等其他违法犯罪活动而盗窃':[0,0.2]},
    u'为吸毒、赌博等违法活动而盗窃，':{u'为吸毒、赌博等违法活动而盗窃，':[0,0.2]},
    u'采用破坏性手段盗窃，造成其他财物损失，':{u'采用破坏性手段盗窃，造成其他财物损失，':[0,0.2]},
    u'以黑恶势力名义敲诈勒索':{u'以黑恶势力名义敲诈勒索':[0.0, 0.3]},
    u'多次敲诈勒索':{u'多次敲诈勒索':[0.0, 0.3]},
    u'以严重犯罪相威胁敲诈勒索':{u'以严重犯罪相威胁敲诈勒索':[0.0, 0.3]},
    u'以危险方法制造事端进行敲诈勒索':{u'以危险方法制造事端进行敲诈勒索':[0.0, 0.3]},
    u'以非法手段获取他人隐私敲诈勒索':{u'以非法手段获取他人隐私敲诈勒索':[0.0, 0.3]},
    u'为吸毒、赌博等违法活动而敲诈勒索':{ u'为吸毒、赌博等违法活动而敲诈勒索':[0.0, 0.3]},
    u'曾因敲诈勒索受过刑事处罚':{u'曾因敲诈勒索受过刑事处罚':[0.0, 0.3]},
    u'利用或者冒充特殊身份敲诈勒索':{ u'利用或者冒充特殊身份敲诈勒索':[0.0, 0.3]},
    u'因邻里纠纷、索取债务等矛盾激化而敲诈勒索他人':{ u'因邻里纠纷、索取债务等矛盾激化而敲诈勒索他人':[-0.2, -0]},
    u'造成其他严重后果':{ u'造成其他严重后果':[0.0, 0.3]},
    u'敲诈勒索近亲属财物':{ u'敲诈勒索近亲属财物':[-0.0, -0.0]},
    u'一年内曾因敲诈勒索受过行政处罚':{u'一年内曾因敲诈勒索受过行政处罚':[0.0, 0.3]},
    u'以非法拘禁等手段进行敲诈勒索':{ u'以非法拘禁等手段进行敲诈勒索':[0.0, 0.3]},
    u'犯罪对象为弱势人员':{u'犯罪对象为弱势人员':[0.0, 0.3]},


    u'采用破坏性手段盗窃，造成其他财物损失，':{u'采用破坏性手段盗窃，造成其他财物损失，'   : [0.0, 0.2]}
    ,
    u'初次、偶然盗窃，':{u'初次、偶然盗窃，' :   [-0.2, -0]}
    ,
    u'一年内曾因盗窃受过行政处罚；':{u'一年内曾因盗窃受过行政处罚；' :   [0.0, 0.2]}
    ,
    u'入户盗窃；':{ u'入户盗窃；'   : [0.0, 0.2]}
    ,
    u'在医院盗窃病人及亲友；':{u'在医院盗窃病人及亲友；':    [0.0, 0.2]}
    ,
    u'确因生活、学习、治病急需而盗窃，':{u'确因生活、学习、治病急需而盗窃，' :   [0.0, 0.2]}
    ,
    u'盗窃近亲属财物，':{u'盗窃近亲属财物，' :   [-0.5, -0.2]}
    ,
    u'盗窃7种特定款物；':{u'盗窃7种特定款物；' :   [0.0, 0.2]}
    ,
    u'因盗窃造成严重后果；':{u'因盗窃造成严重后果；' :   [0.0, 0.2]}
    ,
    u'多次盗窃，':{u'多次盗窃，' :   [0.0, 0.2]}
    ,
    u'组织、控制未成年人盗窃；':{u'组织、控制未成年人盗窃；' :   [0.0, 0.2]}
    ,
    u'在自然、事故、安全突发事件发生地盗窃；':{u'在自然、事故、安全突发事件发生地盗窃；' :   [0.0, 0.2]}
    ,
    u'曾因盗窃受过刑事处罚；':{u'曾因盗窃受过刑事处罚；'  :  [0.0, 0.2]}
    ,
    u'携带凶器盗窃，':{u'携带凶器盗窃，':    [0.0, 0.2]}
    ,
    u'为吸毒、赌博等违法活动而盗窃，':{u'为吸毒、赌博等违法活动而盗窃，' :   [0.0, 0.2]}
    ,

}
# from filterprocess import res_re
# import pickle
# import codecs
# 读取量刑公式时, 减刑项表示为负数, 加刑项表示为正数
# with codecs.open('liangxingqingjie.txt', 'r', encoding='utf8') as f:
#     p = pickle.Pickler(f)
#     base_data = p.loads()
# base_data = #res_re
# base_data = {
#     u'未成年犯罪':{u'未成年犯罪':[0.5,0.9]},
#     u'老年人犯罪':{u'老年人犯罪':[0.8,1]},
#     u'盲人聋哑人犯罪':{u'盲人聋哑人犯罪':[0.6,1]},
#     u'限制行为能力人犯罪':{u'限制行为能力人犯罪':[0.6,1]},
#     u'预备犯':{u'预备犯':[0,0.6]},
#     u'中止犯':{u'中止犯':[0.4,0.7]},
#     u'未遂犯':{u'未遂犯':[0.8,1]},
#     u'从犯':{u'从犯':[0.5,0.8]},
#     u'胁从犯':{u'胁从犯':[0,0.5]},
#     u'自首':{u'自首':[0.6,0.8]},
#     u'立功':{u'立功':[0.8,1]},
#     u'坦白':{u'坦白':[0.9,1]},
#     u'前科':{u'前科':[1,1.1]},
#     u'累犯':{u'累犯':[1.1,1.3]},
#     u'刑事和解':{u'刑事和解':[0.5,1]},
#     u'退赃退赔':{u'退赃退赔':[0.7,1]},
#     u'积极赔偿':{u'积极赔偿':[0.7,1]},
#     u'取得谅解':{u'取得谅解':[0.8,1]},
#     u'被害人有过错':{u'被害人有过错':[0.6,1]},
#     u'配合追缴违法所得 晚会叫法损失':{u'配合追缴违法做的 挽回较大损失':[0.9,1]},
#     u'盗窃近亲属财务':{u'盗窃近亲属财务':[0.5,0.8]},
#     u'确因生活学习治病继续而盗窃':{u'确因生活学习治病继续而盗窃':[0.8,1]},
#     u'初次 偶然':{u'初次 偶然':[0.8,1]},
#     u'盗窃家庭成员或近亲属财务':{u'盗窃家庭成员或近亲属财务':[1,1.2]},
#     u'却因生活学习治病急需而盗窃':{u'却因生活学习治病急需而盗窃':[1,1.2]},
#     u'赃款赃物已返还或者被公安机关扣押':{u'赃款赃物已返还或者被公安机关扣押':[1,1.2]},
#     u'被害人明确表示谅解':{u'被害人明确表示谅解':[1,1.2]},
#     u'入户盗窃 携带凶器盗窃 扒窃一次且数额在500元以下':{u'入户盗窃 携带凶器盗窃 扒窃一次且数额在500元以下':[1,1.2]},
#     u'入户盗窃 携带凶器盗窃 扒窃一次且数额在1000元以下':{u'入户盗窃 携带凶器盗窃 扒窃一次且数额在1000元以下':[1,1.2]},
#     u'盗窃财务数额10000元以上':{u'盗窃财务数额10000元以上':[1,1.2]},
#     u'以破坏性手段盗窃造成公司财产损失':{u'以破坏性手段盗窃造成公司财产损失':[1,1.2]},
#     u'盗窃残疾人 孤寡老人 未成年人或者用于紧急治病的款物':{u'盗窃残疾人 孤寡老人 未成年人或者用于紧急治病的款物':[1,1.2]},
#     u'盗窃用于救灾 抢险 防汛 扶贫 移民 救济等款物':{u'盗窃用于救灾 抢险 防汛 扶贫 移民 救济等款物':[1,1.2]},
#     u'为实施吸毒 赌博等其他违法犯罪活动而盗窃':{u'为实施吸毒 赌博等其他违法犯罪活动而盗窃':[1,1.2]},
# }
# '''
# {u'年龄':{u'年龄=65-74, 故意犯罪': [0.8,1],
#                u'年龄=65-74, 过失犯罪':[0.6,0.9],
#                u'年龄大于等于75, 故意犯罪':[0.6,1],
#                u'年龄大于等于75, 过失犯罪':[0.5,0.8]},
#          u'限制行为能力人':{u'限制行为能力人':[0.6,1]},
#          u'聋哑人或盲人':{u'聋哑人或盲人':[0.6,1]},
#          u'预备犯':{u'预备犯':[0,0.6]},
#          u'未遂犯':{u'实行终了, 造成损害后果':[0.8,1],
#                  u'实行终了, 未造成损害后果':[0.6,1],
#                  u'未实行终了, 造成严重后果':[0.5, 1],
#                  u'未实行终了, 未造成严重后果':[0.5,1],
#                  },
#          u'中止犯':{u'造成较重损害的':[0.4,0.7],
#                  u'造成较轻损害的':[0.2,0.5]},
#          }
# '''

# for k in example_data.keys():
#     try:
#         val = example_data.get(k)
#         res = base_data.get(k).get(val)
#
#         # print k, val, res
#
#     except Exception, e:
#         print e


# 根据法定处罚情节和酌定处罚情节分别计算出计算系数
# 需优先计算的量刑情节

list_serious = [
    u'未成年犯罪',
    u'老年人犯罪',
    u'限制行为能力的精神病人犯罪',
    # u'',
    u'又聋又哑的人或者盲人犯罪',
    u'盲人聋哑人犯罪',
    u'防卫过当',
    u'避险过当',
    u'犯罪预备',
    u'犯罪未遂',
    u'犯罪中止',
    u'从犯',
    u'胁从犯',
    u'教唆犯',
    # u'前科',
]
def getCoefficientOfSerious(postdata):
    # res= [1,1]
    res = np.array([1, 1], dtype=np.float64)#.reshape((2,1))
    # print res
    flag = True
    ks = [ks for ks in postdata.keys() if ks in list_serious]
    if len(ks) == 1:
        k = ks[0]
    # for k in ks:
        try:
            val = postdata.get(k)
            print val
            coeff = base_data.get(k).get(val)

            #
            # temp = np.array(coeff)
            # res = res * temp
            res[0] *= np.abs(coeff[0])
            res[1] *= np.abs(coeff[1])
            postdata[k] = None
            res *= -1
        except Exception,e:
            print e, 'coefficientofserious postdata'
    else:
        for k in ks:
            val = postdata.get(k)
            print val
            if val is None or base_data.get(k) is None:
                continue
            coeff = base_data.get(k).get(val)
            if coeff is None:
                continue
            #
            # temp = np.array(coeff)
            # res = res * temp
            res[0] *= (1 - np.abs(coeff[0]))
            res[1] *= (1 - np.abs(coeff[1]))
            postdata[k] = None
            flag = False
        res -= 1
    # if flag :
    #     res = res - 1

    # res *= -1
    return res  # np.array(res)

def test_getCoefficientOfSerious(example_data):
    return getCoefficientOfSerious(example_data)

# 酌定 相加减
list_discretionary = [
    u'曾因盗窃受过刑事处罚',
    u'一年内曾因盗窃受过行政处罚',
    u'退赃, 退赔',
    u'积极赔偿',
    u'盗窃家庭成员或近亲属财务',
    u'却因生活学习治病急需而盗窃',
    u'赃款赃物已返还或者被公安机关扣押',
    u'被害人明确表示谅解',
    u'入户盗窃',
    u'入户盗窃 携带凶器盗窃 扒窃一次且数额在500元以下',
    u'入户盗窃 携带凶器盗窃 扒窃一次且数额在1000元以下',
    u'盗窃财务数额10000元以上',
    u'以破坏性手段盗窃造成公司财产损失',
    u'盗窃残疾人 孤寡老人 未成年人或者用于紧急治病的款物',
    u'盗窃用于救灾 抢险 防汛 扶贫 移民 救济等款物',
    u'为实施吸毒 赌博等其他违法犯罪活动而盗窃',
]
def getCoefficientOfDiscretionary(postdata):
    # res= [1,1]
    res = np.array([1, 1], dtype=np.float64).reshape((2,1))
    # print res
    for k in postdata.keys():
        if k in list_discretionary:
            val = postdata.get(k)
            if val is None or base_data.get(k) is None:
                continue
            coeff = base_data[k].get(val)
            if coeff is None :
                continue
            #
            # temp = np.array(coeff)
            # res = res * temp
            res[0] *= coeff[0]
            res[1] *= coeff[1]



    # print res
    return res # np.array(res)


def test_discretionary(example_data):
    return getCoefficientOfDiscretionary(example_data)




# 法定 相乘
list_legal = [
    u'累犯',
    u'刑事和解',
    u'老年人犯罪',
    u'未遂犯',
    u'退赃退赔',
    u'积极赔偿',
    u'取得谅解',
    u'被害人有过错',
    u'配合追缴违法所得 挽回较大损失',
    u'盗窃近亲属财务',
    u'确因生活学习治病继续而盗窃',
    u'初次 偶然',
]

def getCoefficientOfLegal(postdata):
    res = np.array([1, 1], dtype=np.float64).reshape((2,1))
    # print res
    # res = [1,1]
    for k in postdata.keys():
        if k in list_legal:
            val = postdata.get(k)
            if val is None or base_data.get(k) is None:
                continue
            coeff = base_data.get(k).get(val)
            # temp = np.array(coeff).T
            temp = coeff
            if temp is None:
                continue

            # print k, val, temp

            # res = res * temp
            res[0] = res[0]*temp[0]
            res[1] = res[1]*temp[1]
    print 'getCoefficientOfLegal: ', res - 1
    return res # np.array(res)

def test_legal(example_data):
    return getCoefficientOfLegal(example_data)




# 计算量刑幅度
def getSentencingRange(startpoint, penaltyAmount, coeffDiscretionary, coeffOfFirst, coeffLegal):
    # print type(startpoint), type(penaltyAmount), type(coeffDiscretionary), type(coeffLegal)

    # res_min = (startpoint + penaltyAmount)*coeffDiscretionary*coeffLegal
    # res_max = (startpoint + penaltyAmount)*coeffDiscretionary*coeffLegal
    res = (np.array(startpoint) + penaltyAmount) * coeffDiscretionary *coeffOfFirst*coeffLegal
    return res #[res_min, res_max]





# 根据基准刑计算量刑幅度, 并确保在给定范围内
def getCaseSentencingRange(benchmarkPunishment, case_list):
    caselist = np.array(case_list[0:2])
    ben = benchmarkPunishment*caselist
    print u'该情节量刑幅度: \n', benchmarkPunishment,'\n', case_list, '\n', ben
    try:
        b = np.abs(ben)
        print b
        for i in range(len(b)):
            '''
            :TODO

            '''
            # 变化幅度不小于, 变化幅度不大于...该如何区分. 暂时木有思路
            if b[i] < case_list[-1]:
                ben[i] = case_list[-1]
    except Exception, e:
        print u'量刑幅度无范围约束.', e

    print u'该情节量刑幅度: \n', benchmarkPunishment, '\n', caselist, '\n', ben

    return ben

# API
def getSentencingRange_API(amountoftheft, actionoftheft, postdata, zuiming):
    # 依据罪名, 作案情节 确定量刑起点和应增加的刑罚量
    startpoint = getSentencingStartingPoint(amountoftheft, actionoftheft, zuiming)
    startpoint = np.array(startpoint)
    penaltyAmount = getPenaltyAmount(amountoftheft, actionoftheft, zuiming)
    # 量刑起点
    beginLiangXing = startpoint+penaltyAmount
    print u'量刑起点为: ', beginLiangXing
    # 需要优先处理的情节, 确定基准刑
    coeffOfSerious = test_getCoefficientOfSerious(postdata)
    benchmarkPunishment = beginLiangXing*(1+coeffOfSerious)
    print u'基准刑: ', benchmarkPunishment, '/', coeffOfSerious, '/', beginLiangXing*np.array((1,1))

    result = benchmarkPunishment
    # 计算调节幅度, 并确保在给定范围内
    # 特定情节
    cases = [case for case in postdata.keys() if case in base_data.keys()]
    print 'cases: ', cases
    for case in cases:
        print 'case: ', case
        try:
            case_list = base_data.get(case).get(postdata.get(case))
            result += getCaseSentencingRange(benchmarkPunishment, case_list)
        except Exception, e:
            print u'相加减....', e

    print u'量刑调节结果: ', result

    return result


    # drop
    # coeffDiscretionary = test_discretionary(postdata)
    # coeffLegal = test_legal(postdata)
    # sentencingRange = getSentencingRange(startpoint=startpoint,
    #                                      penaltyAmount=penaltyAmount,
    #                                      coeffOfFirst=coeffOfSerious,
    #                                      coeffDiscretionary=coeffDiscretionary,
    #                                      coeffLegal=coeffLegal)
    # return sentencingRange





if __name__ == '__main__':

    amountoftheft = 20000
    actionoftheft = [u'普通盗窃']

    print '基准刑: '
    startpoint = getSentencingStartingPoint(amountoftheft, actionoftheft)
    print '量刑起点: ', startpoint
    penaltyAmount = getPenaltyAmount(amountoftheft, actionoftheft)
    print '应增加的刑罚量: ', penaltyAmount


    example_data = {
        u'未成年犯罪':u'未成年犯罪',
        # u'年龄': [35, u'过失犯罪', ],
        # u'限制行为能力人': u'限制行为能力人',
        # u'聋哑人或盲人': u'聋哑人或盲人',
        # u'未遂犯': u'(3)未实行终了+造成损害后果的',
        # u'共同犯罪': u'教唆犯, 教唆对象为限制行为能力人',
    }
    #
    # coeffDiscretionary = test_discretionary(example_data)
    #
    # print '酌定处罚系数: ', coeffDiscretionary
    #
    # coeffLegal = test_legal(example_data)
    #
    # print '法定处罚系数: ', coeffLegal

    # print '量刑幅度: ', getSentencingRange(startpoint, penaltyAmount, coeffDiscretionary, coeffLegal)

    print 'result: ', getSentencingRange_API(amountoftheft, actionoftheft, example_data)