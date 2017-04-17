# coding=utf8
'''
根据盗窃罪中人物的基本信息及行为打分
'''



'''
本评分标准依据 <<太原市人民检察院逮捕必要性评估参考
标准(试行)>> 制定

:author mrli008
:date 2017,03,29
:功能描述 见注释
'''


# 1 描述
# 2 原则
# 3 适用于 侦查机关 提请比准逮捕的可能
# 判处三年以下有期徒刑刑法
# 的犯罪嫌疑人

# 4 评估逮捕必要性的方法
'''
根据犯罪事实, 情节及影响量刑的其他因素, 参照山西省人民法院制定的
<<人民法院量刑指导意见实施细则>>
综合全案, 预测犯罪嫌疑人 实际可能判处的刑法在
三年以下有期徒刑的,
启动评估程序
'''
# 分为共性因素, 常见罪名的个性因素 评估打分

# 基础分为50分
score_base = 50

# 评判分界线
score_separatrix = 70

# 批准逮捕 根据分值确定 是否批准逮捕
# :传入分值,
#   True 逮捕必要性较大
#   False 逮捕必要性较小
def approvalArrest(score_):
    if score_ < score_separatrix:
        return True
    else:
        return False


# 5 对有证据证明有犯罪事实的
# 可能判处徒刑以上想法的犯罪嫌疑人, 具有下列情形的
# 应当批准逮捕

# 6 对副歌逮捕条件的犯罪嫌疑人, 具有下列情形之一的可以不予批准逮捕
condition_necessary = [
    u'患有严重疾病, 生活不能自理',
    u'怀孕或者正在步入自己婴儿的妇女',
    u'系生活不能自理的人的唯一抚养人'
]

from collections import Iterable
def negativeArrest(situation):
    if isinstance(situation, Iterable):
        for con in condition_necessary:
            if con in situation:
                # 不予批准逮捕, 返回100分
                return False

    return 0


# 7 影响逮捕必要性的共性因素分值, 包含1,2,3项
condition_self = [
    (u'未成年人', 10),
    (u'六十五岁以上老年人', 10),
    (u'盲人',10),
    (u'聋哑人或者其他残疾人',5),
    (u'限制形式责任能力的精神病人',10),
    (u'在校学生', 10),
    (u'在本地长期有固定住处', 3),
    (u'有稳定职业, 收入', 5),
    (u'在本地无固定住处', -3),
    (u'不能踢动保证人或者缴纳保证金', -20)
]
def selfsituation(situation, score_):
    if isinstance(situation, Iterable):
        for con,score in condition_self:
            if con in situation:
                score_ += score

    return score_


# 8 常见罪名中影响逮捕必要性的个性因素分值
# 盗窃罪
condition_for_theft = [
    (u'盗窃家庭成员或者近亲属的财务', 10),
    (u'确因生活, 学习, 治病急需而盗窃', 3),
]

def fortheft(situation, score_):
    if isinstance(situation, Iterable):
        for conn, score in condition_for_theft:
            if conn in situation:
                score_ += score

    return score_

# 计算分值
def calculatorscore(situation):
    score = 50 \
            + selfsituation(situation,0)\
            + fortheft(situation, 0)

    if negativeArrest(situation) and \
        approvalArrest(score):

        return True
    else:
        return False


if __name__ == '__main__':
    situation = [
        u'未成年人',
        u'盲人',
        u'在校学生',
        u'盗窃家庭成员或者近亲属的财务',
    ]


    if calculatorscore(situation):

        print '逮捕必要性较大, 一般批准逮捕'
    else:
        print '逮捕必要性较小, 一般不予批准逮捕'
