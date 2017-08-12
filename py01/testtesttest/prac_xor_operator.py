# coding=utf8
''' 测试异或运算是否可反算
        不可.
        0会渐渐变多?

    功能要求:
        给定一个字符串, 经过有限的异或运算得到一个hash值
        
        再根据最后一个字符, 和hash值, 得到整个字符串

'''


def encode_xor_operator(content):
    # init x
    x = 3

    print 'init: ', x

    for c in content:
        x = x ^ int(c)

    print 'result hash: ', x


    return x


def decode_xor_operator(lastchar, hash_value, length):

    print 'last char: ', lastchar
    print 'hash_value: ', hash_value
    x = hash_value
    content = lastchar

    for i in range(length):
        x = x^int(content[-1])
        content += str(x)

    print 'result: ', content





if __name__ == '__main__':

    content = '1234567'*100

    hash_value = encode_xor_operator(content)
    result = decode_xor_operator(content[-1], hash_value, len(content))