# coding=utf8
'''
根据盗窃量刑流程, 生成情节判定字典
'''
import codecs
import re
str1 = u'填写.{,15}项下选择'
str2 = u'.{,50}到基准刑乘以.{,50}'
strnum = '0\.?\d*'
strend = u'.{,10}罪量刑情节.{,10}'
another = u'（注：.*'
partternprojectName = re.compile(str1)
partternprojectValue = re.compile(str2)
partternprojectNum = re.compile(strnum)
partternprojectEnd = re.compile(strend)
partternprojectAnother = re.compile(another)

# 表示盗窃罪的量刑标准
# 根据盗窃量刑流程, 解析得到
# 针对罪犯的各种行为, 情节, 拿到量刑变化系数的上下限, 以及范围
res_re = dict()

with codecs.open('zong.txt', 'r', encoding='gb2312') as f:

    projectName = 0
    subPorjectName = 0
    state = 1
    for line in f.readlines():
        line= line.replace('\r\n','')
        if len(line) == 0:
            continue
        # line = line.trip()
        # print '*'*3, line,'*'*3,

        # out key
        isInProjectName = True
        res = partternprojectName.findall(line)
        if res not in (None, []):
            projectName = res[0]
            if projectName not in res_re.keys():
                isInProjectName = False
                state = 1

                res_re[projectName] = dict()
        else:
            res = partternprojectEnd.findall(line)
            if res not in (None, []):
                # 匹配后半部分

                projectName = res[0]
                if projectName not in res_re.keys():
                    isInProjectName = False

                    res_re[projectName] = dict()
                    state = 2



        if isInProjectName:
            # in key
            if state == 1:
                res = partternprojectValue.findall(line)

                if res not in (None, []):

                        # if res not in res_re.get(projectName).keys():
                        #     subPorjectName = res[0]
                        #     res_re[projectName][subPorjectName] = None
                        for r in res:

                            # print r
                            subPorjectName = r
                            if r not in res_re.get(projectName).keys():
                                res_re[projectName][subPorjectName] = list()
            elif state == 2:
                subPorjectName = line
                res_re[projectName][subPorjectName] = list()
                state += 1



                # subproject = r
                # if len(subproject) >= 2:
                #     index = ''.join(subproject[0:-1])
                #     res_re.get(projectName)[index]=map(float, partternprojectNum.findall(subproject[-1]))
                # else:
                #     nums = list()
                #     for s in subproject:
                #         nums += partternprojectNum.findall(s)
                #     res_re.get(projectName)[projectName] = map(float, nums)
                # print r,'='*3,
            # in value
            # res = partternprojectValue.findall(line)
            # if res in (None, []):
            #     continue

            res = partternprojectValue.findall(line)

            if res not in (None, []):
                res = partternprojectNum.findall(line)
                if res not in (None, []):


                    if re.compile(u'减刑幅度').findall(line) not in (None, []):
                        v = -1
                    elif re.compile(u'加刑幅度').findall(line) not in (None, []):
                        v = 1
                    else:
                        v = 1

                    try:

                        res_re.get(projectName)[subPorjectName] = res_re.get(projectName)[subPorjectName][:] \
                                                                  + map(lambda x: float(x)*v, res)[:]
                        an = partternprojectAnother.findall(line)
                        if an not in (None, []):
                            num = re.compile('\d+').findall(an[0])
                            res_re.get(projectName)[subPorjectName] = \
                            res_re.get(projectName)[subPorjectName][:] \
                            + map(float,num)


                    except Exception, e:
                        print e,'出错了'
                if state == 3:
                    state -= 1


        print state, ':', projectName, '{', subPorjectName, '=', res

    # print '/','*'*40,'/'

if __name__ == '__main__':

    import pickle
    with open(u'量刑情节'+'.txt', 'wb') as f:
        p = pickle.Pickler(f)
        p.dump(res_re)
    for k in res_re.keys():
        print k,'-'
        for vk in res_re.get(k).keys():
            print '\t', vk, '=', res_re.get(k).get(vk)