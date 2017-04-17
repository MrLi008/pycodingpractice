# coding=utf8

'''
基准刑 = 量刑起点 + 应增加的刑法量
benchmark punishment = sentencing starting point
        + the amount of penalty should be increased
'''


import numpy as np
import pandas as pd
# columns = [u'普通盗窃', u'入户盗窃', u'携带凶器盗窃', u'扒窃', u'多次扒窃', u'二条1到8项之一', u'二条3到8项'之一]
indexes = ['0-1000', '1000-2000', '2000-25000', '25000-50000', '50000-200000', '200000-400000', '400000以上']
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
    if amount <= 1000:
        return '0-1000'
    if amount <= 2000:
        return '1000-2000'
    if amount <= 25000:
        return '2000-25000'
    if amount <= 50000:
        return '25000-50000'
    if amount <= 200000:
        return '50000-200000'
    if amount <= 400000:
        return '200000-400000'
    return u'400000以上'




# 确认盗窃情节归属,
def confirmascriptionplotoftheft(actionoftheft):
    return actionoftheft





# 量刑起点
def getSentencingStartingPoint(amountoftheft, actionoftheft):
    standard = pd.read_excel('sentencingstart.xlsx')
    standard.index = indexes

    res = standard.loc[confirmrangeofamount(amountoftheft),
                       confirmascriptionplotoftheft(actionoftheft)]
    res = [int(x) for x in list(res[0].split('[')[1].split(']')[0].split(','))]
    return res





# 应增加的刑罚量
def getPenaltyAmount(amountoftheft, actionoftheft):
    standard = pd.read_excel('calculationformula.xlsx')
    standard.index = indexes

    temp_res = standard.loc[confirmrangeofamount(amountoftheft),
                       confirmascriptionplotoftheft(actionoftheft)][0].replace('m', str(amountoftheft))

    '''
    :warnning 可能被恶意利用
    '''
    res = eval(temp_res)

    # print res

    return res




# calculationformula = data.loc[confirmrangeofamount(amountoftheft), actionoftheft]
# res = calculationformula[0].replace('m', str(amountoftheft ))
# # print type(calculationformula),  res
# print '基准刑: '
# print '量刑起点: ', getSentencingStartingPoint(amountoftheft, actionoftheft)
# print '应增加的刑罚量: ', getPenaltyAmount(amountoftheft, actionoftheft)


# 设定量刑起点的标准




base_data = {u'项目名称':{u'行为':[0.6, 1]},}
from filterprocess import res_re
base_data = res_re
'''
{u'年龄':{u'年龄=65-74, 故意犯罪': [0.8,1],
               u'年龄=65-74, 过失犯罪':[0.6,0.9],
               u'年龄大于等于75, 故意犯罪':[0.6,1],
               u'年龄大于等于75, 过失犯罪':[0.5,0.8]},
         u'限制行为能力人':{u'限制行为能力人':[0.6,1]},
         u'聋哑人或盲人':{u'聋哑人或盲人':[0.6,1]},
         u'预备犯':{u'预备犯':[0,0.6]},
         u'未遂犯':{u'实行终了, 造成损害后果':[0.8,1],
                 u'实行终了, 未造成损害后果':[0.6,1],
                 u'未实行终了, 造成严重后果':[0.5, 1],
                 u'未实行终了, 未造成严重后果':[0.5,1],
                 },
         u'中止犯':{u'造成较重损害的':[0.4,0.7],
                 u'造成较轻损害的':[0.2,0.5]},
         }
'''

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
# 需有限计算的量刑情节

list_serious = [
    u''
]
# 酌定 相加减
list_discretionary = [
    u'曾因盗窃受过刑事处罚',
    u'一年内曾因盗窃受过行政处罚',
    u'退赃, 退赔',
    u'积极赔偿',
]
def getCoefficientOfDiscretionary(postdata):
    # res= [1,1]
    res = np.array([1, 1], dtype=np.float64).reshape((2,1))
    # print res
    for k in postdata.keys():
        if k in list_discretionary:
            val = postdata.get(k)
            coeff = base_data(k).get(val)
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
    u'未成年人犯罪',
    u'老年人犯罪',
    u'未遂犯',
]

def getCoefficientOfLegal(postdata):
    res = np.array([1, 1], dtype=np.float64).reshape((2,1))
    # print res
    # res = [1,1]
    for k in postdata.keys():
        if k in list_legal:
            val = postdata.get(k)
            coeff = base_data.get(k).get(val)
            # temp = np.array(coeff).T
            temp = coeff

            # print k, val, temp

            # res = res * temp
            res[0] = res[0]*temp[0]
            res[1] = res[1]*temp[1]
    # print res
    return res # np.array(res)

def test_legal(example_data):
    return getCoefficientOfLegal(example_data)




# 计算量刑幅度
def getSentencingRange(startpoint, penaltyAmount, coeffDiscretionary, coeffLegal):
    # print type(startpoint), type(penaltyAmount), type(coeffDiscretionary), type(coeffLegal)

    # res_min = (startpoint + penaltyAmount)*coeffDiscretionary*coeffLegal
    # res_max = (startpoint + penaltyAmount)*coeffDiscretionary*coeffLegal
    res = (np.array(startpoint) + penaltyAmount) * coeffDiscretionary * coeffLegal
    return res #[res_min, res_max]







# API
def getSentencingRange_API(amountoftheft, actionoftheft, postdata):
    startpoint = getSentencingStartingPoint(amountoftheft, actionoftheft)
    penaltyAmount = getPenaltyAmount(amountoftheft, actionoftheft)
    coeffDiscretionary = test_discretionary(postdata)
    coeffLegal = test_legal(postdata)
    sentencingRange = getSentencingRange(startpoint=startpoint,
                                         penaltyAmount=penaltyAmount,
                                         coeffDiscretionary=coeffDiscretionary,
                                         coeffLegal=coeffLegal)
    return sentencingRange




if __name__ == '__main__':

    amountoftheft = 52000
    actionoftheft = [u'入户盗窃']

    print '基准刑: '
    startpoint = getSentencingStartingPoint(amountoftheft, actionoftheft)
    print '量刑起点: ', startpoint
    penaltyAmount = getPenaltyAmount(amountoftheft, actionoftheft)
    print '应增加的刑罚量: ', penaltyAmount


    example_data = {
        u'年龄': [35, u'过失犯罪', ],
        u'限制行为能力人': u'限制行为能力人',
        u'聋哑人或盲人': u'聋哑人或盲人',
        u'未遂犯': u'(3)未实行终了+造成损害后果的',
        u'共同犯罪': u'教唆犯, 教唆对象为限制行为能力人',
    }

    coeffDiscretionary = test_discretionary(example_data)

    print '酌定处罚系数: ', coeffDiscretionary

    coeffLegal = test_legal(example_data)

    print '法定处罚系数: ', coeffLegal

    print '量刑幅度: ', getSentencingRange(startpoint, penaltyAmount, coeffDiscretionary, coeffLegal)

    print 'result: ', getSentencingRange_API(amountoftheft, actionoftheft, example_data)